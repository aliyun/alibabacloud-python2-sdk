# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_paielasticdatasetaccelerator20220801 import models as paielastic_dataset_accelerator_20220801_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('paielasticdatasetaccelerator', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_endpoint_with_options(self, endpoint_id, slot_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints/%s/slots/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(endpoint_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.BindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_endpoint(self, endpoint_id, slot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    def create_endpoint_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            body['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_endpoint_with_options(request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_endpoint):
            body['MaxEndpoint'] = request.max_endpoint
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.provider_type):
            body['ProviderType'] = request.provider_type
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def create_slot_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_ids):
            body['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.endpoints):
            body['Endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_slot(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_slot_with_options(request, headers, runtime)

    def create_slots_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.slots):
            body['Slots'] = request.slots
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlots',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/batch/slots/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_slots(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_slots_with_options(request, headers, runtime)

    def create_tag_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tag_with_options(request, headers, runtime)

    def delete_endpoint_with_options(self, endpoint_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(endpoint_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_endpoint(self, endpoint_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_endpoint_with_options(endpoint_id, headers, runtime)

    def delete_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    def delete_slot_with_options(self, slot_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_slot(self, slot_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_slot_with_options(slot_id, request, headers, runtime)

    def delete_tag_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(request, headers, runtime)

    def describe_component_with_options(self, component_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.DescribeComponentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        query = {}
        if not UtilClient.is_unset(request.render_template):
            query['RenderTemplate'] = request.render_template
        if not UtilClient.is_unset(request.values_shrink):
            query['Values'] = request.values_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponent',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/components/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(component_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component(self, component_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_component_with_options(component_id, request, headers, runtime)

    def describe_endpoint_with_options(self, endpoint_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(endpoint_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_endpoint(self, endpoint_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_endpoint_with_options(endpoint_id, headers, runtime)

    def describe_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    def describe_slot_with_options(self, slot_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.DescribeSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slot(self, slot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_slot_with_options(slot_id, headers, runtime)

    def list_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
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
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    def list_endpoints_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpoints',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_endpoints(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_endpoints_with_options(request, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
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
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_slots_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.slot_ids):
            query['SlotIds'] = request.slot_ids
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            query['StorageUri'] = request.storage_uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlots',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_slots(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slots_with_options(request, headers, runtime)

    def list_tags_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    def query_instance_metrics_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/metrics/action/query' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instance_metrics(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_instance_metrics_with_options(instance_id, request, headers, runtime)

    def query_slot_metrics_with_options(self, slot_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlotMetrics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s/metrics/action/query' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QuerySlotMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_slot_metrics(self, slot_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_slot_metrics_with_options(slot_id, request, headers, runtime)

    def query_statistic_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatistic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/statistics/action/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.QueryStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def query_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_statistic_with_options(request, headers, runtime)

    def reload_slot_with_options(self, slot_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReloadSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s/action/reload' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.ReloadSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def reload_slot(self, slot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reload_slot_with_options(slot_id, headers, runtime)

    def stop_slot_with_options(self, slot_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s/action/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.StopSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_slot(self, slot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_slot_with_options(slot_id, headers, runtime)

    def unbind_endpoint_with_options(self, endpoint_id, slot_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEndpoint',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/endpoints/%s/slots/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(endpoint_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UnbindEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_endpoint(self, endpoint_id, slot_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_endpoint_with_options(endpoint_id, slot_id, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.max_slot):
            body['MaxSlot'] = request.max_slot
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    def update_slot_with_options(self, slot_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.life_cycle):
            body['LifeCycle'] = request.life_cycle
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_uri):
            body['StorageUri'] = request.storage_uri
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSlot',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/api/v1/slots/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(slot_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paielastic_dataset_accelerator_20220801_models.UpdateSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def update_slot(self, slot_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_slot_with_options(slot_id, request, headers, runtime)
