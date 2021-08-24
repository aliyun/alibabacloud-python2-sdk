# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenest20210601 import models as compute_nest_20210601_models
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
        self._endpoint = self.get_endpoint('computenest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def continue_deploy_service_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ContinueDeployServiceInstanceResponse(),
            self.do_rpcrequest('ContinueDeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continue_deploy_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    def create_service_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceInstanceResponse(),
            self.do_rpcrequest('CreateServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    def delete_service_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeleteServiceInstancesResponse(),
            self.do_rpcrequest('DeleteServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    def deploy_service_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeployServiceInstanceResponse(),
            self.do_rpcrequest('DeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_service_instance_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceResponse(),
            self.do_rpcrequest('GetService', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    def get_service_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceResponse(),
            self.do_rpcrequest('GetServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    def list_inuse_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListInuseServicesResponse(),
            self.do_rpcrequest('ListInuseServices', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_inuse_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_inuse_services_with_options(request, runtime)

    def list_service_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstancesResponse(),
            self.do_rpcrequest('ListServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)
