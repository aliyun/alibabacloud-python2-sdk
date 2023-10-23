# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ots20160620 import models as ots_20160620_models
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
        self._endpoint = self.get_endpoint('ots', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_instance_2vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.virtual_switch_id):
            query['VirtualSwitchId'] = request.virtual_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.BindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_instance_2vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_instance_2vpc_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_ots_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOtsServiceStatus',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetOtsServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ots_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ots_service_status_with_options(request, runtime)

    def insert_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_instance_with_options(request, runtime)

    def insert_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_tags_with_options(request, runtime)

    def list_cluster_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterType',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListClusterTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_type_with_options(request, runtime)

    def list_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    def list_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    def list_vpc_info_by_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpc_info_by_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_info_by_instance_with_options(request, runtime)

    def list_vpc_info_by_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByVpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpc_info_by_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_info_by_vpc_with_options(request, runtime)

    def open_ots_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenOtsService',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.OpenOtsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_ots_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_ots_service_with_options(runtime)

    def unbind_instance_2vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UnbindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_instance_2vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_instance_2vpc_with_options(request, runtime)

    def update_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)
