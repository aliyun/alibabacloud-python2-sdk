# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from RPC.client import Client as RPCClient
from alibabacloud_iot20180120 import models as iot_20180120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-2': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-3': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'iot.ap-northeast-1.aliyuncs.com',
            'cn-beijing': 'iot.aliyuncs.com',
            'cn-beijing-finance-1': 'iot.aliyuncs.com',
            'cn-beijing-finance-pop': 'iot.aliyuncs.com',
            'cn-beijing-gov-1': 'iot.aliyuncs.com',
            'cn-beijing-nu16-b01': 'iot.aliyuncs.com',
            'cn-chengdu': 'iot.aliyuncs.com',
            'cn-edge-1': 'iot.aliyuncs.com',
            'cn-fujian': 'iot.aliyuncs.com',
            'cn-haidian-cm12-c01': 'iot.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'iot.aliyuncs.com',
            'cn-hangzhou-finance': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'iot.aliyuncs.com',
            'cn-hangzhou-test-306': 'iot.aliyuncs.com',
            'cn-hongkong': 'iot.aliyuncs.com',
            'cn-hongkong-finance-pop': 'iot.aliyuncs.com',
            'cn-huhehaote': 'iot.aliyuncs.com',
            'cn-north-2-gov-1': 'iot.aliyuncs.com',
            'cn-qingdao': 'iot.aliyuncs.com',
            'cn-qingdao-nebula': 'iot.aliyuncs.com',
            'cn-shanghai-et15-b01': 'iot.aliyuncs.com',
            'cn-shanghai-et2-b01': 'iot.aliyuncs.com',
            'cn-shanghai-finance-1': 'iot.aliyuncs.com',
            'cn-shanghai-inner': 'iot.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'iot.aliyuncs.com',
            'cn-shenzhen': 'iot.aliyuncs.com',
            'cn-shenzhen-finance-1': 'iot.aliyuncs.com',
            'cn-shenzhen-inner': 'iot.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'iot.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'iot.aliyuncs.com',
            'cn-wuhan': 'iot.aliyuncs.com',
            'cn-yushanfang': 'iot.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'iot.aliyuncs.com',
            'cn-zhangjiakou': 'iot.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'iot.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'iot.aliyuncs.com',
            'eu-west-1': 'iot.ap-northeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'iot.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'iot.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'iot.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('iot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def list_analytics_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListAnalyticsDataResponse().from_map(
            self.do_request('ListAnalyticsData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_analytics_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_analytics_data_with_options(request, runtime)

    def batch_bind_devices_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchBindDevicesIntoProjectResponse().from_map(
            self.do_request('BatchBindDevicesIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_devices_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_devices_into_project_with_options(request, runtime)

    def batch_bind_products_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchBindProductsIntoProjectResponse().from_map(
            self.do_request('BatchBindProductsIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_products_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_products_into_project_with_options(request, runtime)

    def batch_unbind_project_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchUnbindProjectDevicesResponse().from_map(
            self.do_request('BatchUnbindProjectDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_devices_with_options(request, runtime)

    def batch_unbind_project_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchUnbindProjectProductsResponse().from_map(
            self.do_request('BatchUnbindProjectProducts', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_products_with_options(request, runtime)

    def sync_speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SyncSpeechByCombinationResponse().from_map(
            self.do_request('SyncSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def sync_speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_speech_by_combination_with_options(request, runtime)

    def open_iot_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.OpenIotServiceResponse().from_map(
            self.do_request('OpenIotService', 'HTTPS', 'POST', '2018-01-20', 'AK,APP,PrivateKey,BearerToken', None, TeaCore.to_map(request), runtime)
        )

    def open_iot_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_iot_service_with_options(request, runtime)

    def create_ruleng_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateRulengDistributeJobResponse().from_map(
            self.do_request('CreateRulengDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_ruleng_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ruleng_distribute_job_with_options(request, runtime)

    def list_task_by_page_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.ListTaskByPageShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device):
            request.device_shrink = UtilClient.to_jsonstring(tmp.device)
        return iot_20180120_models.ListTaskByPageResponse().from_map(
            self.do_request('ListTaskByPage', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_task_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_by_page_with_options(request, runtime)

    def list_task_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.ListTaskShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device):
            request.device_shrink = UtilClient.to_jsonstring(tmp.device)
        return iot_20180120_models.ListTaskResponse().from_map(
            self.do_request('ListTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    def query_job_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryJobStatisticsResponse().from_map(
            self.do_request('QueryJobStatistics', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def query_job_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_statistics_with_options(request, runtime)

    def delete_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteJobResponse().from_map(
            self.do_request('DeleteJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    def cancel_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CancelJobResponse().from_map(
            self.do_request('CancelJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    def list_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListJobResponse().from_map(
            self.do_request('ListJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    def query_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryJobResponse().from_map(
            self.do_request('QueryJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_with_options(request, runtime)

    def update_job_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        return iot_20180120_models.UpdateJobResponse().from_map(
            self.do_request('UpdateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    def create_job_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.job_file):
            request.job_file_shrink = UtilClient.to_jsonstring(tmp.job_file)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.target_config):
            request.target_config_shrink = UtilClient.to_jsonstring(tmp.target_config)
        return iot_20180120_models.CreateJobResponse().from_map(
            self.do_request('CreateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    def generate_file_upload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GenerateFileUploadURLResponse().from_map(
            self.do_request('GenerateFileUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_file_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_file_upload_urlwith_options(request, runtime)

    def create_product_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateProductDistributeJobResponse().from_map(
            self.do_request('CreateProductDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_distribute_job_with_options(request, runtime)

    def query_device_original_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceOriginalPropertyDataResponse().from_map(
            self.do_request('QueryDeviceOriginalPropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_data_with_options(request, runtime)

    def query_device_original_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceOriginalEventDataResponse().from_map(
            self.do_request('QueryDeviceOriginalEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_event_data_with_options(request, runtime)

    def query_device_original_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse().from_map(
            self.do_request('QueryDeviceOriginalPropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_status_with_options(request, runtime)

    def query_device_original_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceOriginalServiceDataResponse().from_map(
            self.do_request('QueryDeviceOriginalServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_service_data_with_options(request, runtime)

    def create_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateThingScriptResponse().from_map(
            self.do_request('CreateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_script_with_options(request, runtime)

    def update_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateThingScriptResponse().from_map(
            self.do_request('UpdateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_script_with_options(request, runtime)

    def get_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetThingScriptResponse().from_map(
            self.do_request('GetThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_script_with_options(request, runtime)

    def list_otamodule_versions_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTAModuleVersionsByDeviceResponse().from_map(
            self.do_request('ListOTAModuleVersionsByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otamodule_versions_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_versions_by_device_with_options(request, runtime)

    def batch_pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchPubResponse().from_map(
            self.do_request('BatchPub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_pub_with_options(request, runtime)

    def speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SpeechByCombinationResponse().from_map(
            self.do_request('SpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.speech_by_combination_with_options(request, runtime)

    def update_thing_model_validation_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateThingModelValidationConfigResponse().from_map(
            self.do_request('UpdateThingModelValidationConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_model_validation_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_validation_config_with_options(request, runtime)

    def query_device_by_sqlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceBySQLResponse().from_map(
            self.do_request('QueryDeviceBySQL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_sql(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_sqlwith_options(request, runtime)

    def list_otamodule_by_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTAModuleByProductResponse().from_map(
            self.do_request('ListOTAModuleByProduct', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def list_otamodule_by_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_by_product_with_options(request, runtime)

    def delete_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteOTAModuleResponse().from_map(
            self.do_request('DeleteOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otamodule_with_options(request, runtime)

    def generate_device_name_list_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GenerateDeviceNameListURLResponse().from_map(
            self.do_request('GenerateDeviceNameListURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_device_name_list_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_device_name_list_urlwith_options(request, runtime)

    def update_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateOTAModuleResponse().from_map(
            self.do_request('UpdateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_otamodule_with_options(request, runtime)

    def create_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateOTAModuleResponse().from_map(
            self.do_request('CreateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otamodule_with_options(request, runtime)

    def query_thing_model_extend_config_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryThingModelExtendConfigPublishedResponse().from_map(
            self.do_request('QueryThingModelExtendConfigPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_published_with_options(request, runtime)

    def get_thing_model_tsl_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetThingModelTslPublishedResponse().from_map(
            self.do_request('GetThingModelTslPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_published_with_options(request, runtime)

    def query_thing_model_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryThingModelPublishedResponse().from_map(
            self.do_request('QueryThingModelPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_published_with_options(request, runtime)

    def query_thing_model_extend_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryThingModelExtendConfigResponse().from_map(
            self.do_request('QueryThingModelExtendConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_with_options(request, runtime)

    def list_distributed_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListDistributedDeviceResponse().from_map(
            self.do_request('ListDistributedDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_device_with_options(request, runtime)

    def list_distributed_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListDistributedProductResponse().from_map(
            self.do_request('ListDistributedProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_product_with_options(request, runtime)

    def query_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QuerySubscribeRelationResponse().from_map(
            self.do_request('QuerySubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_subscribe_relation_with_options(request, runtime)

    def create_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse().from_map(
            self.do_request('CreateConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_subscribe_relation_with_options(request, runtime)

    def update_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateSubscribeRelationResponse().from_map(
            self.do_request('UpdateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_subscribe_relation_with_options(request, runtime)

    def delete_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse().from_map(
            self.do_request('DeleteConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_subscribe_relation_with_options(request, runtime)

    def reset_consumer_group_position_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ResetConsumerGroupPositionResponse().from_map(
            self.do_request('ResetConsumerGroupPosition', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_consumer_group_position(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_consumer_group_position_with_options(request, runtime)

    def update_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateConsumerGroupResponse().from_map(
            self.do_request('UpdateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_consumer_group_with_options(request, runtime)

    def batch_delete_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse().from_map(
            self.do_request('BatchDeleteEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_edge_instance_channel_with_options(request, runtime)

    def batch_set_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse().from_map(
            self.do_request('BatchSetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_channel_with_options(request, runtime)

    def batch_get_edge_instance_device_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse().from_map(
            self.do_request('BatchGetEdgeInstanceDeviceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_driver_with_options(request, runtime)

    def batch_get_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse().from_map(
            self.do_request('BatchGetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_channel_with_options(request, runtime)

    def release_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ReleaseEdgeDriverVersionResponse().from_map(
            self.do_request('ReleaseEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_edge_driver_version_with_options(request, runtime)

    def query_edge_instance_device_by_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse().from_map(
            self.do_request('QueryEdgeInstanceDeviceByDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device_by_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_by_driver_with_options(request, runtime)

    def disable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DisableSceneRuleResponse().from_map(
            self.do_request('DisableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_rule_with_options(request, runtime)

    def trigger_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.TriggerSceneRuleResponse().from_map(
            self.do_request('TriggerSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def trigger_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_scene_rule_with_options(request, runtime)

    def unbind_scene_rule_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse().from_map(
            self.do_request('UnbindSceneRuleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_scene_rule_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_scene_rule_from_edge_instance_with_options(request, runtime)

    def query_edge_instance_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceSceneRuleResponse().from_map(
            self.do_request('QueryEdgeInstanceSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_scene_rule_with_options(request, runtime)

    def create_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateSceneRuleResponse().from_map(
            self.do_request('CreateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_rule_with_options(request, runtime)

    def query_detail_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDetailSceneRuleLogResponse().from_map(
            self.do_request('QueryDetailSceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_detail_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_detail_scene_rule_log_with_options(request, runtime)

    def enable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.EnableSceneRuleResponse().from_map(
            self.do_request('EnableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_rule_with_options(request, runtime)

    def update_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateSceneRuleResponse().from_map(
            self.do_request('UpdateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_rule_with_options(request, runtime)

    def query_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QuerySceneRuleResponse().from_map(
            self.do_request('QuerySceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_scene_rule_with_options(request, runtime)

    def query_summary_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QuerySummarySceneRuleLogResponse().from_map(
            self.do_request('QuerySummarySceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_summary_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_summary_scene_rule_log_with_options(request, runtime)

    def get_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetSceneRuleResponse().from_map(
            self.do_request('GetSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_rule_with_options(request, runtime)

    def delete_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteSceneRuleResponse().from_map(
            self.do_request('DeleteSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_rule_with_options(request, runtime)

    def bind_scene_rule_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BindSceneRuleToEdgeInstanceResponse().from_map(
            self.do_request('BindSceneRuleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_scene_rule_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_scene_rule_to_edge_instance_with_options(request, runtime)

    def create_edge_oss_pre_signed_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeOssPreSignedAddressResponse().from_map(
            self.do_request('CreateEdgeOssPreSignedAddress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_oss_pre_signed_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_oss_pre_signed_address_with_options(request, runtime)

    def update_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateEdgeDriverVersionResponse().from_map(
            self.do_request('UpdateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_driver_version_with_options(request, runtime)

    def delete_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteEdgeDriverVersionResponse().from_map(
            self.do_request('DeleteEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_version_with_options(request, runtime)

    def create_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeDriverVersionResponse().from_map(
            self.do_request('CreateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_version_with_options(request, runtime)

    def delete_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteEdgeDriverResponse().from_map(
            self.do_request('DeleteEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_with_options(request, runtime)

    def query_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeDriverResponse().from_map(
            self.do_request('QueryEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_with_options(request, runtime)

    def batch_get_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeDriverResponse().from_map(
            self.do_request('BatchGetEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_driver_with_options(request, runtime)

    def create_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeDriverResponse().from_map(
            self.do_request('CreateEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_with_options(request, runtime)

    def get_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetEdgeDriverVersionResponse().from_map(
            self.do_request('GetEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_driver_version_with_options(request, runtime)

    def query_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeDriverVersionResponse().from_map(
            self.do_request('QueryEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_version_with_options(request, runtime)

    def batch_get_device_bind_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetDeviceBindStatusResponse().from_map(
            self.do_request('BatchGetDeviceBindStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_bind_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_bind_status_with_options(request, runtime)

    def list_otajob_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTAJobByDeviceResponse().from_map(
            self.do_request('ListOTAJobByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_device_with_options(request, runtime)

    def update_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateThingModelResponse().from_map(
            self.do_request('UpdateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_with_options(request, runtime)

    def create_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateThingModelResponse().from_map(
            self.do_request('CreateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_model_with_options(request, runtime)

    def list_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTATaskByJobResponse().from_map(
            self.do_request('ListOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otatask_by_job_with_options(request, runtime)

    def list_thing_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListThingTemplatesResponse().from_map(
            self.do_request('ListThingTemplates', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_templates_with_options(request, runtime)

    def get_thing_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetThingTemplateResponse().from_map(
            self.do_request('GetThingTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_template_with_options(request, runtime)

    def list_thing_model_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListThingModelVersionResponse().from_map(
            self.do_request('ListThingModelVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_model_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_model_version_with_options(request, runtime)

    def import_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ImportThingModelTslResponse().from_map(
            self.do_request('ImportThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_thing_model_tsl_with_options(request, runtime)

    def publish_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.PublishThingModelResponse().from_map(
            self.do_request('PublishThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_thing_model_with_options(request, runtime)

    def copy_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CopyThingModelResponse().from_map(
            self.do_request('CopyThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def copy_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_thing_model_with_options(request, runtime)

    def get_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetThingModelTslResponse().from_map(
            self.do_request('GetThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_with_options(request, runtime)

    def query_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryThingModelResponse().from_map(
            self.do_request('QueryThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_with_options(request, runtime)

    def delete_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteThingModelResponse().from_map(
            self.do_request('DeleteThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_thing_model_with_options(request, runtime)

    def update_product_filter_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateProductFilterConfigResponse().from_map(
            self.do_request('UpdateProductFilterConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_filter_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_filter_config_with_options(request, runtime)

    def cancel_otastrategy_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CancelOTAStrategyByJobResponse().from_map(
            self.do_request('CancelOTAStrategyByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otastrategy_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otastrategy_by_job_with_options(request, runtime)

    def list_otajob_by_firmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTAJobByFirmwareResponse().from_map(
            self.do_request('ListOTAJobByFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_firmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_firmware_with_options(request, runtime)

    def list_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListOTAFirmwareResponse().from_map(
            self.do_request('ListOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otafirmware_with_options(request, runtime)

    def cancel_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CancelOTATaskByJobResponse().from_map(
            self.do_request('CancelOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_job_with_options(request, runtime)

    def create_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateDeviceDistributeJobResponse().from_map(
            self.do_request('CreateDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_distribute_job_with_options(request, runtime)

    def query_device_distribute_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceDistributeDetailResponse().from_map(
            self.do_request('QueryDeviceDistributeDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_detail_with_options(request, runtime)

    def list_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListDeviceDistributeJobResponse().from_map(
            self.do_request('ListDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_distribute_job_with_options(request, runtime)

    def query_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceDistributeJobResponse().from_map(
            self.do_request('QueryDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_job_with_options(request, runtime)

    def delete_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteDeviceDistributeJobResponse().from_map(
            self.do_request('DeleteDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_distribute_job_with_options(request, runtime)

    def query_device_by_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceByStatusResponse().from_map(
            self.do_request('QueryDeviceByStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_status_with_options(request, runtime)

    def generate_otaupload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GenerateOTAUploadURLResponse().from_map(
            self.do_request('GenerateOTAUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_otaupload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_otaupload_urlwith_options(request, runtime)

    def query_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryProductCertInfoResponse().from_map(
            self.do_request('QueryProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_cert_info_with_options(request, runtime)

    def set_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetProductCertInfoResponse().from_map(
            self.do_request('SetProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_product_cert_info_with_options(request, runtime)

    def create_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateSubscribeRelationResponse().from_map(
            self.do_request('CreateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_relation_with_options(request, runtime)

    def delete_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteSubscribeRelationResponse().from_map(
            self.do_request('DeleteSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_relation_with_options(request, runtime)

    def query_consumer_group_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryConsumerGroupStatusResponse().from_map(
            self.do_request('QueryConsumerGroupStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_status_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteConsumerGroupResponse().from_map(
            self.do_request('DeleteConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def query_consumer_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryConsumerGroupListResponse().from_map(
            self.do_request('QueryConsumerGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_list_with_options(request, runtime)

    def query_consumer_group_by_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryConsumerGroupByGroupIdResponse().from_map(
            self.do_request('QueryConsumerGroupByGroupId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_by_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_by_group_id_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateConsumerGroupResponse().from_map(
            self.do_request('CreateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_otadynamic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateOTADynamicUpgradeJobResponse().from_map(
            self.do_request('CreateOTADynamicUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otadynamic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otadynamic_upgrade_job_with_options(request, runtime)

    def create_otastatic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateOTAStaticUpgradeJobResponse().from_map(
            self.do_request('CreateOTAStaticUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otastatic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otastatic_upgrade_job_with_options(request, runtime)

    def create_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateOTAFirmwareResponse().from_map(
            self.do_request('CreateOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otafirmware_with_options(request, runtime)

    def create_otaverify_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateOTAVerifyJobResponse().from_map(
            self.do_request('CreateOTAVerifyJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otaverify_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otaverify_job_with_options(request, runtime)

    def query_otajob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryOTAJobResponse().from_map(
            self.do_request('QueryOTAJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otajob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otajob_with_options(request, runtime)

    def cancel_otatask_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CancelOTATaskByDeviceResponse().from_map(
            self.do_request('CancelOTATaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_device_with_options(request, runtime)

    def delete_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteOTAFirmwareResponse().from_map(
            self.do_request('DeleteOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otafirmware_with_options(request, runtime)

    def query_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryOTAFirmwareResponse().from_map(
            self.do_request('QueryOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otafirmware_with_options(request, runtime)

    def unbind_application_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse().from_map(
            self.do_request('UnbindApplicationFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_application_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_application_from_edge_instance_with_options(request, runtime)

    def bind_application_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BindApplicationToEdgeInstanceResponse().from_map(
            self.do_request('BindApplicationToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_application_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_application_to_edge_instance_with_options(request, runtime)

    def query_cert_url_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryCertUrlByApplyIdResponse().from_map(
            self.do_request('QueryCertUrlByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_cert_url_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cert_url_by_apply_id_with_options(request, runtime)

    def query_device_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceCertResponse().from_map(
            self.do_request('QueryDeviceCert', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_cert_with_options(request, runtime)

    def close_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CloseEdgeInstanceDeploymentResponse().from_map(
            self.do_request('CloseEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_edge_instance_deployment_with_options(request, runtime)

    def unbind_driver_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UnbindDriverFromEdgeInstanceResponse().from_map(
            self.do_request('UnbindDriverFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_driver_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_driver_from_edge_instance_with_options(request, runtime)

    def replace_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ReplaceEdgeInstanceGatewayResponse().from_map(
            self.do_request('ReplaceEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def replace_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_edge_instance_gateway_with_options(request, runtime)

    def bind_driver_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BindDriverToEdgeInstanceResponse().from_map(
            self.do_request('BindDriverToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_driver_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_driver_to_edge_instance_with_options(request, runtime)

    def batch_query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchQueryDeviceDetailResponse().from_map(
            self.do_request('BatchQueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_device_detail_with_options(request, runtime)

    def get_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetEdgeInstanceDeploymentResponse().from_map(
            self.do_request('GetEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_deployment_with_options(request, runtime)

    def query_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryTaskResponse().from_map(
            self.do_request('QueryTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_with_options(request, runtime)

    def create_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateDataAPIServiceResponse().from_map(
            self.do_request('CreateDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_apiservice_with_options(request, runtime)

    def get_data_apiservice_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetDataAPIServiceDetailResponse().from_map(
            self.do_request('GetDataAPIServiceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_data_apiservice_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_apiservice_detail_with_options(request, runtime)

    def invoke_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.InvokeDataAPIServiceResponse().from_map(
            self.do_request('InvokeDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_data_apiservice_with_options(request, runtime)

    def update_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateEdgeInstanceChannelResponse().from_map(
            self.do_request('UpdateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_channel_with_options(request, runtime)

    def query_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceChannelResponse().from_map(
            self.do_request('QueryEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_channel_with_options(request, runtime)

    def batch_unbind_device_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse().from_map(
            self.do_request('BatchUnbindDeviceFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_device_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_device_from_edge_instance_with_options(request, runtime)

    def set_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetEdgeInstanceDriverConfigsResponse().from_map(
            self.do_request('SetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_edge_instance_driver_configs_with_options(request, runtime)

    def create_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeInstanceChannelResponse().from_map(
            self.do_request('CreateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_channel_with_options(request, runtime)

    def batch_bind_device_to_edge_instance_with_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse().from_map(
            self.do_request('BatchBindDeviceToEdgeInstanceWithDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_device_to_edge_instance_with_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_device_to_edge_instance_with_driver_with_options(request, runtime)

    def batch_get_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeInstanceChannelResponse().from_map(
            self.do_request('BatchGetEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_channel_with_options(request, runtime)

    def batch_set_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse().from_map(
            self.do_request('BatchSetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_config_with_options(request, runtime)

    def batch_clear_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse().from_map(
            self.do_request('BatchClearEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_clear_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_clear_edge_instance_device_config_with_options(request, runtime)

    def batch_get_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse().from_map(
            self.do_request('BatchGetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_config_with_options(request, runtime)

    def batch_get_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse().from_map(
            self.do_request('BatchGetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_driver_configs_with_options(request, runtime)

    def clear_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse().from_map(
            self.do_request('ClearEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def clear_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_edge_instance_driver_configs_with_options(request, runtime)

    def create_lo_ra_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateLoRaNodesTaskResponse().from_map(
            self.do_request('CreateLoRaNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_lo_ra_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_lo_ra_nodes_task_with_options(request, runtime)

    def get_lora_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetLoraNodesTaskResponse().from_map(
            self.do_request('GetLoraNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_lora_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_lora_nodes_task_with_options(request, runtime)

    def query_lo_ra_join_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryLoRaJoinPermissionsResponse().from_map(
            self.do_request('QueryLoRaJoinPermissions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_lo_ra_join_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_lo_ra_join_permissions_with_options(request, runtime)

    def query_edge_instance_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceDriverResponse().from_map(
            self.do_request('QueryEdgeInstanceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_driver_with_options(request, runtime)

    def batch_update_device_nickname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchUpdateDeviceNicknameResponse().from_map(
            self.do_request('BatchUpdateDeviceNickname', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_update_device_nickname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_device_nickname_with_options(request, runtime)

    def query_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceFileResponse().from_map(
            self.do_request('QueryDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_with_options(request, runtime)

    def query_device_file_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceFileListResponse().from_map(
            self.do_request('QueryDeviceFileList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_list_with_options(request, runtime)

    def delete_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteDeviceFileResponse().from_map(
            self.do_request('DeleteDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_file_with_options(request, runtime)

    def get_nodes_adding_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetNodesAddingTaskResponse().from_map(
            self.do_request('GetNodesAddingTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_nodes_adding_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_nodes_adding_task_with_options(request, runtime)

    def set_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetDeviceDesiredPropertyResponse().from_map(
            self.do_request('SetDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_desired_property_with_options(request, runtime)

    def query_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceDesiredPropertyResponse().from_map(
            self.do_request('QueryDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_desired_property_with_options(request, runtime)

    def query_edge_instance_historic_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse().from_map(
            self.do_request('QueryEdgeInstanceHistoricDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_historic_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_historic_deployment_with_options(request, runtime)

    def create_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateProductTagsResponse().from_map(
            self.do_request('CreateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_tags_with_options(request, runtime)

    def update_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateProductTagsResponse().from_map(
            self.do_request('UpdateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_tags_with_options(request, runtime)

    def delete_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteProductTagsResponse().from_map(
            self.do_request('DeleteProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_tags_with_options(request, runtime)

    def list_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListProductTagsResponse().from_map(
            self.do_request('ListProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_tags_with_options(request, runtime)

    def list_product_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListProductByTagsResponse().from_map(
            self.do_request('ListProductByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_tags_with_options(request, runtime)

    def query_device_group_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceGroupByTagsResponse().from_map(
            self.do_request('QueryDeviceGroupByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_tags_with_options(request, runtime)

    def batch_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchAddThingTopoResponse().from_map(
            self.do_request('BatchAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_thing_topo_with_options(request, runtime)

    def query_device_list_by_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceListByDeviceGroupResponse().from_map(
            self.do_request('QueryDeviceListByDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_list_by_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_list_by_device_group_with_options(request, runtime)

    def query_device_properties_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDevicePropertiesDataResponse().from_map(
            self.do_request('QueryDevicePropertiesData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_properties_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_properties_data_with_options(request, runtime)

    def unbind_role_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UnbindRoleFromEdgeInstanceResponse().from_map(
            self.do_request('UnbindRoleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_role_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_role_from_edge_instance_with_options(request, runtime)

    def update_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateEdgeInstanceResponse().from_map(
            self.do_request('UpdateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_with_options(request, runtime)

    def get_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetEdgeInstanceResponse().from_map(
            self.do_request('GetEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_with_options(request, runtime)

    def delete_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteEdgeInstanceResponse().from_map(
            self.do_request('DeleteEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_with_options(request, runtime)

    def create_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeInstanceResponse().from_map(
            self.do_request('CreateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_with_options(request, runtime)

    def query_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceGatewayResponse().from_map(
            self.do_request('QueryEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_gateway_with_options(request, runtime)

    def query_edge_instance_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceDeviceResponse().from_map(
            self.do_request('QueryEdgeInstanceDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_with_options(request, runtime)

    def bind_gateway_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BindGatewayToEdgeInstanceResponse().from_map(
            self.do_request('BindGatewayToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_gateway_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_gateway_to_edge_instance_with_options(request, runtime)

    def query_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryEdgeInstanceResponse().from_map(
            self.do_request('QueryEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_with_options(request, runtime)

    def create_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateEdgeInstanceDeploymentResponse().from_map(
            self.do_request('CreateEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_deployment_with_options(request, runtime)

    def bind_role_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BindRoleToEdgeInstanceResponse().from_map(
            self.do_request('BindRoleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_role_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_role_to_edge_instance_with_options(request, runtime)

    def query_super_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QuerySuperDeviceGroupResponse().from_map(
            self.do_request('QuerySuperDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_super_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_super_device_group_with_options(request, runtime)

    def query_device_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceByTagsResponse().from_map(
            self.do_request('QueryDeviceByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_tags_with_options(request, runtime)

    def set_devices_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetDevicesPropertyResponse().from_map(
            self.do_request('SetDevicesProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_devices_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_devices_property_with_options(request, runtime)

    def invoke_things_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.InvokeThingsServiceResponse().from_map(
            self.do_request('InvokeThingsService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_things_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_things_service_with_options(request, runtime)

    def set_device_group_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetDeviceGroupTagsResponse().from_map(
            self.do_request('SetDeviceGroupTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_group_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_group_tags_with_options(request, runtime)

    def query_app_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryAppDeviceListResponse().from_map(
            self.do_request('QueryAppDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_app_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_app_device_list_with_options(request, runtime)

    def update_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateDeviceGroupResponse().from_map(
            self.do_request('UpdateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_group_with_options(request, runtime)

    def query_device_group_tag_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceGroupTagListResponse().from_map(
            self.do_request('QueryDeviceGroupTagList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_tag_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_tag_list_with_options(request, runtime)

    def query_device_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceGroupListResponse().from_map(
            self.do_request('QueryDeviceGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_list_with_options(request, runtime)

    def query_device_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceGroupInfoResponse().from_map(
            self.do_request('QueryDeviceGroupInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_info_with_options(request, runtime)

    def query_device_group_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceGroupByDeviceResponse().from_map(
            self.do_request('QueryDeviceGroupByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_device_with_options(request, runtime)

    def delete_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteDeviceGroupResponse().from_map(
            self.do_request('DeleteDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_group_with_options(request, runtime)

    def create_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateDeviceGroupResponse().from_map(
            self.do_request('CreateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_group_with_options(request, runtime)

    def batch_delete_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse().from_map(
            self.do_request('BatchDeleteDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_device_group_relations_with_options(request, runtime)

    def batch_add_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchAddDeviceGroupRelationsResponse().from_map(
            self.do_request('BatchAddDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_device_group_relations_with_options(request, runtime)

    def rrpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.RRpcResponse().from_map(
            self.do_request('RRpc', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rrpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rrpc_with_options(request, runtime)

    def query_page_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryPageByApplyIdResponse().from_map(
            self.do_request('QueryPageByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_page_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_page_by_apply_id_with_options(request, runtime)

    def query_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceResponse().from_map(
            self.do_request('QueryDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_with_options(request, runtime)

    def save_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SaveDevicePropResponse().from_map(
            self.do_request('SaveDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def save_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_device_prop_with_options(request, runtime)

    def query_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryTopicRouteTableResponse().from_map(
            self.do_request('QueryTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_route_table_with_options(request, runtime)

    def query_topic_reverse_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryTopicReverseRouteTableResponse().from_map(
            self.do_request('QueryTopicReverseRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_reverse_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_reverse_route_table_with_options(request, runtime)

    def pub_broadcast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.PubBroadcastResponse().from_map(
            self.do_request('PubBroadcast', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub_broadcast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_broadcast_with_options(request, runtime)

    def delete_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteTopicRouteTableResponse().from_map(
            self.do_request('DeleteTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_route_table_with_options(request, runtime)

    def delete_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteDevicePropResponse().from_map(
            self.do_request('DeleteDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_prop_with_options(request, runtime)

    def create_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateTopicRouteTableResponse().from_map(
            self.do_request('CreateTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_route_table_with_options(request, runtime)

    def batch_get_device_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchGetDeviceStateResponse().from_map(
            self.do_request('BatchGetDeviceState', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_state_with_options(request, runtime)

    def update_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateRuleActionResponse().from_map(
            self.do_request('UpdateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_action_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateRuleResponse().from_map(
            self.do_request('UpdateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateProductTopicResponse().from_map(
            self.do_request('UpdateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_topic_with_options(request, runtime)

    def update_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateDeviceShadowResponse().from_map(
            self.do_request('UpdateDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_shadow_with_options(request, runtime)

    def stop_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.StopRuleResponse().from_map(
            self.do_request('StopRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_rule_with_options(request, runtime)

    def start_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.StartRuleResponse().from_map(
            self.do_request('StartRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_rule_with_options(request, runtime)

    def query_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryProductTopicResponse().from_map(
            self.do_request('QueryProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_topic_with_options(request, runtime)

    def query_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDevicePropResponse().from_map(
            self.do_request('QueryDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_prop_with_options(request, runtime)

    def pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.PubResponse().from_map(
            self.do_request('Pub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_with_options(request, runtime)

    def list_rule_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListRuleActionsResponse().from_map(
            self.do_request('ListRuleActions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_actions_with_options(request, runtime)

    def list_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ListRuleResponse().from_map(
            self.do_request('ListRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_with_options(request, runtime)

    def get_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetRuleActionResponse().from_map(
            self.do_request('GetRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_action_with_options(request, runtime)

    def get_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetRuleResponse().from_map(
            self.do_request('GetRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    def get_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetDeviceShadowResponse().from_map(
            self.do_request('GetDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_shadow_with_options(request, runtime)

    def delete_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteRuleActionResponse().from_map(
            self.do_request('DeleteRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_action_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteRuleResponse().from_map(
            self.do_request('DeleteRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def delete_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteProductTopicResponse().from_map(
            self.do_request('DeleteProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_topic_with_options(request, runtime)

    def create_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateRuleActionResponse().from_map(
            self.do_request('CreateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_action_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateRuleResponse().from_map(
            self.do_request('CreateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateProductTopicResponse().from_map(
            self.do_request('CreateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_topic_with_options(request, runtime)

    def query_batch_register_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryBatchRegisterDeviceStatusResponse().from_map(
            self.do_request('QueryBatchRegisterDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_batch_register_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_batch_register_device_status_with_options(request, runtime)

    def get_gateway_by_sub_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetGatewayBySubDeviceResponse().from_map(
            self.do_request('GetGatewayBySubDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_gateway_by_sub_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_by_sub_device_with_options(request, runtime)

    def reset_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.ResetThingResponse().from_map(
            self.do_request('ResetThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_thing_with_options(request, runtime)

    def remove_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.RemoveThingTopoResponse().from_map(
            self.do_request('RemoveThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def remove_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_thing_topo_with_options(request, runtime)

    def notify_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.NotifyAddThingTopoResponse().from_map(
            self.do_request('NotifyAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def notify_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.notify_add_thing_topo_with_options(request, runtime)

    def get_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetThingTopoResponse().from_map(
            self.do_request('GetThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_topo_with_options(request, runtime)

    def query_device_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDevicePropertyStatusResponse().from_map(
            self.do_request('QueryDevicePropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_status_with_options(request, runtime)

    def query_device_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDevicePropertyDataResponse().from_map(
            self.do_request('QueryDevicePropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_data_with_options(request, runtime)

    def batch_register_device_with_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse().from_map(
            self.do_request('BatchRegisterDeviceWithApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device_with_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_apply_id_with_options(request, runtime)

    def batch_register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchRegisterDeviceResponse().from_map(
            self.do_request('BatchRegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_options(request, runtime)

    def batch_check_device_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.BatchCheckDeviceNamesResponse().from_map(
            self.do_request('BatchCheckDeviceNames', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_device_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_device_names_with_options(request, runtime)

    def update_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.UpdateProductResponse().from_map(
            self.do_request('UpdateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    def set_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.SetDevicePropertyResponse().from_map(
            self.do_request('SetDeviceProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_property_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.RegisterDeviceResponse().from_map(
            self.do_request('RegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryProductListResponse().from_map(
            self.do_request('QueryProductList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    def query_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryProductResponse().from_map(
            self.do_request('QueryProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_with_options(request, runtime)

    def query_device_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceStatisticsResponse().from_map(
            self.do_request('QueryDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_statistics_with_options(request, runtime)

    def query_device_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceServiceDataResponse().from_map(
            self.do_request('QueryDeviceServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_service_data_with_options(request, runtime)

    def query_device_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceEventDataResponse().from_map(
            self.do_request('QueryDeviceEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_data_with_options(request, runtime)

    def query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.QueryDeviceDetailResponse().from_map(
            self.do_request('QueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_detail_with_options(request, runtime)

    def invoke_thing_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.InvokeThingServiceResponse().from_map(
            self.do_request('InvokeThingService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_thing_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_thing_service_with_options(request, runtime)

    def get_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.GetDeviceStatusResponse().from_map(
            self.do_request('GetDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_status_with_options(request, runtime)

    def enable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.EnableThingResponse().from_map(
            self.do_request('EnableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_thing_with_options(request, runtime)

    def disable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DisableThingResponse().from_map(
            self.do_request('DisableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_thing_with_options(request, runtime)

    def delete_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteProductResponse().from_map(
            self.do_request('DeleteProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.DeleteDeviceResponse().from_map(
            self.do_request('DeleteDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def create_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return iot_20180120_models.CreateProductResponse().from_map(
            self.do_request('CreateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
