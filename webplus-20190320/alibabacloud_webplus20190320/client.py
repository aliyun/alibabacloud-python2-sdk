# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_webplus20190320 import models as web_plus_20190320_models
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
            'cn-beijing': 'webplus.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'webplus.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'webplus.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'webplus.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'webplus.aliyuncs.com',
            'ap-south-1': 'webplus.aliyuncs.com',
            'ap-southeast-1': 'webplus.aliyuncs.com',
            'ap-southeast-2': 'webplus.aliyuncs.com',
            'ap-southeast-3': 'webplus.aliyuncs.com',
            'ap-southeast-5': 'webplus.aliyuncs.com',
            'cn-chengdu': 'webplus.aliyuncs.com',
            'cn-hongkong': 'webplus-vpc.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'webplus.aliyuncs.com',
            'cn-qingdao': 'webplus.aliyuncs.com',
            'eu-central-1': 'webplus.aliyuncs.com',
            'eu-west-1': 'webplus.aliyuncs.com',
            'me-east-1': 'webplus.aliyuncs.com',
            'us-east-1': 'webplus.aliyuncs.com',
            'us-west-1': 'webplus.aliyuncs.com',
            'cn-hangzhou-finance': 'webplus.aliyuncs.com',
            'cn-shenzhen-finance-1': 'webplus.aliyuncs.com',
            'cn-shanghai-finance-1': 'webplus.aliyuncs.com',
            'cn-north-2-gov-1': 'webplus.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('webplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_change(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_change_with_options(request, headers, runtime)

    def abort_change_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.change_id):
            body['ChangeId'] = request.change_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.AbortChangeResponse().from_map(
            self.do_roarequest_with_form('AbortChange', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/change/abort', 'json', req, runtime)
        )

    def create_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_env_with_options(request, headers, runtime)

    def create_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_name):
            body['EnvName'] = request.env_name
        if not UtilClient.is_unset(request.env_description):
            body['EnvDescription'] = request.env_description
        if not UtilClient.is_unset(request.stack_id):
            body['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pkg_version_id):
            body['PkgVersionId'] = request.pkg_version_id
        if not UtilClient.is_unset(request.option_settings):
            body['OptionSettings'] = request.option_settings
        if not UtilClient.is_unset(request.profile_name):
            body['ProfileName'] = request.profile_name
        if not UtilClient.is_unset(request.source_env_id):
            body['SourceEnvId'] = request.source_env_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.extra_properties):
            body['ExtraProperties'] = request.extra_properties
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.CreateAppEnvResponse().from_map(
            self.do_roarequest_with_form('CreateAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv', 'json', req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    def create_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_description):
            body['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.using_shared_storage):
            body['UsingSharedStorage'] = request.using_shared_storage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.CreateApplicationResponse().from_map(
            self.do_roarequest_with_form('CreateApplication', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/application', 'json', req, runtime)
        )

    def create_config_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_template_with_options(request, headers, runtime)

    def create_config_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_description):
            body['TemplateDescription'] = request.template_description
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.stack_id):
            body['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.source_template_id):
            body['SourceTemplateId'] = request.source_template_id
        if not UtilClient.is_unset(request.source_env_id):
            body['SourceEnvId'] = request.source_env_id
        if not UtilClient.is_unset(request.profile_name):
            body['ProfileName'] = request.profile_name
        if not UtilClient.is_unset(request.pkg_version_id):
            body['PkgVersionId'] = request.pkg_version_id
        if not UtilClient.is_unset(request.option_settings):
            body['OptionSettings'] = request.option_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.CreateConfigTemplateResponse().from_map(
            self.do_roarequest_with_form('CreateConfigTemplate', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/configTemplate', 'json', req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_order_with_options(request, headers, runtime)

    def create_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.CreateOrderResponse().from_map(
            self.do_roarequest_with_form('CreateOrder', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/paas/createOrder', 'json', req, runtime)
        )

    def create_pkg_version(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pkg_version_with_options(request, headers, runtime)

    def create_pkg_version_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.pkg_version_label):
            body['PkgVersionLabel'] = request.pkg_version_label
        if not UtilClient.is_unset(request.pkg_version_description):
            body['PkgVersionDescription'] = request.pkg_version_description
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_source):
            body['PackageSource'] = request.package_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.CreatePkgVersionResponse().from_map(
            self.do_roarequest_with_form('CreatePkgVersion', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/pkgVersion', 'json', req, runtime)
        )

    def create_storage(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_storage_with_options(request, headers, runtime)

    def create_storage_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.CreateStorageResponse().from_map(
            self.do_roarequest('CreateStorage', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/storage', 'json', req, runtime)
        )

    def delete_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_env_with_options(request, headers, runtime)

    def delete_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DeleteAppEnvResponse().from_map(
            self.do_roarequest('DeleteAppEnv', '2019-03-20', 'HTTPS', 'DELETE', 'AK', '/pop/v1/wam/appEnv', 'json', req, runtime)
        )

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    def delete_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DeleteApplicationResponse().from_map(
            self.do_roarequest('DeleteApplication', '2019-03-20', 'HTTPS', 'DELETE', 'AK', '/pop/v1/wam/application', 'json', req, runtime)
        )

    def delete_change(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_change_with_options(request, headers, runtime)

    def delete_change_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_id):
            query['ChangeId'] = request.change_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DeleteChangeResponse().from_map(
            self.do_roarequest('DeleteChange', '2019-03-20', 'HTTPS', 'DELETE', 'AK', '/pop/v1/wam/change', 'json', req, runtime)
        )

    def delete_config_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_template_with_options(request, headers, runtime)

    def delete_config_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DeleteConfigTemplateResponse().from_map(
            self.do_roarequest('DeleteConfigTemplate', '2019-03-20', 'HTTPS', 'DELETE', 'AK', '/pop/v1/wam/configTemplate', 'json', req, runtime)
        )

    def delete_pkg_version(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pkg_version_with_options(request, headers, runtime)

    def delete_pkg_version_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pkg_version_id):
            query['PkgVersionId'] = request.pkg_version_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DeletePkgVersionResponse().from_map(
            self.do_roarequest('DeletePkgVersion', '2019-03-20', 'HTTPS', 'DELETE', 'AK', '/pop/v1/wam/pkgVersion', 'json', req, runtime)
        )

    def deploy_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_app_env_with_options(request, headers, runtime)

    def deploy_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.batch_percent):
            body['BatchPercent'] = request.batch_percent
        if not UtilClient.is_unset(request.batch_interval):
            body['BatchInterval'] = request.batch_interval
        if not UtilClient.is_unset(request.pause_between_batches):
            body['PauseBetweenBatches'] = request.pause_between_batches
        if not UtilClient.is_unset(request.pkg_version_id):
            body['PkgVersionId'] = request.pkg_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.DeployAppEnvResponse().from_map(
            self.do_roarequest_with_form('DeployAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/deploy', 'json', req, runtime)
        )

    def describe_app_env_instance_health(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_env_instance_health_with_options(request, headers, runtime)

    def describe_app_env_instance_health_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeAppEnvInstanceHealthResponse().from_map(
            self.do_roarequest('DescribeAppEnvInstanceHealth', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/appEnv/instanceHealth', 'json', req, runtime)
        )

    def describe_app_envs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_envs_with_options(request, headers, runtime)

    def describe_app_envs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.include_terminated):
            query['IncludeTerminated'] = request.include_terminated
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.env_name):
            query['EnvName'] = request.env_name
        if not UtilClient.is_unset(request.env_search):
            query['EnvSearch'] = request.env_search
        if not UtilClient.is_unset(request.recent_updated):
            query['RecentUpdated'] = request.recent_updated
        if not UtilClient.is_unset(request.stack_search):
            query['StackSearch'] = request.stack_search
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeAppEnvsResponse().from_map(
            self.do_roarequest('DescribeAppEnvs', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/appEnv', 'json', req, runtime)
        )

    def describe_app_env_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_env_status_with_options(request, headers, runtime)

    def describe_app_env_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeAppEnvStatusResponse().from_map(
            self.do_roarequest('DescribeAppEnvStatus', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/appEnv/status', 'json', req, runtime)
        )

    def describe_applications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_applications_with_options(request, headers, runtime)

    def describe_applications_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_search):
            query['AppSearch'] = request.app_search
        if not UtilClient.is_unset(request.env_search):
            query['EnvSearch'] = request.env_search
        if not UtilClient.is_unset(request.stack_search):
            query['StackSearch'] = request.stack_search
        if not UtilClient.is_unset(request.category_search):
            query['CategorySearch'] = request.category_search
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeApplicationsResponse().from_map(
            self.do_roarequest('DescribeApplications', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/application', 'json', req, runtime)
        )

    def describe_categories(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_categories_with_options(request, headers, runtime)

    def describe_categories_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeCategoriesResponse().from_map(
            self.do_roarequest('DescribeCategories', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/category', 'json', req, runtime)
        )

    def describe_change(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_change_with_options(request, headers, runtime)

    def describe_change_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.change_id):
            query['ChangeId'] = request.change_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeChangeResponse().from_map(
            self.do_roarequest('DescribeChange', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/changeInfo', 'json', req, runtime)
        )

    def describe_changes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_changes_with_options(request, headers, runtime)

    def describe_changes_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeChangesResponse().from_map(
            self.do_roarequest('DescribeChanges', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/change', 'json', req, runtime)
        )

    def describe_config_index(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_index_with_options(request, headers, runtime)

    def describe_config_index_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.profile_name):
            query['ProfileName'] = request.profile_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeConfigIndexResponse().from_map(
            self.do_roarequest('DescribeConfigIndex', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/config/configIndex', 'json', req, runtime)
        )

    def describe_config_options(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_options_with_options(request, headers, runtime)

    def describe_config_options_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.profile_name):
            query['ProfileName'] = request.profile_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeConfigOptionsResponse().from_map(
            self.do_roarequest('DescribeConfigOptions', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/config/configOption', 'json', req, runtime)
        )

    def describe_config_settings(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_settings_with_options(request, headers, runtime)

    def describe_config_settings_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.path_name):
            query['PathName'] = request.path_name
        if not UtilClient.is_unset(request.option_name):
            query['OptionName'] = request.option_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeConfigSettingsResponse().from_map(
            self.do_roarequest('DescribeConfigSettings', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/config/configSetting', 'json', req, runtime)
        )

    def describe_config_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_templates_with_options(request, headers, runtime)

    def describe_config_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_search):
            query['TemplateSearch'] = request.template_search
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeConfigTemplatesResponse().from_map(
            self.do_roarequest('DescribeConfigTemplates', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/configTemplate', 'json', req, runtime)
        )

    def describe_env_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_env_resource_with_options(request, headers, runtime)

    def describe_env_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeEnvResourceResponse().from_map(
            self.do_roarequest('DescribeEnvResource', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/envResource', 'json', req, runtime)
        )

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_events_with_options(request, headers, runtime)

    def describe_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.change_id):
            query['ChangeId'] = request.change_id
        if not UtilClient.is_unset(request.last_change_events):
            query['LastChangeEvents'] = request.last_change_events
        if not UtilClient.is_unset(request.reverse_by_timestamp):
            query['ReverseByTimestamp'] = request.reverse_by_timestamp
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeEventsResponse().from_map(
            self.do_roarequest('DescribeEvents', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/event', 'json', req, runtime)
        )

    def describe_gather_log_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_gather_log_result_with_options(request, headers, runtime)

    def describe_gather_log_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_id):
            query['ChangeId'] = request.change_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeGatherLogResultResponse().from_map(
            self.do_roarequest('DescribeGatherLogResult', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/appEnv/gatherLog', 'json', req, runtime)
        )

    def describe_gather_stats_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_gather_stats_result_with_options(request, headers, runtime)

    def describe_gather_stats_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_id):
            query['ChangeId'] = request.change_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeGatherStatsResultResponse().from_map(
            self.do_roarequest('DescribeGatherStatsResult', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/appEnv/gatherStats', 'json', req, runtime)
        )

    def describe_instance_health(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_health_with_options(request, headers, runtime)

    def describe_instance_health_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeInstanceHealthResponse().from_map(
            self.do_roarequest('DescribeInstanceHealth', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/instance/health', 'json', req, runtime)
        )

    def describe_pkg_versions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pkg_versions_with_options(request, headers, runtime)

    def describe_pkg_versions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.pkg_version_label):
            query['PkgVersionLabel'] = request.pkg_version_label
        if not UtilClient.is_unset(request.pkg_version_search):
            query['PkgVersionSearch'] = request.pkg_version_search
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribePkgVersionsResponse().from_map(
            self.do_roarequest('DescribePkgVersions', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/pkgVersion', 'json', req, runtime)
        )

    def describe_public_config_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_public_config_templates_with_options(request, headers, runtime)

    def describe_public_config_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribePublicConfigTemplatesResponse().from_map(
            self.do_roarequest('DescribePublicConfigTemplates', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/publicConfigTemplate', 'json', req, runtime)
        )

    def describe_stacks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_stacks_with_options(request, headers, runtime)

    def describe_stacks_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.recommended_only):
            query['RecommendedOnly'] = request.recommended_only
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeStacksResponse().from_map(
            self.do_roarequest('DescribeStacks', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/stack', 'json', req, runtime)
        )

    def describe_storage(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_storage_with_options(request, headers, runtime)

    def describe_storage_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.using_shared_storage):
            query['UsingSharedStorage'] = request.using_shared_storage
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return web_plus_20190320_models.DescribeStorageResponse().from_map(
            self.do_roarequest('DescribeStorage', '2019-03-20', 'HTTPS', 'GET', 'AK', '/pop/v1/wam/storage', 'json', req, runtime)
        )

    def gather_app_env_log(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.gather_app_env_log_with_options(request, headers, runtime)

    def gather_app_env_log_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.target_instances):
            body['TargetInstances'] = request.target_instances
        if not UtilClient.is_unset(request.log_path):
            body['LogPath'] = request.log_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.GatherAppEnvLogResponse().from_map(
            self.do_roarequest_with_form('GatherAppEnvLog', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/gatherLog', 'json', req, runtime)
        )

    def gather_app_env_stats(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.gather_app_env_stats_with_options(request, headers, runtime)

    def gather_app_env_stats_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.target_instances):
            body['TargetInstances'] = request.target_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.GatherAppEnvStatsResponse().from_map(
            self.do_roarequest_with_form('GatherAppEnvStats', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/gatherStats', 'json', req, runtime)
        )

    def pause_change(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_change_with_options(request, headers, runtime)

    def pause_change_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.change_id):
            body['ChangeId'] = request.change_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.PauseChangeResponse().from_map(
            self.do_roarequest_with_form('PauseChange', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/change/pause', 'json', req, runtime)
        )

    def rebuild_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rebuild_app_env_with_options(request, headers, runtime)

    def rebuild_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.RebuildAppEnvResponse().from_map(
            self.do_roarequest_with_form('RebuildAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/rebuild', 'json', req, runtime)
        )

    def restart_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_app_env_with_options(request, headers, runtime)

    def restart_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.batch_percent):
            body['BatchPercent'] = request.batch_percent
        if not UtilClient.is_unset(request.batch_interval):
            body['BatchInterval'] = request.batch_interval
        if not UtilClient.is_unset(request.pause_between_batches):
            body['PauseBetweenBatches'] = request.pause_between_batches
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.RestartAppEnvResponse().from_map(
            self.do_roarequest_with_form('RestartAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/restart', 'json', req, runtime)
        )

    def resume_change(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_change_with_options(request, headers, runtime)

    def resume_change_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.change_id):
            body['ChangeId'] = request.change_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.ResumeChangeResponse().from_map(
            self.do_roarequest_with_form('ResumeChange', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/change/resume', 'json', req, runtime)
        )

    def start_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_app_env_with_options(request, headers, runtime)

    def start_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.StartAppEnvResponse().from_map(
            self.do_roarequest_with_form('StartAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/start', 'json', req, runtime)
        )

    def stop_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_app_env_with_options(request, headers, runtime)

    def stop_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.StopAppEnvResponse().from_map(
            self.do_roarequest_with_form('StopAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/stop', 'json', req, runtime)
        )

    def terminate_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_app_env_with_options(request, headers, runtime)

    def terminate_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.TerminateAppEnvResponse().from_map(
            self.do_roarequest_with_form('TerminateAppEnv', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/appEnv/terminate', 'json', req, runtime)
        )

    def update_app_env(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_env_with_options(request, headers, runtime)

    def update_app_env_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_description):
            body['EnvDescription'] = request.env_description
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.pkg_version_id):
            body['PkgVersionId'] = request.pkg_version_id
        if not UtilClient.is_unset(request.option_settings):
            body['OptionSettings'] = request.option_settings
        if not UtilClient.is_unset(request.stack_id):
            body['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.extra_properties):
            body['ExtraProperties'] = request.extra_properties
        if not UtilClient.is_unset(request.batch_size):
            body['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.batch_percent):
            body['BatchPercent'] = request.batch_percent
        if not UtilClient.is_unset(request.batch_interval):
            body['BatchInterval'] = request.batch_interval
        if not UtilClient.is_unset(request.pause_between_batches):
            body['PauseBetweenBatches'] = request.pause_between_batches
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.UpdateAppEnvResponse().from_map(
            self.do_roarequest_with_form('UpdateAppEnv', '2019-03-20', 'HTTPS', 'PUT', 'AK', '/pop/v1/wam/appEnv', 'json', req, runtime)
        )

    def update_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_with_options(request, headers, runtime)

    def update_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_description):
            body['AppDescription'] = request.app_description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.UpdateApplicationResponse().from_map(
            self.do_roarequest_with_form('UpdateApplication', '2019-03-20', 'HTTPS', 'PUT', 'AK', '/pop/v1/wam/application', 'json', req, runtime)
        )

    def update_config_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_template_with_options(request, headers, runtime)

    def update_config_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.template_description):
            body['TemplateDescription'] = request.template_description
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.option_settings):
            body['OptionSettings'] = request.option_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.UpdateConfigTemplateResponse().from_map(
            self.do_roarequest_with_form('UpdateConfigTemplate', '2019-03-20', 'HTTPS', 'PUT', 'AK', '/pop/v1/wam/configTemplate', 'json', req, runtime)
        )

    def validate_config_setting(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_config_setting_with_options(request, headers, runtime)

    def validate_config_setting_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.stack_id):
            body['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.option_settings):
            body['OptionSettings'] = request.option_settings
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return web_plus_20190320_models.ValidateConfigSettingResponse().from_map(
            self.do_roarequest_with_form('ValidateConfigSetting', '2019-03-20', 'HTTPS', 'POST', 'AK', '/pop/v1/wam/config/configSetting/validate', 'json', req, runtime)
        )
