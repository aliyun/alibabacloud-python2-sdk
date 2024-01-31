# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paifeaturestore20230621 import models as pai_feature_store_20230621_models
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
        self._endpoint = self.get_endpoint('paifeaturestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_project_feature_entity_hot_id_version_with_options(self, instance_id, project_id, feature_entity_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeProjectFeatureEntityHotIdVersion',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureentities/%s/action/changehotidversion' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ChangeProjectFeatureEntityHotIdVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def change_project_feature_entity_hot_id_version(self, instance_id, project_id, feature_entity_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_project_feature_entity_hot_id_version_with_options(instance_id, project_id, feature_entity_name, request, headers, runtime)

    def check_instance_datasource_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/action/checkdatasource' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CheckInstanceDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_instance_datasource(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_datasource_with_options(instance_id, request, headers, runtime)

    def create_datasource_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_datasource(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_datasource_with_options(instance_id, request, headers, runtime)

    def create_feature_entity_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_id):
            body['JoinId'] = request.join_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureentities' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_feature_entity(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_entity_with_options(instance_id, request, headers, runtime)

    def create_feature_view_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not UtilClient.is_unset(request.register_table):
            body['RegisterTable'] = request.register_table
        if not UtilClient.is_unset(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not UtilClient.is_unset(request.ttl):
            body['TTL'] = request.ttl
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.write_method):
            body['WriteMethod'] = request.write_method
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    def create_feature_view(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_view_with_options(instance_id, request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def create_label_table_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/labeltables' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_label_table(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_label_table_with_options(instance_id, request, headers, runtime)

    def create_model_feature_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model_feature(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_feature_with_options(instance_id, request, headers, runtime)

    def create_model_feature_training_set_fgtable_with_options(self, instance_id, model_feature_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateModelFeatureTrainingSetFGTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/trainingsetfgtable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureTrainingSetFGTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model_feature_training_set_fgtable(self, instance_id, model_feature_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_feature_training_set_fgtable_with_options(instance_id, model_feature_id, headers, runtime)

    def create_project_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not UtilClient.is_unset(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not UtilClient.is_unset(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(instance_id, request, headers, runtime)

    def create_service_identity_role_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/serviceidentityroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_identity_role(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(request, headers, runtime)

    def delete_datasource_with_options(self, instance_id, datasource_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(datasource_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_datasource(self, instance_id, datasource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_datasource_with_options(instance_id, datasource_id, headers, runtime)

    def delete_feature_entity_with_options(self, instance_id, feature_entity_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureentities/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_feature_entity(self, instance_id, feature_entity_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    def delete_feature_view_with_options(self, instance_id, feature_view_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_feature_view(self, instance_id, feature_view_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    def delete_label_table_with_options(self, instance_id, label_table_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/labeltables/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_table_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_label_table(self, instance_id, label_table_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_label_table_with_options(instance_id, label_table_id, headers, runtime)

    def delete_model_feature_with_options(self, instance_id, model_feature_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model_feature(self, instance_id, model_feature_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    def delete_project_with_options(self, instance_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, instance_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(instance_id, project_id, headers, runtime)

    def export_model_feature_training_set_fgtable_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.training_set_fg_config):
            body['TrainingSetFgConfig'] = request.training_set_fg_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetFGTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/action/exporttrainingsetfgtable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetFGTableResponse(),
            self.call_api(params, req, runtime)
        )

    def export_model_feature_training_set_fgtable(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_model_feature_training_set_fgtable_with_options(instance_id, model_feature_id, request, headers, runtime)

    def export_model_feature_training_set_table_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not UtilClient.is_unset(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not UtilClient.is_unset(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/action/exporttrainingsettable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse(),
            self.call_api(params, req, runtime)
        )

    def export_model_feature_training_set_table(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_model_feature_training_set_table_with_options(instance_id, model_feature_id, request, headers, runtime)

    def get_datasource_with_options(self, instance_id, datasource_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(datasource_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_datasource(self, instance_id, datasource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_with_options(instance_id, datasource_id, headers, runtime)

    def get_datasource_table_with_options(self, instance_id, datasource_id, table_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasourceTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources/%s/tables/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(datasource_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(table_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_datasource_table(self, instance_id, datasource_id, table_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_table_with_options(instance_id, datasource_id, table_name, headers, runtime)

    def get_feature_entity_with_options(self, instance_id, feature_entity_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureentities/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_feature_entity(self, instance_id, feature_entity_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    def get_feature_view_with_options(self, instance_id, feature_view_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_feature_view(self, instance_id, feature_view_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_label_table_with_options(self, instance_id, label_table_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/labeltables/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_table_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_label_table(self, instance_id, label_table_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_label_table_with_options(instance_id, label_table_id, headers, runtime)

    def get_model_feature_with_options(self, instance_id, model_feature_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_feature(self, instance_id, model_feature_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fgfeature_with_options(self, instance_id, model_feature_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/fgfeature' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_feature_fgfeature(self, instance_id, model_feature_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_fgfeature_with_options(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fginfo_with_options(self, instance_id, model_feature_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGInfo',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/fginfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_feature_fginfo(self, instance_id, model_feature_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_fginfo_with_options(instance_id, model_feature_id, headers, runtime)

    def get_project_with_options(self, instance_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project(self, instance_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(instance_id, project_id, headers, runtime)

    def get_project_feature_entity_with_options(self, instance_id, project_id, feature_entity_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureentities/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_feature_entity(self, instance_id, project_id, feature_entity_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_with_options(instance_id, project_id, feature_entity_name, headers, runtime)

    def get_project_feature_entity_hot_ids_with_options(self, instance_id, project_id, next_seq_number, feature_entity_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureentities/%s/hotids/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(next_seq_number))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityHotIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_feature_entity_hot_ids(self, instance_id, project_id, next_seq_number, feature_entity_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_hot_ids_with_options(instance_id, project_id, next_seq_number, feature_entity_name, headers, runtime)

    def get_project_feature_view_with_options(self, instance_id, project_id, feature_view_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureviews/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_feature_view(self, instance_id, project_id, feature_view_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_view_with_options(instance_id, project_id, feature_view_name, headers, runtime)

    def get_project_model_feature_with_options(self, instance_id, project_id, model_feature_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/modelfeatures/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_model_feature(self, instance_id, project_id, model_feature_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_model_feature_with_options(instance_id, project_id, model_feature_name, headers, runtime)

    def get_service_identity_role_with_options(self, role_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/serviceidentityroles/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(role_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_identity_role(self, role_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(role_name, headers, runtime)

    def get_task_with_options(self, instance_id, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/tasks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, instance_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(instance_id, task_id, headers, runtime)

    def list_datasource_tables_with_options(self, instance_id, datasource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasourceTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources/%s/tables' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(datasource_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_datasource_tables(self, instance_id, datasource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasource_tables_with_options(instance_id, datasource_id, request, headers, runtime)

    def list_datasources_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasources',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_datasources(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasources_with_options(instance_id, request, headers, runtime)

    def list_feature_entities_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureEntities',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureentities' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_entities(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_entities_with_options(instance_id, request, headers, runtime)

    def list_feature_view_field_relationships_with_options(self, instance_id, feature_view_id, field_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewFieldRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s/fields/%s/relationships' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(field_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_view_field_relationships(self, instance_id, feature_view_id, field_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_field_relationships_with_options(instance_id, feature_view_id, field_name, headers, runtime)

    def list_feature_view_relationships_with_options(self, instance_id, feature_view_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s/relationships' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_view_relationships(self, instance_id, feature_view_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_relationships_with_options(instance_id, feature_view_id, headers, runtime)

    def list_feature_views_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_feature_views(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_views_with_options(instance_id, request, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_label_tables_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListLabelTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_table_ids):
            request.label_table_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLabelTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/labeltables' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListLabelTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_label_tables(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_label_tables_with_options(instance_id, request, headers, runtime)

    def list_model_feature_available_features_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatureAvailableFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/availablefeatures' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_model_feature_available_features(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_feature_available_features_with_options(instance_id, model_feature_id, request, headers, runtime)

    def list_model_features_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListModelFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_model_features(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_features_with_options(instance_id, request, headers, runtime)

    def list_project_feature_view_owners_with_options(self, instance_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewOwners',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureviewowners' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewOwnersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_feature_view_owners(self, instance_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_view_owners_with_options(instance_id, project_id, headers, runtime)

    def list_project_feature_view_tags_with_options(self, instance_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViewTags',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureviewtags' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_feature_view_tags(self, instance_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_view_tags_with_options(instance_id, project_id, headers, runtime)

    def list_project_feature_views_with_options(self, instance_id, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureviews' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_feature_views(self, instance_id, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_views_with_options(instance_id, project_id, headers, runtime)

    def list_projects_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_ids):
            request.project_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(instance_id, request, headers, runtime)

    def list_task_logs_with_options(self, instance_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskLogs',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/tasks/%s/logs' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task_logs(self, instance_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_logs_with_options(instance_id, task_id, request, headers, runtime)

    def list_tasks_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(instance_id, request, headers, runtime)

    def publish_feature_view_table_with_options(self, instance_id, feature_view_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.event_time):
            body['EventTime'] = request.event_time
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s/action/publishtable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.PublishFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_feature_view_table(self, instance_id, feature_view_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    def update_datasource_with_options(self, instance_id, datasource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/datasources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(datasource_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_datasource(self, instance_id, datasource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_datasource_with_options(instance_id, datasource_id, request, headers, runtime)

    def update_label_table_with_options(self, instance_id, label_table_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/labeltables/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_table_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_label_table(self, instance_id, label_table_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_label_table_with_options(instance_id, label_table_id, request, headers, runtime)

    def update_model_feature_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def update_model_feature(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_with_options(instance_id, model_feature_id, request, headers, runtime)

    def update_model_feature_fgfeature_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lookup_features):
            body['LookupFeatures'] = request.lookup_features
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.reserves):
            body['Reserves'] = request.reserves
        if not UtilClient.is_unset(request.sequence_features):
            body['SequenceFeatures'] = request.sequence_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/fgfeature' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def update_model_feature_fgfeature(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_fgfeature_with_options(instance_id, model_feature_id, request, headers, runtime)

    def update_model_feature_fginfo_with_options(self, instance_id, model_feature_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeatureFGInfo',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/modelfeatures/%s/fginfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(model_feature_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureFGInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_model_feature_fginfo(self, instance_id, model_feature_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_fginfo_with_options(instance_id, model_feature_id, request, headers, runtime)

    def update_project_with_options(self, instance_id, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project(self, instance_id, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(instance_id, project_id, request, headers, runtime)

    def write_feature_view_table_with_options(self, instance_id, feature_view_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        if not UtilClient.is_unset(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/featureviews/%s/action/writetable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_view_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    def write_feature_view_table(self, instance_id, feature_view_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.write_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    def write_project_feature_entity_hot_ids_with_options(self, instance_id, project_id, feature_entity_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hot_ids):
            body['HotIds'] = request.hot_ids
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteProjectFeatureEntityHotIds',
            version='2023-06-21',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/projects/%s/featureentities/%s/action/writehotids' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(feature_entity_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteProjectFeatureEntityHotIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def write_project_feature_entity_hot_ids(self, instance_id, project_id, feature_entity_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.write_project_feature_entity_hot_ids_with_options(instance_id, project_id, feature_entity_name, request, headers, runtime)
