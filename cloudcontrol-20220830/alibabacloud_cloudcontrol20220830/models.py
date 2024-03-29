# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTaskResponse, self).to_map()
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
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(self, body=None, client_token=None, region_id=None):
        self.body = body  # type: dict[str, any]
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_id=None, resource_path=None, task_id=None):
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_path = resource_path  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceResponse, self).to_map()
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
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceResponse, self).to_map()
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
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPriceRequest(TeaModel):
    def __init__(self, region_id=None, resource_attributes=None):
        self.region_id = region_id  # type: str
        self.resource_attributes = resource_attributes  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        return self


class GetPriceShrinkRequest(TeaModel):
    def __init__(self, region_id=None, resource_attributes_shrink=None):
        self.region_id = region_id  # type: str
        self.resource_attributes_shrink = resource_attributes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_attributes_shrink is not None:
            result['resourceAttributes'] = self.resource_attributes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceAttributes') is not None:
            self.resource_attributes_shrink = m.get('resourceAttributes')
        return self


class GetPriceResponseBodyPriceModuleDetails(TeaModel):
    def __init__(self, cost_after_discount=None, invoice_discount=None, module_code=None, module_name=None,
                 original_cost=None, price_type=None):
        self.cost_after_discount = cost_after_discount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.module_code = module_code  # type: str
        self.module_name = module_name  # type: str
        self.original_cost = original_cost  # type: float
        self.price_type = price_type  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceResponseBodyPriceModuleDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_after_discount is not None:
            result['costAfterDiscount'] = self.cost_after_discount
        if self.invoice_discount is not None:
            result['invoiceDiscount'] = self.invoice_discount
        if self.module_code is not None:
            result['moduleCode'] = self.module_code
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.original_cost is not None:
            result['originalCost'] = self.original_cost
        if self.price_type is not None:
            result['priceType'] = self.price_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('costAfterDiscount') is not None:
            self.cost_after_discount = m.get('costAfterDiscount')
        if m.get('invoiceDiscount') is not None:
            self.invoice_discount = m.get('invoiceDiscount')
        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('originalCost') is not None:
            self.original_cost = m.get('originalCost')
        if m.get('priceType') is not None:
            self.price_type = m.get('priceType')
        return self


class GetPriceResponseBodyPricePromotionDetails(TeaModel):
    def __init__(self, promotion_desc=None, promotion_id=None, promotion_name=None):
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: long
        self.promotion_name = promotion_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceResponseBodyPricePromotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['promotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['promotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['promotionName'] = self.promotion_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('promotionDesc') is not None:
            self.promotion_desc = m.get('promotionDesc')
        if m.get('promotionId') is not None:
            self.promotion_id = m.get('promotionId')
        if m.get('promotionName') is not None:
            self.promotion_name = m.get('promotionName')
        return self


class GetPriceResponseBodyPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, module_details=None, original_price=None,
                 promotion_details=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.module_details = module_details  # type: list[GetPriceResponseBodyPriceModuleDetails]
        self.original_price = original_price  # type: float
        self.promotion_details = promotion_details  # type: list[GetPriceResponseBodyPricePromotionDetails]
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.module_details:
            for k in self.module_details:
                if k:
                    k.validate()
        if self.promotion_details:
            for k in self.promotion_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPriceResponseBodyPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['currency'] = self.currency
        if self.discount_price is not None:
            result['discountPrice'] = self.discount_price
        result['moduleDetails'] = []
        if self.module_details is not None:
            for k in self.module_details:
                result['moduleDetails'].append(k.to_map() if k else None)
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        result['promotionDetails'] = []
        if self.promotion_details is not None:
            for k in self.promotion_details:
                result['promotionDetails'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['tradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')
        if m.get('discountPrice') is not None:
            self.discount_price = m.get('discountPrice')
        self.module_details = []
        if m.get('moduleDetails') is not None:
            for k in m.get('moduleDetails'):
                temp_model = GetPriceResponseBodyPriceModuleDetails()
                self.module_details.append(temp_model.from_map(k))
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        self.promotion_details = []
        if m.get('promotionDetails') is not None:
            for k in m.get('promotionDetails'):
                temp_model = GetPriceResponseBodyPricePromotionDetails()
                self.promotion_details.append(temp_model.from_map(k))
        if m.get('tradePrice') is not None:
            self.trade_price = m.get('tradePrice')
        return self


class GetPriceResponseBody(TeaModel):
    def __init__(self, price=None, request_id=None):
        self.price = price  # type: GetPriceResponseBodyPrice
        self.request_id = request_id  # type: str

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super(GetPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['price'] = self.price.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('price') is not None:
            temp_model = GetPriceResponseBodyPrice()
            self.price = temp_model.from_map(m['price'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPriceResponse, self).to_map()
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
            temp_model = GetPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_accept_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_accept_language = x_acs_accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_accept_language is not None:
            result['x-acs-accept-language'] = self.x_acs_accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-accept-language') is not None:
            self.x_acs_accept_language = m.get('x-acs-accept-language')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersCreate(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlersCreate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersDelete(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlersDelete, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersGet(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlersGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersList(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlersList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlersUpdate(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlersUpdate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class GetResourceTypeResponseBodyResourceTypeHandlers(TeaModel):
    def __init__(self, create=None, delete=None, get=None, list=None, update=None):
        self.create = create  # type: GetResourceTypeResponseBodyResourceTypeHandlersCreate
        self.delete = delete  # type: GetResourceTypeResponseBodyResourceTypeHandlersDelete
        self.get = get  # type: GetResourceTypeResponseBodyResourceTypeHandlersGet
        self.list = list  # type: GetResourceTypeResponseBodyResourceTypeHandlersList
        self.update = update  # type: GetResourceTypeResponseBodyResourceTypeHandlersUpdate

    def validate(self):
        if self.create:
            self.create.validate()
        if self.delete:
            self.delete.validate()
        if self.get:
            self.get.validate()
        if self.list:
            self.list.validate()
        if self.update:
            self.update.validate()

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeHandlers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create is not None:
            result['create'] = self.create.to_map()
        if self.delete is not None:
            result['delete'] = self.delete.to_map()
        if self.get is not None:
            result['get'] = self.get.to_map()
        if self.list is not None:
            result['list'] = self.list.to_map()
        if self.update is not None:
            result['update'] = self.update.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('create') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersCreate()
            self.create = temp_model.from_map(m['create'])
        if m.get('delete') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersDelete()
            self.delete = temp_model.from_map(m['delete'])
        if m.get('get') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersGet()
            self.get = temp_model.from_map(m['get'])
        if m.get('list') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersList()
            self.list = temp_model.from_map(m['list'])
        if m.get('update') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlersUpdate()
            self.update = temp_model.from_map(m['update'])
        return self


class GetResourceTypeResponseBodyResourceTypeInfo(TeaModel):
    def __init__(self, charge_type=None, delivery_scope=None, description=None, title=None):
        self.charge_type = charge_type  # type: str
        self.delivery_scope = delivery_scope  # type: str
        self.description = description  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceTypeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetResourceTypeResponseBodyResourceType(TeaModel):
    def __init__(self, create_only_properties=None, delete_only_properties=None, filter_properties=None,
                 get_only_properties=None, get_response_properties=None, handlers=None, info=None, list_only_properties=None,
                 list_response_properties=None, primary_identifier=None, product=None, properties=None, public_properties=None,
                 read_only_properties=None, required=None, resource_type=None, sensitive_info_properties=None,
                 update_only_properties=None, update_type_properties=None):
        self.create_only_properties = create_only_properties  # type: list[str]
        self.delete_only_properties = delete_only_properties  # type: list[str]
        self.filter_properties = filter_properties  # type: list[str]
        self.get_only_properties = get_only_properties  # type: list[str]
        self.get_response_properties = get_response_properties  # type: list[str]
        self.handlers = handlers  # type: GetResourceTypeResponseBodyResourceTypeHandlers
        self.info = info  # type: GetResourceTypeResponseBodyResourceTypeInfo
        self.list_only_properties = list_only_properties  # type: list[str]
        self.list_response_properties = list_response_properties  # type: list[str]
        self.primary_identifier = primary_identifier  # type: str
        self.product = product  # type: str
        self.properties = properties  # type: dict[str, any]
        self.public_properties = public_properties  # type: list[str]
        self.read_only_properties = read_only_properties  # type: list[str]
        self.required = required  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.sensitive_info_properties = sensitive_info_properties  # type: list[str]
        self.update_only_properties = update_only_properties  # type: list[str]
        self.update_type_properties = update_type_properties  # type: list[str]

    def validate(self):
        if self.handlers:
            self.handlers.validate()
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super(GetResourceTypeResponseBodyResourceType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_only_properties is not None:
            result['createOnlyProperties'] = self.create_only_properties
        if self.delete_only_properties is not None:
            result['deleteOnlyProperties'] = self.delete_only_properties
        if self.filter_properties is not None:
            result['filterProperties'] = self.filter_properties
        if self.get_only_properties is not None:
            result['getOnlyProperties'] = self.get_only_properties
        if self.get_response_properties is not None:
            result['getResponseProperties'] = self.get_response_properties
        if self.handlers is not None:
            result['handlers'] = self.handlers.to_map()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.list_only_properties is not None:
            result['listOnlyProperties'] = self.list_only_properties
        if self.list_response_properties is not None:
            result['listResponseProperties'] = self.list_response_properties
        if self.primary_identifier is not None:
            result['primaryIdentifier'] = self.primary_identifier
        if self.product is not None:
            result['product'] = self.product
        if self.properties is not None:
            result['properties'] = self.properties
        if self.public_properties is not None:
            result['publicProperties'] = self.public_properties
        if self.read_only_properties is not None:
            result['readOnlyProperties'] = self.read_only_properties
        if self.required is not None:
            result['required'] = self.required
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sensitive_info_properties is not None:
            result['sensitiveInfoProperties'] = self.sensitive_info_properties
        if self.update_only_properties is not None:
            result['updateOnlyProperties'] = self.update_only_properties
        if self.update_type_properties is not None:
            result['updateTypeProperties'] = self.update_type_properties
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createOnlyProperties') is not None:
            self.create_only_properties = m.get('createOnlyProperties')
        if m.get('deleteOnlyProperties') is not None:
            self.delete_only_properties = m.get('deleteOnlyProperties')
        if m.get('filterProperties') is not None:
            self.filter_properties = m.get('filterProperties')
        if m.get('getOnlyProperties') is not None:
            self.get_only_properties = m.get('getOnlyProperties')
        if m.get('getResponseProperties') is not None:
            self.get_response_properties = m.get('getResponseProperties')
        if m.get('handlers') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeHandlers()
            self.handlers = temp_model.from_map(m['handlers'])
        if m.get('info') is not None:
            temp_model = GetResourceTypeResponseBodyResourceTypeInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('listOnlyProperties') is not None:
            self.list_only_properties = m.get('listOnlyProperties')
        if m.get('listResponseProperties') is not None:
            self.list_response_properties = m.get('listResponseProperties')
        if m.get('primaryIdentifier') is not None:
            self.primary_identifier = m.get('primaryIdentifier')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('publicProperties') is not None:
            self.public_properties = m.get('publicProperties')
        if m.get('readOnlyProperties') is not None:
            self.read_only_properties = m.get('readOnlyProperties')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('sensitiveInfoProperties') is not None:
            self.sensitive_info_properties = m.get('sensitiveInfoProperties')
        if m.get('updateOnlyProperties') is not None:
            self.update_only_properties = m.get('updateOnlyProperties')
        if m.get('updateTypeProperties') is not None:
            self.update_type_properties = m.get('updateTypeProperties')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_type=None):
        self.request_id = request_id  # type: str
        self.resource_type = resource_type  # type: GetResourceTypeResponseBodyResourceType

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        _map = super(GetResourceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceType') is not None:
            temp_model = GetResourceTypeResponseBodyResourceType()
            self.resource_type = temp_model.from_map(m['resourceType'])
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceTypeResponse, self).to_map()
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
            temp_model = GetResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcesRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, region_id=None):
        self.filter = filter  # type: dict[str, any]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetResourcesShrinkRequest(TeaModel):
    def __init__(self, filter_shrink=None, max_results=None, next_token=None, region_id=None):
        self.filter_shrink = filter_shrink  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetResourcesResponseBodyResource(TeaModel):
    def __init__(self, resource_attributes=None, resource_id=None):
        self.resource_attributes = resource_attributes  # type: dict[str, any]
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcesResponseBodyResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class GetResourcesResponseBodyResources(TeaModel):
    def __init__(self, resource_attributes=None, resource_id=None):
        self.resource_attributes = resource_attributes  # type: dict[str, any]
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class GetResourcesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resource=None, resources=None,
                 total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.resource = resource  # type: GetResourcesResponseBodyResource
        self.resources = resources  # type: list[GetResourcesResponseBodyResources]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resource') is not None:
            temp_model = GetResourcesResponseBodyResource()
            self.resource = temp_model.from_map(m['resource'])
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = GetResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourcesResponse, self).to_map()
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
            temp_model = GetResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskError(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBodyTaskError, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(self, create_time=None, error=None, product=None, region_id=None, resource_id=None,
                 resource_path=None, resource_type=None, status=None, task_action=None, task_id=None):
        self.create_time = create_time  # type: str
        self.error = error  # type: GetTaskResponseBodyTaskError
        self.product = product  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_path = resource_path  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.task_action = task_action  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super(GetTaskResponseBodyTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.product is not None:
            result['product'] = self.product
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.status is not None:
            result['status'] = self.status
        if self.task_action is not None:
            result['taskAction'] = self.task_action
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('error') is not None:
            temp_model = GetTaskResponseBodyTaskError()
            self.error = temp_model.from_map(m['error'])
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskAction') is not None:
            self.task_action = m.get('taskAction')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task=None):
        self.request_id = request_id  # type: str
        self.task = task  # type: GetTaskResponseBodyTask

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
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


class ListDataSourcesRequest(TeaModel):
    def __init__(self, attribute_name=None, filter=None):
        self.attribute_name = attribute_name  # type: str
        self.filter = filter  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['attributeName'] = self.attribute_name
        if self.filter is not None:
            result['filter'] = self.filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attributeName') is not None:
            self.attribute_name = m.get('attributeName')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(self, attribute_name=None, filter_shrink=None):
        self.attribute_name = attribute_name  # type: str
        self.filter_shrink = filter_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['attributeName'] = self.attribute_name
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('attributeName') is not None:
            self.attribute_name = m.get('attributeName')
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        return self


class ListDataSourcesResponseBodyDataSources(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesResponseBodyDataSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(self, data_sources=None, request_id=None):
        self.data_sources = data_sources  # type: list[ListDataSourcesResponseBodyDataSources]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['dataSources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k in m.get('dataSources'):
                temp_model = ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponse, self).to_map()
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_accept_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_accept_language = x_acs_accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_accept_language is not None:
            result['x-acs-accept-language'] = self.x_acs_accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-accept-language') is not None:
            self.x_acs_accept_language = m.get('x-acs-accept-language')
        return self


class ListProductsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(self, product_code=None, product_name=None):
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductsResponseBodyProducts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_name is not None:
            result['productName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, products=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.products = products  # type: list[ListProductsResponseBodyProducts]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProductsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductsResponse, self).to_map()
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_accept_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_accept_language = x_acs_accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_accept_language is not None:
            result['x-acs-accept-language'] = self.x_acs_accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-accept-language') is not None:
            self.x_acs_accept_language = m.get('x-acs-accept-language')
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_types=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_types = resource_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_types_shrink=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_types_shrink = resource_types_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_types_shrink is not None:
            result['resourceTypes'] = self.resource_types_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceTypes') is not None:
            self.resource_types_shrink = m.get('resourceTypes')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersCreate(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlersCreate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersDelete(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlersDelete, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersGet(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlersGet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersList(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlersList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlersUpdate(TeaModel):
    def __init__(self, permissions=None):
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlersUpdate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class ListResourceTypesResponseBodyResourceTypesHandlers(TeaModel):
    def __init__(self, create=None, delete=None, get=None, list=None, update=None):
        self.create = create  # type: ListResourceTypesResponseBodyResourceTypesHandlersCreate
        self.delete = delete  # type: ListResourceTypesResponseBodyResourceTypesHandlersDelete
        self.get = get  # type: ListResourceTypesResponseBodyResourceTypesHandlersGet
        self.list = list  # type: ListResourceTypesResponseBodyResourceTypesHandlersList
        self.update = update  # type: ListResourceTypesResponseBodyResourceTypesHandlersUpdate

    def validate(self):
        if self.create:
            self.create.validate()
        if self.delete:
            self.delete.validate()
        if self.get:
            self.get.validate()
        if self.list:
            self.list.validate()
        if self.update:
            self.update.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesHandlers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create is not None:
            result['create'] = self.create.to_map()
        if self.delete is not None:
            result['delete'] = self.delete.to_map()
        if self.get is not None:
            result['get'] = self.get.to_map()
        if self.list is not None:
            result['list'] = self.list.to_map()
        if self.update is not None:
            result['update'] = self.update.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('create') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersCreate()
            self.create = temp_model.from_map(m['create'])
        if m.get('delete') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersDelete()
            self.delete = temp_model.from_map(m['delete'])
        if m.get('get') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersGet()
            self.get = temp_model.from_map(m['get'])
        if m.get('list') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersList()
            self.list = temp_model.from_map(m['list'])
        if m.get('update') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlersUpdate()
            self.update = temp_model.from_map(m['update'])
        return self


class ListResourceTypesResponseBodyResourceTypesInfo(TeaModel):
    def __init__(self, charge_type=None, delivery_scope=None, description=None, title=None):
        self.charge_type = charge_type  # type: str
        self.delivery_scope = delivery_scope  # type: str
        self.description = description  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypesInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.delivery_scope is not None:
            result['deliveryScope'] = self.delivery_scope
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('deliveryScope') is not None:
            self.delivery_scope = m.get('deliveryScope')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(self, create_only_properties=None, delete_only_properties=None, filter_properties=None,
                 get_only_properties=None, get_response_properties=None, handlers=None, info=None, list_only_properties=None,
                 list_response_properties=None, primary_identifier=None, product=None, properties=None, public_properties=None,
                 read_only_properties=None, required=None, resource_type=None, sensitive_info_properties=None,
                 update_only_properties=None, update_type_properties=None):
        self.create_only_properties = create_only_properties  # type: list[str]
        self.delete_only_properties = delete_only_properties  # type: list[str]
        self.filter_properties = filter_properties  # type: list[str]
        self.get_only_properties = get_only_properties  # type: list[str]
        self.get_response_properties = get_response_properties  # type: list[str]
        self.handlers = handlers  # type: ListResourceTypesResponseBodyResourceTypesHandlers
        self.info = info  # type: ListResourceTypesResponseBodyResourceTypesInfo
        self.list_only_properties = list_only_properties  # type: list[str]
        self.list_response_properties = list_response_properties  # type: list[str]
        self.primary_identifier = primary_identifier  # type: str
        self.product = product  # type: str
        self.properties = properties  # type: dict[str, any]
        self.public_properties = public_properties  # type: list[str]
        self.read_only_properties = read_only_properties  # type: list[str]
        self.required = required  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.sensitive_info_properties = sensitive_info_properties  # type: list[str]
        self.update_only_properties = update_only_properties  # type: list[str]
        self.update_type_properties = update_type_properties  # type: list[str]

    def validate(self):
        if self.handlers:
            self.handlers.validate()
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponseBodyResourceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_only_properties is not None:
            result['createOnlyProperties'] = self.create_only_properties
        if self.delete_only_properties is not None:
            result['deleteOnlyProperties'] = self.delete_only_properties
        if self.filter_properties is not None:
            result['filterProperties'] = self.filter_properties
        if self.get_only_properties is not None:
            result['getOnlyProperties'] = self.get_only_properties
        if self.get_response_properties is not None:
            result['getResponseProperties'] = self.get_response_properties
        if self.handlers is not None:
            result['handlers'] = self.handlers.to_map()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.list_only_properties is not None:
            result['listOnlyProperties'] = self.list_only_properties
        if self.list_response_properties is not None:
            result['listResponseProperties'] = self.list_response_properties
        if self.primary_identifier is not None:
            result['primaryIdentifier'] = self.primary_identifier
        if self.product is not None:
            result['product'] = self.product
        if self.properties is not None:
            result['properties'] = self.properties
        if self.public_properties is not None:
            result['publicProperties'] = self.public_properties
        if self.read_only_properties is not None:
            result['readOnlyProperties'] = self.read_only_properties
        if self.required is not None:
            result['required'] = self.required
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sensitive_info_properties is not None:
            result['sensitiveInfoProperties'] = self.sensitive_info_properties
        if self.update_only_properties is not None:
            result['updateOnlyProperties'] = self.update_only_properties
        if self.update_type_properties is not None:
            result['updateTypeProperties'] = self.update_type_properties
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createOnlyProperties') is not None:
            self.create_only_properties = m.get('createOnlyProperties')
        if m.get('deleteOnlyProperties') is not None:
            self.delete_only_properties = m.get('deleteOnlyProperties')
        if m.get('filterProperties') is not None:
            self.filter_properties = m.get('filterProperties')
        if m.get('getOnlyProperties') is not None:
            self.get_only_properties = m.get('getOnlyProperties')
        if m.get('getResponseProperties') is not None:
            self.get_response_properties = m.get('getResponseProperties')
        if m.get('handlers') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesHandlers()
            self.handlers = temp_model.from_map(m['handlers'])
        if m.get('info') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('listOnlyProperties') is not None:
            self.list_only_properties = m.get('listOnlyProperties')
        if m.get('listResponseProperties') is not None:
            self.list_response_properties = m.get('listResponseProperties')
        if m.get('primaryIdentifier') is not None:
            self.primary_identifier = m.get('primaryIdentifier')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('publicProperties') is not None:
            self.public_properties = m.get('publicProperties')
        if m.get('readOnlyProperties') is not None:
            self.read_only_properties = m.get('readOnlyProperties')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('sensitiveInfoProperties') is not None:
            self.sensitive_info_properties = m.get('sensitiveInfoProperties')
        if m.get('updateOnlyProperties') is not None:
            self.update_only_properties = m.get('updateOnlyProperties')
        if m.get('updateTypeProperties') is not None:
            self.update_type_properties = m.get('updateTypeProperties')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resource_types=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.resource_types = resource_types  # type: list[ListResourceTypesResponseBodyResourceTypes]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceTypesResponse, self).to_map()
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(self, body=None, client_token=None, region_id=None):
        self.body = body  # type: dict[str, any]
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceResponse, self).to_map()
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
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


