# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenestsupplier20210521 import models as compute_nest_supplier_20210521_models
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
        self._endpoint = self.get_endpoint('computenestsupplier', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_artifact_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_artifact_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def delete_artifact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_artifact_with_options(request, runtime)

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def get_artifact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def get_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    def get_artifact_repository_credentials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactRepositoryCredentials',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_artifact_repository_credentials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_repository_credentials_with_options(request, runtime)

    def get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    def get_service_estimate_cost_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceEstimateCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceEstimateCost',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_estimate_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_estimate_cost_with_options(request, runtime)

    def get_service_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    def list_artifact_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactVersions',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_artifact_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_versions_with_options(request, runtime)

    def list_artifacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_artifacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    def list_service_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_deleted):
            query['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    def list_service_usages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceUsages',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_usages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_usages_with_options(request, runtime)

    def list_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_versions):
            query['AllVersions'] = request.all_versions
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    def release_artifact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def release_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_artifact_with_options(request, runtime)

    def update_artifact_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    def update_artifact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_artifact_with_options(request, runtime)

    def update_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)
