# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicecatalog20210901 import models as servicecatalog_20210901_models
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
        self._endpoint = self.get_endpoint('servicecatalog', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.approval_action):
            body['ApprovalAction'] = request.approval_action
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ApproveProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def approve_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.approve_provisioned_product_plan_with_options(request, runtime)

    def associate_principal_with_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociatePrincipalWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociatePrincipalWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_principal_with_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_principal_with_portfolio_with_options(request, runtime)

    def associate_product_with_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateProductWithPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateProductWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_product_with_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_product_with_portfolio_with_options(request, runtime)

    def associate_tag_option_with_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateTagOptionWithResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.AssociateTagOptionWithResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_tag_option_with_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_tag_option_with_resource_with_options(request, runtime)

    def cancel_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CancelProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_provisioned_product_plan_with_options(request, runtime)

    def copy_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_product_arn):
            body['SourceProductArn'] = request.source_product_arn
        if not UtilClient.is_unset(request.target_product_name):
            body['TargetProductName'] = request.target_product_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CopyProductResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_product_with_options(request, runtime)

    def create_constraint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_type):
            body['ConstraintType'] = request.constraint_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    def create_constraint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_constraint_with_options(request, runtime)

    def create_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def create_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_portfolio_with_options(request, runtime)

    def create_product_with_options(self, tmp_req, runtime):
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        

        @param tmp_req: CreateProductRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProductResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.CreateProductShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_version_parameters):
            request.product_version_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_version_parameters, 'ProductVersionParameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.product_version_parameters_shrink):
            body['ProductVersionParameters'] = request.product_version_parameters_shrink
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product(self, request):
        """
        Before you call the CreateProduct operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        

        @param request: CreateProductRequest

        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    def create_product_version_with_options(self, request, runtime):
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        

        @param request: CreateProductVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateProductVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.template_url):
            body['TemplateUrl'] = request.template_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_version(self, request):
        """
        Before you call the CreateProductVersion operation, you must call the [CreateTemplate](~~CreateTemplate~~) operation to create a template.
        

        @param request: CreateProductVersionRequest

        @return: CreateProductVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_version_with_options(request, runtime)

    def create_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_name):
            body['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_type):
            body['PlanType'] = request.plan_type
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_provisioned_product_plan_with_options(request, runtime)

    def create_tag_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tag_option_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.terraform_variables):
            body['TerraformVariables'] = request.terraform_variables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_constraint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_constraint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_constraint_with_options(request, runtime)

    def delete_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeletePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_portfolio_with_options(request, runtime)

    def delete_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    def delete_product_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_version_with_options(request, runtime)

    def delete_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_provisioned_product_plan_with_options(request, runtime)

    def delete_tag_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DeleteTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_option_with_options(request, runtime)

    def dis_associate_tag_option_from_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisAssociateTagOptionFromResource',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisAssociateTagOptionFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def dis_associate_tag_option_from_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dis_associate_tag_option_from_resource_with_options(request, runtime)

    def disassociate_principal_from_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociatePrincipalFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociatePrincipalFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_principal_from_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disassociate_principal_from_portfolio_with_options(request, runtime)

    def disassociate_product_from_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisassociateProductFromPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.DisassociateProductFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_product_from_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disassociate_product_from_portfolio_with_options(request, runtime)

    def execute_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ExecuteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_provisioned_product_plan_with_options(request, runtime)

    def get_constraint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.constraint_id):
            query['ConstraintId'] = request.constraint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    def get_constraint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_constraint_with_options(request, runtime)

    def get_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def get_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_portfolio_with_options(request, runtime)

    def get_product_as_admin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_as_admin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_product_as_admin_with_options(request, runtime)

    def get_product_as_end_user_with_options(self, request, runtime):
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        

        @param request: GetProductAsEndUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProductAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_as_end_user(self, request):
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        

        @param request: GetProductAsEndUserRequest

        @return: GetProductAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_as_end_user_with_options(request, runtime)

    def get_product_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_product_version_with_options(request, runtime)

    def get_provisioned_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    def get_provisioned_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_provisioned_product_with_options(request, runtime)

    def get_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def get_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_provisioned_product_plan_with_options(request, runtime)

    def get_tag_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tag_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tag_option_with_options(request, runtime)

    def get_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def launch_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not UtilClient.is_unset(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LaunchProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.LaunchProductResponse(),
            self.call_api(params, req, runtime)
        )

    def launch_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_product_with_options(request, runtime)

    def list_launch_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLaunchOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListLaunchOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_launch_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_launch_options_with_options(request, runtime)

    def list_portfolios_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortfolios',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPortfoliosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_portfolios(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_portfolios_with_options(request, runtime)

    def list_principals_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrincipals',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListPrincipalsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_principals(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_principals_with_options(request, runtime)

    def list_product_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_versions_with_options(request, runtime)

    def list_products_as_admin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsAdmin',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products_as_admin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_products_as_admin_with_options(request, runtime)

    def list_products_as_end_user_with_options(self, request, runtime):
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        

        @param request: ListProductsAsEndUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProductsAsEndUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductsAsEndUser',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProductsAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products_as_end_user(self, request):
        """
        Make sure that you are granted the permissions to manage relevant products as a user by an administrator. For more information, see [Manage access permissions](~~405233~~).
        

        @param request: ListProductsAsEndUserRequest

        @return: ListProductsAsEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_products_as_end_user_with_options(request, runtime)

    def list_provisioned_product_plan_approvers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlanApprovers',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlanApproversResponse(),
            self.call_api(params, req, runtime)
        )

    def list_provisioned_product_plan_approvers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_product_plan_approvers_with_options(request, runtime)

    def list_provisioned_product_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.approval_filter):
            query['ApprovalFilter'] = request.approval_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProductPlans',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def list_provisioned_product_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_product_plans_with_options(request, runtime)

    def list_provisioned_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionedProducts',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListProvisionedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_provisioned_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_provisioned_products_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_resources_for_tag_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourcesForTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListResourcesForTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources_for_tag_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resources_for_tag_option_with_options(request, runtime)

    def list_tag_options_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = servicecatalog_20210901_models.ListTagOptionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagOptions',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTagOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_options_with_options(request, runtime)

    def list_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    def terminate_provisioned_product_with_options(self, request, runtime):
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        

        @param request: TerminateProvisionedProductRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TerminateProvisionedProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.TerminateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_provisioned_product(self, request):
        """
        After a product instance is terminated, the product instance is deleted from the product instance list. End users cannot manage the product instance throughout its lifecycle. Proceed with caution.
        

        @param request: TerminateProvisionedProductRequest

        @return: TerminateProvisionedProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.terminate_provisioned_product_with_options(request, runtime)

    def update_constraint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConstraint',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    def update_constraint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_constraint_with_options(request, runtime)

    def update_portfolio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePortfolio',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    def update_portfolio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_portfolio_with_options(request, runtime)

    def update_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    def update_product_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.guidance):
            body['Guidance'] = request.guidance
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_version_with_options(request, runtime)

    def update_provisioned_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProduct',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    def update_provisioned_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_provisioned_product_with_options(request, runtime)

    def update_provisioned_product_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.plan_id):
            body['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProvisionedProductPlan',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_provisioned_product_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_provisioned_product_plan_with_options(request, runtime)

    def update_tag_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTagOption',
            version='2021-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicecatalog_20210901_models.UpdateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_tag_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_tag_option_with_options(request, runtime)
