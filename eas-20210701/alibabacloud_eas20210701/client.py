# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eas20210701 import models as eas_20210701_models
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
            'cn-beijing': 'pai-eas.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'pai-eas.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'pai-eas.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai-eas.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai-eas.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai-eas.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai-eas.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'pai-eas.ap-southeast-5.aliyuncs.com',
            'us-west-1': 'pai-eas.us-west-1.aliyuncs.com',
            'us-east-1': 'pai-eas.us-east-1.aliyuncs.com',
            'eu-central-1': 'pai-eas.eu-central-1.aliyuncs.com',
            'ap-south-1': 'pai-eas.ap-south-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'pai-eas.cn-shanghai-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'pai-eas.cn-north-2-gov-1.aliyuncs.com',
            'ap-northeast-1': 'eas.aliyuncs.com',
            'ap-northeast-2-pop': 'eas.aliyuncs.com',
            'ap-southeast-2': 'eas.aliyuncs.com',
            'ap-southeast-3': 'eas.aliyuncs.com',
            'cn-beijing-finance-1': 'eas.aliyuncs.com',
            'cn-beijing-finance-pop': 'eas.aliyuncs.com',
            'cn-beijing-gov-1': 'eas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'eas.aliyuncs.com',
            'cn-chengdu': 'pai-eas.cn-chengdu.aliyuncs.com',
            'cn-edge-1': 'eas.aliyuncs.com',
            'cn-fujian': 'eas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'eas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'eas.aliyuncs.com',
            'cn-hangzhou-finance': 'eas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'eas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'eas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'eas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'eas.aliyuncs.com',
            'cn-hangzhou-test-306': 'eas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'eas.aliyuncs.com',
            'cn-huhehaote': 'eas.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'eas.aliyuncs.com',
            'cn-qingdao': 'eas.aliyuncs.com',
            'cn-qingdao-nebula': 'eas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'eas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'eas.aliyuncs.com',
            'cn-shanghai-inner': 'eas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'eas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'eas.aliyuncs.com',
            'cn-shenzhen-inner': 'eas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'eas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'eas.aliyuncs.com',
            'cn-wuhan': 'eas.aliyuncs.com',
            'cn-wulanchabu': 'eas.aliyuncs.com',
            'cn-yushanfang': 'eas.aliyuncs.com',
            'cn-zhangbei': 'eas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'eas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'eas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'eas.aliyuncs.com',
            'eu-west-1': 'eas.aliyuncs.com',
            'eu-west-1-oxs': 'eas.aliyuncs.com',
            'me-east-1': 'eas.aliyuncs.com',
            'rus-west-1-pop': 'eas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request, headers, runtime)

    def create_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_instances(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    def create_resource_instances_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.auto_renewal):
            body['AutoRenewal'] = request.auto_renewal
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.ecs_instance_count):
            body['EcsInstanceCount'] = request.ecs_instance_count
        if not UtilClient.is_unset(request.ecs_instance_type):
            body['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/instances' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_log(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_log_with_options(cluster_id, resource_id, request, headers, runtime)

    def create_resource_log_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.log_store):
            body['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/log' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    def create_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_auto_scaler(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    def create_service_auto_scaler_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['Max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.strategies):
            body['Strategies'] = request.strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/autoscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_cron_scaler(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    def create_service_cron_scaler_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/cronscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_mirror(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    def create_service_mirror_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/mirror' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.CreateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(cluster_id, resource_id, headers, runtime)

    def delete_resource_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_dlink(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    def delete_resource_dlink_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/dlink' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_instances(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    def delete_resource_instances_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.all_failed):
            query['AllFailed'] = request.all_failed
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/instances' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_log(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    def delete_resource_log_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/log' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(cluster_id, service_name, headers, runtime)

    def delete_service_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_auto_scaler(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    def delete_service_auto_scaler_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/autoscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_cron_scaler(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    def delete_service_cron_scaler_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/cronscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_instances(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    def delete_service_instances_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/instances' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_mirror(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    def delete_service_mirror_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/mirror' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DeleteServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_with_options(cluster_id, resource_id, headers, runtime)

    def describe_resource_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_dlink(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_dlink_with_options(cluster_id, resource_id, headers, runtime)

    def describe_resource_dlink_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/dlink' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_log(self, cluster_id, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resource_log_with_options(cluster_id, resource_id, headers, runtime)

    def describe_resource_log_with_options(self, cluster_id, resource_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeResourceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/log' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeResourceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_with_options(cluster_id, service_name, headers, runtime)

    def describe_service_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_auto_scaler(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_auto_scaler_with_options(cluster_id, service_name, headers, runtime)

    def describe_service_auto_scaler_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/autoscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_cron_scaler(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_cron_scaler_with_options(cluster_id, service_name, headers, runtime)

    def describe_service_cron_scaler_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/cronscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_log(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_log_with_options(cluster_id, service_name, request, headers, runtime)

    def describe_service_log_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLog',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/logs' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_mirror(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_service_mirror_with_options(cluster_id, service_name, headers, runtime)

    def describe_service_mirror_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/mirror' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.DescribeServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_instance_worker(self, cluster_id, resource_id, instance_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instance_worker_with_options(cluster_id, resource_id, instance_name, request, headers, runtime)

    def list_resource_instance_worker_with_options(self, cluster_id, resource_id, instance_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstanceWorker',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/instance/%s/workers' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id), TeaConverter.to_unicode(instance_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstanceWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_instances(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_instances_with_options(cluster_id, resource_id, request, headers, runtime)

    def list_resource_instances_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/instances' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_services(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_services_with_options(cluster_id, resource_id, request, headers, runtime)

    def list_resource_services_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/services' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourceServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    def list_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_instances(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_instances_with_options(cluster_id, service_name, request, headers, runtime)

    def list_service_instances_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/instances' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    def list_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def release_service(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_service_with_options(cluster_id, service_name, request, headers, runtime)

    def release_service_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.weight):
            body['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/release' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.ReleaseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_service(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_service_with_options(cluster_id, service_name, headers, runtime)

    def start_service_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/start' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_service(self, cluster_id, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_service_with_options(cluster_id, service_name, headers, runtime)

    def stop_service_with_options(self, cluster_id, service_name, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/stop' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.StopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(cluster_id, resource_id, request, headers, runtime)

    def update_resource_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_dlink(self, cluster_id, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_dlink_with_options(cluster_id, resource_id, request, headers, runtime)

    def update_resource_dlink_with_options(self, cluster_id, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.destination_cidrs):
            body['DestinationCIDRs'] = request.destination_cidrs
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_list):
            body['VSwitchIdList'] = request.v_switch_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceDLink',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/resources/%s/%s/dlink' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(resource_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateResourceDLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(cluster_id, service_name, request, headers, runtime)

    def update_service_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_auto_scaler(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_auto_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    def update_service_auto_scaler_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.max):
            body['Max'] = request.max
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.strategies):
            body['Strategies'] = request.strategies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceAutoScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/autoscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceAutoScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_cron_scaler(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_cron_scaler_with_options(cluster_id, service_name, request, headers, runtime)

    def update_service_cron_scaler_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.exclude_dates):
            body['ExcludeDates'] = request.exclude_dates
        if not UtilClient.is_unset(request.scale_jobs):
            body['ScaleJobs'] = request.scale_jobs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceCronScaler',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/cronscaler' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceCronScalerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_mirror(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_mirror_with_options(cluster_id, service_name, request, headers, runtime)

    def update_service_mirror_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.ratio):
            body['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.target):
            body['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceMirror',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/mirror' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceMirrorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_version(self, cluster_id, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(cluster_id, service_name, request, headers, runtime)

    def update_service_version_with_options(self, cluster_id, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceVersion',
            version='2021-07-01',
            protocol='HTTPS',
            pathname='/api/v2/services/%s/%s/version' % (TeaConverter.to_unicode(cluster_id), TeaConverter.to_unicode(service_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eas_20210701_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )
