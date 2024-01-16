# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sophonsoar20220728 import models as sophonsoar_20220728_models
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
        self._endpoint = self.get_endpoint('sophonsoar', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_modify_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_modify_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_modify_instance_status_with_options(request, runtime)

    def compare_playbooks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not UtilClient.is_unset(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComparePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ComparePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    def compare_playbooks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_playbooks_with_options(request, runtime)

    def create_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.CreatePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_playbook_with_options(request, runtime)

    def debug_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.record):
            body['Record'] = request.record
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DebugPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def debug_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.debug_playbook_with_options(request, runtime)

    def delete_component_asset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeleteComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_component_asset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_component_asset_with_options(request, runtime)

    def delete_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DeletePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_playbook_with_options(request, runtime)

    def describe_api_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeApiListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_list_with_options(request, runtime)

    def describe_component_asset_form_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssetForm',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component_asset_form(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_component_asset_form_with_options(request, runtime)

    def describe_component_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssets',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_component_assets_with_options(request, runtime)

    def describe_component_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_component_list_with_options(request, runtime)

    def describe_component_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_component_playbook_with_options(request, runtime)

    def describe_components_js_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentsJs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeComponentsJsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_components_js(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_components_js_with_options(request, runtime)

    def describe_distinct_releases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistinctReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_distinct_releases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_distinct_releases_with_options(request, runtime)

    def describe_enum_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnumItems',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeEnumItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_enum_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_enum_items_with_options(request, runtime)

    def describe_execute_playbooks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_execute_playbooks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_execute_playbooks_with_options(request, runtime)

    def describe_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeField',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_field_with_options(request, runtime)

    def describe_latest_record_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLatestRecordSchema',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_latest_record_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_record_schema_with_options(request, runtime)

    def describe_node_param_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeParamTags',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_param_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_param_tags_with_options(request, runtime)

    def describe_node_used_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeUsedInfos',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_used_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_used_infos_with_options(request, runtime)

    def describe_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_with_options(request, runtime)

    def describe_playbook_input_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook_input_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_input_output_with_options(request, runtime)

    def describe_playbook_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_metrics_with_options(request, runtime)

    def describe_playbook_nodes_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNodesOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook_nodes_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_nodes_output_with_options(request, runtime)

    def describe_playbook_number_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNumberMetrics',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook_number_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_number_metrics_with_options(request, runtime)

    def describe_playbook_releases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookReleases',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbook_releases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_releases_with_options(request, runtime)

    def describe_playbooks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybooks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePlaybooksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_playbooks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_playbooks_with_options(request, runtime)

    def describe_pop_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApi',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pop_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_with_options(request, runtime)

    def describe_pop_api_item_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiItemList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiItemListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pop_api_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_item_list_with_options(request, runtime)

    def describe_pop_api_version_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiVersionList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribePopApiVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pop_api_version_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_version_list_with_options(request, runtime)

    def describe_process_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTasks',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeProcessTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_process_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_process_tasks_with_options(request, runtime)

    def describe_soar_record_action_output_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordActionOutputList',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_soar_record_action_output_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_action_output_list_with_options(request, runtime)

    def describe_soar_record_in_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordInOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_soar_record_in_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_in_output_with_options(request, runtime)

    def describe_soar_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecords',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_soar_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_records_with_options(request, runtime)

    def describe_soar_task_and_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarTaskAndActions',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_soar_task_and_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_task_and_actions_with_options(request, runtime)

    def describe_sophon_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSophonCommands',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sophon_commands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sophon_commands_with_options(request, runtime)

    def describer_python_3script_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescriberPython3ScriptLogs',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describer_python_3script_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describer_python_3script_logs_with_options(request, runtime)

    def modify_component_asset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyComponentAsset',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyComponentAssetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_component_asset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_component_asset_with_options(request, runtime)

    def modify_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_with_options(request, runtime)

    def modify_playbook_input_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not UtilClient.is_unset(request.input_params):
            body['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.output_params):
            body['OutputParams'] = request.output_params
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInputOutput',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_playbook_input_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_input_output_with_options(request, runtime)

    def modify_playbook_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInstanceStatus',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_playbook_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_instance_status_with_options(request, runtime)

    def publish_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.PublishPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_playbook_with_options(request, runtime)

    def query_tree_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTreeData',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.QueryTreeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tree_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tree_data_with_options(request, runtime)

    def rename_playbook_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not UtilClient.is_unset(request.old_node_name):
            query['OldNodeName'] = request.old_node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenamePlaybookNode',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def rename_playbook_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rename_playbook_node_with_options(request, runtime)

    def revert_playbook_release_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not UtilClient.is_unset(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertPlaybookRelease',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    def revert_playbook_release(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revert_playbook_release_with_options(request, runtime)

    def run_python_3script_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: RunPython3ScriptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunPython3ScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPython3Script',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.RunPython3ScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def run_python_3script(self, request):
        """
        Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: RunPython3ScriptRequest

        @return: RunPython3ScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_python_3script_with_options(request, runtime)

    def trigger_playbook_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: TriggerPlaybookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TriggerPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_param):
            body['InputParam'] = request.input_param
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_playbook(self, request):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: TriggerPlaybookRequest

        @return: TriggerPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_playbook_with_options(request, runtime)

    def trigger_process_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerProcessTask',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerProcessTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_process_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_process_task_with_options(request, runtime)

    def trigger_sophon_playbook_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: TriggerSophonPlaybookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TriggerSophonPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.input_params):
            query['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSophonPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_sophon_playbook(self, request):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.aliyun.com/price/product#/sas/detail/sas).
        

        @param request: TriggerSophonPlaybookRequest

        @return: TriggerSophonPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_sophon_playbook_with_options(request, runtime)

    def verify_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPlaybook',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_playbook_with_options(request, runtime)

    def verify_python_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPythonFile',
            version='2022-07-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sophonsoar_20220728_models.VerifyPythonFileResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_python_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_python_file_with_options(request, runtime)
