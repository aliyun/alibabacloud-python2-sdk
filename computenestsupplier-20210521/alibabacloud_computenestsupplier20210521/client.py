# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenestsupplier20210521 import models as compute_nest_supplier_20210521_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('computenestsupplier', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def invoke_service_instance_operation_apiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.InvokeServiceInstanceOperationAPIResponse(),
            self.do_rpcrequest('InvokeServiceInstanceOperationAPI', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_service_instance_operation_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_service_instance_operation_apiwith_options(request, runtime)

    def get_service_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            self.do_rpcrequest('GetServiceInstance', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            self.do_rpcrequest('DeleteService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def list_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            self.do_rpcrequest('ListServices', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    def cancel_service_registration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
            self.do_rpcrequest('CancelServiceRegistration', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_service_registration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_service_registration_with_options(request, runtime)

    def list_service_registrations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
            self.do_rpcrequest('ListServiceRegistrations', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_registrations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_registrations_with_options(request, runtime)

    def get_supplier_information_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
            self.do_rpcrequest('GetSupplierInformation', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_supplier_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_supplier_information_with_options(request, runtime)

    def list_service_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            self.do_rpcrequest('ListServiceInstances', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    def register_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RegisterServiceResponse(),
            self.do_rpcrequest('RegisterService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_service_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            self.do_rpcrequest('CreateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def list_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListPoliciesResponse(),
            self.do_rpcrequest('ListPolicies', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    def update_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            self.do_rpcrequest('UpdateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    def launch_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.LaunchServiceResponse(),
            self.do_rpcrequest('LaunchService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_service_with_options(request, runtime)

    def withdraw_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
            self.do_rpcrequest('WithdrawService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def withdraw_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.withdraw_service_with_options(request, runtime)

    def update_supplier_information_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse(),
            self.do_rpcrequest('UpdateSupplierInformation', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_supplier_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_supplier_information_with_options(request, runtime)

    def get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            self.do_rpcrequest('GetService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)
