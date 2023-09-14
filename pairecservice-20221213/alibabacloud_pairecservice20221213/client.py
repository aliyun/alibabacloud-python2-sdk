# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pairecservice20221213 import models as pai_rec_service_20221213_models
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
        self._endpoint = self.get_endpoint('pairecservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def backflow_feature_consistency_check_job_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_features):
            body['ItemFeatures'] = request.item_features
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scores):
            body['Scores'] = request.scores
        if not UtilClient.is_unset(request.user_features):
            body['UserFeatures'] = request.user_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BackflowFeatureConsistencyCheckJobData',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/action/backflowdata',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.BackflowFeatureConsistencyCheckJobDataResponse(),
            self.call_api(params, req, runtime)
        )

    def backflow_feature_consistency_check_job_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.backflow_feature_consistency_check_job_data_with_options(request, headers, runtime)

    def clone_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s/action/clone' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_with_options(experiment_id, request, headers, runtime)

    def clone_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s/action/clone' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def clone_feature_consistency_check_job_config_with_options(self, source_feature_consistency_check_job_config_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobconfigs/%s/action/clone' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(source_feature_consistency_check_job_config_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_feature_consistency_check_job_config(self, source_feature_consistency_check_job_config_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_feature_consistency_check_job_config_with_options(source_feature_consistency_check_job_config_id, request, headers, runtime)

    def clone_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clone_experiment_group):
            body['CloneExperimentGroup'] = request.clone_experiment_group
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s/action/clone' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CloneLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_laboratory_with_options(laboratory_id, request, headers, runtime)

    def create_crowd_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_crowd(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_crowd_with_options(request, headers, runtime)

    def create_experiment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.experiment_group_id):
            body['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_experiment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    def create_experiment_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.reserved_buckets):
            body['ReservedBuckets'] = request.reserved_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_experiment_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_group_with_options(request, headers, runtime)

    def create_feature_consistency_check_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sampling_duration):
            body['SamplingDuration'] = request.sampling_duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_feature_consistency_check_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_with_options(request, headers, runtime)

    def create_feature_consistency_check_job_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_feature_consistency_check_job_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_consistency_check_job_config_with_options(request, headers, runtime)

    def create_laboratory_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_laboratory(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_laboratory_with_options(request, headers, runtime)

    def create_layer_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            body['LaboratoryId'] = request.laboratory_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/layers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_layer(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_with_options(request, headers, runtime)

    def create_param_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/params',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateParamResponse(),
            self.call_api(params, req, runtime)
        )

    def create_param(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_param_with_options(request, headers, runtime)

    def create_scene_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/scenes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scene_with_options(request, headers, runtime)

    def create_sub_crowd_with_options(self, crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s/subcrowds' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.CreateSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sub_crowd(self, crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sub_crowd_with_options(crowd_id, request, headers, runtime)

    def delete_crowd_with_options(self, crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_crowd(self, crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_crowd_with_options(crowd_id, request, headers, runtime)

    def delete_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, request, headers, runtime)

    def delete_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def delete_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_laboratory_with_options(laboratory_id, request, headers, runtime)

    def delete_layer_with_options(self, layer_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/layers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_layer(self, layer_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_with_options(layer_id, request, headers, runtime)

    def delete_param_with_options(self, param_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/params/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(param_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteParamResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_param(self, param_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_param_with_options(param_id, request, headers, runtime)

    def delete_scene_with_options(self, scene_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/scenes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(scene_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene(self, scene_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scene_with_options(scene_id, request, headers, runtime)

    def delete_sub_crowd_with_options(self, crowd_id, sub_crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s/subcrowds/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sub_crowd_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.DeleteSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sub_crowd(self, crowd_id, sub_crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    def get_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, request, headers, runtime)

    def get_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def get_feature_consistency_check_job_with_options(self, feature_consistency_check_job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_feature_consistency_check_job(self, feature_consistency_check_job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    def get_feature_consistency_check_job_config_with_options(self, feature_consistency_check_job_config_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobconfigs/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_feature_consistency_check_job_config(self, feature_consistency_check_job_config_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_laboratory_with_options(laboratory_id, request, headers, runtime)

    def get_layer_with_options(self, layer_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/layers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_layer(self, layer_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_with_options(layer_id, request, headers, runtime)

    def get_scene_with_options(self, scene_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/scenes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(scene_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene(self, scene_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scene_with_options(scene_id, request, headers, runtime)

    def get_sub_crowd_with_options(self, crowd_id, sub_crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s/subcrowds/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(sub_crowd_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.GetSubCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sub_crowd(self, crowd_id, sub_crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sub_crowd_with_options(crowd_id, sub_crowd_id, request, headers, runtime)

    def list_crowd_users_with_options(self, crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowdUsers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s/users' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_crowd_users(self, crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowd_users_with_options(crowd_id, request, headers, runtime)

    def list_crowds_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_crowds(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_crowds_with_options(request, headers, runtime)

    def list_experiment_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            query['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperimentGroups',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_experiment_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiment_groups_with_options(request, headers, runtime)

    def list_experiments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_group_id):
            query['ExperimentGroupId'] = request.experiment_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_experiments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    def list_feature_consistency_check_job_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ListFeatureConsistencyCheckJobConfigs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_consistency_check_job_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_configs_with_options(request, headers, runtime)

    def list_feature_consistency_check_job_feature_reports_with_options(self, feature_consistency_check_job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            query['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            query['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_user_id):
            query['LogUserId'] = request.log_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobFeatureReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/%s/featurereports' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobFeatureReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_consistency_check_job_feature_reports(self, feature_consistency_check_job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_feature_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_job_score_reports_with_options(self, feature_consistency_check_job_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.exclude_request_ids):
            request.exclude_request_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exclude_request_ids, 'ExcludeRequestIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_request_ids_shrink):
            query['ExcludeRequestIds'] = request.exclude_request_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobScoreReports',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/%s/scorereports' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobScoreReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_consistency_check_job_score_reports(self, feature_consistency_check_job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_job_score_reports_with_options(feature_consistency_check_job_id, request, headers, runtime)

    def list_feature_consistency_check_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureConsistencyCheckJobs',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListFeatureConsistencyCheckJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_consistency_check_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_consistency_check_jobs_with_options(request, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_laboratories_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaboratories',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLaboratoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_laboratories(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_laboratories_with_options(request, headers, runtime)

    def list_layers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.laboratory_id):
            query['LaboratoryId'] = request.laboratory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_layers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    def list_params_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParams',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/params',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListParamsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_params(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_params_with_options(request, headers, runtime)

    def list_scenes_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenes',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/scenes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scenes_with_options(request, headers, runtime)

    def list_sub_crowds_with_options(self, crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubCrowds',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s/subcrowds' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.ListSubCrowdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sub_crowds(self, crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sub_crowds_with_options(crowd_id, request, headers, runtime)

    def offline_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s/action/offline' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_with_options(experiment_id, request, headers, runtime)

    def offline_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s/action/offline' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def offline_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s/action/offline' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OfflineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.offline_laboratory_with_options(laboratory_id, request, headers, runtime)

    def online_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s/action/online' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def online_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_with_options(experiment_id, request, headers, runtime)

    def online_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s/action/online' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def online_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def online_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s/action/online' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.OnlineLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def online_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.online_laboratory_with_options(laboratory_id, request, headers, runtime)

    def push_all_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushAllExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s/action/pushall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.PushAllExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def push_all_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_all_experiment_with_options(experiment_id, request, headers, runtime)

    def sync_feature_consistency_check_job_replay_log_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.context_features):
            body['ContextFeatures'] = request.context_features
        if not UtilClient.is_unset(request.feature_consistency_check_job_config_id):
            body['FeatureConsistencyCheckJobConfigId'] = request.feature_consistency_check_job_config_id
        if not UtilClient.is_unset(request.generated_features):
            body['GeneratedFeatures'] = request.generated_features
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_item_id):
            body['LogItemId'] = request.log_item_id
        if not UtilClient.is_unset(request.log_request_id):
            body['LogRequestId'] = request.log_request_id
        if not UtilClient.is_unset(request.log_request_time):
            body['LogRequestTime'] = request.log_request_time
        if not UtilClient.is_unset(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFeatureConsistencyCheckJobReplayLog',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/action/syncreplaylog',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.SyncFeatureConsistencyCheckJobReplayLogResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_feature_consistency_check_job_replay_log(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_feature_consistency_check_job_replay_log_with_options(request, headers, runtime)

    def terminate_feature_consistency_check_job_with_options(self, feature_consistency_check_job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateFeatureConsistencyCheckJob',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobs/%s/action/terminate' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.TerminateFeatureConsistencyCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_feature_consistency_check_job(self, feature_consistency_check_job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_feature_consistency_check_job_with_options(feature_consistency_check_job_id, request, headers, runtime)

    def update_crowd_with_options(self, crowd_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCrowd',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/crowds/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(crowd_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def update_crowd(self, crowd_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_crowd_with_options(crowd_id, request, headers, runtime)

    def update_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flow_percent):
            body['FlowPercent'] = request.flow_percent
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperiment',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experiments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(experiment_id, request, headers, runtime)

    def update_experiment_group_with_options(self, experiment_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.crowd_id):
            body['CrowdId'] = request.crowd_id
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.distribution_time_duration):
            body['DistributionTimeDuration'] = request.distribution_time_duration
        if not UtilClient.is_unset(request.distribution_type):
            body['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.layer_id):
            body['LayerId'] = request.layer_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.need_aa):
            body['NeedAA'] = request.need_aa
        if not UtilClient.is_unset(request.reservced_buckets):
            body['ReservcedBuckets'] = request.reservced_buckets
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentGroup',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/experimentgroups/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_group_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateExperimentGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_experiment_group(self, experiment_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_group_with_options(experiment_group_id, request, headers, runtime)

    def update_feature_consistency_check_job_config_with_options(self, feature_consistency_check_job_config_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compare_feature):
            body['CompareFeature'] = request.compare_feature
        if not UtilClient.is_unset(request.eas_service_name):
            body['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.easy_rec_package_path):
            body['EasyRecPackagePath'] = request.easy_rec_package_path
        if not UtilClient.is_unset(request.easy_rec_version):
            body['EasyRecVersion'] = request.easy_rec_version
        if not UtilClient.is_unset(request.feature_display_exclude):
            body['FeatureDisplayExclude'] = request.feature_display_exclude
        if not UtilClient.is_unset(request.feature_landing_resource_id):
            body['FeatureLandingResourceId'] = request.feature_landing_resource_id
        if not UtilClient.is_unset(request.feature_priority):
            body['FeaturePriority'] = request.feature_priority
        if not UtilClient.is_unset(request.fg_jar_version):
            body['FgJarVersion'] = request.fg_jar_version
        if not UtilClient.is_unset(request.fg_json_file_name):
            body['FgJsonFileName'] = request.fg_json_file_name
        if not UtilClient.is_unset(request.generate_zip):
            body['GenerateZip'] = request.generate_zip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.item_id_field):
            body['ItemIdField'] = request.item_id_field
        if not UtilClient.is_unset(request.item_table):
            body['ItemTable'] = request.item_table
        if not UtilClient.is_unset(request.item_table_partition_field):
            body['ItemTablePartitionField'] = request.item_table_partition_field
        if not UtilClient.is_unset(request.item_table_partition_field_format):
            body['ItemTablePartitionFieldFormat'] = request.item_table_partition_field_format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_resource_id):
            body['OssResourceId'] = request.oss_resource_id
        if not UtilClient.is_unset(request.sample_rate):
            body['SampleRate'] = request.sample_rate
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_id_field):
            body['UserIdField'] = request.user_id_field
        if not UtilClient.is_unset(request.user_table):
            body['UserTable'] = request.user_table
        if not UtilClient.is_unset(request.user_table_partition_field):
            body['UserTablePartitionField'] = request.user_table_partition_field
        if not UtilClient.is_unset(request.user_table_partition_field_format):
            body['UserTablePartitionFieldFormat'] = request.user_table_partition_field_format
        if not UtilClient.is_unset(request.workflow_name):
            body['WorkflowName'] = request.workflow_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFeatureConsistencyCheckJobConfig',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/featureconsistencycheck/jobconfigs/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_consistency_check_job_config_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateFeatureConsistencyCheckJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_feature_consistency_check_job_config(self, feature_consistency_check_job_config_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_feature_consistency_check_job_config_with_options(feature_consistency_check_job_config_id, request, headers, runtime)

    def update_laboratory_with_options(self, laboratory_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_count):
            body['BucketCount'] = request.bucket_count
        if not UtilClient.is_unset(request.bucket_type):
            body['BucketType'] = request.bucket_type
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.debug_crowd_id):
            body['DebugCrowdId'] = request.debug_crowd_id
        if not UtilClient.is_unset(request.debug_users):
            body['DebugUsers'] = request.debug_users
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLaboratory',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/laboratories/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(laboratory_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLaboratoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_laboratory(self, laboratory_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_laboratory_with_options(laboratory_id, request, headers, runtime)

    def update_layer_with_options(self, layer_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLayer',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/layers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_layer(self, layer_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_layer_with_options(layer_id, request, headers, runtime)

    def update_param_with_options(self, param_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParam',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/params/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(param_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateParamResponse(),
            self.call_api(params, req, runtime)
        )

    def update_param(self, param_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_param_with_options(param_id, request, headers, runtime)

    def update_scene_with_options(self, scene_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.flows):
            body['Flows'] = request.flows
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2022-12-13',
            protocol='HTTPS',
            pathname='/api/v1/scenes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(scene_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_rec_service_20221213_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene(self, scene_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_scene_with_options(scene_id, request, headers, runtime)
