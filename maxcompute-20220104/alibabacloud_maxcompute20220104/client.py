# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_maxcompute20220104 import models as max_compute_20220104_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'maxcompute.aliyuncs.com',
            'ap-northeast-2-pop': 'maxcompute.aliyuncs.com',
            'ap-south-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-2': 'maxcompute.aliyuncs.com',
            'ap-southeast-3': 'maxcompute.aliyuncs.com',
            'ap-southeast-5': 'maxcompute.aliyuncs.com',
            'cn-beijing': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-beijing-gov-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-nu16-b01': 'maxcompute.aliyuncs.com',
            'cn-chengdu': 'maxcompute.aliyuncs.com',
            'cn-edge-1': 'maxcompute.aliyuncs.com',
            'cn-fujian': 'maxcompute.aliyuncs.com',
            'cn-haidian-cm12-c01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-finance': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-test-306': 'maxcompute.aliyuncs.com',
            'cn-hongkong': 'maxcompute.aliyuncs.com',
            'cn-hongkong-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-huhehaote': 'maxcompute.aliyuncs.com',
            'cn-north-2-gov-1': 'maxcompute.aliyuncs.com',
            'cn-qingdao': 'maxcompute.aliyuncs.com',
            'cn-qingdao-nebula': 'maxcompute.aliyuncs.com',
            'cn-shanghai': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et15-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et2-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shanghai-inner': 'maxcompute.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-inner': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'maxcompute.aliyuncs.com',
            'cn-wuhan': 'maxcompute.aliyuncs.com',
            'cn-yushanfang': 'maxcompute.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'maxcompute.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'maxcompute.aliyuncs.com',
            'eu-central-1': 'maxcompute.aliyuncs.com',
            'eu-west-1': 'maxcompute.aliyuncs.com',
            'eu-west-1-oxs': 'maxcompute.aliyuncs.com',
            'me-east-1': 'maxcompute.aliyuncs.com',
            'rus-west-1-pop': 'maxcompute.aliyuncs.com',
            'us-east-1': 'maxcompute.aliyuncs.com',
            'us-west-1': 'maxcompute.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('maxcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_package_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/packages' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_package(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_package_with_options(project_name, request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_quota_plan_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/plans' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quota_plan(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_plan_with_options(nickname, request, headers, runtime)

    def create_quota_schedule_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/schedule' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quota_schedule(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_schedule_with_options(nickname, request, headers, runtime)

    def create_role_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_role(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(project_name, request, headers, runtime)

    def delete_quota_plan_with_options(self, nickname, plan_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/plans/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(plan_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quota_plan(self, nickname, plan_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    def get_job_resource_usage_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetJobResourceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResourceUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/jobs/resourceUsage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_resource_usage_with_options(request, headers, runtime)

    def get_package_with_options(self, project_name, package_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/packages/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(package_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_package(self, project_name, package_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_package_with_options(project_name, package_name, request, headers, runtime)

    def get_project_with_options(self, project_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project(self, project_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_name, headers, runtime)

    def get_quota_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(nickname, request, headers, runtime)

    def get_quota_plan_with_options(self, nickname, plan_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/plans/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(plan_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota_plan(self, nickname, plan_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    def get_quota_schedule_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/schedule' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota_schedule(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_schedule_with_options(nickname, request, headers, runtime)

    def get_role_acl_with_options(self, project_name, role_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRoleAcl',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles/%s/roleAcl' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(role_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role_acl(self, project_name, role_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_with_options(project_name, role_name, headers, runtime)

    def get_role_acl_on_object_with_options(self, project_name, role_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoleAclOnObject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles/%s/acl' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(role_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclOnObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role_acl_on_object(self, project_name, role_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_on_object_with_options(project_name, role_name, request, headers, runtime)

    def get_role_policy_with_options(self, project_name, role_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRolePolicy',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles/%s/policy' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(role_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRolePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role_policy(self, project_name, role_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_policy_with_options(project_name, role_name, headers, runtime)

    def get_running_jobs_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetRunningJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/jobs/runningJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRunningJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_running_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_running_jobs_with_options(request, headers, runtime)

    def get_trusted_projects_with_options(self, project_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrustedProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/trustedProjects' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTrustedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trusted_projects(self, project_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trusted_projects_with_options(project_name, headers, runtime)

    def kill_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='KillJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/jobs/kill',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.KillJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def kill_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.kill_jobs_with_options(request, headers, runtime)

    def list_functions_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/functions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_functions(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(project_name, request, headers, runtime)

    def list_packages_with_options(self, project_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPackages',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/packages' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_packages(self, project_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_packages_with_options(project_name, headers, runtime)

    def list_project_users_with_options(self, project_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/users' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_users(self, project_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_users_with_options(project_name, headers, runtime)

    def list_projects_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.quota_name):
            query['quotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    def list_quotas_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quotas(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    def list_quotas_plans_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotasPlans',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/plans' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quotas_plans(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_plans_with_options(nickname, request, headers, runtime)

    def list_resources_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/resources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(project_name, request, headers, runtime)

    def list_roles_with_options(self, project_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_roles(self, project_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(project_name, headers, runtime)

    def list_tables_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/tables' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tables(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(project_name, request, headers, runtime)

    def list_users_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    def list_users_by_role_with_options(self, project_name, role_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsersByRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/roles/%s/users' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(role_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersByRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users_by_role(self, project_name, role_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_by_role_with_options(project_name, role_name, headers, runtime)

    def update_package_with_options(self, project_name, package_name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/packages/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(package_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_package(self, project_name, package_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_package_with_options(project_name, package_name, request, headers, runtime)

    def update_project_ip_white_list_with_options(self, project_name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateProjectIpWhiteList',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/projects/%s/ipWhiteList' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project_ip_white_list(self, project_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_ip_white_list_with_options(project_name, request, headers, runtime)

    def update_quota_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.ak_proven):
            real_headers['AkProven'] = UtilClient.to_jsonstring(headers.ak_proven)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quota(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = max_compute_20220104_models.UpdateQuotaHeaders()
        return self.update_quota_with_options(nickname, request, headers, runtime)

    def update_quota_plan_with_options(self, nickname, plan_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/plans/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(plan_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quota_plan(self, nickname, plan_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    def update_quota_schedule_with_options(self, nickname, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname='/api/v1/quotas/%s/schedule' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nickname)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quota_schedule(self, nickname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_schedule_with_options(nickname, request, headers, runtime)
