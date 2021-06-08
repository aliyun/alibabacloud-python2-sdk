# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
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
            'ap-northeast-1': 'dcdn.aliyuncs.com',
            'ap-northeast-2-pop': 'dcdn.aliyuncs.com',
            'ap-south-1': 'dcdn.aliyuncs.com',
            'ap-southeast-1': 'dcdn.aliyuncs.com',
            'ap-southeast-2': 'dcdn.aliyuncs.com',
            'ap-southeast-3': 'dcdn.aliyuncs.com',
            'ap-southeast-5': 'dcdn.aliyuncs.com',
            'cn-beijing': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-1': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'dcdn.aliyuncs.com',
            'cn-beijing-gov-1': 'dcdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dcdn.aliyuncs.com',
            'cn-chengdu': 'dcdn.aliyuncs.com',
            'cn-edge-1': 'dcdn.aliyuncs.com',
            'cn-fujian': 'dcdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dcdn.aliyuncs.com',
            'cn-hangzhou': 'dcdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dcdn.aliyuncs.com',
            'cn-hangzhou-finance': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dcdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'dcdn.aliyuncs.com',
            'cn-hongkong': 'dcdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dcdn.aliyuncs.com',
            'cn-huhehaote': 'dcdn.aliyuncs.com',
            'cn-north-2-gov-1': 'dcdn.aliyuncs.com',
            'cn-qingdao': 'dcdn.aliyuncs.com',
            'cn-qingdao-nebula': 'dcdn.aliyuncs.com',
            'cn-shanghai': 'dcdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'dcdn.aliyuncs.com',
            'cn-shanghai-inner': 'dcdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen': 'dcdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen-inner': 'dcdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dcdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dcdn.aliyuncs.com',
            'cn-wuhan': 'dcdn.aliyuncs.com',
            'cn-yushanfang': 'dcdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dcdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dcdn.aliyuncs.com',
            'eu-central-1': 'dcdn.aliyuncs.com',
            'eu-west-1': 'dcdn.aliyuncs.com',
            'eu-west-1-oxs': 'dcdn.aliyuncs.com',
            'me-east-1': 'dcdn.aliyuncs.com',
            'rus-west-1-pop': 'dcdn.aliyuncs.com',
            'us-east-1': 'dcdn.aliyuncs.com',
            'us-west-1': 'dcdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            self.do_rpcrequest('AddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    def add_dcdn_ipa_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            self.do_rpcrequest('AddDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    def batch_add_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            self.do_rpcrequest('BatchAddDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_add_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            self.do_rpcrequest('BatchDeleteDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    def batch_set_dcdn_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            self.do_rpcrequest('BatchSetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_certificate_with_options(request, runtime)

    def batch_set_dcdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_dcdn_ipa_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    def batch_start_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            self.do_rpcrequest('BatchStartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    def batch_stop_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            self.do_rpcrequest('BatchStopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    def commit_staging_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            self.do_rpcrequest('CommitStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_staging_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.commit_staging_routine_code_with_options(request, runtime)

    def create_dcdn_certificate_signing_request_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            self.do_rpcrequest('CreateDcdnCertificateSigningRequest', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_certificate_signing_request(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_certificate_signing_request_with_options(request, runtime)

    def create_dcdn_deliver_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            self.do_rpcrequest('CreateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_deliver_task_with_options(request, runtime)

    def create_dcdn_domain_offline_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('CreateDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_domain_offline_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    def create_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            self.do_rpcrequest('CreateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_sub_task_with_options(request, runtime)

    def create_routine_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            self.do_rpcrequest('CreateRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    def delete_dcdn_deliver_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            self.do_rpcrequest('DeleteDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_deliver_task_with_options(request, runtime)

    def delete_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            self.do_rpcrequest('DeleteDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    def delete_dcdn_ipa_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            self.do_rpcrequest('DeleteDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            self.do_rpcrequest('DeleteDcdnIpaSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_ipa_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    def delete_dcdn_specific_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            self.do_rpcrequest('DeleteDcdnSpecificConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            self.do_rpcrequest('DeleteDcdnSpecificStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_specific_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    def delete_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            self.do_rpcrequest('DeleteDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_sub_task_with_options(request, runtime)

    def delete_routine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            self.do_rpcrequest('DeleteRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    def delete_routine_code_revision_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            self.do_rpcrequest('DeleteRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_code_revision_with_options(request, runtime)

    def delete_routine_conf_envs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            self.do_rpcrequest('DeleteRoutineConfEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_routine_conf_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_conf_envs_with_options(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnBgpBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_bgp_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnBgpTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_bgp_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    def describe_dcdn_blocked_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            self.do_rpcrequest('DescribeDcdnBlockedRegions', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_blocked_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_blocked_regions_with_options(request, runtime)

    def describe_dcdn_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            self.do_rpcrequest('DescribeDcdnCertificateDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    def describe_dcdn_certificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            self.do_rpcrequest('DescribeDcdnCertificateList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    def describe_dcdn_config_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            self.do_rpcrequest('DescribeDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_of_version_with_options(request, runtime)

    def describe_dcdn_deliver_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            self.do_rpcrequest('DescribeDcdnDeliverList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_deliver_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deliver_list_with_options(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            self.do_rpcrequest('DescribeDcdnDomainByCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_by_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            self.do_rpcrequest('DescribeDcdnDomainCertificateInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    def describe_dcdn_domain_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            self.do_rpcrequest('DescribeDcdnDomainCname', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    def describe_dcdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            self.do_rpcrequest('DescribeDcdnDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    def describe_dcdn_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            self.do_rpcrequest('DescribeDcdnDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainHitRateData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIpaBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_ipa_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIpaTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_ipa_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainIspData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_isp_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    def describe_dcdn_domain_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            self.do_rpcrequest('DescribeDcdnDomainLog', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainMultiUsageData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_multi_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainOriginBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_origin_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainOriginTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_origin_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            self.do_rpcrequest('DescribeDcdnDomainProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    def describe_dcdn_domain_pv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainPvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_pv_data_with_options(request, runtime)

    def describe_dcdn_domain_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainQpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeBpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeByteHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_byte_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeDetailData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeQpsData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeReqHitRateData', '2018-01-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_req_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeSrcTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRealTimeTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_region_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainRegionData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            self.do_rpcrequest('DescribeDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTopReferVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_top_refer_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTopUrlVisit', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_top_url_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainUvData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketBpsData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketHttpCodeData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            self.do_rpcrequest('DescribeDcdnDomainWebsocketTrafficData', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_domain_websocket_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    def describe_dcdn_https_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            self.do_rpcrequest('DescribeDcdnHttpsDomainList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_https_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            self.do_rpcrequest('DescribeDcdnIpaDomainConfigs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            self.do_rpcrequest('DescribeDcdnIpaDomainDetail', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    def describe_dcdn_ipa_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            self.do_rpcrequest('DescribeDcdnIpaService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            self.do_rpcrequest('DescribeDcdnIpaUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ipa_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    def describe_dcdn_ip_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            self.do_rpcrequest('DescribeDcdnIpInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_ip_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    def describe_dcdn_offline_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_with_options(request, runtime)

    def describe_dcdn_offline_log_delivery_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryFieldResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryField', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_field_with_options(request, runtime)

    def describe_dcdn_offline_log_delivery_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryRegionsResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryRegions', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_regions_with_options(request, runtime)

    def describe_dcdn_offline_log_delivery_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnOfflineLogDeliveryStatusResponse(),
            self.do_rpcrequest('DescribeDcdnOfflineLogDeliveryStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_offline_log_delivery_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_offline_log_delivery_status_with_options(request, runtime)

    def describe_dcdn_refresh_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_refresh_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    def describe_dcdn_refresh_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshTaskById', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_refresh_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_task_by_id_with_options(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            self.do_rpcrequest('DescribeDcdnRefreshTasks', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_refresh_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    def describe_dcdn_region_and_isp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            self.do_rpcrequest('DescribeDcdnRegionAndIsp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_region_and_isp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    def describe_dcdn_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            self.do_rpcrequest('DescribeDcdnReport', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_with_options(request, runtime)

    def describe_dcdn_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            self.do_rpcrequest('DescribeDcdnReportList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_list_with_options(request, runtime)

    def describe_dcdn_sec_func_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            self.do_rpcrequest('DescribeDcdnSecFuncInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_sec_func_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_func_info_with_options(request, runtime)

    def describe_dcdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            self.do_rpcrequest('DescribeDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    def describe_dcdn_staging_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            self.do_rpcrequest('DescribeDcdnStagingIp', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_staging_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(request, runtime)

    def describe_dcdn_sub_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            self.do_rpcrequest('DescribeDcdnSubList', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_sub_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sub_list_with_options(request, runtime)

    def describe_dcdn_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            self.do_rpcrequest('DescribeDcdnTagResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            self.do_rpcrequest('DescribeDcdnTopDomainsByFlow', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    def describe_dcdn_user_bill_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            self.do_rpcrequest('DescribeDcdnUserBillHistory', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_bill_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    def describe_dcdn_user_bill_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            self.do_rpcrequest('DescribeDcdnUserBillType', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_bill_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_type_with_options(request, runtime)

    def describe_dcdn_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            self.do_rpcrequest('DescribeDcdnUserDomains', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            self.do_rpcrequest('DescribeDcdnUserDomainsByFunc', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_domains_by_func(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    def describe_dcdn_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            self.do_rpcrequest('DescribeDcdnUserQuota', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    def describe_dcdn_user_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            self.do_rpcrequest('DescribeDcdnUserResourcePackage', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            self.do_rpcrequest('DescribeDcdnUserSecDrop', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_sec_drop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    def describe_dcdn_user_sec_drop_by_minute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            self.do_rpcrequest('DescribeDcdnUserSecDropByMinute', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_sec_drop_by_minute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_by_minute_with_options(request, runtime)

    def describe_dcdn_user_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            self.do_rpcrequest('DescribeDcdnUserTags', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(request, runtime)

    def describe_dcdn_verify_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            self.do_rpcrequest('DescribeDcdnVerifyContent', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    def describe_dcdn_waf_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            self.do_rpcrequest('DescribeDcdnWafDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dcdn_waf_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    def describe_routine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            self.do_rpcrequest('DescribeRoutine', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_with_options(request, runtime)

    def describe_routine_canary_envs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            self.do_rpcrequest('DescribeRoutineCanaryEnvs', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_routine_canary_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_canary_envs_with_options(request, runtime)

    def describe_routine_code_revision_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            self.do_rpcrequest('DescribeRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_code_revision_with_options(request, runtime)

    def describe_routine_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            self.do_rpcrequest('DescribeRoutineSpec', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_routine_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_spec_with_options(request, runtime)

    def describe_routine_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            self.do_rpcrequest('DescribeRoutineUserInfo', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_routine_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_user_info_with_options(request, runtime)

    def describe_user_dcdn_ipa_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            self.do_rpcrequest('DescribeUserDcdnIpaStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_dcdn_ipa_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    def describe_user_dcdn_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            self.do_rpcrequest('DescribeUserDcdnStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_dcdn_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    def describe_user_er_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            self.do_rpcrequest('DescribeUserErStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_er_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_er_status_with_options(request, runtime)

    def describe_user_logservice_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            self.do_rpcrequest('DescribeUserLogserviceStatus', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_logservice_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_logservice_status_with_options(request, runtime)

    def disable_dcdn_domain_offline_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DisableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_domain_offline_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    def disable_dcdn_offline_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DisableDcdnOfflineLogDeliveryResponse(),
            self.do_rpcrequest('DisableDcdnOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dcdn_offline_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_dcdn_offline_log_delivery_with_options(request, runtime)

    def edit_routine_conf_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            self.do_rpcrequest('EditRoutineConf', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_routine_conf(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_routine_conf_with_options(request, runtime)

    def enable_dcdn_domain_offline_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EnableDcdnDomainOfflineLogDeliveryResponse(),
            self.do_rpcrequest('EnableDcdnDomainOfflineLogDelivery', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_dcdn_domain_offline_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_dcdn_domain_offline_log_delivery_with_options(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            self.do_rpcrequest('ModifyDCdnDomainSchdmByProperty', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dcdn_domain_schdm_by_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    def open_dcdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            self.do_rpcrequest('OpenDcdnService', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_dcdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    def preload_dcdn_object_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            self.do_rpcrequest('PreloadDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preload_dcdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            self.do_rpcrequest('PublishDcdnStagingConfigToProduction', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_dcdn_staging_config_to_production(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    def publish_routine_code_revision_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            self.do_rpcrequest('PublishRoutineCodeRevision', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_routine_code_revision_with_options(request, runtime)

    def refresh_dcdn_object_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            self.do_rpcrequest('RefreshDcdnObjectCaches', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_dcdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    def rollback_dcdn_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            self.do_rpcrequest('RollbackDcdnStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_dcdn_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    def set_dcdn_config_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            self.do_rpcrequest('SetDcdnConfigOfVersion', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_config_of_version_with_options(request, runtime)

    def set_dcdn_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            self.do_rpcrequest('SetDcdnDomainCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_certificate_with_options(request, runtime)

    def set_dcdn_domain_csrcertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            self.do_rpcrequest('SetDcdnDomainCSRCertificate', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_csrcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_csrcertificate_with_options(request, runtime)

    def set_dcdn_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            self.do_rpcrequest('SetDcdnDomainStagingConfig', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_dcdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    def set_routine_subdomain_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            self.do_rpcrequest('SetRoutineSubdomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_routine_subdomain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_routine_subdomain_with_options(request, runtime)

    def start_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            self.do_rpcrequest('StartDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    def start_dcdn_ipa_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            self.do_rpcrequest('StartDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    def stop_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            self.do_rpcrequest('StopDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    def stop_dcdn_ipa_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            self.do_rpcrequest('StopDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    def tag_dcdn_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            self.do_rpcrequest('TagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_dcdn_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    def untag_dcdn_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            self.do_rpcrequest('UntagDcdnResources', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_dcdn_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    def update_dcdn_deliver_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.UpdateDcdnDeliverTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deliver):
            request.deliver_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deliver, 'Deliver', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            self.do_rpcrequest('UpdateDcdnDeliverTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_deliver_task_with_options(request, runtime)

    def update_dcdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            self.do_rpcrequest('UpdateDcdnDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    def update_dcdn_ipa_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            self.do_rpcrequest('UpdateDcdnIpaDomain', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    def update_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            self.do_rpcrequest('UpdateDcdnSubTask', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_sub_task_with_options(request, runtime)

    def upload_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            self.do_rpcrequest('UploadRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_routine_code_with_options(request, runtime)

    def upload_staging_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            self.do_rpcrequest('UploadStagingRoutineCode', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_staging_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_staging_routine_code_with_options(request, runtime)

    def verify_dcdn_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            self.do_rpcrequest('VerifyDcdnDomainOwner', '2018-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_dcdn_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)
