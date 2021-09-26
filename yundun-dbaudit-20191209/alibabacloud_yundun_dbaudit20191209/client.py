# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20191209 import models as yundun_dbaudit_20191209_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def clear_instance_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ClearInstanceStorageResponse(),
            self.do_rpcrequest('ClearInstanceStorage', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_instance_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_instance_storage_with_options(request, runtime)

    def config_instance_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ConfigInstanceWhiteListResponse(),
            self.do_rpcrequest('ConfigInstanceWhiteList', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instance_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.DescribeInstanceStorageResponse(),
            self.do_rpcrequest('DescribeInstanceStorage', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def disable_instance_public_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.DisableInstancePublicAccessResponse(),
            self.do_rpcrequest('DisableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_instance_public_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    def enable_instance_public_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.EnableInstancePublicAccessResponse(),
            self.do_rpcrequest('EnableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_public_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_instance_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.ModifyInstanceStorageResponse(),
            self.do_rpcrequest('ModifyInstanceStorage', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_storage_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20191209_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
