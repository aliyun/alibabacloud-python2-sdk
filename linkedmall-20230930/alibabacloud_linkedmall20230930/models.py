# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddressInfo(TeaModel):
    def __init__(self, address_detail=None, address_id=None, division_code=None, receiver=None, receiver_phone=None,
                 town_division_code=None):
        self.address_detail = address_detail  # type: str
        self.address_id = address_id  # type: long
        self.division_code = division_code  # type: str
        self.receiver = receiver  # type: str
        self.receiver_phone = receiver_phone  # type: str
        self.town_division_code = town_division_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddressInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['addressDetail'] = self.address_detail
        if self.address_id is not None:
            result['addressId'] = self.address_id
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.receiver is not None:
            result['receiver'] = self.receiver
        if self.receiver_phone is not None:
            result['receiverPhone'] = self.receiver_phone
        if self.town_division_code is not None:
            result['townDivisionCode'] = self.town_division_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('addressDetail') is not None:
            self.address_detail = m.get('addressDetail')
        if m.get('addressId') is not None:
            self.address_id = m.get('addressId')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')
        if m.get('receiverPhone') is not None:
            self.receiver_phone = m.get('receiverPhone')
        if m.get('townDivisionCode') is not None:
            self.town_division_code = m.get('townDivisionCode')
        return self


class ApplyReason(TeaModel):
    def __init__(self, reason_text_id=None, reason_tips=None):
        self.reason_text_id = reason_text_id  # type: long
        self.reason_tips = reason_tips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_text_id is not None:
            result['reasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['reasonTips'] = self.reason_tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('reasonTextId') is not None:
            self.reason_text_id = m.get('reasonTextId')
        if m.get('reasonTips') is not None:
            self.reason_tips = m.get('reasonTips')
        return self


class Category(TeaModel):
    def __init__(self, category_id=None, leaf=None, level=None, name=None, parent_id=None):
        self.category_id = category_id  # type: long
        self.leaf = leaf  # type: bool
        self.level = level  # type: int
        self.name = name  # type: str
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Category, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['categoryId'] = self.category_id
        if self.leaf is not None:
            result['leaf'] = self.leaf
        if self.level is not None:
            result['level'] = self.level
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('categoryId') is not None:
            self.category_id = m.get('categoryId')
        if m.get('leaf') is not None:
            self.leaf = m.get('leaf')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        return self


class ConfirmDisburseCmd(TeaModel):
    def __init__(self, order_id=None, purchase_order_id=None):
        self.order_id = order_id  # type: str
        self.purchase_order_id = purchase_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDisburseCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')
        return self


class ConfirmDisburseResult(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDisburseResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CooperationShop(TeaModel):
    def __init__(self, cooperation_company_id=None, cooperation_shop_id=None, shop_id=None):
        self.cooperation_company_id = cooperation_company_id  # type: str
        self.cooperation_shop_id = cooperation_shop_id  # type: str
        self.shop_id = shop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CooperationShop, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cooperation_company_id is not None:
            result['CooperationCompanyId'] = self.cooperation_company_id
        if self.cooperation_shop_id is not None:
            result['CooperationShopId'] = self.cooperation_shop_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CooperationCompanyId') is not None:
            self.cooperation_company_id = m.get('CooperationCompanyId')
        if m.get('CooperationShopId') is not None:
            self.cooperation_shop_id = m.get('CooperationShopId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        return self


class DeliveryInfo(TeaModel):
    def __init__(self, display_name=None, id=None, post_fee=None, service_type=None):
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.post_fee = post_fee  # type: long
        self.service_type = service_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliveryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.id is not None:
            result['id'] = self.id
        if self.post_fee is not None:
            result['postFee'] = self.post_fee
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('postFee') is not None:
            self.post_fee = m.get('postFee')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class DistributionMaxRefundFee(TeaModel):
    def __init__(self, max_refund_fee=None, min_refund_fee=None):
        self.max_refund_fee = max_refund_fee  # type: long
        self.min_refund_fee = min_refund_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DistributionMaxRefundFee, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['maxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['minRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxRefundFee') is not None:
            self.max_refund_fee = m.get('maxRefundFee')
        if m.get('minRefundFee') is not None:
            self.min_refund_fee = m.get('minRefundFee')
        return self


class Division(TeaModel):
    def __init__(self, division_code=None, division_level=None, division_name=None, parent_id=None, pinyin=None):
        self.division_code = division_code  # type: long
        self.division_level = division_level  # type: long
        self.division_name = division_name  # type: str
        self.parent_id = parent_id  # type: long
        self.pinyin = pinyin  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Division, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.division_level is not None:
            result['divisionLevel'] = self.division_level
        if self.division_name is not None:
            result['divisionName'] = self.division_name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.pinyin is not None:
            result['pinyin'] = self.pinyin
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('divisionLevel') is not None:
            self.division_level = m.get('divisionLevel')
        if m.get('divisionName') is not None:
            self.division_name = m.get('divisionName')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('pinyin') is not None:
            self.pinyin = m.get('pinyin')
        return self


class DivisionPageResult(TeaModel):
    def __init__(self, division_list=None, request_id=None):
        self.division_list = division_list  # type: list[Division]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.division_list:
            for k in self.division_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DivisionPageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['divisionList'] = []
        if self.division_list is not None:
            for k in self.division_list:
                result['divisionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.division_list = []
        if m.get('divisionList') is not None:
            for k in m.get('divisionList'):
                temp_model = Division()
                self.division_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DivisionQuery(TeaModel):
    def __init__(self, division_code=None):
        self.division_code = division_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DivisionQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        return self


class GeneralBill(TeaModel):
    def __init__(self, bill_id=None, bill_period=None, download_url=None, end_time=None, gmt_create=None,
                 gmt_modified=None, shop_id=None, shop_name=None, start_time=None, total_amount=None):
        self.bill_id = bill_id  # type: str
        self.bill_period = bill_period  # type: str
        self.download_url = download_url  # type: list[str]
        self.end_time = end_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.shop_id = shop_id  # type: str
        self.shop_name = shop_name  # type: str
        self.start_time = start_time  # type: str
        self.total_amount = total_amount  # type: Money

    def validate(self):
        if self.total_amount:
            self.total_amount.validate()

    def to_map(self):
        _map = super(GeneralBill, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['billId'] = self.bill_id
        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.shop_name is not None:
            result['shopName'] = self.shop_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('billId') is not None:
            self.bill_id = m.get('billId')
        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('totalAmount') is not None:
            temp_model = Money()
            self.total_amount = temp_model.from_map(m['totalAmount'])
        return self


class GeneralBillPageQuery(TeaModel):
    def __init__(self, asc=None, bill_id=None, bill_period=None, limit=None, order_by=None, order_direction=None,
                 page_number=None, page_size=None, shop_id=None, start=None):
        self.asc = asc  # type: bool
        self.bill_id = bill_id  # type: str
        self.bill_period = bill_period  # type: str
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.order_direction = order_direction  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.shop_id = shop_id  # type: str
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GeneralBillPageQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['asc'] = self.asc
        if self.bill_id is not None:
            result['billId'] = self.bill_id
        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period
        if self.limit is not None:
            result['limit'] = self.limit
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('asc') is not None:
            self.asc = m.get('asc')
        if m.get('billId') is not None:
            self.bill_id = m.get('billId')
        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class GeneralBillPageResult(TeaModel):
    def __init__(self, general_bills=None, page_number=None, page_size=None, request_id=None, total=None):
        self.general_bills = general_bills  # type: list[GeneralBill]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.general_bills:
            for k in self.general_bills:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GeneralBillPageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['generalBills'] = []
        if self.general_bills is not None:
            for k in self.general_bills:
                result['generalBills'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.general_bills = []
        if m.get('generalBills') is not None:
            for k in m.get('generalBills'):
                temp_model = GeneralBill()
                self.general_bills.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class Good(TeaModel):
    def __init__(self, good_name=None, product_id=None, quantity=None):
        self.good_name = good_name  # type: str
        self.product_id = product_id  # type: str
        self.quantity = quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(Good, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.good_name is not None:
            result['goodName'] = self.good_name
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('goodName') is not None:
            self.good_name = m.get('goodName')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        return self


class GoodsShippingNoticeCreateCmd(TeaModel):
    def __init__(self, cp_code=None, dispute_id=None, logistics_no=None):
        self.cp_code = cp_code  # type: str
        self.dispute_id = dispute_id  # type: long
        self.logistics_no = logistics_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GoodsShippingNoticeCreateCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_code is not None:
            result['cpCode'] = self.cp_code
        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id
        if self.logistics_no is not None:
            result['logisticsNo'] = self.logistics_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpCode') is not None:
            self.cp_code = m.get('cpCode')
        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')
        if m.get('logisticsNo') is not None:
            self.logistics_no = m.get('logisticsNo')
        return self


class GoodsShippingNoticeCreateResult(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GoodsShippingNoticeCreateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class LeavePictureList(TeaModel):
    def __init__(self, desc=None, picture=None):
        self.desc = desc  # type: str
        self.picture = picture  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LeavePictureList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.picture is not None:
            result['picture'] = self.picture
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('picture') is not None:
            self.picture = m.get('picture')
        return self


class LogisticsDetail(TeaModel):
    def __init__(self, ocurr_time_str=None, standerd_desc=None):
        self.ocurr_time_str = ocurr_time_str  # type: str
        self.standerd_desc = standerd_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogisticsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocurr_time_str is not None:
            result['ocurrTimeStr'] = self.ocurr_time_str
        if self.standerd_desc is not None:
            result['standerdDesc'] = self.standerd_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ocurrTimeStr') is not None:
            self.ocurr_time_str = m.get('ocurrTimeStr')
        if m.get('standerdDesc') is not None:
            self.standerd_desc = m.get('standerdDesc')
        return self


class LogisticsOrderListResult(TeaModel):
    def __init__(self, logistics_order_list=None, request_id=None):
        self.logistics_order_list = logistics_order_list  # type: list[LogisticsOrderResult]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.logistics_order_list:
            for k in self.logistics_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LogisticsOrderListResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['logisticsOrderList'] = []
        if self.logistics_order_list is not None:
            for k in self.logistics_order_list:
                result['logisticsOrderList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logistics_order_list = []
        if m.get('logisticsOrderList') is not None:
            for k in m.get('logisticsOrderList'):
                temp_model = LogisticsOrderResult()
                self.logistics_order_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class LogisticsOrderResult(TeaModel):
    def __init__(self, data_provider=None, data_provider_title=None, goods=None, logistics_company_code=None,
                 logistics_company_name=None, logistics_detail_list=None, mail_no=None):
        self.data_provider = data_provider  # type: str
        self.data_provider_title = data_provider_title  # type: str
        self.goods = goods  # type: list[Good]
        self.logistics_company_code = logistics_company_code  # type: str
        self.logistics_company_name = logistics_company_name  # type: str
        self.logistics_detail_list = logistics_detail_list  # type: list[LogisticsDetail]
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
        _map = super(LogisticsOrderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_provider is not None:
            result['dataProvider'] = self.data_provider
        if self.data_provider_title is not None:
            result['dataProviderTitle'] = self.data_provider_title
        result['goods'] = []
        if self.goods is not None:
            for k in self.goods:
                result['goods'].append(k.to_map() if k else None)
        if self.logistics_company_code is not None:
            result['logisticsCompanyCode'] = self.logistics_company_code
        if self.logistics_company_name is not None:
            result['logisticsCompanyName'] = self.logistics_company_name
        result['logisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k in self.logistics_detail_list:
                result['logisticsDetailList'].append(k.to_map() if k else None)
        if self.mail_no is not None:
            result['mailNo'] = self.mail_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataProvider') is not None:
            self.data_provider = m.get('dataProvider')
        if m.get('dataProviderTitle') is not None:
            self.data_provider_title = m.get('dataProviderTitle')
        self.goods = []
        if m.get('goods') is not None:
            for k in m.get('goods'):
                temp_model = Good()
                self.goods.append(temp_model.from_map(k))
        if m.get('logisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('logisticsCompanyCode')
        if m.get('logisticsCompanyName') is not None:
            self.logistics_company_name = m.get('logisticsCompanyName')
        self.logistics_detail_list = []
        if m.get('logisticsDetailList') is not None:
            for k in m.get('logisticsDetailList'):
                temp_model = LogisticsDetail()
                self.logistics_detail_list.append(temp_model.from_map(k))
        if m.get('mailNo') is not None:
            self.mail_no = m.get('mailNo')
        return self


class MoneyCurrency(TeaModel):
    def __init__(self, currency_code=None, default_fraction_digits=None, display_name=None, numeric_code=None,
                 symbol=None):
        self.currency_code = currency_code  # type: str
        self.default_fraction_digits = default_fraction_digits  # type: int
        self.display_name = display_name  # type: str
        self.numeric_code = numeric_code  # type: int
        self.symbol = symbol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoneyCurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency_code is not None:
            result['currencyCode'] = self.currency_code
        if self.default_fraction_digits is not None:
            result['defaultFractionDigits'] = self.default_fraction_digits
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.numeric_code is not None:
            result['numericCode'] = self.numeric_code
        if self.symbol is not None:
            result['symbol'] = self.symbol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currencyCode') is not None:
            self.currency_code = m.get('currencyCode')
        if m.get('defaultFractionDigits') is not None:
            self.default_fraction_digits = m.get('defaultFractionDigits')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('numericCode') is not None:
            self.numeric_code = m.get('numericCode')
        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')
        return self


class Money(TeaModel):
    def __init__(self, amount=None, amount_as_string=None, amount_string=None, cent=None, currency=None,
                 currency_code=None, positive=None):
        self.amount = amount  # type: long
        self.amount_as_string = amount_as_string  # type: str
        self.amount_string = amount_string  # type: str
        self.cent = cent  # type: long
        self.currency = currency  # type: MoneyCurrency
        self.currency_code = currency_code  # type: str
        self.positive = positive  # type: bool

    def validate(self):
        if self.currency:
            self.currency.validate()

    def to_map(self):
        _map = super(Money, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.amount_as_string is not None:
            result['amountAsString'] = self.amount_as_string
        if self.amount_string is not None:
            result['amountString'] = self.amount_string
        if self.cent is not None:
            result['cent'] = self.cent
        if self.currency is not None:
            result['currency'] = self.currency.to_map()
        if self.currency_code is not None:
            result['currencyCode'] = self.currency_code
        if self.positive is not None:
            result['positive'] = self.positive
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('amountAsString') is not None:
            self.amount_as_string = m.get('amountAsString')
        if m.get('amountString') is not None:
            self.amount_string = m.get('amountString')
        if m.get('cent') is not None:
            self.cent = m.get('cent')
        if m.get('currency') is not None:
            temp_model = MoneyCurrency()
            self.currency = temp_model.from_map(m['currency'])
        if m.get('currencyCode') is not None:
            self.currency_code = m.get('currencyCode')
        if m.get('positive') is not None:
            self.positive = m.get('positive')
        return self


class OrderLineResult(TeaModel):
    def __init__(self, logistics_status=None, number=None, order_id=None, order_line_id=None,
                 order_line_status=None, pay_fee=None, product_id=None, product_pic=None, product_title=None, sku_id=None,
                 sku_title=None):
        self.logistics_status = logistics_status  # type: str
        self.number = number  # type: str
        self.order_id = order_id  # type: str
        self.order_line_id = order_line_id  # type: str
        self.order_line_status = order_line_status  # type: str
        self.pay_fee = pay_fee  # type: long
        self.product_id = product_id  # type: str
        self.product_pic = product_pic  # type: str
        self.product_title = product_title  # type: str
        self.sku_id = sku_id  # type: str
        self.sku_title = sku_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderLineResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logistics_status is not None:
            result['logisticsStatus'] = self.logistics_status
        if self.number is not None:
            result['number'] = self.number
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        if self.order_line_status is not None:
            result['orderLineStatus'] = self.order_line_status
        if self.pay_fee is not None:
            result['payFee'] = self.pay_fee
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_pic is not None:
            result['productPic'] = self.product_pic
        if self.product_title is not None:
            result['productTitle'] = self.product_title
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        if self.sku_title is not None:
            result['skuTitle'] = self.sku_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logisticsStatus') is not None:
            self.logistics_status = m.get('logisticsStatus')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        if m.get('orderLineStatus') is not None:
            self.order_line_status = m.get('orderLineStatus')
        if m.get('payFee') is not None:
            self.pay_fee = m.get('payFee')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productPic') is not None:
            self.product_pic = m.get('productPic')
        if m.get('productTitle') is not None:
            self.product_title = m.get('productTitle')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        if m.get('skuTitle') is not None:
            self.sku_title = m.get('skuTitle')
        return self


class OrderListResult(TeaModel):
    def __init__(self, order_list=None, request_id=None, total=None):
        self.order_list = order_list  # type: list[OrderResult]
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderListResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['orderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['orderList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_list = []
        if m.get('orderList') is not None:
            for k in m.get('orderList'):
                temp_model = OrderResult()
                self.order_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class OrderPageQuery(TeaModel):
    def __init__(self, order_id_list=None, page_number=None, page_size=None, purchase_order_id=None):
        self.order_id_list = order_id_list  # type: list[str]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.purchase_order_id = purchase_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderPageQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id_list is not None:
            result['orderIdList'] = self.order_id_list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('orderIdList') is not None:
            self.order_id_list = m.get('orderIdList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')
        return self


class OrderProductResult(TeaModel):
    def __init__(self, can_sell=None, features=None, message=None, price=None, product_id=None, product_pic_url=None,
                 product_title=None, purchaser_id=None, quantity=None, sku_id=None, sku_title=None):
        self.can_sell = can_sell  # type: bool
        self.features = features  # type: dict[str, any]
        self.message = message  # type: str
        self.price = price  # type: long
        self.product_id = product_id  # type: str
        self.product_pic_url = product_pic_url  # type: str
        self.product_title = product_title  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.quantity = quantity  # type: int
        self.sku_id = sku_id  # type: str
        self.sku_title = sku_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderProductResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        if self.features is not None:
            result['features'] = self.features
        if self.message is not None:
            result['message'] = self.message
        if self.price is not None:
            result['price'] = self.price
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_pic_url is not None:
            result['productPicUrl'] = self.product_pic_url
        if self.product_title is not None:
            result['productTitle'] = self.product_title
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        if self.sku_title is not None:
            result['skuTitle'] = self.sku_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productPicUrl') is not None:
            self.product_pic_url = m.get('productPicUrl')
        if m.get('productTitle') is not None:
            self.product_title = m.get('productTitle')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        if m.get('skuTitle') is not None:
            self.sku_title = m.get('skuTitle')
        return self


class OrderRenderProductDTO(TeaModel):
    def __init__(self, product_id=None, purchaser_id=None, quantity=None, sku_id=None):
        self.product_id = product_id  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.quantity = quantity  # type: int
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderRenderProductDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        return self


class OrderRenderResult(TeaModel):
    def __init__(self, can_sell=None, delivery_info_list=None, ext_info=None, message=None, product_list=None):
        self.can_sell = can_sell  # type: bool
        self.delivery_info_list = delivery_info_list  # type: list[DeliveryInfo]
        self.ext_info = ext_info  # type: dict[str, any]
        self.message = message  # type: str
        self.product_list = product_list  # type: list[OrderProductResult]

    def validate(self):
        if self.delivery_info_list:
            for k in self.delivery_info_list:
                if k:
                    k.validate()
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderRenderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        result['deliveryInfoList'] = []
        if self.delivery_info_list is not None:
            for k in self.delivery_info_list:
                result['deliveryInfoList'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.message is not None:
            result['message'] = self.message
        result['productList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['productList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        self.delivery_info_list = []
        if m.get('deliveryInfoList') is not None:
            for k in m.get('deliveryInfoList'):
                temp_model = DeliveryInfo()
                self.delivery_info_list.append(temp_model.from_map(k))
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.product_list = []
        if m.get('productList') is not None:
            for k in m.get('productList'):
                temp_model = OrderProductResult()
                self.product_list.append(temp_model.from_map(k))
        return self


class OrderResult(TeaModel):
    def __init__(self, create_date=None, distributor_id=None, logistics_status=None, order_amount=None,
                 order_id=None, order_line_list=None, order_status=None, request_id=None):
        self.create_date = create_date  # type: str
        self.distributor_id = distributor_id  # type: str
        self.logistics_status = logistics_status  # type: str
        self.order_amount = order_amount  # type: long
        self.order_id = order_id  # type: str
        self.order_line_list = order_line_list  # type: list[OrderLineResult]
        self.order_status = order_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.order_line_list:
            for k in self.order_line_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['createDate'] = self.create_date
        if self.distributor_id is not None:
            result['distributorId'] = self.distributor_id
        if self.logistics_status is not None:
            result['logisticsStatus'] = self.logistics_status
        if self.order_amount is not None:
            result['orderAmount'] = self.order_amount
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['orderLineList'] = []
        if self.order_line_list is not None:
            for k in self.order_line_list:
                result['orderLineList'].append(k.to_map() if k else None)
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')
        if m.get('distributorId') is not None:
            self.distributor_id = m.get('distributorId')
        if m.get('logisticsStatus') is not None:
            self.logistics_status = m.get('logisticsStatus')
        if m.get('orderAmount') is not None:
            self.order_amount = m.get('orderAmount')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.order_line_list = []
        if m.get('orderLineList') is not None:
            for k in m.get('orderLineList'):
                temp_model = OrderLineResult()
                self.order_line_list.append(temp_model.from_map(k))
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class Product(TeaModel):
    def __init__(self, can_sell=None, category_chain=None, category_leaf_id=None, desc_path=None,
                 division_code=None, fuzzy_quantity=None, images=None, pic_url=None, product_id=None, product_specs=None,
                 product_status=None, product_type=None, properties=None, quantity=None, request_id=None, shop_id=None, skus=None,
                 sold_quantity=None, tax_code=None, tax_rate=None, title=None):
        self.can_sell = can_sell  # type: bool
        self.category_chain = category_chain  # type: list[Category]
        self.category_leaf_id = category_leaf_id  # type: long
        self.desc_path = desc_path  # type: str
        self.division_code = division_code  # type: str
        self.fuzzy_quantity = fuzzy_quantity  # type: str
        self.images = images  # type: list[str]
        self.pic_url = pic_url  # type: str
        self.product_id = product_id  # type: str
        self.product_specs = product_specs  # type: list[ProductSpec]
        self.product_status = product_status  # type: str
        self.product_type = product_type  # type: str
        self.properties = properties  # type: list[ProductProperty]
        self.quantity = quantity  # type: long
        self.request_id = request_id  # type: str
        self.shop_id = shop_id  # type: str
        self.skus = skus  # type: list[Sku]
        self.sold_quantity = sold_quantity  # type: str
        self.tax_code = tax_code  # type: str
        self.tax_rate = tax_rate  # type: int
        self.title = title  # type: str

    def validate(self):
        if self.category_chain:
            for k in self.category_chain:
                if k:
                    k.validate()
        if self.product_specs:
            for k in self.product_specs:
                if k:
                    k.validate()
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Product, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        result['categoryChain'] = []
        if self.category_chain is not None:
            for k in self.category_chain:
                result['categoryChain'].append(k.to_map() if k else None)
        if self.category_leaf_id is not None:
            result['categoryLeafId'] = self.category_leaf_id
        if self.desc_path is not None:
            result['descPath'] = self.desc_path
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity
        if self.images is not None:
            result['images'] = self.images
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.product_id is not None:
            result['productId'] = self.product_id
        result['productSpecs'] = []
        if self.product_specs is not None:
            for k in self.product_specs:
                result['productSpecs'].append(k.to_map() if k else None)
        if self.product_status is not None:
            result['productStatus'] = self.product_status
        if self.product_type is not None:
            result['productType'] = self.product_type
        result['properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['properties'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        result['skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['skus'].append(k.to_map() if k else None)
        if self.sold_quantity is not None:
            result['soldQuantity'] = self.sold_quantity
        if self.tax_code is not None:
            result['taxCode'] = self.tax_code
        if self.tax_rate is not None:
            result['taxRate'] = self.tax_rate
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        self.category_chain = []
        if m.get('categoryChain') is not None:
            for k in m.get('categoryChain'):
                temp_model = Category()
                self.category_chain.append(temp_model.from_map(k))
        if m.get('categoryLeafId') is not None:
            self.category_leaf_id = m.get('categoryLeafId')
        if m.get('descPath') is not None:
            self.desc_path = m.get('descPath')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        self.product_specs = []
        if m.get('productSpecs') is not None:
            for k in m.get('productSpecs'):
                temp_model = ProductSpec()
                self.product_specs.append(temp_model.from_map(k))
        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        self.properties = []
        if m.get('properties') is not None:
            for k in m.get('properties'):
                temp_model = ProductProperty()
                self.properties.append(temp_model.from_map(k))
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        self.skus = []
        if m.get('skus') is not None:
            for k in m.get('skus'):
                temp_model = Sku()
                self.skus.append(temp_model.from_map(k))
        if m.get('soldQuantity') is not None:
            self.sold_quantity = m.get('soldQuantity')
        if m.get('taxCode') is not None:
            self.tax_code = m.get('taxCode')
        if m.get('taxRate') is not None:
            self.tax_rate = m.get('taxRate')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ProductDTO(TeaModel):
    def __init__(self, price=None, product_id=None, purchaser_id=None, quantity=None, sku_id=None):
        self.price = price  # type: long
        self.product_id = product_id  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.quantity = quantity  # type: int
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['price'] = self.price
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        return self


class ProductPageResult(TeaModel):
    def __init__(self, page_number=None, page_size=None, products=None, request_id=None, total=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.products = products  # type: list[Product]
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ProductPageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = Product()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ProductPrice(TeaModel):
    def __init__(self, fund_amount_money=None):
        self.fund_amount_money = fund_amount_money  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount_money is not None:
            result['fundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fundAmountMoney') is not None:
            self.fund_amount_money = m.get('fundAmountMoney')
        return self


class ProductProperty(TeaModel):
    def __init__(self, text=None, values=None):
        self.text = text  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ProductQuery(TeaModel):
    def __init__(self, distributor_shop_id=None, division_code=None):
        self.distributor_shop_id = distributor_shop_id  # type: str
        self.division_code = division_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_shop_id is not None:
            result['distributorShopId'] = self.distributor_shop_id
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('distributorShopId') is not None:
            self.distributor_shop_id = m.get('distributorShopId')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        return self


class ProductSaleInfo(TeaModel):
    def __init__(self, can_sell=None, division_code=None, fuzzy_quantity=None, product_id=None, product_status=None,
                 quantity=None, request_id=None, shop_id=None, skus=None, title=None):
        self.can_sell = can_sell  # type: bool
        self.division_code = division_code  # type: str
        self.fuzzy_quantity = fuzzy_quantity  # type: str
        self.product_id = product_id  # type: str
        self.product_status = product_status  # type: str
        self.quantity = quantity  # type: long
        self.request_id = request_id  # type: str
        self.shop_id = shop_id  # type: str
        self.skus = skus  # type: list[SkuSaleInfo]
        self.title = title  # type: str

    def validate(self):
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ProductSaleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.product_status is not None:
            result['productStatus'] = self.product_status
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        result['skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['skus'].append(k.to_map() if k else None)
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        self.skus = []
        if m.get('skus') is not None:
            for k in m.get('skus'):
                temp_model = SkuSaleInfo()
                self.skus.append(temp_model.from_map(k))
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ProductSaleInfoListQuery(TeaModel):
    def __init__(self, division_code=None, product_ids=None, purchaser_id=None):
        self.division_code = division_code  # type: str
        self.product_ids = product_ids  # type: list[str]
        self.purchaser_id = purchaser_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductSaleInfoListQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.product_ids is not None:
            result['productIds'] = self.product_ids
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        return self


class ProductSaleInfoListResult(TeaModel):
    def __init__(self, product_sale_infos=None, request_id=None):
        self.product_sale_infos = product_sale_infos  # type: list[ProductSaleInfo]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.product_sale_infos:
            for k in self.product_sale_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ProductSaleInfoListResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['productSaleInfos'] = []
        if self.product_sale_infos is not None:
            for k in self.product_sale_infos:
                result['productSaleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_sale_infos = []
        if m.get('productSaleInfos') is not None:
            for k in m.get('productSaleInfos'):
                temp_model = ProductSaleInfo()
                self.product_sale_infos.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ProductSaleInfoQuery(TeaModel):
    def __init__(self, distributor_shop_id=None, division_code=None):
        self.distributor_shop_id = distributor_shop_id  # type: str
        self.division_code = division_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductSaleInfoQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_shop_id is not None:
            result['distributorShopId'] = self.distributor_shop_id
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('distributorShopId') is not None:
            self.distributor_shop_id = m.get('distributorShopId')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        return self


class ProductSpec(TeaModel):
    def __init__(self, key=None, key_id=None, values=None):
        self.key = key  # type: str
        self.key_id = key_id  # type: long
        self.values = values  # type: list[ProductSpecValue]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ProductSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.key_id is not None:
            result['keyId'] = self.key_id
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = ProductSpecValue()
                self.values.append(temp_model.from_map(k))
        return self


class ProductSpecValue(TeaModel):
    def __init__(self, value=None, value_id=None):
        self.value = value  # type: str
        self.value_id = value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductSpecValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        if self.value_id is not None:
            result['valueId'] = self.value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueId') is not None:
            self.value_id = m.get('valueId')
        return self


class PurchaseOrderCreateCmd(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, ext_info=None, outer_purchase_order_id=None,
                 product_list=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: AddressInfo
        self.ext_info = ext_info  # type: dict[str, any]
        self.outer_purchase_order_id = outer_purchase_order_id  # type: str
        self.product_list = product_list  # type: list[ProductDTO]

    def validate(self):
        if self.delivery_address:
            self.delivery_address.validate()
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PurchaseOrderCreateCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['deliveryAddress'] = self.delivery_address.to_map()
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.outer_purchase_order_id is not None:
            result['outerPurchaseOrderId'] = self.outer_purchase_order_id
        result['productList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['productList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')
        if m.get('deliveryAddress') is not None:
            temp_model = AddressInfo()
            self.delivery_address = temp_model.from_map(m['deliveryAddress'])
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('outerPurchaseOrderId') is not None:
            self.outer_purchase_order_id = m.get('outerPurchaseOrderId')
        self.product_list = []
        if m.get('productList') is not None:
            for k in m.get('productList'):
                temp_model = ProductDTO()
                self.product_list.append(temp_model.from_map(k))
        return self


class PurchaseOrderCreateResult(TeaModel):
    def __init__(self, purchase_order_id=None, request_id=None):
        self.purchase_order_id = purchase_order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseOrderCreateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PurchaseOrderRenderQuery(TeaModel):
    def __init__(self, buyer_id=None, delivery_address=None, ext_info=None, product_list=None):
        self.buyer_id = buyer_id  # type: str
        self.delivery_address = delivery_address  # type: AddressInfo
        self.ext_info = ext_info  # type: dict[str, any]
        self.product_list = product_list  # type: list[OrderRenderProductDTO]

    def validate(self):
        if self.delivery_address:
            self.delivery_address.validate()
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PurchaseOrderRenderQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['deliveryAddress'] = self.delivery_address.to_map()
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        result['productList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['productList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')
        if m.get('deliveryAddress') is not None:
            temp_model = AddressInfo()
            self.delivery_address = temp_model.from_map(m['deliveryAddress'])
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        self.product_list = []
        if m.get('productList') is not None:
            for k in m.get('productList'):
                temp_model = OrderRenderProductDTO()
                self.product_list.append(temp_model.from_map(k))
        return self


class PurchaseOrderRenderResult(TeaModel):
    def __init__(self, address_list=None, can_sell=None, ext_info=None, message=None, order_list=None,
                 request_id=None, unsellable_order_list=None):
        self.address_list = address_list  # type: list[AddressInfo]
        self.can_sell = can_sell  # type: bool
        self.ext_info = ext_info  # type: dict[str, any]
        self.message = message  # type: str
        self.order_list = order_list  # type: list[OrderRenderResult]
        self.request_id = request_id  # type: str
        self.unsellable_order_list = unsellable_order_list  # type: list[OrderRenderResult]

    def validate(self):
        if self.address_list:
            for k in self.address_list:
                if k:
                    k.validate()
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()
        if self.unsellable_order_list:
            for k in self.unsellable_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PurchaseOrderRenderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addressList'] = []
        if self.address_list is not None:
            for k in self.address_list:
                result['addressList'].append(k.to_map() if k else None)
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.message is not None:
            result['message'] = self.message
        result['orderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['orderList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['unsellableOrderList'] = []
        if self.unsellable_order_list is not None:
            for k in self.unsellable_order_list:
                result['unsellableOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address_list = []
        if m.get('addressList') is not None:
            for k in m.get('addressList'):
                temp_model = AddressInfo()
                self.address_list.append(temp_model.from_map(k))
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.order_list = []
        if m.get('orderList') is not None:
            for k in m.get('orderList'):
                temp_model = OrderRenderResult()
                self.order_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.unsellable_order_list = []
        if m.get('unsellableOrderList') is not None:
            for k in m.get('unsellableOrderList'):
                temp_model = OrderRenderResult()
                self.unsellable_order_list.append(temp_model.from_map(k))
        return self


class PurchaseOrderStatusResult(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseOrderStatusResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class RefundFeeData(TeaModel):
    def __init__(self, max_refund_fee=None, min_refund_fee=None):
        self.max_refund_fee = max_refund_fee  # type: long
        self.min_refund_fee = min_refund_fee  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundFeeData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['maxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['minRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxRefundFee') is not None:
            self.max_refund_fee = m.get('maxRefundFee')
        if m.get('minRefundFee') is not None:
            self.min_refund_fee = m.get('minRefundFee')
        return self


class RefundOrderCmd(TeaModel):
    def __init__(self, apply_reason_text_id=None, apply_reason_tips=None, apply_refund_count=None,
                 apply_refund_fee=None, biz_claim_type=None, goods_status=None, leave_message=None, leave_picture_lists=None,
                 order_line_id=None):
        self.apply_reason_text_id = apply_reason_text_id  # type: long
        self.apply_reason_tips = apply_reason_tips  # type: str
        self.apply_refund_count = apply_refund_count  # type: int
        self.apply_refund_fee = apply_refund_fee  # type: long
        self.biz_claim_type = biz_claim_type  # type: int
        self.goods_status = goods_status  # type: int
        self.leave_message = leave_message  # type: str
        self.leave_picture_lists = leave_picture_lists  # type: list[LeavePictureList]
        self.order_line_id = order_line_id  # type: str

    def validate(self):
        if self.leave_picture_lists:
            for k in self.leave_picture_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundOrderCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['applyReasonTextId'] = self.apply_reason_text_id
        if self.apply_reason_tips is not None:
            result['applyReasonTips'] = self.apply_reason_tips
        if self.apply_refund_count is not None:
            result['applyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['applyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type
        if self.goods_status is not None:
            result['goodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['leaveMessage'] = self.leave_message
        result['leavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k in self.leave_picture_lists:
                result['leavePictureLists'].append(k.to_map() if k else None)
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('applyReasonTextId')
        if m.get('applyReasonTips') is not None:
            self.apply_reason_tips = m.get('applyReasonTips')
        if m.get('applyRefundCount') is not None:
            self.apply_refund_count = m.get('applyRefundCount')
        if m.get('applyRefundFee') is not None:
            self.apply_refund_fee = m.get('applyRefundFee')
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')
        if m.get('goodsStatus') is not None:
            self.goods_status = m.get('goodsStatus')
        if m.get('leaveMessage') is not None:
            self.leave_message = m.get('leaveMessage')
        self.leave_picture_lists = []
        if m.get('leavePictureLists') is not None:
            for k in m.get('leavePictureLists'):
                temp_model = LeavePictureList()
                self.leave_picture_lists.append(temp_model.from_map(k))
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        return self


class RefundOrderResult(TeaModel):
    def __init__(self, dispute_id=None, dispute_status=None, order_line_id=None, request_id=None):
        self.dispute_id = dispute_id  # type: str
        self.dispute_status = dispute_status  # type: int
        self.order_line_id = order_line_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundOrderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['disputeStatus'] = self.dispute_status
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')
        if m.get('disputeStatus') is not None:
            self.dispute_status = m.get('disputeStatus')
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RefundReason(TeaModel):
    def __init__(self, proof_required=None, reason_text_id=None, reason_tips=None, refund_desc_required=None):
        self.proof_required = proof_required  # type: bool
        self.reason_text_id = reason_text_id  # type: str
        self.reason_tips = reason_tips  # type: str
        self.refund_desc_required = refund_desc_required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proof_required is not None:
            result['proofRequired'] = self.proof_required
        if self.reason_text_id is not None:
            result['reasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['reasonTips'] = self.reason_tips
        if self.refund_desc_required is not None:
            result['refundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('proofRequired') is not None:
            self.proof_required = m.get('proofRequired')
        if m.get('reasonTextId') is not None:
            self.reason_text_id = m.get('reasonTextId')
        if m.get('reasonTips') is not None:
            self.reason_tips = m.get('reasonTips')
        if m.get('refundDescRequired') is not None:
            self.refund_desc_required = m.get('refundDescRequired')
        return self


class RefundRenderCmd(TeaModel):
    def __init__(self, biz_claim_type=None, goods_status=None, order_line_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.goods_status = goods_status  # type: int
        self.order_line_id = order_line_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundRenderCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type
        if self.goods_status is not None:
            result['goodsStatus'] = self.goods_status
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')
        if m.get('goodsStatus') is not None:
            self.goods_status = m.get('goodsStatus')
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        return self


class RefundRenderResult(TeaModel):
    def __init__(self, biz_claim_type=None, max_refund_fee_data=None, order_line_id=None, refund_reason_list=None,
                 request_id=None):
        self.biz_claim_type = biz_claim_type  # type: int
        self.max_refund_fee_data = max_refund_fee_data  # type: DistributionMaxRefundFee
        self.order_line_id = order_line_id  # type: str
        self.refund_reason_list = refund_reason_list  # type: list[RefundReason]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundRenderResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type
        if self.max_refund_fee_data is not None:
            result['maxRefundFeeData'] = self.max_refund_fee_data.to_map()
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        result['refundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['refundReasonList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')
        if m.get('maxRefundFeeData') is not None:
            temp_model = DistributionMaxRefundFee()
            self.max_refund_fee_data = temp_model.from_map(m['maxRefundFeeData'])
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        self.refund_reason_list = []
        if m.get('refundReasonList') is not None:
            for k in m.get('refundReasonList'):
                temp_model = RefundReason()
                self.refund_reason_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RefundResult(TeaModel):
    def __init__(self, apply_dispute_desc=None, apply_reason=None, biz_claim_type=None, dispute_create_time=None,
                 dispute_desc=None, dispute_end_time=None, dispute_id=None, dispute_status=None, order_id=None,
                 order_line_id=None, order_logistics_status=None, refund_fee=None, refund_fee_data=None, refunder_address=None,
                 refunder_name=None, refunder_tel=None, refunder_zip_code=None, return_good_logistics_status=None,
                 seller_agree_msg=None, seller_refuse_agreement_message=None, seller_refuse_reason=None):
        self.apply_dispute_desc = apply_dispute_desc  # type: str
        self.apply_reason = apply_reason  # type: ApplyReason
        self.biz_claim_type = biz_claim_type  # type: int
        self.dispute_create_time = dispute_create_time  # type: str
        self.dispute_desc = dispute_desc  # type: str
        self.dispute_end_time = dispute_end_time  # type: str
        self.dispute_id = dispute_id  # type: str
        self.dispute_status = dispute_status  # type: int
        self.order_id = order_id  # type: str
        self.order_line_id = order_line_id  # type: str
        self.order_logistics_status = order_logistics_status  # type: int
        self.refund_fee = refund_fee  # type: long
        self.refund_fee_data = refund_fee_data  # type: RefundFeeData
        self.refunder_address = refunder_address  # type: str
        self.refunder_name = refunder_name  # type: str
        self.refunder_tel = refunder_tel  # type: str
        self.refunder_zip_code = refunder_zip_code  # type: str
        self.return_good_logistics_status = return_good_logistics_status  # type: int
        self.seller_agree_msg = seller_agree_msg  # type: str
        self.seller_refuse_agreement_message = seller_refuse_agreement_message  # type: str
        self.seller_refuse_reason = seller_refuse_reason  # type: str

    def validate(self):
        if self.apply_reason:
            self.apply_reason.validate()
        if self.refund_fee_data:
            self.refund_fee_data.validate()

    def to_map(self):
        _map = super(RefundResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_dispute_desc is not None:
            result['applyDisputeDesc'] = self.apply_dispute_desc
        if self.apply_reason is not None:
            result['applyReason'] = self.apply_reason.to_map()
        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type
        if self.dispute_create_time is not None:
            result['disputeCreateTime'] = self.dispute_create_time
        if self.dispute_desc is not None:
            result['disputeDesc'] = self.dispute_desc
        if self.dispute_end_time is not None:
            result['disputeEndTime'] = self.dispute_end_time
        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['disputeStatus'] = self.dispute_status
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id
        if self.order_logistics_status is not None:
            result['orderLogisticsStatus'] = self.order_logistics_status
        if self.refund_fee is not None:
            result['refundFee'] = self.refund_fee
        if self.refund_fee_data is not None:
            result['refundFeeData'] = self.refund_fee_data.to_map()
        if self.refunder_address is not None:
            result['refunderAddress'] = self.refunder_address
        if self.refunder_name is not None:
            result['refunderName'] = self.refunder_name
        if self.refunder_tel is not None:
            result['refunderTel'] = self.refunder_tel
        if self.refunder_zip_code is not None:
            result['refunderZipCode'] = self.refunder_zip_code
        if self.return_good_logistics_status is not None:
            result['returnGoodLogisticsStatus'] = self.return_good_logistics_status
        if self.seller_agree_msg is not None:
            result['sellerAgreeMsg'] = self.seller_agree_msg
        if self.seller_refuse_agreement_message is not None:
            result['sellerRefuseAgreementMessage'] = self.seller_refuse_agreement_message
        if self.seller_refuse_reason is not None:
            result['sellerRefuseReason'] = self.seller_refuse_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyDisputeDesc') is not None:
            self.apply_dispute_desc = m.get('applyDisputeDesc')
        if m.get('applyReason') is not None:
            temp_model = ApplyReason()
            self.apply_reason = temp_model.from_map(m['applyReason'])
        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')
        if m.get('disputeCreateTime') is not None:
            self.dispute_create_time = m.get('disputeCreateTime')
        if m.get('disputeDesc') is not None:
            self.dispute_desc = m.get('disputeDesc')
        if m.get('disputeEndTime') is not None:
            self.dispute_end_time = m.get('disputeEndTime')
        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')
        if m.get('disputeStatus') is not None:
            self.dispute_status = m.get('disputeStatus')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')
        if m.get('orderLogisticsStatus') is not None:
            self.order_logistics_status = m.get('orderLogisticsStatus')
        if m.get('refundFee') is not None:
            self.refund_fee = m.get('refundFee')
        if m.get('refundFeeData') is not None:
            temp_model = RefundFeeData()
            self.refund_fee_data = temp_model.from_map(m['refundFeeData'])
        if m.get('refunderAddress') is not None:
            self.refunder_address = m.get('refunderAddress')
        if m.get('refunderName') is not None:
            self.refunder_name = m.get('refunderName')
        if m.get('refunderTel') is not None:
            self.refunder_tel = m.get('refunderTel')
        if m.get('refunderZipCode') is not None:
            self.refunder_zip_code = m.get('refunderZipCode')
        if m.get('returnGoodLogisticsStatus') is not None:
            self.return_good_logistics_status = m.get('returnGoodLogisticsStatus')
        if m.get('sellerAgreeMsg') is not None:
            self.seller_agree_msg = m.get('sellerAgreeMsg')
        if m.get('sellerRefuseAgreementMessage') is not None:
            self.seller_refuse_agreement_message = m.get('sellerRefuseAgreementMessage')
        if m.get('sellerRefuseReason') is not None:
            self.seller_refuse_reason = m.get('sellerRefuseReason')
        return self


class Shop(TeaModel):
    def __init__(self, cooperation_shops=None, distributor_id=None, end_date=None, purchaser_id=None,
                 request_id=None, shop_id=None, shop_name=None, shop_type=None, start_date=None, status=None):
        self.cooperation_shops = cooperation_shops  # type: list[CooperationShop]
        self.distributor_id = distributor_id  # type: str
        self.end_date = end_date  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.request_id = request_id  # type: str
        self.shop_id = shop_id  # type: str
        self.shop_name = shop_name  # type: str
        self.shop_type = shop_type  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.cooperation_shops:
            for k in self.cooperation_shops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Shop, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cooperationShops'] = []
        if self.cooperation_shops is not None:
            for k in self.cooperation_shops:
                result['cooperationShops'].append(k.to_map() if k else None)
        if self.distributor_id is not None:
            result['distributorId'] = self.distributor_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.shop_name is not None:
            result['shopName'] = self.shop_name
        if self.shop_type is not None:
            result['shopType'] = self.shop_type
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cooperation_shops = []
        if m.get('cooperationShops') is not None:
            for k in m.get('cooperationShops'):
                temp_model = CooperationShop()
                self.cooperation_shops.append(temp_model.from_map(k))
        if m.get('distributorId') is not None:
            self.distributor_id = m.get('distributorId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')
        if m.get('shopType') is not None:
            self.shop_type = m.get('shopType')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ShopPageDataResult(TeaModel):
    def __init__(self, cooperation_shops=None, end_date=None, purchaser_id=None, shop_id=None, shop_name=None,
                 shop_type=None, start_date=None, status=None):
        self.cooperation_shops = cooperation_shops  # type: list[CooperationShop]
        self.end_date = end_date  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.shop_id = shop_id  # type: str
        self.shop_name = shop_name  # type: str
        self.shop_type = shop_type  # type: str
        self.start_date = start_date  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.cooperation_shops:
            for k in self.cooperation_shops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ShopPageDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cooperationShops'] = []
        if self.cooperation_shops is not None:
            for k in self.cooperation_shops:
                result['cooperationShops'].append(k.to_map() if k else None)
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.shop_name is not None:
            result['shopName'] = self.shop_name
        if self.shop_type is not None:
            result['shopType'] = self.shop_type
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cooperation_shops = []
        if m.get('cooperationShops') is not None:
            for k in m.get('cooperationShops'):
                temp_model = CooperationShop()
                self.cooperation_shops.append(temp_model.from_map(k))
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')
        if m.get('shopType') is not None:
            self.shop_type = m.get('shopType')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ShopPageResult(TeaModel):
    def __init__(self, request_id=None, shop_list=None, total=None):
        self.request_id = request_id  # type: str
        self.shop_list = shop_list  # type: list[ShopPageDataResult]
        self.total = total  # type: int

    def validate(self):
        if self.shop_list:
            for k in self.shop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ShopPageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['shopList'] = []
        if self.shop_list is not None:
            for k in self.shop_list:
                result['shopList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.shop_list = []
        if m.get('shopList') is not None:
            for k in m.get('shopList'):
                temp_model = ShopPageDataResult()
                self.shop_list.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class Sku(TeaModel):
    def __init__(self, can_sell=None, division_code=None, fuzzy_quantity=None, mark_price=None, pic_url=None,
                 platform_price=None, price=None, product_id=None, quantity=None, shop_id=None, sku_id=None, sku_specs=None,
                 sku_specs_code=None, sku_status=None, title=None):
        self.can_sell = can_sell  # type: bool
        self.division_code = division_code  # type: str
        self.fuzzy_quantity = fuzzy_quantity  # type: str
        self.mark_price = mark_price  # type: long
        self.pic_url = pic_url  # type: str
        self.platform_price = platform_price  # type: long
        self.price = price  # type: long
        self.product_id = product_id  # type: str
        self.quantity = quantity  # type: long
        self.shop_id = shop_id  # type: str
        self.sku_id = sku_id  # type: str
        self.sku_specs = sku_specs  # type: list[SkuSpec]
        self.sku_specs_code = sku_specs_code  # type: str
        self.sku_status = sku_status  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.sku_specs:
            for k in self.sku_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Sku, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity
        if self.mark_price is not None:
            result['markPrice'] = self.mark_price
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.platform_price is not None:
            result['platformPrice'] = self.platform_price
        if self.price is not None:
            result['price'] = self.price
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        result['skuSpecs'] = []
        if self.sku_specs is not None:
            for k in self.sku_specs:
                result['skuSpecs'].append(k.to_map() if k else None)
        if self.sku_specs_code is not None:
            result['skuSpecsCode'] = self.sku_specs_code
        if self.sku_status is not None:
            result['skuStatus'] = self.sku_status
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')
        if m.get('markPrice') is not None:
            self.mark_price = m.get('markPrice')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('platformPrice') is not None:
            self.platform_price = m.get('platformPrice')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        self.sku_specs = []
        if m.get('skuSpecs') is not None:
            for k in m.get('skuSpecs'):
                temp_model = SkuSpec()
                self.sku_specs.append(temp_model.from_map(k))
        if m.get('skuSpecsCode') is not None:
            self.sku_specs_code = m.get('skuSpecsCode')
        if m.get('skuStatus') is not None:
            self.sku_status = m.get('skuStatus')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SkuQueryParam(TeaModel):
    def __init__(self, product_id=None, sku_id=None):
        self.product_id = product_id  # type: str
        self.sku_id = sku_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkuQueryParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        return self


class SkuSaleInfo(TeaModel):
    def __init__(self, can_sell=None, division_code=None, fuzzy_quantity=None, mark_price=None, price=None,
                 product_id=None, quantity=None, shop_id=None, sku_id=None, sku_status=None, title=None):
        self.can_sell = can_sell  # type: bool
        self.division_code = division_code  # type: str
        self.fuzzy_quantity = fuzzy_quantity  # type: str
        self.mark_price = mark_price  # type: long
        self.price = price  # type: long
        self.product_id = product_id  # type: str
        self.quantity = quantity  # type: long
        self.shop_id = shop_id  # type: str
        self.sku_id = sku_id  # type: str
        self.sku_status = sku_status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkuSaleInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['canSell'] = self.can_sell
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.fuzzy_quantity is not None:
            result['fuzzyQuantity'] = self.fuzzy_quantity
        if self.mark_price is not None:
            result['markPrice'] = self.mark_price
        if self.price is not None:
            result['price'] = self.price
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.shop_id is not None:
            result['shopId'] = self.shop_id
        if self.sku_id is not None:
            result['skuId'] = self.sku_id
        if self.sku_status is not None:
            result['skuStatus'] = self.sku_status
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('fuzzyQuantity') is not None:
            self.fuzzy_quantity = m.get('fuzzyQuantity')
        if m.get('markPrice') is not None:
            self.mark_price = m.get('markPrice')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')
        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')
        if m.get('skuStatus') is not None:
            self.sku_status = m.get('skuStatus')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class SkuSaleInfoListQuery(TeaModel):
    def __init__(self, division_code=None, purchaser_id=None, sku_query_params=None):
        self.division_code = division_code  # type: str
        self.purchaser_id = purchaser_id  # type: str
        self.sku_query_params = sku_query_params  # type: list[SkuQueryParam]

    def validate(self):
        if self.sku_query_params:
            for k in self.sku_query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SkuSaleInfoListQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        result['skuQueryParams'] = []
        if self.sku_query_params is not None:
            for k in self.sku_query_params:
                result['skuQueryParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        self.sku_query_params = []
        if m.get('skuQueryParams') is not None:
            for k in m.get('skuQueryParams'):
                temp_model = SkuQueryParam()
                self.sku_query_params.append(temp_model.from_map(k))
        return self


class SkuSaleInfoListResult(TeaModel):
    def __init__(self, request_id=None, sku_sale_infos=None):
        self.request_id = request_id  # type: str
        self.sku_sale_infos = sku_sale_infos  # type: list[SkuSaleInfo]

    def validate(self):
        if self.sku_sale_infos:
            for k in self.sku_sale_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SkuSaleInfoListResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['skuSaleInfos'] = []
        if self.sku_sale_infos is not None:
            for k in self.sku_sale_infos:
                result['skuSaleInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.sku_sale_infos = []
        if m.get('skuSaleInfos') is not None:
            for k in m.get('skuSaleInfos'):
                temp_model = SkuSaleInfo()
                self.sku_sale_infos.append(temp_model.from_map(k))
        return self


class SkuSpec(TeaModel):
    def __init__(self, key=None, key_id=None, value=None, value_id=None):
        self.key = key  # type: str
        self.key_id = key_id  # type: long
        self.value = value  # type: str
        self.value_id = value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkuSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.key_id is not None:
            result['keyId'] = self.key_id
        if self.value is not None:
            result['value'] = self.value
        if self.value_id is not None:
            result['valueId'] = self.value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueId') is not None:
            self.value_id = m.get('valueId')
        return self


class CancelRefundOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundOrderResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRefundOrderResponse, self).to_map()
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
            temp_model = RefundOrderResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDisburseRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: ConfirmDisburseCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmDisburseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ConfirmDisburseCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDisburseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmDisburseResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmDisburseResponse, self).to_map()
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
            temp_model = ConfirmDisburseResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGoodsShippingNoticeRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: GoodsShippingNoticeCreateCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGoodsShippingNoticeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = GoodsShippingNoticeCreateCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGoodsShippingNoticeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GoodsShippingNoticeCreateResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGoodsShippingNoticeResponse, self).to_map()
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
            temp_model = GoodsShippingNoticeCreateResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePurchaseOrderRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: PurchaseOrderCreateCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePurchaseOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PurchaseOrderCreateCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePurchaseOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurchaseOrderCreateResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePurchaseOrderResponse, self).to_map()
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
            temp_model = PurchaseOrderCreateResult()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRefundOrderRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: RefundOrderCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRefundOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = RefundOrderCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRefundOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundOrderResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRefundOrderResponse, self).to_map()
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
            temp_model = RefundOrderResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrderResponse, self).to_map()
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
            temp_model = OrderResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPurchaseOrderStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurchaseOrderStatusResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPurchaseOrderStatusResponse, self).to_map()
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
            temp_model = PurchaseOrderStatusResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPurchaserShopResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Shop

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPurchaserShopResponse, self).to_map()
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
            temp_model = Shop()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRefundOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRefundOrderResponse, self).to_map()
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
            temp_model = RefundResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSelectionProductRequest(TeaModel):
    def __init__(self, division_code=None, purchaser_id=None):
        self.division_code = division_code  # type: str
        self.purchaser_id = purchaser_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSelectionProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        return self


class GetSelectionProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Product

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSelectionProductResponse, self).to_map()
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
            temp_model = Product()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSelectionProductSaleInfoRequest(TeaModel):
    def __init__(self, division_code=None, purchaser_id=None):
        self.division_code = division_code  # type: str
        self.purchaser_id = purchaser_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSelectionProductSaleInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['divisionCode'] = self.division_code
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        return self


class GetSelectionProductSaleInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProductSaleInfo

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSelectionProductSaleInfoResponse, self).to_map()
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
            temp_model = ProductSaleInfo()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogisticsOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogisticsOrderListResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogisticsOrdersResponse, self).to_map()
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
            temp_model = LogisticsOrderListResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPurchaserShopsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPurchaserShopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPurchaserShopsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShopPageResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPurchaserShopsResponse, self).to_map()
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
            temp_model = ShopPageResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectionProductSaleInfosRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: ProductSaleInfoListQuery

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSelectionProductSaleInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ProductSaleInfoListQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectionProductSaleInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProductSaleInfoListResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSelectionProductSaleInfosResponse, self).to_map()
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
            temp_model = ProductSaleInfoListResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectionProductsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, purchaser_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.purchaser_id = purchaser_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSelectionProductsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')
        return self


class ListSelectionProductsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProductPageResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSelectionProductsResponse, self).to_map()
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
            temp_model = ProductPageResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectionSkuSaleInfosRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: SkuSaleInfoListQuery

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSelectionSkuSaleInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SkuSaleInfoListQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectionSkuSaleInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SkuSaleInfoListResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSelectionSkuSaleInfosResponse, self).to_map()
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
            temp_model = SkuSaleInfoListResult()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChildDivisionCodeRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: DivisionQuery

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChildDivisionCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DivisionQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChildDivisionCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DivisionPageResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChildDivisionCodeResponse, self).to_map()
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
            temp_model = DivisionPageResult()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrdersRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: OrderPageQuery

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = OrderPageQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderListResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrdersResponse, self).to_map()
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
            temp_model = OrderListResult()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderPurchaseOrderRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: PurchaseOrderRenderQuery

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenderPurchaseOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PurchaseOrderRenderQuery()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderPurchaseOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurchaseOrderRenderResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenderPurchaseOrderResponse, self).to_map()
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
            temp_model = PurchaseOrderRenderResult()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderRefundOrderRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: RefundRenderCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenderRefundOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = RefundRenderCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderRefundOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundRenderResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenderRefundOrderResponse, self).to_map()
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
            temp_model = RefundRenderResult()
            self.body = temp_model.from_map(m['body'])
        return self


