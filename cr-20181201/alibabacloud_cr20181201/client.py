# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cr20181201 import models as cr_20181201_models
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
        self._endpoint = self.get_endpoint('cr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_artifact_build_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_artifact_build_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_artifact_build_task_with_options(request, runtime)

    def cancel_repo_build_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CancelRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_repo_build_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_repo_build_record_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def create_artifact_build_rule_with_options(self, tmp_req, runtime):
        """
        The ID of the rule.
        

        @param tmp_req: CreateArtifactBuildRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateArtifactBuildRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.CreateArtifactBuildRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.scope_id):
            query['ScopeId'] = request.scope_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_artifact_build_rule(self, request):
        """
        The ID of the rule.
        

        @param request: CreateArtifactBuildRuleRequest

        @return: CreateArtifactBuildRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_artifact_build_rule_with_options(request, runtime)

    def create_build_record_by_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_build_record_by_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_build_record_by_record_with_options(request, runtime)

    def create_build_record_by_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBuildRecordByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateBuildRecordByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_build_record_by_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_build_record_by_rule_with_options(request, runtime)

    def create_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_chain_with_options(request, runtime)

    def create_chart_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_chart_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_chart_namespace_with_options(request, runtime)

    def create_chart_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_chart_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_chart_repository_with_options(request, runtime)

    def create_instance_endpoint_acl_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_endpoint_acl_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_endpoint_acl_policy_with_options(request, runtime)

    def create_instance_vpc_endpoint_linked_vpc_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: CreateInstanceVpcEndpointLinkedVpcRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_create_dnsrecord_in_pvzt):
            query['EnableCreateDNSRecordInPvzt'] = request.enable_create_dnsrecord_in_pvzt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_vpc_endpoint_linked_vpc(self, request):
        """
        The ID of the request.
        

        @param request: CreateInstanceVpcEndpointLinkedVpcRequest

        @return: CreateInstanceVpcEndpointLinkedVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    def create_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    def create_repo_build_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_build_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_build_rule_with_options(request, runtime)

    def create_repo_source_code_repo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_source_code_repo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_source_code_repo_with_options(request, runtime)

    def create_repo_sync_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.sync_rule_name):
            query['SyncRuleName'] = request.sync_rule_name
        if not UtilClient.is_unset(request.sync_scope):
            query['SyncScope'] = request.sync_scope
        if not UtilClient.is_unset(request.sync_trigger):
            query['SyncTrigger'] = request.sync_trigger
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace_name):
            query['TargetNamespaceName'] = request.target_namespace_name
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_sync_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_rule_with_options(request, runtime)

    def create_repo_sync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not UtilClient.is_unset(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not UtilClient.is_unset(request.target_tag):
            query['TargetTag'] = request.target_tag
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_sync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_task_with_options(request, runtime)

    def create_repo_sync_task_by_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoSyncTaskByRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoSyncTaskByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_sync_task_by_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_sync_task_by_rule_with_options(request, runtime)

    def create_repo_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_tag):
            query['FromTag'] = request.from_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.to_tag):
            query['ToTag'] = request.to_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_tag_with_options(request, runtime)

    def create_repo_tag_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_service):
            query['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTagScanTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTagScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_tag_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_tag_scan_task_with_options(request, runtime)

    def create_repo_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repo_trigger_with_options(request, runtime)

    def create_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_repository_with_options(request, runtime)

    def delete_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_chain_with_options(request, runtime)

    def delete_chart_namespace_with_options(self, request, runtime):
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        

        @param request: DeleteChartNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteChartNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_chart_namespace(self, request):
        """
        >  If you delete a chart namespace, all repositories in the namespace and the charts in all repositories are deleted.
        

        @param request: DeleteChartNamespaceRequest

        @return: DeleteChartNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_namespace_with_options(request, runtime)

    def delete_chart_release_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_chart_release(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_release_with_options(request, runtime)

    def delete_chart_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_chart_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_chart_repository_with_options(request, runtime)

    def delete_event_center_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_center_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_center_rule_with_options(request, runtime)

    def delete_instance_endpoint_acl_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceEndpointAclPolicy',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance_endpoint_acl_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_endpoint_acl_policy_with_options(request, runtime)

    def delete_instance_vpc_endpoint_linked_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceVpcEndpointLinkedVpc',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance_vpc_endpoint_linked_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    def delete_namespace_with_options(self, request, runtime):
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        

        @param request: DeleteNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_namespace(self, request):
        """
        > After you delete a namespace, all repositories in the namespace and all images in these repositories are deleted as well.
        

        @param request: DeleteNamespaceRequest

        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    def delete_repo_build_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_build_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_build_rule_with_options(request, runtime)

    def delete_repo_sync_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_sync_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_sync_rule_with_options(request, runtime)

    def delete_repo_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_tag_with_options(request, runtime)

    def delete_repo_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_repo_trigger_with_options(request, runtime)

    def delete_repository_with_options(self, request, runtime):
        """
        If you delete a repository, all images in the repository are also deleted.
        

        @param request: DeleteRepositoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRepositoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repository(self, request):
        """
        If you delete a repository, all images in the repository are also deleted.
        

        @param request: DeleteRepositoryRequest

        @return: DeleteRepositoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_repository_with_options(request, runtime)

    def get_artifact_build_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_artifact_build_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_build_rule_with_options(request, runtime)

    def get_artifact_build_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactBuildTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_artifact_build_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_build_task_with_options(request, runtime)

    def get_authorization_token_with_options(self, request, runtime):
        """
        The ID of the Container Registry instance.
        

        @param request: GetAuthorizationTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAuthorizationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetAuthorizationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization_token(self, request):
        """
        The ID of the Container Registry instance.
        

        @param request: GetAuthorizationTokenRequest

        @return: GetAuthorizationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_token_with_options(request, runtime)

    def get_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chain_with_options(request, runtime)

    def get_chart_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chart_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chart_namespace_with_options(request, runtime)

    def get_chart_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chart_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chart_repository_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_instance_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetInstanceCount',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_count(self):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_with_options(runtime)

    def get_instance_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_endpoint_with_options(request, runtime)

    def get_instance_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceUsage',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_usage_with_options(request, runtime)

    def get_instance_vpc_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceVpcEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetInstanceVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_vpc_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_vpc_endpoint_with_options(request, runtime)

    def get_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_with_options(request, runtime)

    def get_repo_build_record_with_options(self, request, runtime):
        """
        ***\
        

        @param request: GetRepoBuildRecordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRepoBuildRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_build_record(self, request):
        """
        ***\
        

        @param request: GetRepoBuildRecordRequest

        @return: GetRepoBuildRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_repo_build_record_with_options(request, runtime)

    def get_repo_build_record_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildRecordStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoBuildRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_build_record_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_build_record_status_with_options(request, runtime)

    def get_repo_source_code_repo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_source_code_repo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_source_code_repo_with_options(request, runtime)

    def get_repo_sync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_sync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_sync_task_with_options(request, runtime)

    def get_repo_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_with_options(request, runtime)

    def get_repo_tag_layers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagLayers',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagLayersResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_layers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_layers_with_options(request, runtime)

    def get_repo_tag_manifest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagManifest',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagManifestResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_manifest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_manifest_with_options(request, runtime)

    def get_repo_tag_scan_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_scan_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_scan_status_with_options(request, runtime)

    def get_repo_tag_scan_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepoTagScanSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_scan_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repo_tag_scan_summary_with_options(request, runtime)

    def get_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repository_with_options(request, runtime)

    def list_artifact_build_task_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactBuildTaskLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListArtifactBuildTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_artifact_build_task_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_build_task_log_with_options(request, runtime)

    def list_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chain_with_options(request, runtime)

    def list_chain_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChainInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChainInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chain_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chain_instance_with_options(request, runtime)

    def list_chart_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chart_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chart_namespace_with_options(request, runtime)

    def list_chart_release_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chart):
            query['Chart'] = request.chart
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRelease',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chart_release(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chart_release_with_options(request, runtime)

    def list_chart_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chart_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chart_repository_with_options(request, runtime)

    def list_event_center_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_center_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_center_record_with_options(request, runtime)

    def list_event_center_rule_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventCenterRuleName',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListEventCenterRuleNameResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_center_rule_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_center_rule_name_with_options(request, runtime)

    def list_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    def list_instance_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceEndpoint',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_endpoint_with_options(request, runtime)

    def list_instance_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceRegion',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListInstanceRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_region_with_options(request, runtime)

    def list_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_namespace_with_options(request, runtime)

    def list_repo_build_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecord',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_build_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_record_with_options(request, runtime)

    def list_repo_build_record_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRecordLog',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRecordLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_build_record_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_record_log_with_options(request, runtime)

    def list_repo_build_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_build_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_build_rule_with_options(request, runtime)

    def list_repo_sync_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_sync_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_sync_rule_with_options(request, runtime)

    def list_repo_sync_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.sync_record_id):
            query['SyncRecordId'] = request.sync_record_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoSyncTask',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_sync_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_sync_task_with_options(request, runtime)

    def list_repo_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTag',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_tag_with_options(request, runtime)

    def list_repo_tag_scan_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vul_query_key):
            query['VulQueryKey'] = request.vul_query_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTagScanResult',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTagScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_tag_scan_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_tag_scan_result_with_options(request, runtime)

    def list_repo_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repo_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repo_trigger_with_options(request, runtime)

    def list_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ListRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_repository_with_options(request, runtime)

    def reset_login_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetLoginPassword',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.ResetLoginPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_login_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_login_password_with_options(request, runtime)

    def update_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not UtilClient.is_unset(request.chain_id):
            query['ChainId'] = request.chain_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChain',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_chain_with_options(request, runtime)

    def update_chart_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_chart_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_chart_namespace_with_options(request, runtime)

    def update_chart_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateChartRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_chart_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_chart_repository_with_options(request, runtime)

    def update_event_center_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cr_20181201_models.UpdateEventCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespaces):
            request.namespaces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not UtilClient.is_unset(tmp_req.repo_names):
            request.repo_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.event_channel):
            query['EventChannel'] = request.event_channel
        if not UtilClient.is_unset(request.event_config):
            query['EventConfig'] = request.event_config
        if not UtilClient.is_unset(request.event_scope):
            query['EventScope'] = request.event_scope
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not UtilClient.is_unset(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not UtilClient.is_unset(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventCenterRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_event_center_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_event_center_rule_with_options(request, runtime)

    def update_instance_endpoint_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceEndpointStatus',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateInstanceEndpointStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_endpoint_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_endpoint_status_with_options(request, runtime)

    def update_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not UtilClient.is_unset(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_with_options(request, runtime)

    def update_repo_build_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_args):
            query['BuildArgs'] = request.build_args
        if not UtilClient.is_unset(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not UtilClient.is_unset(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not UtilClient.is_unset(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.platforms):
            query['Platforms'] = request.platforms
        if not UtilClient.is_unset(request.push_name):
            query['PushName'] = request.push_name
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo_build_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_repo_build_rule_with_options(request, runtime)

    def update_repo_source_code_repo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.code_repo_id):
            query['CodeRepoId'] = request.code_repo_id
        if not UtilClient.is_unset(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not UtilClient.is_unset(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not UtilClient.is_unset(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not UtilClient.is_unset(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoSourceCodeRepo',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo_source_code_repo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_repo_source_code_repo_with_options(request, runtime)

    def update_repo_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        if not UtilClient.is_unset(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepoTrigger',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_repo_trigger_with_options(request, runtime)

    def update_repository_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not UtilClient.is_unset(request.repo_type):
            query['RepoType'] = request.repo_type
        if not UtilClient.is_unset(request.summary):
            query['Summary'] = request.summary
        if not UtilClient.is_unset(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRepository',
            version='2018-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20181201_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repository(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_repository_with_options(request, runtime)
