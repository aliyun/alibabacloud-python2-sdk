# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApproveProvisionedProductPlanRequest(TeaModel):
    def __init__(self, approval_action=None, comment=None, plan_id=None):
        # The review action. Valid values:
        # 
        # *   Approve
        # *   Reject
        self.approval_action = approval_action  # type: str
        # The review description.
        self.comment = comment  # type: str
        # The ID of the plan.
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class ApproveProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApproveProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApproveProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApproveProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociatePrincipalWithPortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None, principal_id=None, principal_type=None):
        self.portfolio_id = portfolio_id  # type: str
        self.principal_id = principal_id  # type: str
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociatePrincipalWithPortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class AssociatePrincipalWithPortfolioResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociatePrincipalWithPortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociatePrincipalWithPortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociatePrincipalWithPortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociatePrincipalWithPortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociatePrincipalWithPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateProductWithPortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None, product_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateProductWithPortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class AssociateProductWithPortfolioResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateProductWithPortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateProductWithPortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateProductWithPortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateProductWithPortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateProductWithPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateTagOptionWithResourceRequest(TeaModel):
    def __init__(self, resource_id=None, tag_option_id=None):
        # The ID of the resource with which the tag option is associated.
        self.resource_id = resource_id  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTagOptionWithResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        return self


class AssociateTagOptionWithResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTagOptionWithResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateTagOptionWithResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateTagOptionWithResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateTagOptionWithResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateTagOptionWithResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelProvisionedProductPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class CancelProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyProductRequest(TeaModel):
    def __init__(self, source_product_arn=None, target_product_name=None):
        # The Alibaba Cloud Resource Name (ARN) of the source product.
        # 
        # > The source product can belong to the current account or belong to a product portfolio that is shared by another account.
        self.source_product_arn = source_product_arn  # type: str
        # The name of the destination product.
        self.target_product_name = target_product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_product_arn is not None:
            result['SourceProductArn'] = self.source_product_arn
        if self.target_product_name is not None:
            result['TargetProductName'] = self.target_product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceProductArn') is not None:
            self.source_product_arn = m.get('SourceProductArn')
        if m.get('TargetProductName') is not None:
            self.target_product_name = m.get('TargetProductName')
        return self


class CopyProductResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopyProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CopyProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConstraintRequest(TeaModel):
    def __init__(self, config=None, constraint_type=None, description=None, portfolio_id=None, product_id=None):
        # The configuration of the constraint.
        # 
        # Format: { "LocalRoleName": "\<role_name>" }.
        self.config = config  # type: str
        # The type of the constraint.
        # 
        # The value is fixed as Launch, which specifies the launch constraint.
        self.constraint_type = constraint_type  # type: str
        # The description of the constraint.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The ID of the product portfolio to which the constraint belongs.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product for which the constraint is created.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConstraintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class CreateConstraintResponseBody(TeaModel):
    def __init__(self, constraint_id=None, request_id=None):
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConstraintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConstraintResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConstraintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConstraintResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePortfolioRequest(TeaModel):
    def __init__(self, description=None, portfolio_name=None, provider_name=None):
        # The description of the product portfolio.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The name of the product portfolio.
        # 
        # The value must be 1 to 128 characters in length.
        self.portfolio_name = portfolio_name  # type: str
        # The provider of the product portfolio.
        # 
        # The value must be 1 to 128 characters in length.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreatePortfolioResponseBody(TeaModel):
    def __init__(self, portfolio_id=None, request_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequestProductVersionParameters(TeaModel):
    def __init__(self, active=None, description=None, guidance=None, product_version_name=None, template_type=None,
                 template_url=None):
        # Specifies whether to enable the product version. Valid values:
        # 
        # *   true: enables the product version. This is the default value.
        # *   false: disables the product version.
        self.active = active  # type: bool
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommended version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance  # type: str
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_version_name = product_version_name  # type: str
        # The type of the template.
        # 
        # Set the value to RosTerraformTemplate, which specifies the Terraform template that is supported by ROS.
        self.template_type = template_type  # type: str
        # The URL of the template.
        # 
        # For more information about how to obtain the URL of a template, see [CreateTemplate](~~CreateTemplate~~).
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductRequestProductVersionParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateProductRequest(TeaModel):
    def __init__(self, description=None, product_name=None, product_type=None, product_version_parameters=None,
                 provider_name=None):
        # The description of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The name of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # Set the value to Ros, which specifies Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The information about the product version.
        self.product_version_parameters = product_version_parameters  # type: CreateProductRequestProductVersionParameters
        # The provider of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.provider_name = provider_name  # type: str

    def validate(self):
        if self.product_version_parameters:
            self.product_version_parameters.validate()

    def to_map(self):
        _map = super(CreateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_version_parameters is not None:
            result['ProductVersionParameters'] = self.product_version_parameters.to_map()
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductVersionParameters') is not None:
            temp_model = CreateProductRequestProductVersionParameters()
            self.product_version_parameters = temp_model.from_map(m['ProductVersionParameters'])
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreateProductShrinkRequest(TeaModel):
    def __init__(self, description=None, product_name=None, product_type=None,
                 product_version_parameters_shrink=None, provider_name=None):
        # The description of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The name of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # Set the value to Ros, which specifies Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The information about the product version.
        self.product_version_parameters_shrink = product_version_parameters_shrink  # type: str
        # The provider of the product.
        # 
        # The value must be 1 to 128 characters in length.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_version_parameters_shrink is not None:
            result['ProductVersionParameters'] = self.product_version_parameters_shrink
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductVersionParameters') is not None:
            self.product_version_parameters_shrink = m.get('ProductVersionParameters')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(self, product_id=None, product_version_id=None, request_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionRequest(TeaModel):
    def __init__(self, active=None, description=None, guidance=None, product_id=None, product_version_name=None,
                 template_type=None, template_url=None):
        # Specifies whether the product version is active. Valid values:
        # 
        # *   true: The product version is active. This is the default value.
        # *   false: The product version is inactive.
        self.active = active  # type: bool
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommendation version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance  # type: str
        # The ID of the product to which the product version belongs.
        self.product_id = product_id  # type: str
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_version_name = product_version_name  # type: str
        # The type of the template.
        # 
        # The value is fixed as RosTerraformTemplate, which specifies the Terraform template that is supported by Resource Orchestration Service (ROS).
        self.template_type = template_type  # type: str
        # The URL of the template.
        # 
        # For more information about how to obtain the URL of a template, see [CreateTemplate](~~CreateTemplate~~).
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateProductVersionResponseBody(TeaModel):
    def __init__(self, product_version_id=None, request_id=None):
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProvisionedProductPlanRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the parameter in the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProvisionedProductPlanRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class CreateProvisionedProductPlanRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom tag.
        # 
        # The key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the custom tag.
        # 
        # The value can be up to 128 characters in length, and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProvisionedProductPlanRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateProvisionedProductPlanRequest(TeaModel):
    def __init__(self, description=None, operation_type=None, parameters=None, plan_name=None, plan_type=None,
                 portfolio_id=None, product_id=None, product_version_id=None, provisioned_product_name=None,
                 stack_region_id=None, tags=None):
        # The description of the plan.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The type of the operation that you want the plan to perform. Valid values:
        # 
        # *   LaunchProduct: launches the product. This is the default value.
        # *   UpdateProvisionedProduct: updates the information about the product instance.
        # *   TerminateProvisionedProduct: terminates the product instance.
        self.operation_type = operation_type  # type: str
        # An array that consists of the parameters in the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > If you specify Parameters, you must specify ParameterKey and ParameterValue.
        self.parameters = parameters  # type: list[CreateProvisionedProductPlanRequestParameters]
        # The plan name.
        # 
        # The value must be 1 to 128 characters in length.
        self.plan_name = plan_name  # type: str
        # The plan type.
        # 
        # Set the value to Ros, which specifies Resource Orchestration Service (ROS).
        self.plan_type = plan_type  # type: str
        # The product portfolio ID.
        # 
        # > If PortfolioId is not required, you do not need to specify PortfolioId. If PortfolioId is required, you must specify PortfolioId. For more information about how to obtain the value of PortfolioId, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id  # type: str
        # The product ID.
        self.product_id = product_id  # type: str
        # The product version ID.
        self.product_version_id = product_version_id  # type: str
        # The product instance name.
        # 
        # The value must be 1 to 128 characters in length.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The ID of the region to which the ROS stack belongs.
        # 
        # For more information about how to obtain the regions that are supported by ROS, see [DescribeRegions](~~131035~~).
        self.stack_region_id = stack_region_id  # type: str
        # An array that consists of custom tags.
        # 
        # Maximum value of N: 20.
        # 
        # > 
        # *   If you specify Tags, you must specify Tags.N.Key and Tags.N.Value.
        # *   The tag of a stack is propagated to each resource that supports the tag feature in the stack.
        self.tags = tags  # type: list[CreateProvisionedProductPlanRequestTags]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateProvisionedProductPlanRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateProvisionedProductPlanRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, plan_id=None, provisioned_product_id=None, request_id=None):
        # The plan ID.
        self.plan_id = plan_id  # type: str
        # The product instance ID.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagOptionRequest(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag option.
        # 
        # The key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the tag option.
        # 
        # The value can be up to 128 characters in length. It cannot start with `acs:`and cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTagOptionResponseBodyTagOptionDetail(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active  # type: bool
        # The key of the tag option.
        # 
        # The key must be 1 to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        # 
        # The value must be 1 to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagOptionResponseBodyTagOptionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTagOptionResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_option_detail=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the details of the tag option.
        self.tag_option_detail = tag_option_detail  # type: CreateTagOptionResponseBodyTagOptionDetail

    def validate(self):
        if self.tag_option_detail:
            self.tag_option_detail.validate()

    def to_map(self):
        _map = super(CreateTagOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_option_detail is not None:
            result['TagOptionDetail'] = self.tag_option_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagOptionDetail') is not None:
            temp_model = CreateTagOptionResponseBodyTagOptionDetail()
            self.tag_option_detail = temp_model.from_map(m['TagOptionDetail'])
        return self


class CreateTagOptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTagOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequestTerraformVariables(TeaModel):
    def __init__(self, description=None, variable_name=None):
        # The description of the variable.
        # 
        # For more information about the format of variable descriptions, see [Methods and suggestions for Terraform code development](~~322216~~).
        self.description = description  # type: str
        # The name of the variable.
        self.variable_name = variable_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequestTerraformVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, template_body=None, template_type=None, terraform_variables=None):
        # The content of the template.
        # 
        # For more information about the template syntax, see [Structure of Terraform templates](~~184397~~).
        self.template_body = template_body  # type: str
        # The type of the template.
        # 
        # Set the value to RosTerraformTemplate, which specifies the Terraform template that is supported by Resource Orchestration Service (ROS).
        self.template_type = template_type  # type: str
        # The variable settings of the Terraform template. You can configure the variables in a structured manner. Service Catalog applies the variable settings to the template.
        # 
        # > The variables must be defined in the Terraform template.
        self.terraform_variables = terraform_variables  # type: list[CreateTemplateRequestTerraformVariables]

    def validate(self):
        if self.terraform_variables:
            for k in self.terraform_variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        result['TerraformVariables'] = []
        if self.terraform_variables is not None:
            for k in self.terraform_variables:
                result['TerraformVariables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        self.terraform_variables = []
        if m.get('TerraformVariables') is not None:
            for k in m.get('TerraformVariables'):
                temp_model = CreateTemplateRequestTerraformVariables()
                self.terraform_variables.append(temp_model.from_map(k))
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_url=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The URL of the template.
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConstraintRequest(TeaModel):
    def __init__(self, constraint_id=None):
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConstraintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        return self


class DeleteConstraintResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConstraintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConstraintResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConstraintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConstraintResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class DeletePortfolioResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductRequest(TeaModel):
    def __init__(self, product_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionRequest(TeaModel):
    def __init__(self, product_version_id=None):
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class DeleteProductVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProductVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProvisionedProductPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagOptionRequest(TeaModel):
    def __init__(self, tag_option_id=None):
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        return self


class DeleteTagOptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTagOptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTagOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisAssociateTagOptionFromResourceRequest(TeaModel):
    def __init__(self, resource_id=None, tag_option_id=None):
        # The ID of the resource with which the tag option is associated.
        self.resource_id = resource_id  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisAssociateTagOptionFromResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        return self


class DisAssociateTagOptionFromResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisAssociateTagOptionFromResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisAssociateTagOptionFromResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisAssociateTagOptionFromResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisAssociateTagOptionFromResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisAssociateTagOptionFromResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociatePrincipalFromPortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None, principal_id=None, principal_type=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the RAM entity.
        # 
        # For more information about how to obtain the ID of a RAM user, see [GetUser](~~28681~~).
        # 
        # For more information about how to obtain the ID of a RAM role, see [GetRole](~~28711~~).
        self.principal_id = principal_id  # type: str
        # The type of the Resource Access Management (RAM) entity. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociatePrincipalFromPortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class DisassociatePrincipalFromPortfolioResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociatePrincipalFromPortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociatePrincipalFromPortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociatePrincipalFromPortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociatePrincipalFromPortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociatePrincipalFromPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateProductFromPortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None, product_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateProductFromPortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DisassociateProductFromPortfolioResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateProductFromPortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateProductFromPortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociateProductFromPortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociateProductFromPortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateProductFromPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteProvisionedProductPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class ExecuteProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, plan_id=None, request_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConstraintRequest(TeaModel):
    def __init__(self, constraint_id=None):
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConstraintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        return self


class GetConstraintResponseBodyConstraintDetail(TeaModel):
    def __init__(self, config=None, constraint_id=None, constraint_type=None, create_time=None, description=None,
                 portfolio_id=None, product_id=None, product_name=None):
        # The configuration of the constraint.
        # 
        # Format: { "LocalRoleName": "\<role_name>" }.
        self.config = config  # type: str
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str
        # The type of the constraint.
        # 
        # The value is fixed as Launch, which indicates the launch constraint.
        self.constraint_type = constraint_type  # type: str
        # The time when the constraint was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the constraint.
        self.description = description  # type: str
        # The ID of the product portfolio to which the constraint belongs.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product for which the constraint is created.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConstraintResponseBodyConstraintDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class GetConstraintResponseBody(TeaModel):
    def __init__(self, constraint_detail=None, request_id=None):
        # The details of the constraint.
        self.constraint_detail = constraint_detail  # type: GetConstraintResponseBodyConstraintDetail
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.constraint_detail:
            self.constraint_detail.validate()

    def to_map(self):
        _map = super(GetConstraintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_detail is not None:
            result['ConstraintDetail'] = self.constraint_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintDetail') is not None:
            temp_model = GetConstraintResponseBodyConstraintDetail()
            self.constraint_detail = temp_model.from_map(m['ConstraintDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConstraintResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConstraintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConstraintResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPortfolioRequest(TeaModel):
    def __init__(self, portfolio_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class GetPortfolioResponseBodyPortfolioDetail(TeaModel):
    def __init__(self, create_time=None, description=None, portfolio_arn=None, portfolio_id=None,
                 portfolio_name=None, provider_name=None):
        # The time when the product portfolio was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product portfolio.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product portfolio.
        self.portfolio_arn = portfolio_arn  # type: str
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The name of the product portfolio.
        self.portfolio_name = portfolio_name  # type: str
        # The provider of the product portfolio.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPortfolioResponseBodyPortfolioDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_arn is not None:
            result['PortfolioArn'] = self.portfolio_arn
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioArn') is not None:
            self.portfolio_arn = m.get('PortfolioArn')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetPortfolioResponseBodyTagOptions(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # - true (default)
        # - false
        self.active = active  # type: bool
        # The key of the tag option.
        self.key = key  # type: str
        # The ID of the owner of the tag option.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPortfolioResponseBodyTagOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPortfolioResponseBody(TeaModel):
    def __init__(self, portfolio_detail=None, request_id=None, tag_options=None):
        # The details of the product portfolio.
        self.portfolio_detail = portfolio_detail  # type: GetPortfolioResponseBodyPortfolioDetail
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The tag options associated with the service portfolio.
        self.tag_options = tag_options  # type: list[GetPortfolioResponseBodyTagOptions]

    def validate(self):
        if self.portfolio_detail:
            self.portfolio_detail.validate()
        if self.tag_options:
            for k in self.tag_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_detail is not None:
            result['PortfolioDetail'] = self.portfolio_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagOptions'] = []
        if self.tag_options is not None:
            for k in self.tag_options:
                result['TagOptions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioDetail') is not None:
            temp_model = GetPortfolioResponseBodyPortfolioDetail()
            self.portfolio_detail = temp_model.from_map(m['PortfolioDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_options = []
        if m.get('TagOptions') is not None:
            for k in m.get('TagOptions'):
                temp_model = GetPortfolioResponseBodyTagOptions()
                self.tag_options.append(temp_model.from_map(k))
        return self


class GetPortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductAsAdminRequest(TeaModel):
    def __init__(self, product_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductAsAdminRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class GetProductAsAdminResponseBodyProductDetail(TeaModel):
    def __init__(self, create_time=None, description=None, product_arn=None, product_id=None, product_name=None,
                 product_type=None, provider_name=None):
        # The creation time.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The provider of the product.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductAsAdminResponseBodyProductDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetProductAsAdminResponseBodyTagOptions(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # - true (default)
        # - false
        self.active = active  # type: bool
        # The key of the tag option.
        self.key = key  # type: str
        # The ID of the owner of the tag option.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductAsAdminResponseBodyTagOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProductAsAdminResponseBody(TeaModel):
    def __init__(self, product_detail=None, request_id=None, tag_options=None):
        # The information about the product.
        self.product_detail = product_detail  # type: GetProductAsAdminResponseBodyProductDetail
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The tag options associated with the product.
        self.tag_options = tag_options  # type: list[GetProductAsAdminResponseBodyTagOptions]

    def validate(self):
        if self.product_detail:
            self.product_detail.validate()
        if self.tag_options:
            for k in self.tag_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductAsAdminResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagOptions'] = []
        if self.tag_options is not None:
            for k in self.tag_options:
                result['TagOptions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductDetail') is not None:
            temp_model = GetProductAsAdminResponseBodyProductDetail()
            self.product_detail = temp_model.from_map(m['ProductDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_options = []
        if m.get('TagOptions') is not None:
            for k in m.get('TagOptions'):
                temp_model = GetProductAsAdminResponseBodyTagOptions()
                self.tag_options.append(temp_model.from_map(k))
        return self


class GetProductAsAdminResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProductAsAdminResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductAsAdminResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductAsAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductAsEndUserRequest(TeaModel):
    def __init__(self, product_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductAsEndUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class GetProductAsEndUserResponseBodyProductSummary(TeaModel):
    def __init__(self, create_time=None, description=None, has_default_launch_option=None, product_arn=None,
                 product_id=None, product_name=None, product_type=None, provider_name=None):
        # The time when the product was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product.
        self.description = description  # type: str
        # Indicates whether the default launch option exists. Valid values:
        # 
        # *   true: The default launch option exists. In this case, the PortfolioId parameter is not required when the product is launched or when the information about the product instance is updated.
        # *   false: The default launch option does not exist. In this case, the PortfolioId parameter is required when the product is launched or when the information about the product instance is updated. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        # 
        # > If the product is added to only one product portfolio, the default launch option exists. If the product is added to multiple product portfolios, multiple launch options exist at the same time. However, no default launch options exist.
        self.has_default_launch_option = has_default_launch_option  # type: bool
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The provider of the product.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductAsEndUserResponseBodyProductSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.has_default_launch_option is not None:
            result['HasDefaultLaunchOption'] = self.has_default_launch_option
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasDefaultLaunchOption') is not None:
            self.has_default_launch_option = m.get('HasDefaultLaunchOption')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetProductAsEndUserResponseBody(TeaModel):
    def __init__(self, product_summary=None, request_id=None):
        # The information about the product.
        self.product_summary = product_summary  # type: GetProductAsEndUserResponseBodyProductSummary
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.product_summary:
            self.product_summary.validate()

    def to_map(self):
        _map = super(GetProductAsEndUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_summary is not None:
            result['ProductSummary'] = self.product_summary.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductSummary') is not None:
            temp_model = GetProductAsEndUserResponseBodyProductSummary()
            self.product_summary = temp_model.from_map(m['ProductSummary'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductAsEndUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProductAsEndUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductAsEndUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductAsEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionRequest(TeaModel):
    def __init__(self, product_version_id=None):
        self.product_version_id = product_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class GetProductVersionResponseBodyProductVersionDetail(TeaModel):
    def __init__(self, active=None, create_time=None, description=None, guidance=None, product_id=None,
                 product_version_id=None, product_version_name=None, template_type=None, template_url=None):
        self.active = active  # type: bool
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.guidance = guidance  # type: str
        self.product_id = product_id  # type: str
        self.product_version_id = product_version_id  # type: str
        self.product_version_name = product_version_name  # type: str
        self.template_type = template_type  # type: str
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionResponseBodyProductVersionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class GetProductVersionResponseBody(TeaModel):
    def __init__(self, product_version_detail=None, request_id=None):
        self.product_version_detail = product_version_detail  # type: GetProductVersionResponseBodyProductVersionDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.product_version_detail:
            self.product_version_detail.validate()

    def to_map(self):
        _map = super(GetProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_detail is not None:
            result['ProductVersionDetail'] = self.product_version_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductVersionDetail') is not None:
            temp_model = GetProductVersionResponseBodyProductVersionDetail()
            self.product_version_detail = temp_model.from_map(m['ProductVersionDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionedProductRequest(TeaModel):
    def __init__(self, provisioned_product_id=None):
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        return self


class GetProvisionedProductResponseBodyProvisionedProductDetail(TeaModel):
    def __init__(self, create_time=None, last_provisioning_task_id=None,
                 last_successful_provisioning_task_id=None, last_task_id=None, owner_principal_id=None, owner_principal_type=None, portfolio_id=None,
                 product_id=None, product_name=None, product_version_id=None, product_version_name=None,
                 provisioned_product_arn=None, provisioned_product_id=None, provisioned_product_name=None, provisioned_product_type=None,
                 stack_id=None, stack_region_id=None, status=None, status_message=None):
        # The time when the product instance was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The ID of the task that was last run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_provisioning_task_id = last_provisioning_task_id  # type: str
        # The ID of the last task that was successfully run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_successful_provisioning_task_id = last_successful_provisioning_task_id  # type: str
        # The ID of the task that was last run.
        self.last_task_id = last_task_id  # type: str
        # The ID of the RAM entity to which the product instance belongs.
        self.owner_principal_id = owner_principal_id  # type: str
        # The type of the Resource Access Management (RAM) entity to which the product instance belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type  # type: str
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product version.
        self.product_version_name = product_version_name  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product instance.
        self.provisioned_product_arn = provisioned_product_arn  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The type of the product instance.
        # 
        # The value is fixed as RosStack, which indicates an ROS stack.
        self.provisioned_product_type = provisioned_product_type  # type: str
        # The ID of the Resource Orchestration Service (ROS) stack.
        self.stack_id = stack_id  # type: str
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id  # type: str
        # The state of the product instance. Valid values:
        # 
        # *   Available: The product instance was available.
        # *   UnderChange: The information about the product instance was being changed.
        # *   Error: An exception occurred on the product instance.
        self.status = status  # type: str
        # The message that is returned for the status of the product instance.
        # 
        # > This parameter is returned only when Error is returned for the Status parameter.
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductResponseBodyProvisionedProductDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_provisioning_task_id is not None:
            result['LastProvisioningTaskId'] = self.last_provisioning_task_id
        if self.last_successful_provisioning_task_id is not None:
            result['LastSuccessfulProvisioningTaskId'] = self.last_successful_provisioning_task_id
        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_arn is not None:
            result['ProvisionedProductArn'] = self.provisioned_product_arn
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.provisioned_product_type is not None:
            result['ProvisionedProductType'] = self.provisioned_product_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastProvisioningTaskId') is not None:
            self.last_provisioning_task_id = m.get('LastProvisioningTaskId')
        if m.get('LastSuccessfulProvisioningTaskId') is not None:
            self.last_successful_provisioning_task_id = m.get('LastSuccessfulProvisioningTaskId')
        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductArn') is not None:
            self.provisioned_product_arn = m.get('ProvisionedProductArn')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('ProvisionedProductType') is not None:
            self.provisioned_product_type = m.get('ProvisionedProductType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class GetProvisionedProductResponseBody(TeaModel):
    def __init__(self, provisioned_product_detail=None, request_id=None):
        # The details of the product instance.
        self.provisioned_product_detail = provisioned_product_detail  # type: GetProvisionedProductResponseBodyProvisionedProductDetail
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.provisioned_product_detail:
            self.provisioned_product_detail.validate()

    def to_map(self):
        _map = super(GetProvisionedProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_detail is not None:
            result['ProvisionedProductDetail'] = self.provisioned_product_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvisionedProductDetail') is not None:
            temp_model = GetProvisionedProductResponseBodyProvisionedProductDetail()
            self.provisioned_product_detail = temp_model.from_map(m['ProvisionedProductDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProvisionedProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProvisionedProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProvisionedProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionedProductPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator(TeaModel):
    def __init__(self, principal_id=None, principal_name=None, principal_type=None):
        # The RAM entity ID of the operator.
        self.principal_id = principal_id  # type: str
        # The RAM entity name of the operator.
        self.principal_name = principal_name  # type: str
        # The RAM entity type of the operator. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords(TeaModel):
    def __init__(self, approval_action=None, comment=None, create_time=None, operator=None):
        # The operation that is performed by the operator on the plan. Valid values:
        # 
        # *   Submit: submits the plan.
        # *   Cancel: cancels the plan.
        # *   Approve: approves the plan.
        # *   reject: rejects the plan.
        self.approval_action = approval_action  # type: str
        # The review comment of the operator.
        self.comment = comment  # type: str
        # The time when the operation was performed.
        self.create_time = create_time  # type: str
        # The operator who performs operations on the plan.
        self.operator = operator  # type: GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.operator is not None:
            result['Operator'] = self.operator.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Operator') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator()
            self.operator = temp_model.from_map(m['Operator'])
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator(TeaModel):
    def __init__(self, principal_name=None, principal_type=None):
        # The RAM entity name of the operator.
        self.principal_name = principal_name  # type: str
        # The RAM entity type of the operator. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks(TeaModel):
    def __init__(self, operator=None):
        # The operator who performs operations on the plan.
        self.operator = operator  # type: GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operator') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator()
            self.operator = temp_model.from_map(m['Operator'])
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities(TeaModel):
    def __init__(self, activity_name=None, tasks=None):
        # The name of the operation that is being performed by the plan.
        self.activity_name = activity_name  # type: str
        # An array consisting of tasks that are pending for review.
        self.tasks = tasks  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail(TeaModel):
    def __init__(self, operation_records=None, todo_task_activities=None):
        # An array that consists of operations that are performed by the operator.
        self.operation_records = operation_records  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords]
        # An array that consists of operations that are being performed by the plan.
        self.todo_task_activities = todo_task_activities  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities]

    def validate(self):
        if self.operation_records:
            for k in self.operation_records:
                if k:
                    k.validate()
        if self.todo_task_activities:
            for k in self.todo_task_activities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperationRecords'] = []
        if self.operation_records is not None:
            for k in self.operation_records:
                result['OperationRecords'].append(k.to_map() if k else None)
        result['TodoTaskActivities'] = []
        if self.todo_task_activities is not None:
            for k in self.todo_task_activities:
                result['TodoTaskActivities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.operation_records = []
        if m.get('OperationRecords') is not None:
            for k in m.get('OperationRecords'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords()
                self.operation_records.append(temp_model.from_map(k))
        self.todo_task_activities = []
        if m.get('TodoTaskActivities') is not None:
            for k in m.get('TodoTaskActivities'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities()
                self.todo_task_activities.append(temp_model.from_map(k))
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers(TeaModel):
    def __init__(self, principal_name=None, principal_type=None):
        # The RAM entity name of the reviewer.
        self.principal_name = principal_name  # type: str
        # The type of the Resource Access Management (RAM) entity of the reviewer. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the parameter in the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetailTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom tag.
        self.key = key  # type: str
        # The value of the custom tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetailTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProvisionedProductPlanResponseBodyPlanDetail(TeaModel):
    def __init__(self, approval_detail=None, assigned_approvers=None, create_time=None, description=None,
                 operation_type=None, owner_principal_id=None, owner_principal_name=None, owner_principal_type=None,
                 parameters=None, plan_id=None, plan_name=None, plan_type=None, portfolio_id=None, product_id=None,
                 product_version_id=None, provisioned_product_id=None, provisioned_product_name=None, stack_id=None,
                 stack_region_id=None, status=None, status_message=None, tags=None, uid=None, update_time=None):
        # The review details of the plan.
        self.approval_detail = approval_detail  # type: GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail
        # An array that consists of reviewers.
        self.assigned_approvers = assigned_approvers  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers]
        # The time when the plan was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the plan.
        self.description = description  # type: str
        # The purpose of the plan. Valid values:
        # 
        # *   LaunchProduct: launches the product.
        # *   UpdateProvisionedProduct: updates the information about the product instance.
        # *   TerminateProvisionedProduct: terminates the product instance.
        self.operation_type = operation_type  # type: str
        # The ID of the RAM entity to which the plan belongs.
        self.owner_principal_id = owner_principal_id  # type: str
        # The name of the RAM entity to which the plan belongs.
        self.owner_principal_name = owner_principal_name  # type: str
        # The type of the RAM entity to which the plan belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type  # type: str
        # An array that consists of the parameters in the template.
        self.parameters = parameters  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailParameters]
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The name of the plan.
        self.plan_name = plan_name  # type: str
        # The type of the plan.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.plan_type = plan_type  # type: str
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The ID of the ROS stack.
        self.stack_id = stack_id  # type: str
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id  # type: str
        # The state of the plan. Valid values:
        # 
        # *   PreviewInProgress: The plan is being prechecked.
        # *   PreviewSuccess: The precheck is successful.
        # *   PreviewFailed: The precheck fails.
        # *   ExecuteInProgress: The plan is being run.
        # *   ExecuteSuccess: The plan is run.
        # *   ExecuteFailed: The plan fails to be run.
        self.status = status  # type: str
        # The message returned for the state.
        # 
        # > This parameter is returned only when PreviewFailed or ExecuteFailed is returned for Status.
        self.status_message = status_message  # type: str
        # An array that consists of custom tags.
        self.tags = tags  # type: list[GetProvisionedProductPlanResponseBodyPlanDetailTags]
        # The ID of the Alibaba Cloud account to which the plan belongs.
        self.uid = uid  # type: str
        # The last time when the task was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.approval_detail:
            self.approval_detail.validate()
        if self.assigned_approvers:
            for k in self.assigned_approvers:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyPlanDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail.to_map()
        result['AssignedApprovers'] = []
        if self.assigned_approvers is not None:
            for k in self.assigned_approvers:
                result['AssignedApprovers'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_name is not None:
            result['OwnerPrincipalName'] = self.owner_principal_name
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApprovalDetail') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail()
            self.approval_detail = temp_model.from_map(m['ApprovalDetail'])
        self.assigned_approvers = []
        if m.get('AssignedApprovers') is not None:
            for k in m.get('AssignedApprovers'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers()
                self.assigned_approvers.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalName') is not None:
            self.owner_principal_name = m.get('OwnerPrincipalName')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetProvisionedProductPlanResponseBodyPlanDetailTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetProvisionedProductPlanResponseBodyProductDetail(TeaModel):
    def __init__(self, create_time=None, description=None, product_arn=None, product_id=None, product_name=None,
                 product_type=None, provider_name=None):
        # The creation time.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates ROS.
        self.product_type = product_type  # type: str
        # The provider of the product.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyProductDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetProvisionedProductPlanResponseBodyProductVersionDetail(TeaModel):
    def __init__(self, active=None, create_time=None, description=None, guidance=None, product_id=None,
                 product_version_id=None, product_version_name=None, template_type=None, template_url=None):
        # Indicates whether the product version is visible to end users. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active  # type: bool
        # The time when the product version was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product version.
        self.description = description  # type: str
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommendation version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be deprecated.
        self.guidance = guidance  # type: str
        # The ID of the product to which the product version belongs.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name for the version of the product.
        self.product_version_name = product_version_name  # type: str
        # The type of the template.
        # 
        # The value is fixed as RosTerraformTemplate, which indicates that the Terraform template is supported by ROS.
        self.template_type = template_type  # type: str
        # The URL of the template.
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyProductVersionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class GetProvisionedProductPlanResponseBodyResourceChanges(TeaModel):
    def __init__(self, action=None, logical_resource_id=None, physical_resource_id=None, replacement=None,
                 resource_type=None):
        # The action that is performed on the resource. Valid values:
        # 
        # *   Add
        # *   Modify
        # *   Remove
        # *   None
        self.action = action  # type: str
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id  # type: str
        # The physical ID of the resource.
        # 
        # > This parameter is returned only when Action is set to Modify or Remove.
        self.physical_resource_id = physical_resource_id  # type: str
        # Indicates whether a replacement update is performed on the template. Valid values:
        # 
        # *   True: A replacement update is performed on the template.
        # *   False: A change is made on the template.
        # *   Conditional: A replacement update may be performed on the template. You can check whether a replacement update is performed when the template is in use.
        # 
        # > This parameter is returned only when Action is set to Modify.
        self.replacement = replacement  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBodyResourceChanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.replacement is not None:
            result['Replacement'] = self.replacement
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, plan_detail=None, product_detail=None, product_version_detail=None, request_id=None,
                 resource_changes=None):
        # The details of the plan.
        self.plan_detail = plan_detail  # type: GetProvisionedProductPlanResponseBodyPlanDetail
        # The details of the product.
        self.product_detail = product_detail  # type: GetProvisionedProductPlanResponseBodyProductDetail
        # The details of the product version.
        self.product_version_detail = product_version_detail  # type: GetProvisionedProductPlanResponseBodyProductVersionDetail
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the resources to be changed in the plan.
        self.resource_changes = resource_changes  # type: list[GetProvisionedProductPlanResponseBodyResourceChanges]

    def validate(self):
        if self.plan_detail:
            self.plan_detail.validate()
        if self.product_detail:
            self.product_detail.validate()
        if self.product_version_detail:
            self.product_version_detail.validate()
        if self.resource_changes:
            for k in self.resource_changes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_detail is not None:
            result['PlanDetail'] = self.plan_detail.to_map()
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail.to_map()
        if self.product_version_detail is not None:
            result['ProductVersionDetail'] = self.product_version_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceChanges'] = []
        if self.resource_changes is not None:
            for k in self.resource_changes:
                result['ResourceChanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanDetail') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyPlanDetail()
            self.plan_detail = temp_model.from_map(m['PlanDetail'])
        if m.get('ProductDetail') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyProductDetail()
            self.product_detail = temp_model.from_map(m['ProductDetail'])
        if m.get('ProductVersionDetail') is not None:
            temp_model = GetProvisionedProductPlanResponseBodyProductVersionDetail()
            self.product_version_detail = temp_model.from_map(m['ProductVersionDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_changes = []
        if m.get('ResourceChanges') is not None:
            for k in m.get('ResourceChanges'):
                temp_model = GetProvisionedProductPlanResponseBodyResourceChanges()
                self.resource_changes.append(temp_model.from_map(k))
        return self


class GetProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagOptionRequest(TeaModel):
    def __init__(self, tag_option_id=None):
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        return self


class GetTagOptionResponseBodyTagOptionDetail(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.active = active  # type: bool
        # The key of the tag option.
        self.key = key  # type: str
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagOptionResponseBodyTagOptionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTagOptionResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_option_detail=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the tag option.
        self.tag_option_detail = tag_option_detail  # type: GetTagOptionResponseBodyTagOptionDetail

    def validate(self):
        if self.tag_option_detail:
            self.tag_option_detail.validate()

    def to_map(self):
        _map = super(GetTagOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_option_detail is not None:
            result['TagOptionDetail'] = self.tag_option_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagOptionDetail') is not None:
            temp_model = GetTagOptionResponseBodyTagOptionDetail()
            self.tag_option_detail = temp_model.from_map(m['TagOptionDetail'])
        return self


class GetTagOptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTagOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTagOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTagOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResponseBodyTaskDetailLogTerraformLogs(TeaModel):
    def __init__(self, command=None, content=None, stream=None):
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Basic CLI Features](https://www.terraform.io/cli/commands).
        self.command = command  # type: str
        # The content of the output stream that is returned after the command is run.
        self.content = content  # type: str
        # The output stream. Valid values:
        # 
        # *   stdout: a standard output stream
        # *   stderr: a standard error stream
        self.stream = stream  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetailLogTerraformLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class GetTaskResponseBodyTaskDetailLog(TeaModel):
    def __init__(self, terraform_logs=None):
        # The Terraform logs.
        self.terraform_logs = terraform_logs  # type: list[GetTaskResponseBodyTaskDetailLogTerraformLogs]

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetailLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = GetTaskResponseBodyTaskDetailLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class GetTaskResponseBodyTaskDetailOutputs(TeaModel):
    def __init__(self, description=None, output_key=None, output_value=None):
        # The description of the output parameter for the template.
        self.description = description  # type: str
        # The name of the output parameter for the template.
        self.output_key = output_key  # type: str
        # The value of the output parameter for the template.
        self.output_value = output_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetailOutputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.output_value is not None:
            result['OutputValue'] = self.output_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        if m.get('OutputValue') is not None:
            self.output_value = m.get('OutputValue')
        return self


class GetTaskResponseBodyTaskDetailParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the input parameter for the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetailParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetTaskResponseBodyTaskDetailTaskTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The custom tag key.
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The custom tag value.
        # 
        # The value must be 1 to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetailTaskTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTaskResponseBodyTaskDetail(TeaModel):
    def __init__(self, create_time=None, log=None, outputs=None, parameters=None, portfolio_id=None, product_id=None,
                 product_name=None, product_version_id=None, product_version_name=None, provisioned_product_id=None,
                 provisioned_product_name=None, status=None, status_message=None, task_id=None, task_tags=None, task_type=None,
                 update_time=None):
        # The time when the task was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The logs of the instance.
        self.log = log  # type: GetTaskResponseBodyTaskDetailLog
        # The output parameters of the template.
        self.outputs = outputs  # type: list[GetTaskResponseBodyTaskDetailOutputs]
        # The parameters that are specified in the template.
        self.parameters = parameters  # type: list[GetTaskResponseBodyTaskDetailParameters]
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product version.
        self.product_version_name = product_version_name  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The state of the task. Valid values:
        # 
        # *   Succeeded: The task was successful.
        # *   InProgress: The task was in progress.
        # *   Failed: The task failed.
        self.status = status  # type: str
        # The message that is returned for the status of the task.
        # 
        # > This parameter is returned only when Failed is returned for the Status parameter.
        self.status_message = status_message  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str
        # The custom tags.
        self.task_tags = task_tags  # type: list[GetTaskResponseBodyTaskDetailTaskTags]
        # The type of the task. Valid values:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.task_type = task_type  # type: str
        # The time when the task was last modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.log:
            self.log.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.task_tags:
            for k in self.task_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['TaskTags'] = []
        if self.task_tags is not None:
            for k in self.task_tags:
                result['TaskTags'].append(k.to_map() if k else None)
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Log') is not None:
            temp_model = GetTaskResponseBodyTaskDetailLog()
            self.log = temp_model.from_map(m['Log'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GetTaskResponseBodyTaskDetailOutputs()
                self.outputs.append(temp_model.from_map(k))
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTaskResponseBodyTaskDetailParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.task_tags = []
        if m.get('TaskTags') is not None:
            for k in m.get('TaskTags'):
                temp_model = GetTaskResponseBodyTaskDetailTaskTags()
                self.task_tags.append(temp_model.from_map(k))
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_detail=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the task.
        self.task_detail = task_detail  # type: GetTaskResponseBodyTaskDetail

    def validate(self):
        if self.task_detail:
            self.task_detail.validate()

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskDetail') is not None:
            temp_model = GetTaskResponseBodyTaskDetail()
            self.task_detail = temp_model.from_map(m['TaskDetail'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, product_id=None, product_version_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_body=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The content of the template.
        # 
        # For more information about the template syntax, see [Structure of Terraform templates](~~184397~~).
        self.template_body = template_body  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LaunchProductRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the input parameter for the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LaunchProductRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class LaunchProductRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the custom tag.
        # 
        # The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The tag value of the custom tag.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LaunchProductRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LaunchProductRequest(TeaModel):
    def __init__(self, parameters=None, portfolio_id=None, product_id=None, product_version_id=None,
                 provisioned_product_name=None, stack_region_id=None, tags=None):
        # The input parameters of the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > This parameter is optional. If you specify the Parameters parameter, you must specify the ParameterKey and ParameterValue parameters.
        self.parameters = parameters  # type: list[LaunchProductRequestParameters]
        # The ID of the product portfolio.
        # 
        # > If the PortfolioId parameter is not required, you do not need to specify the PortfolioId parameter. If the PortfolioId parameter is required, you must specify the PortfolioId parameter. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product instance.
        # 
        # The value must be 1 to 128 characters in length.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The ID of the region to which the Resource Orchestration Service (ROS) stack belongs.
        # 
        # For more information about how to obtain the regions that are supported by ROS, see [DescribeRegions](~~131035~~).
        self.stack_region_id = stack_region_id  # type: str
        # The custom tags that are specified by the end user.
        # 
        # Maximum value of N: 20.
        # 
        # > 
        # 
        # *   The Tags parameter is optional. If you specify the Tags parameter, you must specify the Tags.N.Key and Tags.N.Value parameters.
        # 
        # *   The tag is propagated to each stack resource that supports the tag feature.
        self.tags = tags  # type: list[LaunchProductRequestTags]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LaunchProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = LaunchProductRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = LaunchProductRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class LaunchProductResponseBody(TeaModel):
    def __init__(self, provisioned_product_id=None, request_id=None):
        # The ID of the instance
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LaunchProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LaunchProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LaunchProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LaunchProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LaunchProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLaunchOptionsRequest(TeaModel):
    def __init__(self, product_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLaunchOptionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries(TeaModel):
    def __init__(self, constraint_type=None, description=None, operation_types=None, stack_regions=None):
        # The type of the constraint. Valid values:
        # 
        # 1.  Launch
        # 2.  Template
        # 3.  Approval
        # 4.  StackRegion
        self.constraint_type = constraint_type  # type: str
        # The description of the constraint.
        self.description = description  # type: str
        # The types of operations that require approval. If the type of the constraint is Approval, this parameter is not empty.
        self.operation_types = operation_types  # type: list[str]
        # The regions in which users can launch the service. If the type of the constraint is StackRegion, this parameter is not empty.
        self.stack_regions = stack_regions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.description is not None:
            result['Description'] = self.description
        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types
        if self.stack_regions is not None:
            result['StackRegions'] = self.stack_regions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')
        if m.get('StackRegions') is not None:
            self.stack_regions = m.get('StackRegions')
        return self


class ListLaunchOptionsResponseBodyLaunchOptionSummaries(TeaModel):
    def __init__(self, constraint_summaries=None, portfolio_id=None, portfolio_name=None):
        # The constraints.
        self.constraint_summaries = constraint_summaries  # type: list[ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries]
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The name of the product portfolio.
        self.portfolio_name = portfolio_name  # type: str

    def validate(self):
        if self.constraint_summaries:
            for k in self.constraint_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLaunchOptionsResponseBodyLaunchOptionSummaries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstraintSummaries'] = []
        if self.constraint_summaries is not None:
            for k in self.constraint_summaries:
                result['ConstraintSummaries'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.constraint_summaries = []
        if m.get('ConstraintSummaries') is not None:
            for k in m.get('ConstraintSummaries'):
                temp_model = ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries()
                self.constraint_summaries.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        return self


class ListLaunchOptionsResponseBody(TeaModel):
    def __init__(self, launch_option_summaries=None, request_id=None):
        # The launch options.
        self.launch_option_summaries = launch_option_summaries  # type: list[ListLaunchOptionsResponseBodyLaunchOptionSummaries]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.launch_option_summaries:
            for k in self.launch_option_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLaunchOptionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LaunchOptionSummaries'] = []
        if self.launch_option_summaries is not None:
            for k in self.launch_option_summaries:
                result['LaunchOptionSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.launch_option_summaries = []
        if m.get('LaunchOptionSummaries') is not None:
            for k in m.get('LaunchOptionSummaries'):
                temp_model = ListLaunchOptionsResponseBodyLaunchOptionSummaries()
                self.launch_option_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLaunchOptionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLaunchOptionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLaunchOptionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLaunchOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortfoliosRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortfoliosRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPortfoliosRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, product_id=None, scope=None, sort_by=None,
                 sort_order=None):
        self.filters = filters  # type: list[ListPortfoliosRequestFilters]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_id = product_id  # type: str
        self.scope = scope  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPortfoliosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListPortfoliosRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListPortfoliosResponseBodyPortfolioDetails(TeaModel):
    def __init__(self, create_time=None, description=None, portfolio_arn=None, portfolio_id=None,
                 portfolio_name=None, provider_name=None):
        # 代表创建时间的资源属性字段
        self.create_time = create_time  # type: str
        # 产品组合描述
        self.description = description  # type: str
        self.portfolio_arn = portfolio_arn  # type: str
        # 代表资源一级ID的资源属性字段
        self.portfolio_id = portfolio_id  # type: str
        # 代表资源名称的资源属性字段
        self.portfolio_name = portfolio_name  # type: str
        # 产品组合提供方
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPortfoliosResponseBodyPortfolioDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_arn is not None:
            result['PortfolioArn'] = self.portfolio_arn
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioArn') is not None:
            self.portfolio_arn = m.get('PortfolioArn')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListPortfoliosResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, portfolio_details=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.portfolio_details = portfolio_details  # type: list[ListPortfoliosResponseBodyPortfolioDetails]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.portfolio_details:
            for k in self.portfolio_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPortfoliosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortfolioDetails'] = []
        if self.portfolio_details is not None:
            for k in self.portfolio_details:
                result['PortfolioDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.portfolio_details = []
        if m.get('PortfolioDetails') is not None:
            for k in m.get('PortfolioDetails'):
                temp_model = ListPortfoliosResponseBodyPortfolioDetails()
                self.portfolio_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPortfoliosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPortfoliosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPortfoliosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPortfoliosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrincipalsRequest(TeaModel):
    def __init__(self, portfolio_id=None):
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrincipalsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class ListPrincipalsResponseBodyPrincipals(TeaModel):
    def __init__(self, principal_id=None, principal_type=None):
        # The ID of the RAM entity.
        self.principal_id = principal_id  # type: str
        # The type of the RAM entity. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrincipalsResponseBodyPrincipals, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class ListPrincipalsResponseBody(TeaModel):
    def __init__(self, principals=None, request_id=None):
        # The RAM entities.
        self.principals = principals  # type: list[ListPrincipalsResponseBodyPrincipals]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrincipalsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = ListPrincipalsResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrincipalsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrincipalsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrincipalsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrincipalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(self, product_id=None):
        # The ID of the product.
        self.product_id = product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListProductVersionsResponseBodyProductVersionDetails(TeaModel):
    def __init__(self, active=None, create_time=None, description=None, guidance=None, product_id=None,
                 product_version_id=None, product_version_name=None, template_type=None, template_url=None):
        # Indicates whether the product version is enabled. Valid values:
        # 
        # true: The product version is enabled. This is the default value. false: The product version is disabled.
        self.active = active  # type: bool
        # The time when the product version was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product version.
        self.description = description  # type: str
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommended version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance  # type: str
        # The ID of the product to which the product version belongs.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product version.
        self.product_version_name = product_version_name  # type: str
        # The type of the template.
        # 
        # The value is fixed as RosTerraformTemplate, which indicates the Terraform template that is supported by Resource Orchestration Service (ROS).
        self.template_type = template_type  # type: str
        # The URL of the template.
        self.template_url = template_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyProductVersionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(self, product_version_details=None, request_id=None):
        # The versions of the product.
        self.product_version_details = product_version_details  # type: list[ListProductVersionsResponseBodyProductVersionDetails]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.product_version_details:
            for k in self.product_version_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductVersionDetails'] = []
        if self.product_version_details is not None:
            for k in self.product_version_details:
                result['ProductVersionDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_version_details = []
        if m.get('ProductVersionDetails') is not None:
            for k in m.get('ProductVersionDetails'):
                temp_model = ListProductVersionsResponseBodyProductVersionDetails()
                self.product_version_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsAsAdminRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The name of the filter condition. Valid values:
        # 
        # *   ProductName: performs exact matches by product name. Product names are not case-sensitive.
        # *   FullTextSearch: performs full-text searches by product name, product provider, or product description. Fuzzy match is supported.
        self.key = key  # type: str
        # The value of the filter condition.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsAsAdminRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductsAsAdminRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, portfolio_id=None, scope=None, sort_by=None,
                 sort_order=None):
        # The filter conditions.
        self.filters = filters  # type: list[ListProductsAsAdminRequestFilters]
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The query scope. Valid values:
        # 
        # *   Local: the products that are created by using the current account. This is the default value.
        # *   Import: the products that are imported from other accounts.
        # *   All: all available products.
        self.scope = scope  # type: str
        # The field that is used to sort the queried data.
        # 
        # Set the value to CreateTime, which specifies the time when the product was created.
        self.sort_by = sort_by  # type: str
        # The order in which you want to sort the queried data. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc: the descending order
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsAsAdminRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProductsAsAdminRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductsAsAdminResponseBodyProductDetails(TeaModel):
    def __init__(self, create_time=None, description=None, product_arn=None, product_id=None, product_name=None,
                 product_type=None, provider_name=None):
        # The time when the product was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The provider of the product.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsAsAdminResponseBodyProductDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListProductsAsAdminResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, product_details=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The products.
        self.product_details = product_details  # type: list[ListProductsAsAdminResponseBodyProductDetails]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.product_details:
            for k in self.product_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsAsAdminResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProductDetails'] = []
        if self.product_details is not None:
            for k in self.product_details:
                result['ProductDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.product_details = []
        if m.get('ProductDetails') is not None:
            for k in m.get('ProductDetails'):
                temp_model = ListProductsAsAdminResponseBodyProductDetails()
                self.product_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsAsAdminResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductsAsAdminResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsAsAdminResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsAsAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsAsEndUserRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The name of the filter condition. Valid values:
        # 
        # *   ProductName: performs exact matches by product name. Product names are not case-sensitive.
        # *   FullTextSearch: performs full-text searches by product name, product provider, or product description. Fuzzy match is supported.
        self.key = key  # type: str
        # The value of the filter condition.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsAsEndUserRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductsAsEndUserRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, sort_by=None, sort_order=None):
        # The filter conditions.
        self.filters = filters  # type: list[ListProductsAsEndUserRequestFilters]
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The field that is used to sort the queried data.
        # 
        # Set the value to CreateTime, which specifies the time when the product was created.
        self.sort_by = sort_by  # type: str
        # The order in which you want to sort the queried data. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc: the descending order
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsAsEndUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProductsAsEndUserRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductsAsEndUserResponseBodyProductSummaries(TeaModel):
    def __init__(self, create_time=None, description=None, has_default_launch_option=None, product_arn=None,
                 product_id=None, product_name=None, product_type=None, provider_name=None):
        # The time when the product was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the product.
        self.description = description  # type: str
        # Indicates whether the default launch option exists. Valid values:
        # 
        # *   true: The default launch option exists. In this case, the PortfolioId parameter is not required when the product is launched or when the information about the product instance is updated.
        # *   false: The default launch option does not exist. In this case, the PortfolioId parameter is required when the product is launched or when the information about the product instance is updated. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        # 
        # > If the product is added to only one product portfolio, the default launch option exists. If the product is added to multiple product portfolios, multiple launch options exist at the same time. However, no default launch options exist.
        self.has_default_launch_option = has_default_launch_option  # type: bool
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.product_type = product_type  # type: str
        # The provider of the product.
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsAsEndUserResponseBodyProductSummaries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.has_default_launch_option is not None:
            result['HasDefaultLaunchOption'] = self.has_default_launch_option
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasDefaultLaunchOption') is not None:
            self.has_default_launch_option = m.get('HasDefaultLaunchOption')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListProductsAsEndUserResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, product_summaries=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The products.
        self.product_summaries = product_summaries  # type: list[ListProductsAsEndUserResponseBodyProductSummaries]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.product_summaries:
            for k in self.product_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsAsEndUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProductSummaries'] = []
        if self.product_summaries is not None:
            for k in self.product_summaries:
                result['ProductSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.product_summaries = []
        if m.get('ProductSummaries') is not None:
            for k in m.get('ProductSummaries'):
                temp_model = ListProductsAsEndUserResponseBodyProductSummaries()
                self.product_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsAsEndUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductsAsEndUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsAsEndUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsAsEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionedProductPlanApproversRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductPlanApproverName: performs fuzzy match by reviewer name.
        self.key = key  # type: str
        # The value of the filter condition.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlanApproversRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProvisionedProductPlanApproversRequest(TeaModel):
    def __init__(self, access_level_filter=None, approval_filter=None, filters=None):
        # The access filter. Valid values:
        # 
        # *   User (default): queries the plans that are created by the current requester.
        # *   Account: queries the plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectory: queries the plans that belong to the current resource directory.
        # 
        # >  You must specify one of the `ApprovalFilter` and `AccessLevelFilter` parameters, but not both.
        self.access_level_filter = access_level_filter  # type: str
        # The access filter of the review dimension. Valid values:
        # 
        # *   AccountRequests: queries all reviewed plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectoryRequests: queries all plans that belong to the current resource directory.
        # 
        # >  You must specify one of the `ApprovalFilter` and `AccessLevelFilter` parameters, but not both.
        self.approval_filter = approval_filter  # type: str
        # An array that consists of filter conditions.
        self.filters = filters  # type: list[ListProvisionedProductPlanApproversRequestFilters]

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlanApproversRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter
        if self.approval_filter is not None:
            result['ApprovalFilter'] = self.approval_filter
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')
        if m.get('ApprovalFilter') is not None:
            self.approval_filter = m.get('ApprovalFilter')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProvisionedProductPlanApproversRequestFilters()
                self.filters.append(temp_model.from_map(k))
        return self


class ListProvisionedProductPlanApproversResponseBodyApprovers(TeaModel):
    def __init__(self, principal_name=None, principal_type=None):
        # The name of the reviewer.
        self.principal_name = principal_name  # type: str
        # The type of the Resource Access Management (RAM) entity of the reviewer. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlanApproversResponseBodyApprovers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class ListProvisionedProductPlanApproversResponseBody(TeaModel):
    def __init__(self, approvers=None, request_id=None):
        # An array that consists of reviewers.
        self.approvers = approvers  # type: list[ListProvisionedProductPlanApproversResponseBodyApprovers]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.approvers:
            for k in self.approvers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlanApproversResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Approvers'] = []
        if self.approvers is not None:
            for k in self.approvers:
                result['Approvers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.approvers = []
        if m.get('Approvers') is not None:
            for k in m.get('Approvers'):
                temp_model = ListProvisionedProductPlanApproversResponseBodyApprovers()
                self.approvers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProvisionedProductPlanApproversResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProvisionedProductPlanApproversResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlanApproversResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProvisionedProductPlanApproversResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionedProductPlansRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductPlanName: performs exact matches by plan name. Plan names are not case-sensitive.
        # *   ProvisionedProductPlanApprover: performs exact matches by reviewer. You must specify a reviewer in the `RamUser/RamRole:<Name of the reviewer>` format. You can specify multiple reviewers.
        # *   ProvisionedProductPlanApproverName: performs matches by reviewer name. You must specify the Resource Access Management (RAM) entity name of the reviewer. You can specify multiple reviewer names.
        # *   ProvisionedProductPlanStatus: performs matches by plan status. You must specify the state of the plan. You can specify multiple states.
        # *   ProvisionedProductPlanOwnerUid: performs exact matches by ID of Alibaba Cloud account to which a plan belongs.
        # *   FullTextSearch: performs fuzzy full-text searches by plan name.
        self.key = key  # type: str
        # The value of the filter condition.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlansRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProvisionedProductPlansRequest(TeaModel):
    def __init__(self, access_level_filter=None, approval_filter=None, filters=None, page_number=None,
                 page_size=None, provisioned_product_id=None, sort_by=None, sort_order=None):
        # The access filter. Valid values:
        # 
        # *   User (default): queries the plans that are created by the current requester.
        # *   Account: queries the plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectory: queries the plans that belong to the current resource directory.
        self.access_level_filter = access_level_filter  # type: str
        # The access filter of the review dimension. Valid values:
        # 
        # *   ReceivedRequests: queries plans that are pending for review.
        # *   ApprovalHistory: queries review history.
        # *   AccountRequests: queries all plans that belong to the current Alibaba Cloud account.
        # *   AccountRequests: queries all plans that belong to the current Alibaba Cloud account.
        self.approval_filter = approval_filter  # type: str
        # An array that consists of filter conditions.
        self.filters = filters  # type: list[ListProvisionedProductPlansRequestFilters]
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of plans.
        self.sort_by = sort_by  # type: str
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order.
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter
        if self.approval_filter is not None:
            result['ApprovalFilter'] = self.approval_filter
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')
        if m.get('ApprovalFilter') is not None:
            self.approval_filter = m.get('ApprovalFilter')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProvisionedProductPlansRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers(TeaModel):
    def __init__(self, principal_name=None, principal_type=None):
        # The RAM entity name of the reviewer.
        self.principal_name = principal_name  # type: str
        # The type of the RAM entity of the reviewer. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class ListProvisionedProductPlansResponseBodyPlanDetailsParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the parameter in the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponseBodyPlanDetailsParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class ListProvisionedProductPlansResponseBodyPlanDetailsTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom tag.
        self.key = key  # type: str
        # The value of the custom tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponseBodyPlanDetailsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProvisionedProductPlansResponseBodyPlanDetails(TeaModel):
    def __init__(self, assigned_approvers=None, create_time=None, description=None, operation_type=None,
                 owner_principal_id=None, owner_principal_name=None, owner_principal_type=None, parameters=None, plan_id=None,
                 plan_name=None, plan_type=None, portfolio_id=None, product_id=None, product_name=None,
                 product_version_id=None, provisioned_product_id=None, provisioned_product_name=None, stack_id=None,
                 stack_region_id=None, status=None, status_message=None, tags=None, uid=None, update_time=None):
        # An array that consists of reviewers.
        self.assigned_approvers = assigned_approvers  # type: list[ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers]
        # The time when the plan was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the plan.
        self.description = description  # type: str
        # The purpose of the plan. Valid values:
        # 
        # *   LaunchProduct: launches the product. This is the default value.
        # *   UpdateProvisionedProduct: updates the information about the product instance.
        # *   TerminateProvisionedProduct: terminates the product instance.
        self.operation_type = operation_type  # type: str
        # The ID of the RAM entity to which the plan belongs.
        self.owner_principal_id = owner_principal_id  # type: str
        # The name of the RAM entity to which the plan belongs.
        self.owner_principal_name = owner_principal_name  # type: str
        # The type of the RAM entity to which the plan belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type  # type: str
        # An array that consists of the parameters in the template.
        self.parameters = parameters  # type: list[ListProvisionedProductPlansResponseBodyPlanDetailsParameters]
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The name of the plan.
        self.plan_name = plan_name  # type: str
        # The type of the plan.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.plan_type = plan_type  # type: str
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The ID of the ROS stack.
        self.stack_id = stack_id  # type: str
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id  # type: str
        # The state of the plan. Valid values:
        # 
        # *   PreviewInProgress: The plan is being prechecked.
        # *   PreviewSuccess: The precheck is successful.
        # *   PreviewFailed: The precheck fails.
        # *   ApplicationInProgress: The plan is being reviewed.
        # *   ApplicationApproved: The plan is approved.
        # *   ApplicationRejected: The approval is rejected.
        # *   ExecuteInProgress: The plan is being run.
        # *   ExecuteSuccess: The plan is run.
        # *   ExecuteFailed: The plan fails to be run.
        # *   Canceled: The plan is canceled.
        self.status = status  # type: str
        # The message returned for the state.
        # 
        # > This parameter is returned only when PreviewFailed or ExecuteFailed is returned for the Status parameter.
        self.status_message = status_message  # type: str
        # An array that consists of custom tags.
        self.tags = tags  # type: list[ListProvisionedProductPlansResponseBodyPlanDetailsTags]
        # The ID of the Alibaba Cloud account to which the plan belongs.
        self.uid = uid  # type: str
        # The last time when the task was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.assigned_approvers:
            for k in self.assigned_approvers:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponseBodyPlanDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssignedApprovers'] = []
        if self.assigned_approvers is not None:
            for k in self.assigned_approvers:
                result['AssignedApprovers'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_name is not None:
            result['OwnerPrincipalName'] = self.owner_principal_name
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.assigned_approvers = []
        if m.get('AssignedApprovers') is not None:
            for k in m.get('AssignedApprovers'):
                temp_model = ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers()
                self.assigned_approvers.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalName') is not None:
            self.owner_principal_name = m.get('OwnerPrincipalName')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListProvisionedProductPlansResponseBodyPlanDetailsParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListProvisionedProductPlansResponseBodyPlanDetailsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListProvisionedProductPlansResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, plan_details=None, request_id=None, total_count=None):
        # The page number of the returned page.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # An array that consists of plans.
        self.plan_details = plan_details  # type: list[ListProvisionedProductPlansResponseBodyPlanDetails]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.plan_details:
            for k in self.plan_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PlanDetails'] = []
        if self.plan_details is not None:
            for k in self.plan_details:
                result['PlanDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.plan_details = []
        if m.get('PlanDetails') is not None:
            for k in m.get('PlanDetails'):
                temp_model = ListProvisionedProductPlansResponseBodyPlanDetails()
                self.plan_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProvisionedProductPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProvisionedProductPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProvisionedProductPlansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProvisionedProductPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionedProductsRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductName: performs exact matches by product instance name. Product instance names are not case-sensitive.
        # *   FullTextSearch: performs full-text searches by product instance name. Fuzzy match is supported.
        self.key = key  # type: str
        # The value of the filter condition.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductsRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProvisionedProductsRequest(TeaModel):
    def __init__(self, access_level_filter=None, filters=None, page_number=None, page_size=None, sort_by=None,
                 sort_order=None):
        # The access filter. Valid values:
        # 
        # *   User: queries the product instances that are created by the current requester. This is the default value.
        # *   Account: queries the product instances that belong to the current Alibaba Cloud account.
        self.access_level_filter = access_level_filter  # type: str
        # The filter conditions.
        self.filters = filters  # type: list[ListProvisionedProductsRequestFilters]
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The field that is used to sort the queried data.
        # 
        # Set the value to CreateTime, which specifies the time when the product instance was created.
        self.sort_by = sort_by  # type: str
        # The sorting method. Valid values:
        # 
        # *   Asc: the ascending order.
        # *   Desc (default): the descending order.
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProvisionedProductsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProvisionedProductsResponseBodyProvisionedProductDetails(TeaModel):
    def __init__(self, create_time=None, last_provisioning_task_id=None,
                 last_successful_provisioning_task_id=None, last_task_id=None, owner_principal_id=None, owner_principal_type=None, portfolio_id=None,
                 product_id=None, product_name=None, product_version_id=None, product_version_name=None,
                 provisioned_product_arn=None, provisioned_product_id=None, provisioned_product_name=None, provisioned_product_type=None,
                 stack_id=None, stack_region_id=None, status=None, status_message=None):
        # The time when the product instance was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The ID of the task that was last run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_provisioning_task_id = last_provisioning_task_id  # type: str
        # The ID of the last task that was successfully run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_successful_provisioning_task_id = last_successful_provisioning_task_id  # type: str
        # The ID of the task that was last run.
        self.last_task_id = last_task_id  # type: str
        # The ID of the RAM entity to which the product instance belongs.
        self.owner_principal_id = owner_principal_id  # type: str
        # The type of the Resource Access Management (RAM) entity to which the product instance belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type  # type: str
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The name of the product.
        self.product_name = product_name  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product version.
        self.product_version_name = product_version_name  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the product instance.
        self.provisioned_product_arn = provisioned_product_arn  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name  # type: str
        # The type of the product instance.
        # 
        # The value is fixed as RosStack, which indicates an ROS stack.
        self.provisioned_product_type = provisioned_product_type  # type: str
        # The ID of the Resource Orchestration Service (ROS) stack.
        self.stack_id = stack_id  # type: str
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id  # type: str
        # The state of the product instance. Valid values:
        # 
        # *   Available: The product instance was available.
        # *   UnderChange: The information about the product instance was being changed.
        # *   Error: An exception occurred on the product instance.
        self.status = status  # type: str
        # The message that is returned for the status of the product instance.
        # 
        # > This parameter is returned only when Error is returned for the Status parameter.
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionedProductsResponseBodyProvisionedProductDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_provisioning_task_id is not None:
            result['LastProvisioningTaskId'] = self.last_provisioning_task_id
        if self.last_successful_provisioning_task_id is not None:
            result['LastSuccessfulProvisioningTaskId'] = self.last_successful_provisioning_task_id
        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_arn is not None:
            result['ProvisionedProductArn'] = self.provisioned_product_arn
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.provisioned_product_type is not None:
            result['ProvisionedProductType'] = self.provisioned_product_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastProvisioningTaskId') is not None:
            self.last_provisioning_task_id = m.get('LastProvisioningTaskId')
        if m.get('LastSuccessfulProvisioningTaskId') is not None:
            self.last_successful_provisioning_task_id = m.get('LastSuccessfulProvisioningTaskId')
        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductArn') is not None:
            self.provisioned_product_arn = m.get('ProvisionedProductArn')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('ProvisionedProductType') is not None:
            self.provisioned_product_type = m.get('ProvisionedProductType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class ListProvisionedProductsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, provisioned_product_details=None, request_id=None,
                 total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The product instances.
        self.provisioned_product_details = provisioned_product_details  # type: list[ListProvisionedProductsResponseBodyProvisionedProductDetails]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.provisioned_product_details:
            for k in self.provisioned_product_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionedProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProvisionedProductDetails'] = []
        if self.provisioned_product_details is not None:
            for k in self.provisioned_product_details:
                result['ProvisionedProductDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.provisioned_product_details = []
        if m.get('ProvisionedProductDetails') is not None:
            for k in m.get('ProvisionedProductDetails'):
                temp_model = ListProvisionedProductsResponseBodyProvisionedProductDetails()
                self.provisioned_product_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProvisionedProductsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProvisionedProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProvisionedProductsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProvisionedProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The details of regions.
        self.regions = regions  # type: list[ListRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesForTagOptionRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_type=None, tag_option_id=None):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100 Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The type of resource that is associated with the tag option. Valid values:
        # 
        # *   product: product
        # *   Portfolio: product portfolio
        self.resource_type = resource_type  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesForTagOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        return self


class ListResourcesForTagOptionResponseBodyResourceDetails(TeaModel):
    def __init__(self, create_time=None, description=None, resource_arn=None, resource_id=None, resource_name=None):
        # The time when the resource was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the resource.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        self.resource_arn = resource_arn  # type: str
        # The ID of the resource with which the tag option is associated.
        self.resource_id = resource_id  # type: str
        # The name of the resource.
        self.resource_name = resource_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesForTagOptionResponseBodyResourceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class ListResourcesForTagOptionResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, resource_details=None, total_count=None):
        # The page number of the returned page.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100 Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the associated resources.
        self.resource_details = resource_details  # type: list[ListResourcesForTagOptionResponseBodyResourceDetails]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resource_details:
            for k in self.resource_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesForTagOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceDetails'] = []
        if self.resource_details is not None:
            for k in self.resource_details:
                result['ResourceDetails'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_details = []
        if m.get('ResourceDetails') is not None:
            for k in m.get('ResourceDetails'):
                temp_model = ListResourcesForTagOptionResponseBodyResourceDetails()
                self.resource_details.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesForTagOptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesForTagOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesForTagOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesForTagOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagOptionsRequestFilters(TeaModel):
    def __init__(self, active=None, full_text_search=None, key=None, value=None):
        # Specifies whether to enable the tag option. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active  # type: bool
        # The full-text search method.
        self.full_text_search = full_text_search  # type: str
        # The key of the tag option.
        self.key = key  # type: str
        # The value of the tag option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagOptionsRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.full_text_search is not None:
            result['FullTextSearch'] = self.full_text_search
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('FullTextSearch') is not None:
            self.full_text_search = m.get('FullTextSearch')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagOptionsRequest(TeaModel):
    def __init__(self, filters=None, page_number=None, page_size=None, sort_by=None, sort_order=None):
        # The filter condition.
        self.filters = filters  # type: ListTagOptionsRequestFilters
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of tag options.
        self.sort_by = sort_by  # type: str
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order
        self.sort_order = sort_order  # type: str

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super(ListTagOptionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filters') is not None:
            temp_model = ListTagOptionsRequestFilters()
            self.filters = temp_model.from_map(m['Filters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListTagOptionsShrinkRequest(TeaModel):
    def __init__(self, filters_shrink=None, page_number=None, page_size=None, sort_by=None, sort_order=None):
        # The filter condition.
        self.filters_shrink = filters_shrink  # type: str
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of tag options.
        self.sort_by = sort_by  # type: str
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order
        self.sort_order = sort_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagOptionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters_shrink is not None:
            result['Filters'] = self.filters_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters_shrink = m.get('Filters')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListTagOptionsResponseBodyTagOptionDetails(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.active = active  # type: bool
        # The key of the tag option.
        self.key = key  # type: str
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagOptionsResponseBodyTagOptionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagOptionsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tag_option_details=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the details of the tag option.
        self.tag_option_details = tag_option_details  # type: list[ListTagOptionsResponseBodyTagOptionDetails]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tag_option_details:
            for k in self.tag_option_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagOptionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagOptionDetails'] = []
        if self.tag_option_details is not None:
            for k in self.tag_option_details:
                result['TagOptionDetails'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_option_details = []
        if m.get('TagOptionDetails') is not None:
            for k in m.get('TagOptionDetails'):
                temp_model = ListTagOptionsResponseBodyTagOptionDetails()
                self.tag_option_details.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagOptionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagOptionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagOptionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, provisioned_product_id=None, sort_by=None, sort_order=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.provisioned_product_id = provisioned_product_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_order = sort_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListTasksResponseBodyTaskDetailsLogTerraformLogs(TeaModel):
    def __init__(self, command=None, content=None, stream=None):
        self.command = command  # type: str
        self.content = content  # type: str
        self.stream = stream  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTaskDetailsLogTerraformLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class ListTasksResponseBodyTaskDetailsLog(TeaModel):
    def __init__(self, terraform_logs=None):
        self.terraform_logs = terraform_logs  # type: list[ListTasksResponseBodyTaskDetailsLogTerraformLogs]

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBodyTaskDetailsLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = ListTasksResponseBodyTaskDetailsLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class ListTasksResponseBodyTaskDetailsOutputs(TeaModel):
    def __init__(self, description=None, output_key=None, output_value=None):
        self.description = description  # type: str
        self.output_key = output_key  # type: str
        self.output_value = output_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTaskDetailsOutputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.output_value is not None:
            result['OutputValue'] = self.output_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        if m.get('OutputValue') is not None:
            self.output_value = m.get('OutputValue')
        return self


class ListTasksResponseBodyTaskDetailsParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTaskDetailsParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class ListTasksResponseBodyTaskDetails(TeaModel):
    def __init__(self, create_time=None, log=None, outputs=None, parameters=None, portfolio_id=None, product_id=None,
                 product_name=None, product_version_id=None, product_version_name=None, provisioned_product_id=None,
                 provisioned_product_name=None, status=None, status_message=None, task_id=None, task_type=None, update_time=None):
        self.create_time = create_time  # type: str
        self.log = log  # type: ListTasksResponseBodyTaskDetailsLog
        self.outputs = outputs  # type: list[ListTasksResponseBodyTaskDetailsOutputs]
        self.parameters = parameters  # type: list[ListTasksResponseBodyTaskDetailsParameters]
        self.portfolio_id = portfolio_id  # type: str
        self.product_id = product_id  # type: str
        self.product_name = product_name  # type: str
        self.product_version_id = product_version_id  # type: str
        self.product_version_name = product_version_name  # type: str
        self.provisioned_product_id = provisioned_product_id  # type: str
        self.provisioned_product_name = provisioned_product_name  # type: str
        self.status = status  # type: str
        self.status_message = status_message  # type: str
        # 代表资源名称的资源属性字段
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.log:
            self.log.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBodyTaskDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Log') is not None:
            temp_model = ListTasksResponseBodyTaskDetailsLog()
            self.log = temp_model.from_map(m['Log'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListTasksResponseBodyTaskDetailsOutputs()
                self.outputs.append(temp_model.from_map(k))
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListTasksResponseBodyTaskDetailsParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, task_details=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.task_details = task_details  # type: list[ListTasksResponseBodyTaskDetails]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.task_details:
            for k in self.task_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskDetails'] = []
        if self.task_details is not None:
            for k in self.task_details:
                result['TaskDetails'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_details = []
        if m.get('TaskDetails') is not None:
            for k in m.get('TaskDetails'):
                temp_model = ListTasksResponseBodyTaskDetails()
                self.task_details.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateProvisionedProductRequest(TeaModel):
    def __init__(self, provisioned_product_id=None):
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateProvisionedProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        return self


class TerminateProvisionedProductResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateProvisionedProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminateProvisionedProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TerminateProvisionedProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TerminateProvisionedProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TerminateProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConstraintRequest(TeaModel):
    def __init__(self, config=None, constraint_id=None, description=None):
        # The configurations of the constraint.
        # 
        # Format: { "LocalRoleName": "\<role_name>" }.
        self.config = config  # type: str
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str
        # The description of the constraint.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConstraintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateConstraintResponseBody(TeaModel):
    def __init__(self, constraint_id=None, request_id=None):
        # The ID of the constraint.
        self.constraint_id = constraint_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConstraintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConstraintResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConstraintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConstraintResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePortfolioRequest(TeaModel):
    def __init__(self, description=None, portfolio_id=None, portfolio_name=None, provider_name=None):
        # 产品组合描述
        self.description = description  # type: str
        # 代表资源一级ID的资源属性字段
        self.portfolio_id = portfolio_id  # type: str
        # 代表资源名称的资源属性字段
        self.portfolio_name = portfolio_name  # type: str
        # 产品组合提供方
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePortfolioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class UpdatePortfolioResponseBody(TeaModel):
    def __init__(self, portfolio_id=None, request_id=None):
        self.portfolio_id = portfolio_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePortfolioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePortfolioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePortfolioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePortfolioResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(self, description=None, product_id=None, product_name=None, provider_name=None):
        # 产品描述
        self.description = description  # type: str
        # 代表资源一级ID的资源属性字段
        self.product_id = product_id  # type: str
        # 代表资源名称的资源属性字段
        self.product_name = product_name  # type: str
        # 产品提供方
        self.provider_name = provider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(self, product_id=None, request_id=None):
        self.product_id = product_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(self, active=None, description=None, guidance=None, product_version_id=None,
                 product_version_name=None):
        # Specifies whether to enable the product version. Valid values:
        # 
        # *   true: enables the product version. This is the default value.
        # *   false: disables the product version.
        self.active = active  # type: bool
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description  # type: str
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommended version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.product_version_name = product_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(self, product_version_id=None, request_id=None):
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProvisionedProductRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the input parameter for the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateProvisionedProductRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the custom tag.
        # 
        # The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The tag value of the custom tag.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateProvisionedProductRequest(TeaModel):
    def __init__(self, parameters=None, portfolio_id=None, product_id=None, product_version_id=None,
                 provisioned_product_id=None, tags=None):
        # The input parameters of the template.
        # 
        # You can specify up to 200 parameters.
        # 
        # > - This parameter is optional. If you specify the Parameters parameter, you must specify the ParameterKey and ParameterValue parameters.
        # > - If the values of the ProductVersionId and Parameters parameters are not changed, you are not allowed to update the information about the product instance.
        self.parameters = parameters  # type: list[UpdateProvisionedProductRequestParameters]
        # The ID of the product portfolio.
        # 
        # > The PortfolioId parameter is not required if the default launch option exists. The PortfolioId parameter is required if the default launch option does not exist. For more information about how to obtain the value of the PortfolioId parameter, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        # 
        # > If the values of the ProductVersionId and Parameters parameters are not changed, the information about the product instance cannot be updated.
        self.product_version_id = product_version_id  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The input custom tags.
        # 
        # Maximum value of N: 20.
        # 
        # > - The Tags parameter is optional. If you need to specify the Tags parameter, you must specify the Tags.N.Key and Tags.N.Value parameters.
        # > - The tag is propagated to each stack resource that supports the tag feature.
        self.tags = tags  # type: list[UpdateProvisionedProductRequestTags]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateProvisionedProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateProvisionedProductRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateProvisionedProductRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdateProvisionedProductResponseBody(TeaModel):
    def __init__(self, provisioned_product_id=None, request_id=None):
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProvisionedProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProvisionedProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProvisionedProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProvisionedProductPlanRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key  # type: str
        # The value of the parameter in the template.
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductPlanRequestParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateProvisionedProductPlanRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom tag.
        # 
        # The key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the custom tag.
        # 
        # The value can be up to 128 characters in length, and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductPlanRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateProvisionedProductPlanRequest(TeaModel):
    def __init__(self, description=None, parameters=None, plan_id=None, portfolio_id=None, product_id=None,
                 product_version_id=None, tags=None):
        # The description of the plan.
        self.description = description  # type: str
        # An array that consists of the parameters in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify ParameterKey and ParameterValue.
        self.parameters = parameters  # type: list[UpdateProvisionedProductPlanRequestParameters]
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the product portfolio.
        # 
        # > If the default launch option exists, you do not need to specify PortfolioId. If the default launch option does not exist, you must specify PortfolioId. For more information about how to obtain the value of PortfolioId, see [ListLaunchOptions](~~ListLaunchOptions~~).
        self.portfolio_id = portfolio_id  # type: str
        # The ID of the product.
        self.product_id = product_id  # type: str
        # The ID of the product version.
        self.product_version_id = product_version_id  # type: str
        # An array that consists of custom tags.
        # 
        # Maximum value of N: 20.
        # 
        # > 
        # *   If you specify Tags, you must specify Tags.N.Key and Tags.N.Value.
        # *   The tag of a stack is propagated to each resource that supports the tag feature in the stack.
        self.tags = tags  # type: list[UpdateProvisionedProductPlanRequestTags]

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateProvisionedProductPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateProvisionedProductPlanRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateProvisionedProductPlanRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdateProvisionedProductPlanResponseBody(TeaModel):
    def __init__(self, plan_id=None, provisioned_product_id=None, request_id=None):
        # The ID of the plan.
        self.plan_id = plan_id  # type: str
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProvisionedProductPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProvisionedProductPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProvisionedProductPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProvisionedProductPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProvisionedProductPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTagOptionRequest(TeaModel):
    def __init__(self, active=None, tag_option_id=None, value=None):
        # Specifies whether to enable the tag option. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active  # type: bool
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        # 
        # The value can be up to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTagOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateTagOptionResponseBodyTagOptionDetail(TeaModel):
    def __init__(self, active=None, key=None, owner=None, tag_option_id=None, value=None):
        # Indicates whether the tag option is enabled. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active  # type: bool
        # The key of the tag option.
        # 
        # The key must be 1 to 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The ID of the Alibaba Cloud account to which the tag option belongs.
        self.owner = owner  # type: str
        # The ID of the tag option.
        self.tag_option_id = tag_option_id  # type: str
        # The value of the tag option.
        # 
        # The value must be 1 to 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTagOptionResponseBodyTagOptionDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.key is not None:
            result['Key'] = self.key
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateTagOptionResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_option_detail=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the tag option.
        self.tag_option_detail = tag_option_detail  # type: UpdateTagOptionResponseBodyTagOptionDetail

    def validate(self):
        if self.tag_option_detail:
            self.tag_option_detail.validate()

    def to_map(self):
        _map = super(UpdateTagOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_option_detail is not None:
            result['TagOptionDetail'] = self.tag_option_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagOptionDetail') is not None:
            temp_model = UpdateTagOptionResponseBodyTagOptionDetail()
            self.tag_option_detail = temp_model.from_map(m['TagOptionDetail'])
        return self


class UpdateTagOptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTagOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTagOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTagOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


