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

    def create_instance_shutdown_timer_v2(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_shutdown_timer_v2with_options(instance_id, request, headers, runtime)

    def create_instance_shutdown_timer_v2with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['DueTime'] = request.due_time
        if not UtilClient.is_unset(request.remaining_time_in_ms):
            body['RemainingTimeInMs'] = request.remaining_time_in_ms
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/shutdowntimer' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceShutdownTimerV2Response(),
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

    def create_instance_snapshot_v2(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_snapshot_v2with_options(instance_id, request, headers, runtime)

    def create_instance_snapshot_v2with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.snapshot_description):
            body['SnapshotDescription'] = request.snapshot_description
        if not UtilClient.is_unset(request.snapshot_name):
            body['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    def create_instance_v2(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_v2with_options(request, headers, runtime)

    def create_instance_v2with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.CreateInstanceV2Response(),
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

    def delete_instance_shutdown_timer_v2(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_shutdown_timer_v2with_options(instance_id, headers, runtime)

    def delete_instance_shutdown_timer_v2with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/shutdowntimer' % TeaConverter.to_unicode(instance_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceShutdownTimerV2Response(),
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

    def delete_instance_snapshot_v2(self, instance_id, snapshot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_snapshot_v2with_options(instance_id, snapshot_id, headers, runtime)

    def delete_instance_snapshot_v2with_options(self, instance_id, snapshot_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/snapshots/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(snapshot_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    def delete_instance_v2(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_v2with_options(instance_id, headers, runtime)

    def delete_instance_v2with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.DeleteInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    def foobar(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.foobar_with_options(headers, runtime)

    def foobar_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Foobar',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/foobar',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.FoobarResponse(),
            self.call_api(params, req, runtime)
        )

    def foobar_1(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.foobar_1with_options(headers, runtime)

    def foobar_1with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Foobar1',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v1/foobar1',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.Foobar1Response(),
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

    def get_instance_shutdown_timer_v2(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_shutdown_timer_v2with_options(instance_id, headers, runtime)

    def get_instance_shutdown_timer_v2with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceShutdownTimerV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/shutdowntimer' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceShutdownTimerV2Response(),
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

    def get_instance_snapshot_v2(self, instance_id, snapshot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_snapshot_v2with_options(instance_id, snapshot_id, headers, runtime)

    def get_instance_snapshot_v2with_options(self, instance_id, snapshot_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        snapshot_id = OpenApiUtilClient.get_encode_param(snapshot_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/snapshots/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(snapshot_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceSnapshotV2Response(),
            self.call_api(params, req, runtime)
        )

    def get_instance_v2(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_v2with_options(instance_id, headers, runtime)

    def get_instance_v2with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetInstanceV2Response(),
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

    def get_user_config_v2(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_config_v2with_options(headers, runtime)

    def get_user_config_v2with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUserConfigV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/userconfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.GetUserConfigV2Response(),
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

    def list_ecs_specs_v2(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_v2with_options(request, headers, runtime)

    def list_ecs_specs_v2with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
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
            action='ListEcsSpecsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListEcsSpecsV2Response(),
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

    def list_instance_snapshot_v2(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_snapshot_v2with_options(instance_id, request, headers, runtime)

    def list_instance_snapshot_v2with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='ListInstanceSnapshotV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceSnapshotV2Response(),
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

    def list_instance_statistics_v2(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_statistics_v2with_options(request, headers, runtime)

    def list_instance_statistics_v2with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatisticsV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instancestatistics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstanceStatisticsV2Response(),
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

    def list_instances_v2(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_v2with_options(request, headers, runtime)

    def list_instances_v2with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action='ListInstancesV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.ListInstancesV2Response(),
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

    def start_instance_v2(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_instance_v2with_options(instance_id, headers, runtime)

    def start_instance_v2with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/start' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StartInstanceV2Response(),
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

    def stop_instance_v2(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_v2with_options(instance_id, request, headers, runtime)

    def stop_instance_v2with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.save_image):
            body['SaveImage'] = request.save_image
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s/stop' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.StopInstanceV2Response(),
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

    def update_instance_v2(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_v2with_options(instance_id, request, headers, runtime)

    def update_instance_v2with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.accelerator_type):
            body['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.accumulated_running_time_in_ms):
            body['AccumulatedRunningTimeInMs'] = request.accumulated_running_time_in_ms
        if not UtilClient.is_unset(request.datasets):
            body['Datasets'] = request.datasets
        if not UtilClient.is_unset(request.ecs_spec):
            body['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.environment_variables):
            body['EnvironmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.gmt_create_time):
            body['GmtCreateTime'] = request.gmt_create_time
        if not UtilClient.is_unset(request.gmt_modified_time):
            body['GmtModifiedTime'] = request.gmt_modified_time
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_shutdown_timer):
            body['InstanceShutdownTimer'] = request.instance_shutdown_timer
        if not UtilClient.is_unset(request.instance_url):
            body['InstanceUrl'] = request.instance_url
        if not UtilClient.is_unset(request.jupyterlab_url):
            body['JupyterlabUrl'] = request.jupyterlab_url
        if not UtilClient.is_unset(request.latest_snapshot):
            body['LatestSnapshot'] = request.latest_snapshot
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.reason_code):
            body['ReasonCode'] = request.reason_code
        if not UtilClient.is_unset(request.reason_message):
            body['ReasonMessage'] = request.reason_message
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.terminal_url):
            body['TerminalUrl'] = request.terminal_url
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.web_ideurl):
            body['WebIDEUrl'] = request.web_ideurl
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.workspace_name):
            body['WorkspaceName'] = request.workspace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceV2',
            version='2021-02-26',
            protocol='HTTPS',
            pathname='/api/v2/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dsw_20210226_models.UpdateInstanceV2Response(),
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
