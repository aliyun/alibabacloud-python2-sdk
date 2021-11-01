# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_foasconsole20190601 import models as foasconsole_20190601_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('foasconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def convert_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ConvertInstanceResponse(),
            self.do_rpcrequest('ConvertInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.CreateNamespaceResponse(),
            self.do_rpcrequest('CreateNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DeleteNamespaceResponse(),
            self.do_rpcrequest('DeleteNamespace', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_namespaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.DescribeNamespacesResponse(),
            self.do_rpcrequest('DescribeNamespaces', '2019-06-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_namespaces_with_options(request, runtime)

    def modify_prepay_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayInstanceSpecResponse(),
            self.do_rpcrequest('ModifyPrepayInstanceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    def modify_prepay_namespace_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.ModifyPrepayNamespaceSpecResponse(),
            self.do_rpcrequest('ModifyPrepayNamespaceSpec', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_namespace_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_namespace_spec_with_options(request, runtime)

    def query_convert_instance_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.QueryConvertInstancePriceResponse(),
            self.do_rpcrequest('QueryConvertInstancePrice', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_convert_instance_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_convert_instance_price_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            foasconsole_20190601_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)
