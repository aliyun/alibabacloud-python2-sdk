# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hologram20220601 import models as hologram_20220601_models
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
        self._endpoint = self.get_endpoint('hologram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_instance_with_options(self, request, headers, runtime):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        *   When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        

        @param request: CreateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['autoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.leader_instance_id):
            body['leaderInstanceId'] = request.leader_instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['pricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about the billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/developer-reference/api-hologram-2022-06-01-createinstance).
        *   When you purchase a Hologres instance, you must specify the region and zone in which the Hologres instance resides. A region may correspond to multiple zones. Example:
        <!---->
        cn-hangzhou: cn-hangzhou-h, cn-hangzhou-j
        cn-shanghai: cn-shanghai-e, cn-shanghai-f
        cn-beijing: cn-beijing-i, cn-beijing-g
        cn-zhangjiakou: cn-zhangjiakou-b
        cn-shenzhen: cn-shenzhen-e
        cn-hongkong: cn-hongkong-b
        cn-shanghai-finance-1: cn-shanghai-finance-1z
        ap-northeast-1: ap-northeast-1a
        ap-southeast-1: ap-southeast-1c
        ap-southeast-3: ap-southeast-3b
        ap-southeast-5: ap-southeast-5b
        ap-south-1: ap-south-1b
        eu-central-1: eu-central-1a
        us-east-1: us-east-1a
        us-west-1: us-west-1b
        

        @param request: CreateInstanceRequest

        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def delete_instance_with_options(self, instance_id, request, headers, runtime):
        """
        > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        *   After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        *   You can delete only pay-as-you-go instances.
        *   If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        

        @param request: DeleteInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id, request):
        """
        > Before you call this operation, read the documentation and make sure that you understand the prerequisites and impacts of this operation.
        *   After you delete a Hologres instance, data and objects in the instance cannot be restored. Proceed with caution. For more information, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview#section-h6a-x58-jc0).
        *   You can delete only pay-as-you-go instances.
        *   If you want to unsubscribe from a subscription instance, submit a ticket.[](https://help.aliyun.com/document_detail/150284.html#section-ogc-9vc-858)
        

        @param request: DeleteInstanceRequest

        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cms_instance_type):
            body['cmsInstanceType'] = request.cms_instance_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def renew_instance_with_options(self, instance_id, request, headers, runtime):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        *   For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        *   You can renew only subscription instances.
        

        @param request: RenewInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/renew' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, instance_id, request):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about billing details of Hologres, see [Pricing](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        *   For more information about how to renew a Hologres instance, see [Manage renewals](https://www.alibabacloud.com/help/en/hologres/product-overview/manage-renewals?spm=a2c63.p38356.0.0.73f27c8d1Q0FUi).
        *   You can renew only subscription instances.
        

        @param request: RenewInstanceRequest

        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    def restart_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/restart' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, headers, runtime)

    def resume_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_instance_with_options(instance_id, headers, runtime)

    def scale_instance_with_options(self, instance_id, request, headers, runtime):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about the billing details of Hologres, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        *   During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resources of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade and downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications?spm=a2c63.p38356.0.0.2bb57c8dbVt68U).
        

        @param request: ScaleInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScaleInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not UtilClient.is_unset(request.scale_type):
            body['scaleType'] = request.scale_type
        if not UtilClient.is_unset(request.storage_size):
            body['storageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/scale' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.ScaleInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_instance(self, instance_id, request):
        """
        > Before you call this operation, make sure that you understand the billing method and pricing of Hologres because this operation is charged.
        *   For more information about the billing details of Hologres, see [Billing overview](https://www.alibabacloud.com/help/en/hologres/product-overview/billing-overview).
        *   During the change of computing resource specifications of a Hologres instance, the instance is unavailable. During the change of storage resources of a Hologres instance, the instance can work normally. Do not frequently change instance specifications. For more information, see [Upgrade and downgrade instance specifications](https://www.alibabacloud.com/help/en/hologres/product-overview/upgrade-or-downgrade-instance-specifications?spm=a2c63.p38356.0.0.2bb57c8dbVt68U).
        

        @param request: ScaleInstanceRequest

        @return: ScaleInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_instance_with_options(instance_id, request, headers, runtime)

    def stop_instance_with_options(self, instance_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, headers, runtime)

    def update_instance_name_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/instanceName' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_name(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(instance_id, request, headers, runtime)

    def update_instance_network_type_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not UtilClient.is_unset(request.network_types):
            body['networkTypes'] = request.network_types
        if not UtilClient.is_unset(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceNetworkType',
            version='2022-06-01',
            protocol='HTTPS',
            pathname='/api/v1/instances/%s/network' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            hologram_20220601_models.UpdateInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_network_type(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_network_type_with_options(instance_id, request, headers, runtime)
