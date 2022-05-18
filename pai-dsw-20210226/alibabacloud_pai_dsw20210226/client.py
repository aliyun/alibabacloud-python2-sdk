# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pai_dsw20210226 import models as pai_dsw_20210226_models
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
        self._endpoint = self.get_endpoint('pai-dsw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_list):
            body['DatasetList'] = request.dataset_list
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environments):
            body['Environments'] = request.environments
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_public):
            body['IsPublic'] = request.is_public
        if not UtilClient.is_unset(request.nas_file_system_id):
            body['NasFileSystemId'] = request.nas_file_system_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_shutdown_timer(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_with_options(instance_id, request, headers, runtime)

    def create_instance_shutdown_timer_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.schedule_time):
            body['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.ttl_in_millis):
            body['TtlInMillis'] = request.ttl_in_millis
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/shutdownTimer' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_snapshot(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_with_options(instance_id, request, headers, runtime)

    def create_instance_snapshot_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_description):
            body['InstanceSnapshotDescription'] = request.instance_snapshot_description
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        if not UtilClient.is_unset(request.instance_snapshot_repo_url):
            body['InstanceSnapshotRepoUrl'] = request.instance_snapshot_repo_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    def delete_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance_shutdown_timer(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    def delete_instance_shutdown_timer_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/shutdownTimer' % TeaConverter.to_unicode(instance_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance_snapshot(self, instance_id, instance_snapshot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_with_options(instance_id, instance_snapshot_id, headers, runtime)

    def delete_instance_snapshot_with_options(self, instance_id, instance_snapshot_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/snapshots/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(instance_snapshot_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_authorization_with_options(headers, runtime)

    def get_authorization_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/authorization',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dashboard_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_statistics_with_options(request, headers, runtime)

    def get_dashboard_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDashboardStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/statistics/dashboard',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetDashboardStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_shutdown_timer(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_with_options(instance_id, headers, runtime)

    def get_instance_shutdown_timer_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimer',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/shutdownTimer' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_snapshot(self, instance_id, instance_snapshot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_with_options(instance_id, instance_snapshot_id, headers, runtime)

    def get_instance_snapshot_with_options(self, instance_id, instance_snapshot_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/snapshots/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(instance_snapshot_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instances_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instances_statistics_with_options(request, headers, runtime)

    def get_instances_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesStatistics',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/statistics/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstancesStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ecs_specs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    def list_ecs_specs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/ecsSpecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    def list_images_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type_equals):
            query['AcceleratorTypeEquals'] = request.accelerator_type_equals
        if not UtilClient.is_unset(request.image_name_contains):
            query['ImageNameContains'] = request.image_name_contains
        if not UtilClient.is_unset(request.image_type_equals):
            query['ImageTypeEquals'] = request.image_type_equals
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_snapshots(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshots_with_options(instance_id, headers, runtime)

    def list_instance_snapshots_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInstanceSnapshots',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.in_workspace):
            query['InWorkspace'] = request.in_workspace
        if not UtilClient.is_unset(request.instance_name_contains):
            query['InstanceNameContains'] = request.instance_name_contains
        if not UtilClient.is_unset(request.instance_status_equals):
            query['InstanceStatusEquals'] = request.instance_status_equals
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.workspace_id_equals):
            query['WorkspaceIdEquals'] = request.workspace_id_equals
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_status_with_options(request, headers, runtime)

    def list_instances_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesStatus',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/statuses/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_with_options(instance_id, headers, runtime)

    def start_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/start' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, request, headers, runtime)

    def stop_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.save_image):
            query['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/stop' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_snapshot(self, instance_id, instance_snapshot_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_snapshot_with_options(instance_id, instance_snapshot_id, request, headers, runtime)

    def update_instance_snapshot_with_options(self, instance_id, instance_snapshot_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        instance_snapshot_id = OpenApiUtilClient.get_encode_param(instance_snapshot_id)
        body = {}
        if not UtilClient.is_unset(request.instance_snapshot_name):
            body['InstanceSnapshotName'] = request.instance_snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSnapshot',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/snapshots/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(instance_snapshot_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def update_v3instance_by_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_v3instance_by_user_with_options(request, headers, runtime)

    def update_v3instance_by_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateV3InstanceByUser',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/instances/migrate/user',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateV3InstanceByUserResponse(),
            self.call_api(params, req, runtime)
        )
