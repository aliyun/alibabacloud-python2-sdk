# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ice20201109 import models as ice20201109_models
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
            'ap-northeast-1': 'ice.aliyuncs.com',
            'ap-northeast-2-pop': 'ice.aliyuncs.com',
            'ap-south-1': 'ice.aliyuncs.com',
            'ap-southeast-1': 'ice.aliyuncs.com',
            'ap-southeast-2': 'ice.aliyuncs.com',
            'ap-southeast-3': 'ice.aliyuncs.com',
            'ap-southeast-5': 'ice.aliyuncs.com',
            'cn-beijing': 'ice.aliyuncs.com',
            'cn-beijing-finance-1': 'ice.aliyuncs.com',
            'cn-beijing-finance-pop': 'ice.aliyuncs.com',
            'cn-beijing-gov-1': 'ice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ice.aliyuncs.com',
            'cn-chengdu': 'ice.aliyuncs.com',
            'cn-edge-1': 'ice.aliyuncs.com',
            'cn-fujian': 'ice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ice.aliyuncs.com',
            'cn-hangzhou': 'ice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ice.aliyuncs.com',
            'cn-hangzhou-finance': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ice.aliyuncs.com',
            'cn-hangzhou-test-306': 'ice.aliyuncs.com',
            'cn-hongkong': 'ice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ice.aliyuncs.com',
            'cn-huhehaote': 'ice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ice.aliyuncs.com',
            'cn-north-2-gov-1': 'ice.aliyuncs.com',
            'cn-qingdao': 'ice.aliyuncs.com',
            'cn-qingdao-nebula': 'ice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ice.aliyuncs.com',
            'cn-shanghai-finance-1': 'ice.aliyuncs.com',
            'cn-shanghai-inner': 'ice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ice.aliyuncs.com',
            'cn-shenzhen': 'ice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ice.aliyuncs.com',
            'cn-shenzhen-inner': 'ice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ice.aliyuncs.com',
            'cn-wuhan': 'ice.aliyuncs.com',
            'cn-wulanchabu': 'ice.aliyuncs.com',
            'cn-yushanfang': 'ice.aliyuncs.com',
            'cn-zhangbei': 'ice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ice.aliyuncs.com',
            'cn-zhangjiakou': 'ice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ice.aliyuncs.com',
            'eu-central-1': 'ice.aliyuncs.com',
            'eu-west-1': 'ice.aliyuncs.com',
            'eu-west-1-oxs': 'ice.aliyuncs.com',
            'me-east-1': 'ice.aliyuncs.com',
            'rus-west-1-pop': 'ice.aliyuncs.com',
            'us-east-1': 'ice.aliyuncs.com',
            'us-west-1': 'ice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def list_smart_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            self.do_rpcrequest('ListSmartJobs', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_smart_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_smart_jobs_with_options(request, runtime)

    def describe_related_authorization_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeRelatedAuthorizationStatusResponse(),
            self.do_rpcrequest('DescribeRelatedAuthorizationStatus', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_related_authorization_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_related_authorization_status_with_options(runtime)

    def delete_smart_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            self.do_rpcrequest('DeleteSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_smart_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_job_with_options(request, runtime)

    def add_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            self.do_rpcrequest('AddTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    def update_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            self.do_rpcrequest('UpdateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    def list_media_producing_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaProducingJobsResponse(),
            self.do_rpcrequest('ListMediaProducingJobs', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_producing_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_media_producing_jobs_with_options(request, runtime)

    def get_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            self.do_rpcrequest('GetEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    def get_default_storage_location_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            self.do_rpcrequest('GetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_storage_location(self):
        runtime = util_models.RuntimeOptions()
        return self.get_default_storage_location_with_options(runtime)

    def delete_media_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            self.do_rpcrequest('DeleteMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_media_infos_with_options(request, runtime)

    def set_event_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            self.do_rpcrequest('SetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_event_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_event_callback_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def register_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            self.do_rpcrequest('RegisterMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_media_info_with_options(request, runtime)

    def create_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            self.do_rpcrequest('CreateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_editing_project_with_options(request, runtime)

    def batch_get_media_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            self.do_rpcrequest('BatchGetMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_get_media_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_media_infos_with_options(request, runtime)

    def set_default_storage_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            self.do_rpcrequest('SetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_storage_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_storage_location_with_options(request, runtime)

    def update_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            self.do_rpcrequest('UpdateMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_media_info_with_options(request, runtime)

    def get_media_producing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            self.do_rpcrequest('GetMediaProducingJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_media_producing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_producing_job_with_options(request, runtime)

    def describe_ice_product_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeIceProductStatusResponse(),
            self.do_rpcrequest('DescribeIceProductStatus', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ice_product_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_ice_product_status_with_options(runtime)

    def list_media_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            self.do_rpcrequest('ListMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_media_basic_infos_with_options(request, runtime)

    def submit_subtitle_produce_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            self.do_rpcrequest('SubmitSubtitleProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_subtitle_produce_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_subtitle_produce_job_with_options(request, runtime)

    def submit_key_word_cut_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitKeyWordCutJobResponse(),
            self.do_rpcrequest('SubmitKeyWordCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_key_word_cut_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_key_word_cut_job_with_options(request, runtime)

    def add_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            self.do_rpcrequest('AddEditingProjectMaterials', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    def submit_asrjob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            self.do_rpcrequest('SubmitASRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_asrjob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_asrjob_with_options(request, runtime)

    def get_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            self.do_rpcrequest('GetEditingProject', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    def list_sys_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSysTemplatesResponse(),
            self.do_rpcrequest('ListSysTemplates', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_sys_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sys_templates_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            self.do_rpcrequest('DeleteTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def submit_irjob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitIRJobResponse(),
            self.do_rpcrequest('SubmitIRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_irjob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_irjob_with_options(request, runtime)

    def delete_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            self.do_rpcrequest('DeleteEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    def search_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            self.do_rpcrequest('SearchEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def delete_editing_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            self.do_rpcrequest('DeleteEditingProjects', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_editing_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_projects_with_options(request, runtime)

    def get_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            self.do_rpcrequest('GetMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_with_options(request, runtime)

    def submit_smart_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSmartJobResponse(),
            self.do_rpcrequest('SubmitSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smart_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smart_job_with_options(request, runtime)

    def submit_delogo_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDelogoJobResponse(),
            self.do_rpcrequest('SubmitDelogoJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_delogo_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_delogo_job_with_options(request, runtime)

    def update_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            self.do_rpcrequest('UpdateTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def submit_audio_produce_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            self.do_rpcrequest('SubmitAudioProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_audio_produce_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_produce_job_with_options(request, runtime)

    def submit_media_producing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            self.do_rpcrequest('SubmitMediaProducingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_producing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_media_producing_job_with_options(request, runtime)

    def update_smart_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateSmartJobResponse(),
            self.do_rpcrequest('UpdateSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_smart_job_with_options(request, runtime)

    def list_all_public_media_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            self.do_rpcrequest('ListAllPublicMediaTags', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_all_public_media_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_all_public_media_tags_with_options(request, runtime)

    def submit_matting_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMattingJobResponse(),
            self.do_rpcrequest('SubmitMattingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_matting_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_matting_job_with_options(request, runtime)

    def get_event_callback_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            self.do_rpcrequest('GetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_event_callback(self):
        runtime = util_models.RuntimeOptions()
        return self.get_event_callback_with_options(runtime)

    def list_public_media_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            self.do_rpcrequest('ListPublicMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_public_media_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_media_basic_infos_with_options(request, runtime)

    def submit_cover_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitCoverJobResponse(),
            self.do_rpcrequest('SubmitCoverJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_cover_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_cover_job_with_options(request, runtime)

    def get_smart_handle_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            self.do_rpcrequest('GetSmartHandleJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_smart_handle_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_smart_handle_job_with_options(request, runtime)

    def submit_h2vjob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitH2VJobResponse(),
            self.do_rpcrequest('SubmitH2VJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_h2vjob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_h2vjob_with_options(request, runtime)

    def submit_pptcut_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPPTCutJobResponse(),
            self.do_rpcrequest('SubmitPPTCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_pptcut_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_pptcut_job_with_options(request, runtime)
