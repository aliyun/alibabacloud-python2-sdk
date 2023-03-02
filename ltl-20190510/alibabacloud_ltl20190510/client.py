# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ltl20190510 import models as ltl_20190510_models
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
            'ap-northeast-1': 'ltl.aliyuncs.com',
            'ap-northeast-2-pop': 'ltl.aliyuncs.com',
            'ap-south-1': 'ltl.aliyuncs.com',
            'ap-southeast-1': 'ltl.aliyuncs.com',
            'ap-southeast-2': 'ltl.aliyuncs.com',
            'ap-southeast-3': 'ltl.aliyuncs.com',
            'ap-southeast-5': 'ltl.aliyuncs.com',
            'cn-beijing': 'ltl.aliyuncs.com',
            'cn-beijing-finance-1': 'ltl.aliyuncs.com',
            'cn-beijing-finance-pop': 'ltl.aliyuncs.com',
            'cn-beijing-gov-1': 'ltl.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ltl.aliyuncs.com',
            'cn-chengdu': 'ltl.aliyuncs.com',
            'cn-edge-1': 'ltl.aliyuncs.com',
            'cn-fujian': 'ltl.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ltl.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ltl.aliyuncs.com',
            'cn-hangzhou-finance': 'ltl.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ltl.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ltl.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ltl.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ltl.aliyuncs.com',
            'cn-hangzhou-test-306': 'ltl.aliyuncs.com',
            'cn-hongkong': 'ltl.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ltl.aliyuncs.com',
            'cn-huhehaote': 'ltl.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ltl.aliyuncs.com',
            'cn-north-2-gov-1': 'ltl.aliyuncs.com',
            'cn-qingdao': 'ltl.aliyuncs.com',
            'cn-qingdao-nebula': 'ltl.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ltl.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ltl.aliyuncs.com',
            'cn-shanghai-finance-1': 'ltl.aliyuncs.com',
            'cn-shanghai-inner': 'ltl.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ltl.aliyuncs.com',
            'cn-shenzhen': 'ltl.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ltl.aliyuncs.com',
            'cn-shenzhen-inner': 'ltl.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ltl.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ltl.aliyuncs.com',
            'cn-wuhan': 'ltl.aliyuncs.com',
            'cn-wulanchabu': 'ltl.aliyuncs.com',
            'cn-yushanfang': 'ltl.aliyuncs.com',
            'cn-zhangbei': 'ltl.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ltl.aliyuncs.com',
            'cn-zhangjiakou': 'ltl.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ltl.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ltl.aliyuncs.com',
            'eu-central-1': 'ltl.aliyuncs.com',
            'eu-west-1': 'ltl.aliyuncs.com',
            'eu-west-1-oxs': 'ltl.aliyuncs.com',
            'me-east-1': 'ltl.aliyuncs.com',
            'rus-west-1-pop': 'ltl.aliyuncs.com',
            'us-east-1': 'ltl.aliyuncs.com',
            'us-west-1': 'ltl.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ltl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_data_model_config_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.data_model_code):
            query['DataModelCode'] = request.data_model_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyDataModelConfigInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ApplyDataModelConfigInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_data_model_config_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_data_model_config_info_with_options(request, runtime)

    def attach_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachData',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.AttachDataResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_data_with_options(request, runtime)

    def attach_data_with_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDataWithSignature',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.AttachDataWithSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_data_with_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_data_with_signature_with_options(request, runtime)

    def authorize_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.AuthorizeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_device_with_options(request, runtime)

    def authorize_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeDeviceGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.AuthorizeDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_device_group_with_options(request, runtime)

    def batch_upload_mpco_sphase_digest_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.BatchUploadMPCoSPhaseDigestInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phase_data_list):
            request.phase_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phase_data_list, 'PhaseDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.phase_data_list_shrink):
            query['PhaseDataList'] = request.phase_data_list_shrink
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUploadMPCoSPhaseDigestInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.BatchUploadMPCoSPhaseDigestInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_upload_mpco_sphase_digest_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_upload_mpco_sphase_digest_info_with_options(request, runtime)

    def batch_upload_mpco_sphase_digest_info_by_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.BatchUploadMPCoSPhaseDigestInfoByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phase_data_list):
            request.phase_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phase_data_list, 'PhaseDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.phase_data_list_shrink):
            query['PhaseDataList'] = request.phase_data_list_shrink
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUploadMPCoSPhaseDigestInfoByDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.BatchUploadMPCoSPhaseDigestInfoByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_upload_mpco_sphase_digest_info_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_upload_mpco_sphase_digest_info_by_device_with_options(request, runtime)

    def batch_upload_mpco_sphase_text_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.BatchUploadMPCoSPhaseTextInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phase_data_list):
            request.phase_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phase_data_list, 'PhaseDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.phase_data_list_shrink):
            query['PhaseDataList'] = request.phase_data_list_shrink
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUploadMPCoSPhaseTextInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.BatchUploadMPCoSPhaseTextInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_upload_mpco_sphase_text_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_upload_mpco_sphase_text_info_with_options(request, runtime)

    def batch_upload_mpco_sphase_text_info_by_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.BatchUploadMPCoSPhaseTextInfoByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phase_data_list):
            request.phase_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phase_data_list, 'PhaseDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.phase_data_list_shrink):
            query['PhaseDataList'] = request.phase_data_list_shrink
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUploadMPCoSPhaseTextInfoByDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.BatchUploadMPCoSPhaseTextInfoByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_upload_mpco_sphase_text_info_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_upload_mpco_sphase_text_info_by_device_with_options(request, runtime)

    def create_mpco_sphase_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMPCoSPhase',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.CreateMPCoSPhaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mpco_sphase(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mpco_sphase_with_options(request, runtime)

    def create_mpco_sphase_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMPCoSPhaseGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.CreateMPCoSPhaseGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mpco_sphase_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mpco_sphase_group_with_options(request, runtime)

    def create_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_contact):
            query['MemberContact'] = request.member_contact
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMember',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.CreateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def create_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_member_with_options(request, runtime)

    def describe_capacity_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeCapacityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_capacity_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_info_with_options(request, runtime)

    def describe_mpco_sauthorized_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPCoSAuthorizedInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeMPCoSAuthorizedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mpco_sauthorized_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mpco_sauthorized_info_with_options(request, runtime)

    def describe_mpco_sphase_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.data_seq):
            query['DataSeq'] = request.data_seq
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPCoSPhaseInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeMPCoSPhaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mpco_sphase_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mpco_sphase_info_with_options(request, runtime)

    def describe_mpco_sresource_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPCoSResourceInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeMPCoSResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mpco_sresource_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mpco_sresource_info_with_options(request, runtime)

    def describe_member_capacity_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberCapacityInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeMemberCapacityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_member_capacity_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_member_capacity_info_with_options(request, runtime)

    def describe_resource_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.DescribeResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_info_with_options(request, runtime)

    def get_block_chain_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBlockChainInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.GetBlockChainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_block_chain_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_block_chain_info_with_options(request, runtime)

    def get_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetData',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.GetDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_with_options(request, runtime)

    def get_data_model_config_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.data_model_code):
            query['DataModelCode'] = request.data_model_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataModelConfigInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.GetDataModelConfigInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_model_config_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_model_config_info_with_options(request, runtime)

    def get_history_data_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryDataCount',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.GetHistoryDataCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_history_data_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_history_data_count_with_options(request, runtime)

    def get_history_data_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryDataList',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.GetHistoryDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_history_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_history_data_list_with_options(request, runtime)

    def list_dependent_data_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDependentDataModels',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListDependentDataModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dependent_data_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dependent_data_models_with_options(request, runtime)

    def list_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_with_options(request, runtime)

    def list_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_group_with_options(request, runtime)

    def list_mpco_sphase_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMPCoSPhase',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListMPCoSPhaseResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mpco_sphase(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mpco_sphase_with_options(request, runtime)

    def list_mpco_sphase_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMPCoSPhaseGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListMPCoSPhaseGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mpco_sphase_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mpco_sphase_group_with_options(request, runtime)

    def list_mpco_sphase_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMPCoSPhaseHistory',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListMPCoSPhaseHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mpco_sphase_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mpco_sphase_history_with_options(request, runtime)

    def list_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMember',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_member_with_options(request, runtime)

    def list_multi_party_collaboration_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiPartyCollaborationChain',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListMultiPartyCollaborationChainResponse(),
            self.call_api(params, req, runtime)
        )

    def list_multi_party_collaboration_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_multi_party_collaboration_chain_with_options(request, runtime)

    def list_psmember_data_type_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPSMemberDataTypeCode',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListPSMemberDataTypeCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_psmember_data_type_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_psmember_data_type_code_with_options(request, runtime)

    def list_proof_chain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProofChain',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ListProofChainResponse(),
            self.call_api(params, req, runtime)
        )

    def list_proof_chain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_proof_chain_with_options(request, runtime)

    def lock_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockMember',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.LockMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_member_with_options(request, runtime)

    def modify_mpco_sphase_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMPCoSPhase',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ModifyMPCoSPhaseResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mpco_sphase(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mpco_sphase_with_options(request, runtime)

    def modify_mpco_sphase_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMPCoSPhaseGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ModifyMPCoSPhaseGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mpco_sphase_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mpco_sphase_group_with_options(request, runtime)

    def modify_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_contact):
            query['MemberContact'] = request.member_contact
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.member_phone):
            query['MemberPhone'] = request.member_phone
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMember',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.ModifyMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_member_with_options(request, runtime)

    def register_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.authorize_type):
            query['AuthorizeType'] = request.authorize_type
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDeviceGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.RegisterDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def register_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_group_with_options(request, runtime)

    def set_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetData',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.SetDataResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_with_options(request, runtime)

    def set_data_with_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataWithSignature',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.SetDataWithSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def set_data_with_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_data_with_signature_with_options(request, runtime)

    def un_authorize_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAuthorizeDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UnAuthorizeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def un_authorize_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_authorize_device_with_options(request, runtime)

    def un_authorize_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAuthorizeDeviceGroup',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UnAuthorizeDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def un_authorize_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_authorize_device_group_with_options(request, runtime)

    def un_lock_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnLockMember',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UnLockMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def un_lock_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_lock_member_with_options(request, runtime)

    def update_mpco_sauthorized_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.UpdateMPCoSAuthorizedInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.authorized_phase_list):
            request.authorized_phase_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.authorized_phase_list, 'AuthorizedPhaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.authorized_phase_list_shrink):
            query['AuthorizedPhaseList'] = request.authorized_phase_list_shrink
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMPCoSAuthorizedInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UpdateMPCoSAuthorizedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mpco_sauthorized_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mpco_sauthorized_info_with_options(request, runtime)

    def upload_mpco_sphase_digest_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.UploadMPCoSPhaseDigestInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_data_list):
            request.related_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_data_list, 'RelatedDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.data_seq):
            query['DataSeq'] = request.data_seq
        if not UtilClient.is_unset(request.phase_data):
            query['PhaseData'] = request.phase_data
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.related_data_list_shrink):
            query['RelatedDataList'] = request.related_data_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMPCoSPhaseDigestInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UploadMPCoSPhaseDigestInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mpco_sphase_digest_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mpco_sphase_digest_info_with_options(request, runtime)

    def upload_mpco_sphase_digest_info_by_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.UploadMPCoSPhaseDigestInfoByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_data_list):
            request.related_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_data_list, 'RelatedDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.data_seq):
            query['DataSeq'] = request.data_seq
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.phase_data):
            query['PhaseData'] = request.phase_data
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.related_data_list_shrink):
            query['RelatedDataList'] = request.related_data_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMPCoSPhaseDigestInfoByDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UploadMPCoSPhaseDigestInfoByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mpco_sphase_digest_info_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mpco_sphase_digest_info_by_device_with_options(request, runtime)

    def upload_mpco_sphase_text_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.UploadMPCoSPhaseTextInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_data_list):
            request.related_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_data_list, 'RelatedDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.data_seq):
            query['DataSeq'] = request.data_seq
        if not UtilClient.is_unset(request.phase_data):
            query['PhaseData'] = request.phase_data
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.related_data_list_shrink):
            query['RelatedDataList'] = request.related_data_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMPCoSPhaseTextInfo',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UploadMPCoSPhaseTextInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mpco_sphase_text_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mpco_sphase_text_info_with_options(request, runtime)

    def upload_mpco_sphase_text_info_by_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ltl_20190510_models.UploadMPCoSPhaseTextInfoByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_data_list):
            request.related_data_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_data_list, 'RelatedDataList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.data_key):
            query['DataKey'] = request.data_key
        if not UtilClient.is_unset(request.data_seq):
            query['DataSeq'] = request.data_seq
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.iot_signature):
            query['IotSignature'] = request.iot_signature
        if not UtilClient.is_unset(request.phase_data):
            query['PhaseData'] = request.phase_data
        if not UtilClient.is_unset(request.phase_group_id):
            query['PhaseGroupId'] = request.phase_group_id
        if not UtilClient.is_unset(request.phase_id):
            query['PhaseId'] = request.phase_id
        if not UtilClient.is_unset(request.related_data_list_shrink):
            query['RelatedDataList'] = request.related_data_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMPCoSPhaseTextInfoByDevice',
            version='2019-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ltl_20190510_models.UploadMPCoSPhaseTextInfoByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mpco_sphase_text_info_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mpco_sphase_text_info_by_device_with_options(request, runtime)
