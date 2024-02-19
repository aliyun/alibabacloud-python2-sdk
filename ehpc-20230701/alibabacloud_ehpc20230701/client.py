# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20230701 import models as ehpc20230701_models
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
        self._endpoint = self.get_endpoint('ehpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_image_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20230701_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.container_image_spec):
            request.container_image_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container_image_spec, 'ContainerImageSpec', 'json')
        if not UtilClient.is_unset(tmp_req.vmimage_spec):
            request.vmimage_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vmimage_spec, 'VMImageSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.container_image_spec_shrink):
            query['ContainerImageSpec'] = request.container_image_spec_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.vmimage_spec_shrink):
            query['VMImageSpec'] = request.vmimage_spec_shrink
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    def add_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    def create_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20230701_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deployment_policy):
            request.deployment_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_policy, 'DeploymentPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.tasks):
            request.tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.deployment_policy_shrink):
            query['DeploymentPolicy'] = request.deployment_policy_shrink
        if not UtilClient.is_unset(request.job_description):
            query['JobDescription'] = request.job_description
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.tasks_shrink):
            query['Tasks'] = request.tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    def delete_jobs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20230701_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_spec):
            request.job_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    def get_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    def get_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    def list_images_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20230701_models.ListImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_ids):
            request.image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_ids_shrink):
            query['ImageIds'] = request.image_ids_shrink
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    def list_jobs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20230701_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not UtilClient.is_unset(tmp_req.sort_by):
            request.sort_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_by, 'SortBy', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by_shrink):
            query['SortBy'] = request.sort_by_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    def remove_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20230701_models.RemoveImageResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_image_with_options(request, runtime)
