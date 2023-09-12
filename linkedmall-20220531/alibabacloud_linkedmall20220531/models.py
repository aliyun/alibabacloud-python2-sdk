# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApplyCreateDistributionOrderRequestItemInfoLists(TeaModel):
    def __init__(self, distribution_mall_id=None, lm_item_id=None, price=None, quantity=None, sku_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.price = price  # type: long
        self.quantity = quantity  # type: int
        # SKU
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyCreateDistributionOrderRequestItemInfoLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.price is not None:
            result['Price'] = self.price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class ApplyCreateDistributionOrderRequest(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, distribution_out_trade_id=None,
                 distribution_supplier_id=None, distributor_id=None, ext_info=None, item_info_lists=None, tenant_id=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: str
        self.distribution_out_trade_id = distribution_out_trade_id  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.ext_info = ext_info  # type: str
        self.item_info_lists = item_info_lists  # type: list[ApplyCreateDistributionOrderRequestItemInfoLists]
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        if self.item_info_lists:
            for k in self.item_info_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyCreateDistributionOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_out_trade_id is not None:
            result['DistributionOutTradeId'] = self.distribution_out_trade_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        result['ItemInfoLists'] = []
        if self.item_info_lists is not None:
            for k in self.item_info_lists:
                result['ItemInfoLists'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionOutTradeId') is not None:
            self.distribution_out_trade_id = m.get('DistributionOutTradeId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        self.item_info_lists = []
        if m.get('ItemInfoLists') is not None:
            for k in m.get('ItemInfoLists'):
                temp_model = ApplyCreateDistributionOrderRequestItemInfoLists()
                self.item_info_lists.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyCreateDistributionOrderShrinkRequest(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, distribution_out_trade_id=None,
                 distribution_supplier_id=None, distributor_id=None, ext_info=None, item_info_lists_shrink=None, tenant_id=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: str
        self.distribution_out_trade_id = distribution_out_trade_id  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.ext_info = ext_info  # type: str
        self.item_info_lists_shrink = item_info_lists_shrink  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyCreateDistributionOrderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_out_trade_id is not None:
            result['DistributionOutTradeId'] = self.distribution_out_trade_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.item_info_lists_shrink is not None:
            result['ItemInfoLists'] = self.item_info_lists_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionOutTradeId') is not None:
            self.distribution_out_trade_id = m.get('DistributionOutTradeId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ItemInfoLists') is not None:
            self.item_info_lists_shrink = m.get('ItemInfoLists')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyCreateDistributionOrderResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: str
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyCreateDistributionOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ApplyCreateDistributionOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyCreateDistributionOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyCreateDistributionOrderResponse, self).to_map()
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
            temp_model = ApplyCreateDistributionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyRefund4DistributionRequestLeavePictureLists(TeaModel):
    def __init__(self, desc=None, picture=None):
        self.desc = desc  # type: str
        self.picture = picture  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyRefund4DistributionRequestLeavePictureLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.picture is not None:
            result['Picture'] = self.picture
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Picture') is not None:
            self.picture = m.get('Picture')
        return self


class ApplyRefund4DistributionRequest(TeaModel):
    def __init__(self, apply_reason_text_id=None, apply_refund_count=None, apply_refund_fee=None,
                 biz_claim_type=None, distributor_id=None, goods_status=None, leave_message=None, leave_picture_lists=None,
                 sub_distribution_order_id=None, tenant_id=None):
        self.apply_reason_text_id = apply_reason_text_id  # type: long
        self.apply_refund_count = apply_refund_count  # type: int
        self.apply_refund_fee = apply_refund_fee  # type: long
        self.biz_claim_type = biz_claim_type  # type: int
        self.distributor_id = distributor_id  # type: str
        self.goods_status = goods_status  # type: int
        self.leave_message = leave_message  # type: str
        self.leave_picture_lists = leave_picture_lists  # type: list[ApplyRefund4DistributionRequestLeavePictureLists]
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        if self.leave_picture_lists:
            for k in self.leave_picture_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyRefund4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        result['LeavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k in self.leave_picture_lists:
                result['LeavePictureLists'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        self.leave_picture_lists = []
        if m.get('LeavePictureLists') is not None:
            for k in m.get('LeavePictureLists'):
                temp_model = ApplyRefund4DistributionRequestLeavePictureLists()
                self.leave_picture_lists.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyRefund4DistributionShrinkRequest(TeaModel):
    def __init__(self, apply_reason_text_id=None, apply_refund_count=None, apply_refund_fee=None,
                 biz_claim_type=None, distributor_id=None, goods_status=None, leave_message=None, leave_picture_lists_shrink=None,
                 sub_distribution_order_id=None, tenant_id=None):
        self.apply_reason_text_id = apply_reason_text_id  # type: long
        self.apply_refund_count = apply_refund_count  # type: int
        self.apply_refund_fee = apply_refund_fee  # type: long
        self.biz_claim_type = biz_claim_type  # type: int
        self.distributor_id = distributor_id  # type: str
        self.goods_status = goods_status  # type: int
        self.leave_message = leave_message  # type: str
        self.leave_picture_lists_shrink = leave_picture_lists_shrink  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyRefund4DistributionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        if self.leave_picture_lists_shrink is not None:
            result['LeavePictureLists'] = self.leave_picture_lists_shrink
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        if m.get('LeavePictureLists') is not None:
            self.leave_picture_lists_shrink = m.get('LeavePictureLists')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(self, dispute_id=None, dispute_status=None, dispute_type=None, sub_distribution_order_id=None):
        self.dispute_id = dispute_id  # type: long
        self.dispute_status = dispute_status  # type: int
        self.dispute_type = dispute_type  # type: int
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyRefund4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class ApplyRefund4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: ApplyRefund4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ApplyRefund4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ApplyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ApplyRefund4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyRefund4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyRefund4DistributionResponse, self).to_map()
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
            temp_model = ApplyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDistributionTradeRequest(TeaModel):
    def __init__(self, distribution_trade_id=None, distributor_id=None, tenant_id=None):
        self.distribution_trade_id = distribution_trade_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDistributionTradeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelDistributionTradeResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, page_number=None, page_size=None, request_id=None,
                 sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDistributionTradeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CancelDistributionTradeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelDistributionTradeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDistributionTradeResponse, self).to_map()
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
            temp_model = CancelDistributionTradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRefund4DistributionRequest(TeaModel):
    def __init__(self, dispute_id=None, distributor_id=None, sub_distribution_order_id=None, tenant_id=None):
        self.dispute_id = dispute_id  # type: long
        self.distributor_id = distributor_id  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRefund4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(self, dispute_id=None, dispute_status=None, dispute_type=None, sub_distribution_order_id=None):
        self.dispute_id = dispute_id  # type: long
        self.dispute_status = dispute_status  # type: int
        self.dispute_type = dispute_type  # type: int
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRefund4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class CancelRefund4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: CancelRefund4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(CancelRefund4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = CancelRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CancelRefund4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelRefund4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRefund4DistributionResponse, self).to_map()
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
            temp_model = CancelRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDisburse4DistributionRequest(TeaModel):
    def __init__(self, distribution_trade_id=None, distributor_id=None, main_distribution_order_id=None,
                 tenant_id=None):
        self.distribution_trade_id = distribution_trade_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.main_distribution_order_id = main_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDisburse4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ConfirmDisburse4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, page_number=None, page_size=None, request_id=None,
                 sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDisburse4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ConfirmDisburse4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmDisburse4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmDisburse4DistributionResponse, self).to_map()
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
            temp_model = ConfirmDisburse4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitApplyRefund4DistributionRequest(TeaModel):
    def __init__(self, biz_claim_type=None, distributor_id=None, goods_status=None, sub_distribution_order_id=None,
                 tenant_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.distributor_id = distributor_id  # type: str
        self.goods_status = goods_status  # type: int
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitApplyRefund4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData(TeaModel):
    def __init__(self, max_refund_fee=None, min_refund_fee=None):
        self.max_refund_fee = max_refund_fee  # type: long
        self.min_refund_fee = min_refund_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class InitApplyRefund4DistributionResponseBodyModelRefundReasonList(TeaModel):
    def __init__(self, proof_required=None, reason_text_id=None, reason_tips=None, refund_desc_required=None):
        self.proof_required = proof_required  # type: bool
        self.reason_text_id = reason_text_id  # type: str
        self.reason_tips = reason_tips  # type: str
        self.refund_desc_required = refund_desc_required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitApplyRefund4DistributionResponseBodyModelRefundReasonList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proof_required is not None:
            result['ProofRequired'] = self.proof_required
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.refund_desc_required is not None:
            result['RefundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProofRequired') is not None:
            self.proof_required = m.get('ProofRequired')
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('RefundDescRequired') is not None:
            self.refund_desc_required = m.get('RefundDescRequired')
        return self


class InitApplyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(self, biz_claim_type=None, main_order_refund=None, max_refund_fee_data=None,
                 refund_reason_list=None, sub_distribution_order_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.main_order_refund = main_order_refund  # type: bool
        self.max_refund_fee_data = max_refund_fee_data  # type: InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData
        self.refund_reason_list = refund_reason_list  # type: list[InitApplyRefund4DistributionResponseBodyModelRefundReasonList]
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InitApplyRefund4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.main_order_refund is not None:
            result['MainOrderRefund'] = self.main_order_refund
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        result['RefundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['RefundReasonList'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('MainOrderRefund') is not None:
            self.main_order_refund = m.get('MainOrderRefund')
        if m.get('MaxRefundFeeData') is not None:
            temp_model = InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        self.refund_reason_list = []
        if m.get('RefundReasonList') is not None:
            for k in m.get('RefundReasonList'):
                temp_model = InitApplyRefund4DistributionResponseBodyModelRefundReasonList()
                self.refund_reason_list.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class InitApplyRefund4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: InitApplyRefund4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(InitApplyRefund4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = InitApplyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class InitApplyRefund4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitApplyRefund4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitApplyRefund4DistributionResponse, self).to_map()
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
            temp_model = InitApplyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitModifyRefund4DistributionRequest(TeaModel):
    def __init__(self, biz_claim_type=None, dispute_id=None, distributor_id=None, sub_distribution_order_id=None,
                 tenant_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.dispute_id = dispute_id  # type: long
        self.distributor_id = distributor_id  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitModifyRefund4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData(TeaModel):
    def __init__(self, max_refund_fee=None, min_refund_fee=None):
        self.max_refund_fee = max_refund_fee  # type: long
        self.min_refund_fee = min_refund_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class InitModifyRefund4DistributionResponseBodyModelRefundReasonList(TeaModel):
    def __init__(self, proof_required=None, reason_text_id=None, reason_tips=None, refund_desc_required=None):
        self.proof_required = proof_required  # type: bool
        self.reason_text_id = reason_text_id  # type: str
        self.reason_tips = reason_tips  # type: str
        self.refund_desc_required = refund_desc_required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitModifyRefund4DistributionResponseBodyModelRefundReasonList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proof_required is not None:
            result['ProofRequired'] = self.proof_required
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.refund_desc_required is not None:
            result['RefundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProofRequired') is not None:
            self.proof_required = m.get('ProofRequired')
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('RefundDescRequired') is not None:
            self.refund_desc_required = m.get('RefundDescRequired')
        return self


class InitModifyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(self, biz_claim_type=None, main_order_refund=None, max_refund_fee_data=None,
                 refund_reason_list=None, sub_distribution_order_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.main_order_refund = main_order_refund  # type: bool
        self.max_refund_fee_data = max_refund_fee_data  # type: InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData
        self.refund_reason_list = refund_reason_list  # type: list[InitModifyRefund4DistributionResponseBodyModelRefundReasonList]
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InitModifyRefund4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.main_order_refund is not None:
            result['MainOrderRefund'] = self.main_order_refund
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        result['RefundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['RefundReasonList'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('MainOrderRefund') is not None:
            self.main_order_refund = m.get('MainOrderRefund')
        if m.get('MaxRefundFeeData') is not None:
            temp_model = InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        self.refund_reason_list = []
        if m.get('RefundReasonList') is not None:
            for k in m.get('RefundReasonList'):
                temp_model = InitModifyRefund4DistributionResponseBodyModelRefundReasonList()
                self.refund_reason_list.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class InitModifyRefund4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: InitModifyRefund4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(InitModifyRefund4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = InitModifyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class InitModifyRefund4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitModifyRefund4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitModifyRefund4DistributionResponse, self).to_map()
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
            temp_model = InitModifyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionItemRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, item_status=None, lm_item_id=None,
                 page_number=None, page_size=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.item_status = item_status  # type: int
        self.lm_item_id = lm_item_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.item_status is not None:
            result['ItemStatus'] = self.item_status
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ItemStatus') is not None:
            self.item_status = m.get('ItemStatus')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionItemResponseBodyModelCategoryChain(TeaModel):
    def __init__(self, category_id=None, leaf=None, level=None, name=None, parent_id=None):
        self.category_id = category_id  # type: long
        self.leaf = leaf  # type: bool
        self.level = level  # type: int
        self.name = name  # type: str
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemResponseBodyModelCategoryChain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class ListDistributionItemResponseBodyModelLmAttributeModels(TeaModel):
    def __init__(self, attr_id=None, category=None, data_type=None, description=None, name=None, restriction=None,
                 scope_list=None, value=None):
        self.attr_id = attr_id  # type: long
        self.category = category  # type: int
        self.data_type = data_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.restriction = restriction  # type: str
        self.scope_list = scope_list  # type: list[str]
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemResponseBodyModelLmAttributeModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attr_id is not None:
            result['AttrId'] = self.attr_id
        if self.category is not None:
            result['Category'] = self.category
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.restriction is not None:
            result['Restriction'] = self.restriction
        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttrId') is not None:
            self.attr_id = m.get('AttrId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Restriction') is not None:
            self.restriction = m.get('Restriction')
        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDistributionItemResponseBodyModelSkuListLmAttributeModels(TeaModel):
    def __init__(self, attr_id=None, category=None, data_type=None, description=None, name=None, restriction=None,
                 scope_list=None, value=None):
        self.attr_id = attr_id  # type: long
        self.category = category  # type: int
        self.data_type = data_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.restriction = restriction  # type: str
        self.scope_list = scope_list  # type: list[str]
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemResponseBodyModelSkuListLmAttributeModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attr_id is not None:
            result['AttrId'] = self.attr_id
        if self.category is not None:
            result['Category'] = self.category
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.restriction is not None:
            result['Restriction'] = self.restriction
        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttrId') is not None:
            self.attr_id = m.get('AttrId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Restriction') is not None:
            self.restriction = m.get('Restriction')
        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDistributionItemResponseBodyModelSkuList(TeaModel):
    def __init__(self, can_sell=None, customized_attribute_map=None, ext_info=None, gmt_modified=None,
                 has_quantity=None, item_id=None, lm_attribute_models=None, lm_item_id=None, price_cent=None, quantity=None,
                 reserved_price=None, simple_quantity=None, sku_desc=None, sku_id=None, sku_pic_url=None, sku_properties=None,
                 sku_properties_json=None, sku_title=None, status=None, tips=None, lm_sku_attribute_map=None):
        self.can_sell = can_sell  # type: bool
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.ext_info = ext_info  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.item_id = item_id  # type: long
        self.lm_attribute_models = lm_attribute_models  # type: list[ListDistributionItemResponseBodyModelSkuListLmAttributeModels]
        self.lm_item_id = lm_item_id  # type: str
        self.price_cent = price_cent  # type: long
        self.quantity = quantity  # type: long
        self.reserved_price = reserved_price  # type: long
        self.simple_quantity = simple_quantity  # type: str
        self.sku_desc = sku_desc  # type: str
        self.sku_id = sku_id  # type: long
        self.sku_pic_url = sku_pic_url  # type: str
        self.sku_properties = sku_properties  # type: dict[str, str]
        self.sku_properties_json = sku_properties_json  # type: str
        self.sku_title = sku_title  # type: str
        self.status = status  # type: int
        self.tips = tips  # type: str
        self.lm_sku_attribute_map = lm_sku_attribute_map  # type: dict[str, str]

    def validate(self):
        if self.lm_attribute_models:
            for k in self.lm_attribute_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemResponseBodyModelSkuList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        result['LmAttributeModels'] = []
        if self.lm_attribute_models is not None:
            for k in self.lm_attribute_models:
                result['LmAttributeModels'].append(k.to_map() if k else None)
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_desc is not None:
            result['SkuDesc'] = self.sku_desc
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_properties is not None:
            result['SkuProperties'] = self.sku_properties
        if self.sku_properties_json is not None:
            result['SkuPropertiesJson'] = self.sku_properties_json
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.lm_sku_attribute_map is not None:
            result['lmSkuAttributeMap'] = self.lm_sku_attribute_map
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        self.lm_attribute_models = []
        if m.get('LmAttributeModels') is not None:
            for k in m.get('LmAttributeModels'):
                temp_model = ListDistributionItemResponseBodyModelSkuListLmAttributeModels()
                self.lm_attribute_models.append(temp_model.from_map(k))
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuDesc') is not None:
            self.sku_desc = m.get('SkuDesc')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuProperties') is not None:
            self.sku_properties = m.get('SkuProperties')
        if m.get('SkuPropertiesJson') is not None:
            self.sku_properties_json = m.get('SkuPropertiesJson')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('lmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('lmSkuAttributeMap')
        return self


class ListDistributionItemResponseBodyModel(TeaModel):
    def __init__(self, category=None, category_chain=None, category_id=None, desc_option=None,
                 distribution_mall_id=None, gmt_create=None, gmt_modified=None, has_quantity=None, is_can_sell=None, item_desc=None,
                 item_id=None, item_id_str=None, item_images=None, item_name=None, item_title=None, lm_attribute_map=None,
                 lm_attribute_models=None, lm_item_id=None, main_pic_url=None, pic_url=None, price_cent_scope=None,
                 properties_json=None, quantity=None, reserved_price=None, reserved_price_scope=None, simple_quantity=None,
                 simple_total_sold_quantity=None, sku_list=None, status=None, tips=None, total_sold_quantity=None):
        self.category = category  # type: str
        self.category_chain = category_chain  # type: list[ListDistributionItemResponseBodyModelCategoryChain]
        self.category_id = category_id  # type: long
        self.desc_option = desc_option  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.is_can_sell = is_can_sell  # type: bool
        self.item_desc = item_desc  # type: str
        self.item_id = item_id  # type: long
        self.item_id_str = item_id_str  # type: str
        self.item_images = item_images  # type: list[str]
        self.item_name = item_name  # type: str
        self.item_title = item_title  # type: str
        self.lm_attribute_map = lm_attribute_map  # type: dict[str, str]
        self.lm_attribute_models = lm_attribute_models  # type: list[ListDistributionItemResponseBodyModelLmAttributeModels]
        self.lm_item_id = lm_item_id  # type: str
        self.main_pic_url = main_pic_url  # type: str
        self.pic_url = pic_url  # type: str
        self.price_cent_scope = price_cent_scope  # type: str
        self.properties_json = properties_json  # type: str
        self.quantity = quantity  # type: int
        self.reserved_price = reserved_price  # type: long
        self.reserved_price_scope = reserved_price_scope  # type: str
        self.simple_quantity = simple_quantity  # type: str
        self.simple_total_sold_quantity = simple_total_sold_quantity  # type: str
        self.sku_list = sku_list  # type: list[ListDistributionItemResponseBodyModelSkuList]
        self.status = status  # type: int
        self.tips = tips  # type: str
        self.total_sold_quantity = total_sold_quantity  # type: int

    def validate(self):
        if self.category_chain:
            for k in self.category_chain:
                if k:
                    k.validate()
        if self.lm_attribute_models:
            for k in self.lm_attribute_models:
                if k:
                    k.validate()
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['CategoryChain'] = []
        if self.category_chain is not None:
            for k in self.category_chain:
                result['CategoryChain'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.item_desc is not None:
            result['ItemDesc'] = self.item_desc
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_id_str is not None:
            result['ItemIdStr'] = self.item_id_str
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_attribute_map is not None:
            result['LmAttributeMap'] = self.lm_attribute_map
        result['LmAttributeModels'] = []
        if self.lm_attribute_models is not None:
            for k in self.lm_attribute_models:
                result['LmAttributeModels'].append(k.to_map() if k else None)
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.price_cent_scope is not None:
            result['PriceCentScope'] = self.price_cent_scope
        if self.properties_json is not None:
            result['PropertiesJson'] = self.properties_json
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.reserved_price_scope is not None:
            result['ReservedPriceScope'] = self.reserved_price_scope
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.simple_total_sold_quantity is not None:
            result['SimpleTotalSoldQuantity'] = self.simple_total_sold_quantity
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_sold_quantity is not None:
            result['TotalSoldQuantity'] = self.total_sold_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.category_chain = []
        if m.get('CategoryChain') is not None:
            for k in m.get('CategoryChain'):
                temp_model = ListDistributionItemResponseBodyModelCategoryChain()
                self.category_chain.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('ItemDesc') is not None:
            self.item_desc = m.get('ItemDesc')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemIdStr') is not None:
            self.item_id_str = m.get('ItemIdStr')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmAttributeMap') is not None:
            self.lm_attribute_map = m.get('LmAttributeMap')
        self.lm_attribute_models = []
        if m.get('LmAttributeModels') is not None:
            for k in m.get('LmAttributeModels'):
                temp_model = ListDistributionItemResponseBodyModelLmAttributeModels()
                self.lm_attribute_models.append(temp_model.from_map(k))
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PriceCentScope') is not None:
            self.price_cent_scope = m.get('PriceCentScope')
        if m.get('PropertiesJson') is not None:
            self.properties_json = m.get('PropertiesJson')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('ReservedPriceScope') is not None:
            self.reserved_price_scope = m.get('ReservedPriceScope')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SimpleTotalSoldQuantity') is not None:
            self.simple_total_sold_quantity = m.get('SimpleTotalSoldQuantity')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = ListDistributionItemResponseBodyModelSkuList()
                self.sku_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalSoldQuantity') is not None:
            self.total_sold_quantity = m.get('TotalSoldQuantity')
        return self


class ListDistributionItemResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[ListDistributionItemResponseBodyModel]
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionItemResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDistributionItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDistributionItemResponse, self).to_map()
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
            temp_model = ListDistributionItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionItemWithoutCacheRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, item_status=None, lm_item_id=None,
                 page_number=None, page_size=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.item_status = item_status  # type: int
        self.lm_item_id = lm_item_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.item_status is not None:
            result['ItemStatus'] = self.item_status
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ItemStatus') is not None:
            self.item_status = m.get('ItemStatus')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuModels(TeaModel):
    def __init__(self, customized_attribute_map=None, distribution_mall_id=None, ext_json=None, has_quantity=None,
                 invoice_type=None, is_can_not_be_sold_code=None, is_can_not_be_sold_message=None, item_id=None,
                 lm_item_id=None, lm_sku_attribute_map=None, price_cent=None, quantity=None, reserved_price=None,
                 simple_quantity=None, sku_id=None, sku_pic_url=None, sku_pvs=None, sku_title=None, status=None, supplier_price=None):
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.ext_json = ext_json  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.invoice_type = invoice_type  # type: int
        self.is_can_not_be_sold_code = is_can_not_be_sold_code  # type: str
        self.is_can_not_be_sold_message = is_can_not_be_sold_message  # type: str
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_sku_attribute_map = lm_sku_attribute_map  # type: dict[str, str]
        self.price_cent = price_cent  # type: long
        self.quantity = quantity  # type: int
        self.reserved_price = reserved_price  # type: long
        self.simple_quantity = simple_quantity  # type: str
        self.sku_id = sku_id  # type: long
        self.sku_pic_url = sku_pic_url  # type: str
        self.sku_pvs = sku_pvs  # type: str
        self.sku_title = sku_title  # type: str
        self.status = status  # type: int
        self.supplier_price = supplier_price  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponseBodyModelSkuModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_not_be_sold_code is not None:
            result['IsCanNotBeSoldCode'] = self.is_can_not_be_sold_code
        if self.is_can_not_be_sold_message is not None:
            result['IsCanNotBeSoldMessage'] = self.is_can_not_be_sold_message
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_price is not None:
            result['SupplierPrice'] = self.supplier_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanNotBeSoldCode') is not None:
            self.is_can_not_be_sold_code = m.get('IsCanNotBeSoldCode')
        if m.get('IsCanNotBeSoldMessage') is not None:
            self.is_can_not_be_sold_message = m.get('IsCanNotBeSoldMessage')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPrice') is not None:
            self.supplier_price = m.get('SupplierPrice')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(self, id=None, text=None):
        self.id = id  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys(TeaModel):
    def __init__(self, id=None, text=None, values=None):
        self.id = id  # type: long
        self.text = text  # type: str
        self.values = values  # type: list[ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListDistributionItemWithoutCacheResponseBodyModel(TeaModel):
    def __init__(self, category_id=None, category_ids=None, city=None, current=None, customized_attribute_map=None,
                 desc_option=None, desc_path=None, distribution_mall_id=None, features=None, first_pic_url=None,
                 has_quantity=None, iforest_props=None, invoice_type=None, is_can_not_be_sold_code=None,
                 is_can_not_be_sold_message=None, is_can_sell=None, is_seller_pay_postfee=None, item_id=None, item_images=None,
                 item_title=None, item_total_simple_value=None, item_total_value=None, lm_item_attribute_map=None,
                 lm_item_category=None, lm_item_id=None, main_pic_url=None, min_price=None, properties=None, prov=None, quantity=None,
                 reserved_price=None, secured_transactions=None, simple_quantity=None, sku_models=None, sku_propertys=None,
                 third_party_item_id=None, third_party_name=None, user_type=None, video_pic_url=None, video_url=None,
                 virtual_item_type=None):
        self.category_id = category_id  # type: long
        self.category_ids = category_ids  # type: list[long]
        self.city = city  # type: str
        self.current = current  # type: str
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.desc_option = desc_option  # type: str
        self.desc_path = desc_path  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.features = features  # type: dict[str, str]
        self.first_pic_url = first_pic_url  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.iforest_props = iforest_props  # type: list[dict[str, str]]
        self.invoice_type = invoice_type  # type: int
        self.is_can_not_be_sold_code = is_can_not_be_sold_code  # type: str
        self.is_can_not_be_sold_message = is_can_not_be_sold_message  # type: str
        self.is_can_sell = is_can_sell  # type: bool
        self.is_seller_pay_postfee = is_seller_pay_postfee  # type: bool
        self.item_id = item_id  # type: long
        self.item_images = item_images  # type: list[str]
        self.item_title = item_title  # type: str
        self.item_total_simple_value = item_total_simple_value  # type: str
        self.item_total_value = item_total_value  # type: int
        self.lm_item_attribute_map = lm_item_attribute_map  # type: dict[str, str]
        self.lm_item_category = lm_item_category  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.main_pic_url = main_pic_url  # type: str
        self.min_price = min_price  # type: long
        self.properties = properties  # type: dict[str, list[str]]
        self.prov = prov  # type: str
        self.quantity = quantity  # type: int
        self.reserved_price = reserved_price  # type: long
        self.secured_transactions = secured_transactions  # type: int
        self.simple_quantity = simple_quantity  # type: str
        self.sku_models = sku_models  # type: list[ListDistributionItemWithoutCacheResponseBodyModelSkuModels]
        self.sku_propertys = sku_propertys  # type: list[ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys]
        self.third_party_item_id = third_party_item_id  # type: str
        self.third_party_name = third_party_name  # type: str
        self.user_type = user_type  # type: int
        self.video_pic_url = video_pic_url  # type: str
        self.video_url = video_url  # type: str
        self.virtual_item_type = virtual_item_type  # type: str

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_not_be_sold_code is not None:
            result['IsCanNotBeSoldCode'] = self.is_can_not_be_sold_code
        if self.is_can_not_be_sold_message is not None:
            result['IsCanNotBeSoldMessage'] = self.is_can_not_be_sold_message
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.secured_transactions is not None:
            result['SecuredTransactions'] = self.secured_transactions
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanNotBeSoldCode') is not None:
            self.is_can_not_be_sold_code = m.get('IsCanNotBeSoldCode')
        if m.get('IsCanNotBeSoldMessage') is not None:
            self.is_can_not_be_sold_message = m.get('IsCanNotBeSoldMessage')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SecuredTransactions') is not None:
            self.secured_transactions = m.get('SecuredTransactions')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class ListDistributionItemWithoutCacheResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[ListDistributionItemWithoutCacheResponseBodyModel]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionItemWithoutCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDistributionItemWithoutCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDistributionItemWithoutCacheResponse, self).to_map()
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
            temp_model = ListDistributionItemWithoutCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionMallRequest(TeaModel):
    def __init__(self, channel_supplier_id=None, distribution_mall_id=None, distribution_mall_name=None,
                 distributor_id=None, end_date=None, page_number=None, page_size=None, start_date=None, tenant_id=None):
        self.channel_supplier_id = channel_supplier_id  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_mall_name = distribution_mall_name  # type: str
        self.distributor_id = distributor_id  # type: str
        self.end_date = end_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionMallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionMallResponseBodyModel(TeaModel):
    def __init__(self, channel_supplier_id=None, distribution_mall_id=None, distribution_mall_name=None,
                 distribution_mall_type=None, end_date=None, start_date=None, status=None):
        self.channel_supplier_id = channel_supplier_id  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_mall_name = distribution_mall_name  # type: str
        self.distribution_mall_type = distribution_mall_type  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDistributionMallResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distribution_mall_type is not None:
            result['DistributionMallType'] = self.distribution_mall_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributionMallType') is not None:
            self.distribution_mall_type = m.get('DistributionMallType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDistributionMallResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[ListDistributionMallResponseBodyModel]
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDistributionMallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionMallResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionMallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDistributionMallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDistributionMallResponse, self).to_map()
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
            temp_model = ListDistributionMallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRefund4DistributionRequestLeavePictureLists(TeaModel):
    def __init__(self, desc=None, picture=None):
        self.desc = desc  # type: str
        self.picture = picture  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRefund4DistributionRequestLeavePictureLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.picture is not None:
            result['Picture'] = self.picture
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Picture') is not None:
            self.picture = m.get('Picture')
        return self


class ModifyRefund4DistributionRequest(TeaModel):
    def __init__(self, apply_reason_text_id=None, apply_refund_count=None, apply_refund_fee=None,
                 biz_claim_type=None, dispute_id=None, distributor_id=None, goods_status=None, leave_message=None,
                 leave_picture_lists=None, sub_distribution_order_id=None, tenant_id=None):
        self.apply_reason_text_id = apply_reason_text_id  # type: long
        self.apply_refund_count = apply_refund_count  # type: int
        self.apply_refund_fee = apply_refund_fee  # type: long
        self.biz_claim_type = biz_claim_type  # type: int
        self.dispute_id = dispute_id  # type: long
        self.distributor_id = distributor_id  # type: str
        self.goods_status = goods_status  # type: int
        self.leave_message = leave_message  # type: str
        self.leave_picture_lists = leave_picture_lists  # type: list[ModifyRefund4DistributionRequestLeavePictureLists]
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        if self.leave_picture_lists:
            for k in self.leave_picture_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyRefund4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        result['LeavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k in self.leave_picture_lists:
                result['LeavePictureLists'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        self.leave_picture_lists = []
        if m.get('LeavePictureLists') is not None:
            for k in m.get('LeavePictureLists'):
                temp_model = ModifyRefund4DistributionRequestLeavePictureLists()
                self.leave_picture_lists.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyRefund4DistributionShrinkRequest(TeaModel):
    def __init__(self, apply_reason_text_id=None, apply_refund_count=None, apply_refund_fee=None,
                 biz_claim_type=None, dispute_id=None, distributor_id=None, goods_status=None, leave_message=None,
                 leave_picture_lists_shrink=None, sub_distribution_order_id=None, tenant_id=None):
        self.apply_reason_text_id = apply_reason_text_id  # type: long
        self.apply_refund_count = apply_refund_count  # type: int
        self.apply_refund_fee = apply_refund_fee  # type: long
        self.biz_claim_type = biz_claim_type  # type: int
        self.dispute_id = dispute_id  # type: long
        self.distributor_id = distributor_id  # type: str
        self.goods_status = goods_status  # type: int
        self.leave_message = leave_message  # type: str
        self.leave_picture_lists_shrink = leave_picture_lists_shrink  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRefund4DistributionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        if self.leave_picture_lists_shrink is not None:
            result['LeavePictureLists'] = self.leave_picture_lists_shrink
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        if m.get('LeavePictureLists') is not None:
            self.leave_picture_lists_shrink = m.get('LeavePictureLists')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(self, dispute_id=None, dispute_status=None, dispute_type=None, sub_distribution_order_id=None):
        self.dispute_id = dispute_id  # type: long
        self.dispute_status = dispute_status  # type: int
        self.dispute_type = dispute_type  # type: int
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRefund4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class ModifyRefund4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: ModifyRefund4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ModifyRefund4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ModifyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ModifyRefund4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyRefund4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRefund4DistributionResponse, self).to_map()
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
            temp_model = ModifyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChildDivisionCodeByIdRequest(TeaModel):
    def __init__(self, distributor_id=None, division_code=None, tenant_id=None):
        self.distributor_id = distributor_id  # type: str
        self.division_code = division_code  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChildDivisionCodeByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryChildDivisionCodeByIdResponseBodyModelDivisionList(TeaModel):
    def __init__(self, division_code=None, division_level=None, division_name=None, parent_id=None, pinyin=None):
        self.division_code = division_code  # type: long
        self.division_level = division_level  # type: long
        self.division_name = division_name  # type: str
        self.parent_id = parent_id  # type: long
        self.pinyin = pinyin  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChildDivisionCodeByIdResponseBodyModelDivisionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level
        if self.division_name is not None:
            result['DivisionName'] = self.division_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')
        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        return self


class QueryChildDivisionCodeByIdResponseBodyModel(TeaModel):
    def __init__(self, division_list=None):
        self.division_list = division_list  # type: list[QueryChildDivisionCodeByIdResponseBodyModelDivisionList]

    def validate(self):
        if self.division_list:
            for k in self.division_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryChildDivisionCodeByIdResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DivisionList'] = []
        if self.division_list is not None:
            for k in self.division_list:
                result['DivisionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.division_list = []
        if m.get('DivisionList') is not None:
            for k in m.get('DivisionList'):
                temp_model = QueryChildDivisionCodeByIdResponseBodyModelDivisionList()
                self.division_list.append(temp_model.from_map(k))
        return self


class QueryChildDivisionCodeByIdResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryChildDivisionCodeByIdResponseBodyModel
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryChildDivisionCodeByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryChildDivisionCodeByIdResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryChildDivisionCodeByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryChildDivisionCodeByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChildDivisionCodeByIdResponse, self).to_map()
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
            temp_model = QueryChildDivisionCodeByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionBillDetailRequest(TeaModel):
    def __init__(self, bill_id=None, bill_period=None, bill_status=None, distribution_mall_id=None,
                 distribution_mall_name=None, distributor_id=None, page_number=None, page_size=None, tenant_id=None):
        self.bill_id = bill_id  # type: str
        self.bill_period = bill_period  # type: str
        self.bill_status = bill_status  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_mall_name = distribution_mall_name  # type: str
        self.distributor_id = distributor_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionBillDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.bill_period is not None:
            result['BillPeriod'] = self.bill_period
        if self.bill_status is not None:
            result['BillStatus'] = self.bill_status
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BillPeriod') is not None:
            self.bill_period = m.get('BillPeriod')
        if m.get('BillStatus') is not None:
            self.bill_status = m.get('BillStatus')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionBillDetailResponseBodyModel(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, total=None):
        self.data = data  # type: list[str]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionBillDetailResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryDistributionBillDetailResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, request_id=None, sub_code=None,
                 sub_message=None, success=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryDistributionBillDetailResponseBodyModel
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryDistributionBillDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryDistributionBillDetailResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDistributionBillDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDistributionBillDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDistributionBillDetailResponse, self).to_map()
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
            temp_model = QueryDistributionBillDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionMallRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionMallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionMallResponseBodyModel(TeaModel):
    def __init__(self, channel_supplier_id=None, distribution_mall_id=None, distribution_mall_name=None,
                 distribution_mall_type=None, distributor_id=None, end_date=None, start_date=None, status=None):
        self.channel_supplier_id = channel_supplier_id  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_mall_name = distribution_mall_name  # type: str
        self.distribution_mall_type = distribution_mall_type  # type: str
        self.distributor_id = distributor_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionMallResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distribution_mall_type is not None:
            result['DistributionMallType'] = self.distribution_mall_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributionMallType') is not None:
            self.distribution_mall_type = m.get('DistributionMallType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDistributionMallResponseBody(TeaModel):
    def __init__(self, biz_view_data=None, code=None, logs_id=None, message=None, model=None, page_number=None,
                 page_size=None, request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.biz_view_data = biz_view_data  # type: dict[str, any]
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryDistributionMallResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryDistributionMallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_view_data is not None:
            result['BizViewData'] = self.biz_view_data
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizViewData') is not None:
            self.biz_view_data = m.get('BizViewData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryDistributionMallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDistributionMallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDistributionMallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDistributionMallResponse, self).to_map()
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
            temp_model = QueryDistributionMallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionTradeStatusRequest(TeaModel):
    def __init__(self, distribution_supplier_id=None, distribution_trade_id=None, distributor_id=None,
                 tenant_id=None):
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distribution_trade_id = distribution_trade_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionTradeStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionTradeStatusResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: str
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDistributionTradeStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDistributionTradeStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDistributionTradeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDistributionTradeStatusResponse, self).to_map()
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
            temp_model = QueryDistributionTradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, lm_item_id=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemDetailResponseBodyModelSkuModels(TeaModel):
    def __init__(self, can_not_be_sold_code=None, can_not_be_sold_message=None, customized_attribute_map=None,
                 distribution_mall_id=None, ext_json=None, has_quantity=None, invoice_type=None, item_id=None, lm_item_id=None,
                 lm_sku_attribute_map=None, price_cent=None, quantity=None, reserved_price=None, simple_quantity=None, sku_id=None,
                 sku_pic_url=None, sku_pvs=None, sku_title=None, status=None):
        self.can_not_be_sold_code = can_not_be_sold_code  # type: str
        self.can_not_be_sold_message = can_not_be_sold_message  # type: str
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.ext_json = ext_json  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.invoice_type = invoice_type  # type: int
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_sku_attribute_map = lm_sku_attribute_map  # type: dict[str, str]
        self.price_cent = price_cent  # type: long
        self.quantity = quantity  # type: int
        self.reserved_price = reserved_price  # type: long
        self.simple_quantity = simple_quantity  # type: str
        self.sku_id = sku_id  # type: long
        self.sku_pic_url = sku_pic_url  # type: str
        self.sku_pvs = sku_pvs  # type: str
        self.sku_title = sku_title  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailResponseBodyModelSkuModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_message is not None:
            result['CanNotBeSoldMessage'] = self.can_not_be_sold_message
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMessage') is not None:
            self.can_not_be_sold_message = m.get('CanNotBeSoldMessage')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryItemDetailResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(self, id=None, text=None):
        self.id = id  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailResponseBodyModelSkuPropertysValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QueryItemDetailResponseBodyModelSkuPropertys(TeaModel):
    def __init__(self, id=None, text=None, values=None):
        self.id = id  # type: long
        self.text = text  # type: str
        self.values = values  # type: list[QueryItemDetailResponseBodyModelSkuPropertysValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemDetailResponseBodyModelSkuPropertys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryItemDetailResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryItemDetailResponseBodyModel(TeaModel):
    def __init__(self, can_not_be_sold_code=None, can_not_be_sold_message=None, category_id=None,
                 category_ids=None, city=None, current=None, customized_attribute_map=None, desc_option=None, desc_path=None,
                 distribution_mall_id=None, features=None, first_pic_url=None, has_quantity=None, iforest_props=None, invoice_type=None,
                 is_can_sell=None, is_seller_pay_postfee=None, item_id=None, item_images=None, item_title=None,
                 item_total_simple_value=None, item_total_value=None, lm_item_attribute_map=None, lm_item_category=None, lm_item_id=None,
                 main_pic_url=None, min_price=None, properties=None, prov=None, quantity=None, reserved_price=None,
                 simple_quantity=None, sku_models=None, sku_propertys=None, third_party_item_id=None, third_party_name=None,
                 video_pic_url=None, video_url=None, virtual_item_type=None):
        self.can_not_be_sold_code = can_not_be_sold_code  # type: str
        self.can_not_be_sold_message = can_not_be_sold_message  # type: str
        self.category_id = category_id  # type: long
        self.category_ids = category_ids  # type: list[long]
        self.city = city  # type: str
        self.current = current  # type: str
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.desc_option = desc_option  # type: str
        self.desc_path = desc_path  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.features = features  # type: dict[str, str]
        self.first_pic_url = first_pic_url  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.iforest_props = iforest_props  # type: list[dict[str, str]]
        self.invoice_type = invoice_type  # type: int
        self.is_can_sell = is_can_sell  # type: bool
        self.is_seller_pay_postfee = is_seller_pay_postfee  # type: bool
        self.item_id = item_id  # type: long
        self.item_images = item_images  # type: list[str]
        self.item_title = item_title  # type: str
        self.item_total_simple_value = item_total_simple_value  # type: str
        self.item_total_value = item_total_value  # type: int
        self.lm_item_attribute_map = lm_item_attribute_map  # type: dict[str, str]
        self.lm_item_category = lm_item_category  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.main_pic_url = main_pic_url  # type: str
        self.min_price = min_price  # type: long
        self.properties = properties  # type: dict[str, list[str]]
        self.prov = prov  # type: str
        self.quantity = quantity  # type: int
        self.reserved_price = reserved_price  # type: long
        self.simple_quantity = simple_quantity  # type: str
        # sku list
        self.sku_models = sku_models  # type: list[QueryItemDetailResponseBodyModelSkuModels]
        self.sku_propertys = sku_propertys  # type: list[QueryItemDetailResponseBodyModelSkuPropertys]
        self.third_party_item_id = third_party_item_id  # type: str
        self.third_party_name = third_party_name  # type: str
        self.video_pic_url = video_pic_url  # type: str
        self.video_url = video_url  # type: str
        self.virtual_item_type = virtual_item_type  # type: str

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemDetailResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_message is not None:
            result['CanNotBeSoldMessage'] = self.can_not_be_sold_message
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMessage') is not None:
            self.can_not_be_sold_message = m.get('CanNotBeSoldMessage')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemDetailResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = QueryItemDetailResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class QueryItemDetailResponseBody(TeaModel):
    def __init__(self, biz_view_data=None, code=None, logs_id=None, message=None, model=None, page_number=None,
                 page_size=None, request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.biz_view_data = biz_view_data  # type: dict[str, any]
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryItemDetailResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryItemDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_view_data is not None:
            result['BizViewData'] = self.biz_view_data
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizViewData') is not None:
            self.biz_view_data = m.get('BizViewData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryItemDetailResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryItemDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryItemDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryItemDetailResponse, self).to_map()
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
            temp_model = QueryItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailWithDivisionRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, division_code=None, lm_item_id=None,
                 tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.division_code = division_code  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuModels(TeaModel):
    def __init__(self, can_not_be_sold_code=None, can_not_be_sold_massage=None, customized_attribute_map=None,
                 distribution_mall_id=None, ext_json=None, has_quantity=None, invoice_type=None, item_id=None, lm_item_id=None,
                 lm_sku_attribute_map=None, price_cent=None, quantity=None, reserve_price=None, simple_quantity=None, sku_id=None,
                 sku_pic_url=None, sku_pvs=None, sku_title=None, status=None, supplier_price=None):
        self.can_not_be_sold_code = can_not_be_sold_code  # type: str
        self.can_not_be_sold_massage = can_not_be_sold_massage  # type: str
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.ext_json = ext_json  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.invoice_type = invoice_type  # type: int
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_sku_attribute_map = lm_sku_attribute_map  # type: dict[str, str]
        self.price_cent = price_cent  # type: long
        self.quantity = quantity  # type: int
        self.reserve_price = reserve_price  # type: long
        self.simple_quantity = simple_quantity  # type: str
        self.sku_id = sku_id  # type: long
        self.sku_pic_url = sku_pic_url  # type: str
        self.sku_pvs = sku_pvs  # type: str
        self.sku_title = sku_title  # type: str
        self.status = status  # type: int
        self.supplier_price = supplier_price  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponseBodyModelSkuModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_massage is not None:
            result['CanNotBeSoldMassage'] = self.can_not_be_sold_massage
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_price is not None:
            result['SupplierPrice'] = self.supplier_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMassage') is not None:
            self.can_not_be_sold_massage = m.get('CanNotBeSoldMassage')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPrice') is not None:
            self.supplier_price = m.get('SupplierPrice')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(self, id=None, text=None):
        self.id = id  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuPropertys(TeaModel):
    def __init__(self, id=None, text=None, values=None):
        self.id = id  # type: long
        self.text = text  # type: str
        self.values = values  # type: list[QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponseBodyModelSkuPropertys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryItemDetailWithDivisionResponseBodyModel(TeaModel):
    def __init__(self, can_not_be_sold_code=None, can_not_be_sold_massage=None, can_sell=None, category_id=None,
                 category_ids=None, city=None, current=None, customized_attribute_map=None, desc_option=None, desc_path=None,
                 distribution_mall_id=None, features=None, first_pic_url=None, has_quantity=None, iforest_props=None, invoice_type=None,
                 item_id=None, item_images=None, item_title=None, item_total_simple_value=None, item_total_value=None,
                 lm_item_attribute_map=None, lm_item_category=None, lm_item_id=None, main_pic_url=None, min_price=None, properties=None,
                 prov=None, quantity=None, reserve_price=None, secured_transactions=None, seller_pay_postfee=None,
                 simple_quantity=None, sku_models=None, sku_propertys=None, third_party_item_id=None, third_party_name=None,
                 user_type=None, video_pic_url=None, video_url=None, virtual_item_type=None):
        self.can_not_be_sold_code = can_not_be_sold_code  # type: str
        self.can_not_be_sold_massage = can_not_be_sold_massage  # type: str
        self.can_sell = can_sell  # type: bool
        self.category_id = category_id  # type: long
        self.category_ids = category_ids  # type: list[long]
        self.city = city  # type: str
        self.current = current  # type: str
        self.customized_attribute_map = customized_attribute_map  # type: dict[str, str]
        self.desc_option = desc_option  # type: str
        self.desc_path = desc_path  # type: str
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.features = features  # type: dict[str, str]
        self.first_pic_url = first_pic_url  # type: str
        self.has_quantity = has_quantity  # type: bool
        self.iforest_props = iforest_props  # type: list[dict[str, str]]
        self.invoice_type = invoice_type  # type: int
        self.item_id = item_id  # type: long
        self.item_images = item_images  # type: list[str]
        self.item_title = item_title  # type: str
        self.item_total_simple_value = item_total_simple_value  # type: str
        self.item_total_value = item_total_value  # type: int
        self.lm_item_attribute_map = lm_item_attribute_map  # type: dict[str, str]
        self.lm_item_category = lm_item_category  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.main_pic_url = main_pic_url  # type: str
        self.min_price = min_price  # type: long
        self.properties = properties  # type: dict[str, list[str]]
        self.prov = prov  # type: str
        self.quantity = quantity  # type: int
        self.reserve_price = reserve_price  # type: long
        self.secured_transactions = secured_transactions  # type: int
        self.seller_pay_postfee = seller_pay_postfee  # type: bool
        self.simple_quantity = simple_quantity  # type: str
        # sku list
        self.sku_models = sku_models  # type: list[QueryItemDetailWithDivisionResponseBodyModelSkuModels]
        self.sku_propertys = sku_propertys  # type: list[QueryItemDetailWithDivisionResponseBodyModelSkuPropertys]
        self.third_party_item_id = third_party_item_id  # type: str
        self.third_party_name = third_party_name  # type: str
        self.user_type = user_type  # type: int
        self.video_pic_url = video_pic_url  # type: str
        self.video_url = video_url  # type: str
        self.virtual_item_type = virtual_item_type  # type: str

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_massage is not None:
            result['CanNotBeSoldMassage'] = self.can_not_be_sold_massage
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.secured_transactions is not None:
            result['SecuredTransactions'] = self.secured_transactions
        if self.seller_pay_postfee is not None:
            result['SellerPayPostfee'] = self.seller_pay_postfee
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMassage') is not None:
            self.can_not_be_sold_massage = m.get('CanNotBeSoldMassage')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SecuredTransactions') is not None:
            self.secured_transactions = m.get('SecuredTransactions')
        if m.get('SellerPayPostfee') is not None:
            self.seller_pay_postfee = m.get('SellerPayPostfee')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class QueryItemDetailWithDivisionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryItemDetailWithDivisionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryItemDetailWithDivisionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryItemDetailWithDivisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryItemDetailWithDivisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryItemDetailWithDivisionResponse, self).to_map()
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
            temp_model = QueryItemDetailWithDivisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemGuideRetailPriceRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, lm_item_ids=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.lm_item_ids = lm_item_ids  # type: list[str]
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemGuideRetailPriceShrinkRequest(TeaModel):
    def __init__(self, distribution_mall_id=None, distributor_id=None, lm_item_ids_shrink=None, tenant_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.lm_item_ids_shrink = lm_item_ids_shrink  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemGuideRetailPriceResponseBodyModelSkuModels(TeaModel):
    def __init__(self, distribution_mall_id=None, guide_retail_price=None, item_id=None, lm_item_id=None,
                 low_guide_retail_price=None, price_cent=None, reserved_price=None, sku_id=None, sku_title=None, status=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.guide_retail_price = guide_retail_price  # type: long
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.low_guide_retail_price = low_guide_retail_price  # type: long
        self.price_cent = price_cent  # type: long
        self.reserved_price = reserved_price  # type: long
        self.sku_id = sku_id  # type: long
        self.sku_title = sku_title  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceResponseBodyModelSkuModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.guide_retail_price is not None:
            result['GuideRetailPrice'] = self.guide_retail_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.low_guide_retail_price is not None:
            result['LowGuideRetailPrice'] = self.low_guide_retail_price
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GuideRetailPrice') is not None:
            self.guide_retail_price = m.get('GuideRetailPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LowGuideRetailPrice') is not None:
            self.low_guide_retail_price = m.get('LowGuideRetailPrice')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryItemGuideRetailPriceResponseBodyModel(TeaModel):
    def __init__(self, distribution_mall_id=None, guide_retail_price_scope=None, item_id=None, item_title=None,
                 lm_item_id=None, low_guide_retail_price_scope=None, reserved_price=None, reserved_price_scope=None,
                 sku_models=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.guide_retail_price_scope = guide_retail_price_scope  # type: str
        self.item_id = item_id  # type: long
        self.item_title = item_title  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.low_guide_retail_price_scope = low_guide_retail_price_scope  # type: str
        self.reserved_price = reserved_price  # type: long
        self.reserved_price_scope = reserved_price_scope  # type: str
        self.sku_models = sku_models  # type: list[QueryItemGuideRetailPriceResponseBodyModelSkuModels]

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.guide_retail_price_scope is not None:
            result['GuideRetailPriceScope'] = self.guide_retail_price_scope
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.low_guide_retail_price_scope is not None:
            result['LowGuideRetailPriceScope'] = self.low_guide_retail_price_scope
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.reserved_price_scope is not None:
            result['ReservedPriceScope'] = self.reserved_price_scope
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GuideRetailPriceScope') is not None:
            self.guide_retail_price_scope = m.get('GuideRetailPriceScope')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LowGuideRetailPriceScope') is not None:
            self.low_guide_retail_price_scope = m.get('LowGuideRetailPriceScope')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('ReservedPriceScope') is not None:
            self.reserved_price_scope = m.get('ReservedPriceScope')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemGuideRetailPriceResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        return self


class QueryItemGuideRetailPriceResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, request_id=None, sub_code=None,
                 sub_message=None, success=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[QueryItemGuideRetailPriceResponseBodyModel]
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryItemGuideRetailPriceResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryItemGuideRetailPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryItemGuideRetailPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryItemGuideRetailPriceResponse, self).to_map()
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
            temp_model = QueryItemGuideRetailPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLogistics4DistributionRequest(TeaModel):
    def __init__(self, distributor_id=None, main_distribution_order_id=None, request_id=None, tenant_id=None):
        self.distributor_id = distributor_id  # type: str
        self.main_distribution_order_id = main_distribution_order_id  # type: str
        self.request_id = request_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLogistics4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryLogistics4DistributionResponseBodyModelGoods(TeaModel):
    def __init__(self, good_name=None, item_id=None, quantity=None, sku_id=None):
        self.good_name = good_name  # type: str
        self.item_id = item_id  # type: str
        self.quantity = quantity  # type: int
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLogistics4DistributionResponseBodyModelGoods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.good_name is not None:
            result['GoodName'] = self.good_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GoodName') is not None:
            self.good_name = m.get('GoodName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class QueryLogistics4DistributionResponseBodyModelLogisticsDetailList(TeaModel):
    def __init__(self, ocurr_time_str=None, standerd_desc=None):
        self.ocurr_time_str = ocurr_time_str  # type: str
        self.standerd_desc = standerd_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLogistics4DistributionResponseBodyModelLogisticsDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocurr_time_str is not None:
            result['OcurrTimeStr'] = self.ocurr_time_str
        if self.standerd_desc is not None:
            result['StanderdDesc'] = self.standerd_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OcurrTimeStr') is not None:
            self.ocurr_time_str = m.get('OcurrTimeStr')
        if m.get('StanderdDesc') is not None:
            self.standerd_desc = m.get('StanderdDesc')
        return self


class QueryLogistics4DistributionResponseBodyModel(TeaModel):
    def __init__(self, data_provider=None, data_provider_title=None, goods=None, logistics_company_code=None,
                 logistics_company_name=None, logistics_detail_list=None, mail_no=None):
        self.data_provider = data_provider  # type: str
        self.data_provider_title = data_provider_title  # type: str
        self.goods = goods  # type: list[QueryLogistics4DistributionResponseBodyModelGoods]
        self.logistics_company_code = logistics_company_code  # type: str
        self.logistics_company_name = logistics_company_name  # type: str
        self.logistics_detail_list = logistics_detail_list  # type: list[QueryLogistics4DistributionResponseBodyModelLogisticsDetailList]
        self.mail_no = mail_no  # type: str

    def validate(self):
        if self.goods:
            for k in self.goods:
                if k:
                    k.validate()
        if self.logistics_detail_list:
            for k in self.logistics_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryLogistics4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_provider is not None:
            result['DataProvider'] = self.data_provider
        if self.data_provider_title is not None:
            result['DataProviderTitle'] = self.data_provider_title
        result['Goods'] = []
        if self.goods is not None:
            for k in self.goods:
                result['Goods'].append(k.to_map() if k else None)
        if self.logistics_company_code is not None:
            result['LogisticsCompanyCode'] = self.logistics_company_code
        if self.logistics_company_name is not None:
            result['LogisticsCompanyName'] = self.logistics_company_name
        result['LogisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k in self.logistics_detail_list:
                result['LogisticsDetailList'].append(k.to_map() if k else None)
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataProvider') is not None:
            self.data_provider = m.get('DataProvider')
        if m.get('DataProviderTitle') is not None:
            self.data_provider_title = m.get('DataProviderTitle')
        self.goods = []
        if m.get('Goods') is not None:
            for k in m.get('Goods'):
                temp_model = QueryLogistics4DistributionResponseBodyModelGoods()
                self.goods.append(temp_model.from_map(k))
        if m.get('LogisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('LogisticsCompanyCode')
        if m.get('LogisticsCompanyName') is not None:
            self.logistics_company_name = m.get('LogisticsCompanyName')
        self.logistics_detail_list = []
        if m.get('LogisticsDetailList') is not None:
            for k in m.get('LogisticsDetailList'):
                temp_model = QueryLogistics4DistributionResponseBodyModelLogisticsDetailList()
                self.logistics_detail_list.append(temp_model.from_map(k))
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        return self


class QueryLogistics4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[QueryLogistics4DistributionResponseBodyModel]
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryLogistics4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryLogistics4DistributionResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryLogistics4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLogistics4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLogistics4DistributionResponse, self).to_map()
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
            temp_model = QueryLogistics4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMallCategoryListRequest(TeaModel):
    def __init__(self, category_id=None, distribution_mall_id=None, distributor_id=None, tenant_id=None):
        self.category_id = category_id  # type: long
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMallCategoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryMallCategoryListResponseBodyModel(TeaModel):
    def __init__(self, category_id=None, leaf=None, name=None, parent_id=None):
        self.category_id = category_id  # type: long
        self.leaf = leaf  # type: bool
        self.name = name  # type: str
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMallCategoryListResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class QueryMallCategoryListResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, request_id=None, sub_code=None,
                 sub_message=None, success=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[QueryMallCategoryListResponseBodyModel]
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMallCategoryListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryMallCategoryListResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMallCategoryListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMallCategoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMallCategoryListResponse, self).to_map()
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
            temp_model = QueryMallCategoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderDetail4DistributionRequest(TeaModel):
    def __init__(self, distributor_id=None, main_distribution_order_id=None, tenant_id=None):
        self.distributor_id = distributor_id  # type: str
        self.main_distribution_order_id = main_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice(TeaModel):
    def __init__(self, fund_amount_money=None):
        self.fund_amount_money = fund_amount_money  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderDetail4DistributionResponseBodyModelSubOrderList(TeaModel):
    def __init__(self, item_id=None, item_pic=None, item_price=None, item_title=None, logistics_status=None,
                 main_distribution_order_id=None, number=None, order_status=None, sku_id=None, sku_name=None, sub_distribution_order_id=None):
        self.item_id = item_id  # type: str
        self.item_pic = item_pic  # type: str
        self.item_price = item_price  # type: list[QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice]
        self.item_title = item_title  # type: str
        self.logistics_status = logistics_status  # type: str
        self.main_distribution_order_id = main_distribution_order_id  # type: str
        self.number = number  # type: str
        self.order_status = order_status  # type: str
        self.sku_id = sku_id  # type: str
        self.sku_name = sku_name  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        if self.item_price:
            for k in self.item_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionResponseBodyModelSubOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        result['ItemPrice'] = []
        if self.item_price is not None:
            for k in self.item_price:
                result['ItemPrice'].append(k.to_map() if k else None)
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.number is not None:
            result['Number'] = self.number
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        self.item_price = []
        if m.get('ItemPrice') is not None:
            for k in m.get('ItemPrice'):
                temp_model = QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice()
                self.item_price.append(temp_model.from_map(k))
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryOrderDetail4DistributionResponseBodyModel(TeaModel):
    def __init__(self, create_date=None, distribution_order_id=None, distributor_id=None, logistics_status=None,
                 order_amount=None, order_status=None, sub_order_list=None):
        self.create_date = create_date  # type: str
        self.distribution_order_id = distribution_order_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.logistics_status = logistics_status  # type: str
        self.order_amount = order_amount  # type: str
        self.order_status = order_status  # type: str
        self.sub_order_list = sub_order_list  # type: list[QueryOrderDetail4DistributionResponseBodyModelSubOrderList]

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderDetail4DistributionResponseBodyModelSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderDetail4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryOrderDetail4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryOrderDetail4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryOrderDetail4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOrderDetail4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrderDetail4DistributionResponse, self).to_map()
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
            temp_model = QueryOrderDetail4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderList4DistributionRequest(TeaModel):
    def __init__(self, distributor_id=None, filter_option=None, page_number=None, page_size=None, tenant_id=None):
        self.distributor_id = distributor_id  # type: str
        self.filter_option = filter_option  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderList4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.filter_option is not None:
            result['FilterOption'] = self.filter_option
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('FilterOption') is not None:
            self.filter_option = m.get('FilterOption')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice(TeaModel):
    def __init__(self, fund_amount_money=None):
        self.fund_amount_money = fund_amount_money  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderList4DistributionResponseBodyModelSubOrderList(TeaModel):
    def __init__(self, item_id=None, item_pic=None, item_price=None, item_title=None, logistics_status=None,
                 main_distribution_order_id=None, number=None, order_status=None, sku_id=None, sku_name=None, sub_distribution_order_id=None):
        self.item_id = item_id  # type: str
        self.item_pic = item_pic  # type: str
        self.item_price = item_price  # type: list[QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice]
        self.item_title = item_title  # type: str
        self.logistics_status = logistics_status  # type: str
        self.main_distribution_order_id = main_distribution_order_id  # type: str
        self.number = number  # type: str
        self.order_status = order_status  # type: str
        self.sku_id = sku_id  # type: str
        self.sku_name = sku_name  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        if self.item_price:
            for k in self.item_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderList4DistributionResponseBodyModelSubOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        result['ItemPrice'] = []
        if self.item_price is not None:
            for k in self.item_price:
                result['ItemPrice'].append(k.to_map() if k else None)
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.number is not None:
            result['Number'] = self.number
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        self.item_price = []
        if m.get('ItemPrice') is not None:
            for k in m.get('ItemPrice'):
                temp_model = QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice()
                self.item_price.append(temp_model.from_map(k))
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryOrderList4DistributionResponseBodyModel(TeaModel):
    def __init__(self, create_date=None, distribution_order_id=None, distributor_id=None, logistics_status=None,
                 order_amount=None, order_status=None, sub_order_list=None):
        self.create_date = create_date  # type: str
        self.distribution_order_id = distribution_order_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.logistics_status = logistics_status  # type: str
        self.order_amount = order_amount  # type: str
        self.order_status = order_status  # type: str
        self.sub_order_list = sub_order_list  # type: list[QueryOrderList4DistributionResponseBodyModelSubOrderList]

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderList4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderList4DistributionResponseBodyModelSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderList4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: list[QueryOrderList4DistributionResponseBodyModel]
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderList4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryOrderList4DistributionResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryOrderList4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOrderList4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrderList4DistributionResponse, self).to_map()
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
            temp_model = QueryOrderList4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRefundApplicationDetail4DistributionRequest(TeaModel):
    def __init__(self, distributor_id=None, sub_distribution_order_id=None, tenant_id=None):
        self.distributor_id = distributor_id  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason(TeaModel):
    def __init__(self, reason_text_id=None, reason_tips=None):
        self.reason_text_id = reason_text_id  # type: long
        self.reason_tips = reason_tips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData(TeaModel):
    def __init__(self, max_refund_fee=None, min_refund_fee=None):
        self.max_refund_fee = max_refund_fee  # type: long
        self.min_refund_fee = min_refund_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModel(TeaModel):
    def __init__(self, apply_dispute_desc=None, apply_reason=None, biz_claim_type=None, dispute_create_time=None,
                 dispute_desc=None, dispute_end_time=None, dispute_id=None, dispute_status=None, dispute_type=None,
                 distribution_order_id=None, order_logistics_status=None, real_refund_fee=None, refund_fee=None, refund_fee_data=None,
                 refunder_address=None, refunder_name=None, refunder_tel=None, refunder_zip_code=None, return_good_count=None,
                 return_good_logistics_status=None, seller_agree_msg=None, seller_refuse_agreement_message=None, seller_refuse_reason=None,
                 sub_distribution_order_id=None):
        self.apply_dispute_desc = apply_dispute_desc  # type: str
        self.apply_reason = apply_reason  # type: QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason
        self.biz_claim_type = biz_claim_type  # type: int
        self.dispute_create_time = dispute_create_time  # type: str
        self.dispute_desc = dispute_desc  # type: str
        self.dispute_end_time = dispute_end_time  # type: str
        self.dispute_id = dispute_id  # type: long
        self.dispute_status = dispute_status  # type: int
        self.dispute_type = dispute_type  # type: int
        self.distribution_order_id = distribution_order_id  # type: str
        self.order_logistics_status = order_logistics_status  # type: int
        self.real_refund_fee = real_refund_fee  # type: long
        self.refund_fee = refund_fee  # type: long
        self.refund_fee_data = refund_fee_data  # type: QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData
        self.refunder_address = refunder_address  # type: str
        self.refunder_name = refunder_name  # type: str
        self.refunder_tel = refunder_tel  # type: str
        self.refunder_zip_code = refunder_zip_code  # type: str
        self.return_good_count = return_good_count  # type: long
        self.return_good_logistics_status = return_good_logistics_status  # type: int
        self.seller_agree_msg = seller_agree_msg  # type: str
        self.seller_refuse_agreement_message = seller_refuse_agreement_message  # type: str
        self.seller_refuse_reason = seller_refuse_reason  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str

    def validate(self):
        if self.apply_reason:
            self.apply_reason.validate()
        if self.refund_fee_data:
            self.refund_fee_data.validate()

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_dispute_desc is not None:
            result['ApplyDisputeDesc'] = self.apply_dispute_desc
        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason.to_map()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_create_time is not None:
            result['DisputeCreateTime'] = self.dispute_create_time
        if self.dispute_desc is not None:
            result['DisputeDesc'] = self.dispute_desc
        if self.dispute_end_time is not None:
            result['DisputeEndTime'] = self.dispute_end_time
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.order_logistics_status is not None:
            result['OrderLogisticsStatus'] = self.order_logistics_status
        if self.real_refund_fee is not None:
            result['RealRefundFee'] = self.real_refund_fee
        if self.refund_fee is not None:
            result['RefundFee'] = self.refund_fee
        if self.refund_fee_data is not None:
            result['RefundFeeData'] = self.refund_fee_data.to_map()
        if self.refunder_address is not None:
            result['RefunderAddress'] = self.refunder_address
        if self.refunder_name is not None:
            result['RefunderName'] = self.refunder_name
        if self.refunder_tel is not None:
            result['RefunderTel'] = self.refunder_tel
        if self.refunder_zip_code is not None:
            result['RefunderZipCode'] = self.refunder_zip_code
        if self.return_good_count is not None:
            result['ReturnGoodCount'] = self.return_good_count
        if self.return_good_logistics_status is not None:
            result['ReturnGoodLogisticsStatus'] = self.return_good_logistics_status
        if self.seller_agree_msg is not None:
            result['SellerAgreeMsg'] = self.seller_agree_msg
        if self.seller_refuse_agreement_message is not None:
            result['SellerRefuseAgreementMessage'] = self.seller_refuse_agreement_message
        if self.seller_refuse_reason is not None:
            result['SellerRefuseReason'] = self.seller_refuse_reason
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyDisputeDesc') is not None:
            self.apply_dispute_desc = m.get('ApplyDisputeDesc')
        if m.get('ApplyReason') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason()
            self.apply_reason = temp_model.from_map(m['ApplyReason'])
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeCreateTime') is not None:
            self.dispute_create_time = m.get('DisputeCreateTime')
        if m.get('DisputeDesc') is not None:
            self.dispute_desc = m.get('DisputeDesc')
        if m.get('DisputeEndTime') is not None:
            self.dispute_end_time = m.get('DisputeEndTime')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('OrderLogisticsStatus') is not None:
            self.order_logistics_status = m.get('OrderLogisticsStatus')
        if m.get('RealRefundFee') is not None:
            self.real_refund_fee = m.get('RealRefundFee')
        if m.get('RefundFee') is not None:
            self.refund_fee = m.get('RefundFee')
        if m.get('RefundFeeData') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData()
            self.refund_fee_data = temp_model.from_map(m['RefundFeeData'])
        if m.get('RefunderAddress') is not None:
            self.refunder_address = m.get('RefunderAddress')
        if m.get('RefunderName') is not None:
            self.refunder_name = m.get('RefunderName')
        if m.get('RefunderTel') is not None:
            self.refunder_tel = m.get('RefunderTel')
        if m.get('RefunderZipCode') is not None:
            self.refunder_zip_code = m.get('RefunderZipCode')
        if m.get('ReturnGoodCount') is not None:
            self.return_good_count = m.get('ReturnGoodCount')
        if m.get('ReturnGoodLogisticsStatus') is not None:
            self.return_good_logistics_status = m.get('ReturnGoodLogisticsStatus')
        if m.get('SellerAgreeMsg') is not None:
            self.seller_agree_msg = m.get('SellerAgreeMsg')
        if m.get('SellerRefuseAgreementMessage') is not None:
            self.seller_refuse_agreement_message = m.get('SellerRefuseAgreementMessage')
        if m.get('SellerRefuseReason') is not None:
            self.seller_refuse_reason = m.get('SellerRefuseReason')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryRefundApplicationDetail4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: QueryRefundApplicationDetail4DistributionResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRefundApplicationDetail4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRefundApplicationDetail4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRefundApplicationDetail4DistributionResponse, self).to_map()
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
            temp_model = QueryRefundApplicationDetail4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderDistributionOrderRequestItemInfoLists(TeaModel):
    def __init__(self, distribution_mall_id=None, lm_item_id=None, quantity=None, sku_id=None):
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.quantity = quantity  # type: int
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderRequestItemInfoLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class RenderDistributionOrderRequest(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, distribution_supplier_id=None, distributor_id=None,
                 ext_info=None, item_info_lists=None, tenant_id=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.ext_info = ext_info  # type: str
        self.item_info_lists = item_info_lists  # type: list[RenderDistributionOrderRequestItemInfoLists]
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        if self.item_info_lists:
            for k in self.item_info_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        result['ItemInfoLists'] = []
        if self.item_info_lists is not None:
            for k in self.item_info_lists:
                result['ItemInfoLists'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        self.item_info_lists = []
        if m.get('ItemInfoLists') is not None:
            for k in m.get('ItemInfoLists'):
                temp_model = RenderDistributionOrderRequestItemInfoLists()
                self.item_info_lists.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class RenderDistributionOrderShrinkRequest(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, distribution_supplier_id=None, distributor_id=None,
                 ext_info=None, item_info_lists_shrink=None, tenant_id=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.ext_info = ext_info  # type: str
        self.item_info_lists_shrink = item_info_lists_shrink  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.item_info_lists_shrink is not None:
            result['ItemInfoLists'] = self.item_info_lists_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ItemInfoLists') is not None:
            self.item_info_lists_shrink = m.get('ItemInfoLists')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class RenderDistributionOrderResponseBodyModelAddressInfos(TeaModel):
    def __init__(self, address_detail=None, address_id=None, division_code=None, is_default=None, receiver=None,
                 receiver_phone=None, town_division_code=None):
        self.address_detail = address_detail  # type: str
        self.address_id = address_id  # type: long
        self.division_code = division_code  # type: str
        self.is_default = is_default  # type: bool
        self.receiver = receiver  # type: str
        self.receiver_phone = receiver_phone  # type: str
        self.town_division_code = town_division_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelAddressInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.town_division_code is not None:
            result['TownDivisionCode'] = self.town_division_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('TownDivisionCode') is not None:
            self.town_division_code = m.get('TownDivisionCode')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos(TeaModel):
    def __init__(self, display_name=None, id=None, post_fee=None, service_type=None):
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.post_fee = post_fee  # type: long
        self.service_type = service_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo(TeaModel):
    def __init__(self, desc=None, type=None):
        self.desc = desc  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems(TeaModel):
    def __init__(self, item_id=None, lm_item_id=None, lm_shop_id=None, number=None, points=None, points_amount=None,
                 price_cent=None, removed=None, sku_id=None, tb_seller_id=None, user_pay_fee=None):
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_shop_id = lm_shop_id  # type: long
        self.number = number  # type: int
        self.points = points  # type: long
        self.points_amount = points_amount  # type: long
        self.price_cent = price_cent  # type: long
        self.removed = removed  # type: bool
        self.sku_id = sku_id  # type: long
        self.tb_seller_id = tb_seller_id  # type: long
        self.user_pay_fee = user_pay_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS(TeaModel):
    def __init__(self, available_items=None, can_use=None, discount_price=None, expire_time=None, instance_id=None,
                 level=None, lm_item_id=None, promotion_name=None, promotion_type=None, reason=None, selected=None,
                 sku_ids=None, special_price=None, sub_biz_code=None, tb_seller_id=None, threshold_price=None,
                 use_start_time=None):
        self.available_items = available_items  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems]
        self.can_use = can_use  # type: bool
        self.discount_price = discount_price  # type: long
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.promotion_type = promotion_type  # type: str
        self.reason = reason  # type: str
        self.selected = selected  # type: bool
        self.sku_ids = sku_ids  # type: list[long]
        self.special_price = special_price  # type: long
        self.sub_biz_code = sub_biz_code  # type: str
        self.tb_seller_id = tb_seller_id  # type: long
        self.threshold_price = threshold_price  # type: long
        self.use_start_time = use_start_time  # type: long

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos(TeaModel):
    def __init__(self, can_sell=None, distribution_mall_id=None, distribution_supplier_id=None,
                 distributor_id=None, features=None, item_id=None, item_name=None, item_pic_url=None, item_prom_inst_vos=None,
                 item_url=None, message=None, price=None, promotion_fee=None, quantity=None, reserve_price=None, sku_id=None,
                 sku_name=None, virtual_item_type=None):
        self.can_sell = can_sell  # type: bool
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.features = features  # type: dict[str, str]
        self.item_id = item_id  # type: str
        self.item_name = item_name  # type: str
        self.item_pic_url = item_pic_url  # type: str
        self.item_prom_inst_vos = item_prom_inst_vos  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS]
        self.item_url = item_url  # type: str
        self.message = message  # type: str
        self.price = price  # type: long
        self.promotion_fee = promotion_fee  # type: long
        self.quantity = quantity  # type: int
        self.reserve_price = reserve_price  # type: long
        self.sku_id = sku_id  # type: long
        self.sku_name = sku_name  # type: str
        self.virtual_item_type = virtual_item_type  # type: str

    def validate(self):
        if self.item_prom_inst_vos:
            for k in self.item_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.features is not None:
            result['Features'] = self.features
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        result['ItemPromInstVOS'] = []
        if self.item_prom_inst_vos is not None:
            for k in self.item_prom_inst_vos:
                result['ItemPromInstVOS'].append(k.to_map() if k else None)
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_fee is not None:
            result['PromotionFee'] = self.promotion_fee
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        self.item_prom_inst_vos = []
        if m.get('ItemPromInstVOS') is not None:
            for k in m.get('ItemPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS()
                self.item_prom_inst_vos.append(temp_model.from_map(k))
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionFee') is not None:
            self.promotion_fee = m.get('PromotionFee')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems(TeaModel):
    def __init__(self, item_id=None, lm_item_id=None, lm_shop_id=None, number=None, points=None, points_amount=None,
                 price_cent=None, removed=None, sku_id=None, tb_seller_id=None, user_pay_fee=None):
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_shop_id = lm_shop_id  # type: long
        self.number = number  # type: int
        self.points = points  # type: long
        self.points_amount = points_amount  # type: long
        self.price_cent = price_cent  # type: long
        self.removed = removed  # type: bool
        self.sku_id = sku_id  # type: long
        self.tb_seller_id = tb_seller_id  # type: long
        self.user_pay_fee = user_pay_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS(TeaModel):
    def __init__(self, available_items=None, can_use=None, discount_price=None, expire_time=None, instance_id=None,
                 level=None, lm_item_id=None, promotion_name=None, promotion_type=None, reason=None, selected=None,
                 sku_ids=None, special_price=None, sub_biz_code=None, tb_seller_id=None, threshold_price=None,
                 use_start_time=None):
        self.available_items = available_items  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems]
        self.can_use = can_use  # type: bool
        self.discount_price = discount_price  # type: long
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.promotion_type = promotion_type  # type: str
        self.reason = reason  # type: str
        self.selected = selected  # type: bool
        self.sku_ids = sku_ids  # type: list[long]
        self.special_price = special_price  # type: long
        self.sub_biz_code = sub_biz_code  # type: str
        self.tb_seller_id = tb_seller_id  # type: long
        self.threshold_price = threshold_price  # type: long
        self.use_start_time = use_start_time  # type: long

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfos(TeaModel):
    def __init__(self, can_sell=None, delivery_infos=None, ext_info=None, invoice_info=None, item_infos=None,
                 message=None, shop_prom_inst_vos=None):
        self.can_sell = can_sell  # type: bool
        self.delivery_infos = delivery_infos  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos]
        self.ext_info = ext_info  # type: dict[str, str]
        self.invoice_info = invoice_info  # type: RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo
        self.item_infos = item_infos  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos]
        self.message = message  # type: str
        self.shop_prom_inst_vos = shop_prom_inst_vos  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS]

    def validate(self):
        if self.delivery_infos:
            for k in self.delivery_infos:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.item_infos:
            for k in self.item_infos:
                if k:
                    k.validate()
        if self.shop_prom_inst_vos:
            for k in self.shop_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelRenderOrderInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        result['DeliveryInfos'] = []
        if self.delivery_infos is not None:
            for k in self.delivery_infos:
                result['DeliveryInfos'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.invoice_info is not None:
            result['InvoiceInfo'] = self.invoice_info.to_map()
        result['ItemInfos'] = []
        if self.item_infos is not None:
            for k in self.item_infos:
                result['ItemInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        result['ShopPromInstVOS'] = []
        if self.shop_prom_inst_vos is not None:
            for k in self.shop_prom_inst_vos:
                result['ShopPromInstVOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        self.delivery_infos = []
        if m.get('DeliveryInfos') is not None:
            for k in m.get('DeliveryInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos()
                self.delivery_infos.append(temp_model.from_map(k))
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InvoiceInfo') is not None:
            temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['InvoiceInfo'])
        self.item_infos = []
        if m.get('ItemInfos') is not None:
            for k in m.get('ItemInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos()
                self.item_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.shop_prom_inst_vos = []
        if m.get('ShopPromInstVOS') is not None:
            for k in m.get('ShopPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS()
                self.shop_prom_inst_vos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos(TeaModel):
    def __init__(self, display_name=None, id=None, post_fee=None, service_type=None):
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.post_fee = post_fee  # type: long
        self.service_type = service_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo(TeaModel):
    def __init__(self, desc=None, type=None):
        self.desc = desc  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems(TeaModel):
    def __init__(self, item_id=None, lm_item_id=None, lm_shop_id=None, number=None, points=None, points_amount=None,
                 price_cent=None, removed=None, sku_id=None, tb_seller_id=None, user_pay_fee=None):
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_shop_id = lm_shop_id  # type: long
        self.number = number  # type: int
        self.points = points  # type: long
        self.points_amount = points_amount  # type: long
        self.price_cent = price_cent  # type: long
        self.removed = removed  # type: bool
        self.sku_id = sku_id  # type: long
        self.tb_seller_id = tb_seller_id  # type: long
        self.user_pay_fee = user_pay_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS(TeaModel):
    def __init__(self, available_items=None, can_use=None, discount_price=None, expire_time=None, instance_id=None,
                 level=None, lm_item_id=None, promotion_name=None, promotion_type=None, reason=None, selected=None,
                 sku_ids=None, special_price=None, sub_biz_code=None, tb_seller_id=None, threshold_price=None,
                 use_start_time=None):
        self.available_items = available_items  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems]
        self.can_use = can_use  # type: bool
        self.discount_price = discount_price  # type: long
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.promotion_type = promotion_type  # type: str
        self.reason = reason  # type: str
        self.selected = selected  # type: bool
        self.sku_ids = sku_ids  # type: list[long]
        self.special_price = special_price  # type: long
        self.sub_biz_code = sub_biz_code  # type: str
        self.tb_seller_id = tb_seller_id  # type: long
        self.threshold_price = threshold_price  # type: long
        self.use_start_time = use_start_time  # type: long

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos(TeaModel):
    def __init__(self, can_sell=None, distribution_mall_id=None, distribution_supplier_id=None,
                 distributor_id=None, features=None, item_id=None, item_name=None, item_pic_url=None, item_prom_inst_vos=None,
                 item_url=None, message=None, price=None, promotion_fee=None, quantity=None, reserve_price=None, sku_id=None,
                 sku_name=None, virtual_item_type=None):
        self.can_sell = can_sell  # type: bool
        self.distribution_mall_id = distribution_mall_id  # type: str
        self.distribution_supplier_id = distribution_supplier_id  # type: str
        self.distributor_id = distributor_id  # type: str
        self.features = features  # type: dict[str, str]
        self.item_id = item_id  # type: str
        self.item_name = item_name  # type: str
        self.item_pic_url = item_pic_url  # type: str
        self.item_prom_inst_vos = item_prom_inst_vos  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS]
        self.item_url = item_url  # type: str
        self.message = message  # type: str
        self.price = price  # type: long
        self.promotion_fee = promotion_fee  # type: long
        self.quantity = quantity  # type: int
        self.reserve_price = reserve_price  # type: long
        self.sku_id = sku_id  # type: long
        self.sku_name = sku_name  # type: str
        self.virtual_item_type = virtual_item_type  # type: str

    def validate(self):
        if self.item_prom_inst_vos:
            for k in self.item_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.features is not None:
            result['Features'] = self.features
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        result['ItemPromInstVOS'] = []
        if self.item_prom_inst_vos is not None:
            for k in self.item_prom_inst_vos:
                result['ItemPromInstVOS'].append(k.to_map() if k else None)
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_fee is not None:
            result['PromotionFee'] = self.promotion_fee
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        self.item_prom_inst_vos = []
        if m.get('ItemPromInstVOS') is not None:
            for k in m.get('ItemPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS()
                self.item_prom_inst_vos.append(temp_model.from_map(k))
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionFee') is not None:
            self.promotion_fee = m.get('PromotionFee')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems(TeaModel):
    def __init__(self, item_id=None, lm_item_id=None, lm_shop_id=None, number=None, points=None, points_amount=None,
                 price_cent=None, removed=None, sku_id=None, tb_seller_id=None, user_pay_fee=None):
        self.item_id = item_id  # type: long
        self.lm_item_id = lm_item_id  # type: str
        self.lm_shop_id = lm_shop_id  # type: long
        self.number = number  # type: int
        self.points = points  # type: long
        self.points_amount = points_amount  # type: long
        self.price_cent = price_cent  # type: long
        self.removed = removed  # type: bool
        self.sku_id = sku_id  # type: long
        self.tb_seller_id = tb_seller_id  # type: long
        self.user_pay_fee = user_pay_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS(TeaModel):
    def __init__(self, available_items=None, can_use=None, discount_price=None, expire_time=None, instance_id=None,
                 level=None, lm_item_id=None, promotion_name=None, promotion_type=None, reason=None, selected=None,
                 sku_ids=None, special_price=None, sub_biz_code=None, tb_seller_id=None, threshold_price=None,
                 use_start_time=None):
        self.available_items = available_items  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems]
        self.can_use = can_use  # type: bool
        self.discount_price = discount_price  # type: long
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.lm_item_id = lm_item_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.promotion_type = promotion_type  # type: str
        self.reason = reason  # type: str
        self.selected = selected  # type: bool
        self.sku_ids = sku_ids  # type: list[long]
        self.special_price = special_price  # type: long
        self.sub_biz_code = sub_biz_code  # type: str
        self.tb_seller_id = tb_seller_id  # type: long
        self.threshold_price = threshold_price  # type: long
        self.use_start_time = use_start_time  # type: long

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos(TeaModel):
    def __init__(self, can_sell=None, delivery_infos=None, ext_info=None, invoice_info=None, item_infos=None,
                 message=None, shop_prom_inst_vos=None):
        self.can_sell = can_sell  # type: bool
        self.delivery_infos = delivery_infos  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos]
        self.ext_info = ext_info  # type: dict[str, str]
        self.invoice_info = invoice_info  # type: RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo
        self.item_infos = item_infos  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos]
        self.message = message  # type: str
        self.shop_prom_inst_vos = shop_prom_inst_vos  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS]

    def validate(self):
        if self.delivery_infos:
            for k in self.delivery_infos:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.item_infos:
            for k in self.item_infos:
                if k:
                    k.validate()
        if self.shop_prom_inst_vos:
            for k in self.shop_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        result['DeliveryInfos'] = []
        if self.delivery_infos is not None:
            for k in self.delivery_infos:
                result['DeliveryInfos'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.invoice_info is not None:
            result['InvoiceInfo'] = self.invoice_info.to_map()
        result['ItemInfos'] = []
        if self.item_infos is not None:
            for k in self.item_infos:
                result['ItemInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        result['ShopPromInstVOS'] = []
        if self.shop_prom_inst_vos is not None:
            for k in self.shop_prom_inst_vos:
                result['ShopPromInstVOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        self.delivery_infos = []
        if m.get('DeliveryInfos') is not None:
            for k in m.get('DeliveryInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos()
                self.delivery_infos.append(temp_model.from_map(k))
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InvoiceInfo') is not None:
            temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['InvoiceInfo'])
        self.item_infos = []
        if m.get('ItemInfos') is not None:
            for k in m.get('ItemInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos()
                self.item_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.shop_prom_inst_vos = []
        if m.get('ShopPromInstVOS') is not None:
            for k in m.get('ShopPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS()
                self.shop_prom_inst_vos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBodyModel(TeaModel):
    def __init__(self, address_infos=None, can_sell=None, ext_info=None, message=None, render_order_infos=None,
                 unsellable_render_order_infos=None):
        self.address_infos = address_infos  # type: list[RenderDistributionOrderResponseBodyModelAddressInfos]
        self.can_sell = can_sell  # type: bool
        self.ext_info = ext_info  # type: dict[str, str]
        self.message = message  # type: str
        self.render_order_infos = render_order_infos  # type: list[RenderDistributionOrderResponseBodyModelRenderOrderInfos]
        self.unsellable_render_order_infos = unsellable_render_order_infos  # type: list[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos]

    def validate(self):
        if self.address_infos:
            for k in self.address_infos:
                if k:
                    k.validate()
        if self.render_order_infos:
            for k in self.render_order_infos:
                if k:
                    k.validate()
        if self.unsellable_render_order_infos:
            for k in self.unsellable_render_order_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddressInfos'] = []
        if self.address_infos is not None:
            for k in self.address_infos:
                result['AddressInfos'].append(k.to_map() if k else None)
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.message is not None:
            result['Message'] = self.message
        result['RenderOrderInfos'] = []
        if self.render_order_infos is not None:
            for k in self.render_order_infos:
                result['RenderOrderInfos'].append(k.to_map() if k else None)
        result['UnsellableRenderOrderInfos'] = []
        if self.unsellable_render_order_infos is not None:
            for k in self.unsellable_render_order_infos:
                result['UnsellableRenderOrderInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address_infos = []
        if m.get('AddressInfos') is not None:
            for k in m.get('AddressInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelAddressInfos()
                self.address_infos.append(temp_model.from_map(k))
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.render_order_infos = []
        if m.get('RenderOrderInfos') is not None:
            for k in m.get('RenderOrderInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfos()
                self.render_order_infos.append(temp_model.from_map(k))
        self.unsellable_render_order_infos = []
        if m.get('UnsellableRenderOrderInfos') is not None:
            for k in m.get('UnsellableRenderOrderInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos()
                self.unsellable_render_order_infos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, model=None, page_number=None, page_size=None,
                 request_id=None, sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.model = model  # type: RenderDistributionOrderResponseBodyModel
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = RenderDistributionOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RenderDistributionOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenderDistributionOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenderDistributionOrderResponse, self).to_map()
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
            temp_model = RenderDistributionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitReturnGoodLogistics4DistributionRequest(TeaModel):
    def __init__(self, cp_code=None, dispute_id=None, distributor_id=None, logistics_no=None,
                 sub_distribution_order_id=None, tenant_id=None):
        self.cp_code = cp_code  # type: str
        self.dispute_id = dispute_id  # type: long
        self.distributor_id = distributor_id  # type: str
        self.logistics_no = logistics_no  # type: str
        self.sub_distribution_order_id = sub_distribution_order_id  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitReturnGoodLogistics4DistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class SubmitReturnGoodLogistics4DistributionResponseBody(TeaModel):
    def __init__(self, code=None, logs_id=None, message=None, page_number=None, page_size=None, request_id=None,
                 sub_code=None, sub_message=None, success=None, total_count=None):
        self.code = code  # type: str
        self.logs_id = logs_id  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.sub_code = sub_code  # type: str
        self.sub_message = sub_message  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitReturnGoodLogistics4DistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SubmitReturnGoodLogistics4DistributionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitReturnGoodLogistics4DistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitReturnGoodLogistics4DistributionResponse, self).to_map()
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
            temp_model = SubmitReturnGoodLogistics4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


