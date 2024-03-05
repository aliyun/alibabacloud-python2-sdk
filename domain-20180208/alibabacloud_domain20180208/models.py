# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptDemandRequest(TeaModel):
    def __init__(self, biz_id=None, message=None):
        self.biz_id = biz_id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AcceptDemandResponseBody(TeaModel):
    def __init__(self, bind_url=None, request_id=None):
        self.bind_url = bind_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptDemandResponse, self).to_map()
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
            temp_model = AcceptDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BidDomainRequest(TeaModel):
    def __init__(self, auction_id=None, currency=None, max_bid=None):
        self.auction_id = auction_id  # type: str
        self.currency = currency  # type: str
        self.max_bid = max_bid  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(BidDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')
        return self


class BidDomainResponseBody(TeaModel):
    def __init__(self, auction_id=None, request_id=None):
        self.auction_id = auction_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BidDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BidDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BidDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BidDomainResponse, self).to_map()
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
            temp_model = BidDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeAuctionRequestAuctionListBidRecords(TeaModel):
    def __init__(self, create_time=None, price=None, user_id=None):
        self.create_time = create_time  # type: str
        self.price = price  # type: float
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeAuctionRequestAuctionListBidRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.price is not None:
            result['Price'] = self.price
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ChangeAuctionRequestAuctionList(TeaModel):
    def __init__(self, bid_records=None, domain_name=None, end_time=None, is_reserve=None, reserve_price=None,
                 reserve_range=None, status=None, time_left=None, winner=None, winner_price=None):
        self.bid_records = bid_records  # type: list[ChangeAuctionRequestAuctionListBidRecords]
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.is_reserve = is_reserve  # type: int
        self.reserve_price = reserve_price  # type: float
        self.reserve_range = reserve_range  # type: str
        self.status = status  # type: str
        self.time_left = time_left  # type: long
        self.winner = winner  # type: str
        self.winner_price = winner_price  # type: float

    def validate(self):
        if self.bid_records:
            for k in self.bid_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeAuctionRequestAuctionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BidRecords'] = []
        if self.bid_records is not None:
            for k in self.bid_records:
                result['BidRecords'].append(k.to_map() if k else None)
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_reserve is not None:
            result['IsReserve'] = self.is_reserve
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.reserve_range is not None:
            result['ReserveRange'] = self.reserve_range
        if self.status is not None:
            result['Status'] = self.status
        if self.time_left is not None:
            result['TimeLeft'] = self.time_left
        if self.winner is not None:
            result['Winner'] = self.winner
        if self.winner_price is not None:
            result['WinnerPrice'] = self.winner_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bid_records = []
        if m.get('BidRecords') is not None:
            for k in m.get('BidRecords'):
                temp_model = ChangeAuctionRequestAuctionListBidRecords()
                self.bid_records.append(temp_model.from_map(k))
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsReserve') is not None:
            self.is_reserve = m.get('IsReserve')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('ReserveRange') is not None:
            self.reserve_range = m.get('ReserveRange')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeLeft') is not None:
            self.time_left = m.get('TimeLeft')
        if m.get('Winner') is not None:
            self.winner = m.get('Winner')
        if m.get('WinnerPrice') is not None:
            self.winner_price = m.get('WinnerPrice')
        return self


class ChangeAuctionRequest(TeaModel):
    def __init__(self, auction_list=None):
        self.auction_list = auction_list  # type: list[ChangeAuctionRequestAuctionList]

    def validate(self):
        if self.auction_list:
            for k in self.auction_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeAuctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuctionList'] = []
        if self.auction_list is not None:
            for k in self.auction_list:
                result['AuctionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auction_list = []
        if m.get('AuctionList') is not None:
            for k in m.get('AuctionList'):
                temp_model = ChangeAuctionRequestAuctionList()
                self.auction_list.append(temp_model.from_map(k))
        return self


class ChangeAuctionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeAuctionResponseBody, self).to_map()
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


class ChangeAuctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeAuctionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeAuctionResponse, self).to_map()
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
            temp_model = ChangeAuctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainStatusRequest(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CheckDomainStatusResponseBodyModule(TeaModel):
    def __init__(self, dead_date=None, domain=None, end_time=None, price=None, reg_date=None):
        self.dead_date = dead_date  # type: long
        self.domain = domain  # type: str
        self.end_time = end_time  # type: long
        self.price = price  # type: float
        self.reg_date = reg_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainStatusResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.price is not None:
            result['Price'] = self.price
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        return self


class CheckDomainStatusResponseBody(TeaModel):
    def __init__(self, error_code=None, http_status_code=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: CheckDomainStatusResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(CheckDomainStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CheckDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckDomainStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDomainStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDomainStatusResponse, self).to_map()
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
            temp_model = CheckDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSelectedDomainStatusRequest(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckSelectedDomainStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CheckSelectedDomainStatusResponseBodyModule(TeaModel):
    def __init__(self, dead_date=None, domain=None, end_time=None, premium=None, price=None, reg_date=None):
        self.dead_date = dead_date  # type: long
        self.domain = domain  # type: str
        self.end_time = end_time  # type: long
        self.premium = premium  # type: bool
        self.price = price  # type: float
        self.reg_date = reg_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckSelectedDomainStatusResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.price is not None:
            result['Price'] = self.price
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        return self


class CheckSelectedDomainStatusResponseBody(TeaModel):
    def __init__(self, error_code=None, http_status_code=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: CheckSelectedDomainStatusResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(CheckSelectedDomainStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CheckSelectedDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckSelectedDomainStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckSelectedDomainStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckSelectedDomainStatusResponse, self).to_map()
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
            temp_model = CheckSelectedDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFixedPriceDemandOrderRequest(TeaModel):
    def __init__(self, code=None, contact_id=None, domain=None, source=None):
        self.code = code  # type: str
        self.contact_id = contact_id  # type: str
        self.domain = domain  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFixedPriceDemandOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateFixedPriceDemandOrderResponseBodyModule(TeaModel):
    def __init__(self, domain=None, order_no=None, price=None):
        self.domain = domain  # type: str
        self.order_no = order_no  # type: str
        self.price = price  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFixedPriceDemandOrderResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateFixedPriceDemandOrderResponseBody(TeaModel):
    def __init__(self, error_code=None, http_status_code=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: CreateFixedPriceDemandOrderResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(CreateFixedPriceDemandOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CreateFixedPriceDemandOrderResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFixedPriceDemandOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFixedPriceDemandOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFixedPriceDemandOrderResponse, self).to_map()
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
            temp_model = CreateFixedPriceDemandOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFixedPriceSelectedOrderRequest(TeaModel):
    def __init__(self, code=None, contact_id=None, domain_name=None, expected_price=None, source=None):
        self.code = code  # type: str
        self.contact_id = contact_id  # type: str
        self.domain_name = domain_name  # type: str
        self.expected_price = expected_price  # type: float
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFixedPriceSelectedOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.expected_price is not None:
            result['ExpectedPrice'] = self.expected_price
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ExpectedPrice') is not None:
            self.expected_price = m.get('ExpectedPrice')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateFixedPriceSelectedOrderResponseBodyModule(TeaModel):
    def __init__(self, domain=None, order_no=None, price=None):
        self.domain = domain  # type: str
        self.order_no = order_no  # type: str
        self.price = price  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFixedPriceSelectedOrderResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateFixedPriceSelectedOrderResponseBody(TeaModel):
    def __init__(self, error_code=None, http_status_code=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: CreateFixedPriceSelectedOrderResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(CreateFixedPriceSelectedOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CreateFixedPriceSelectedOrderResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFixedPriceSelectedOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFixedPriceSelectedOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFixedPriceSelectedOrderResponse, self).to_map()
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
            temp_model = CreateFixedPriceSelectedOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailDemandRequest(TeaModel):
    def __init__(self, biz_id=None, message=None):
        self.biz_id = biz_id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class FailDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailDemandResponseBody, self).to_map()
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


class FailDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FailDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FailDemandResponse, self).to_map()
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
            temp_model = FailDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishDemandRequest(TeaModel):
    def __init__(self, biz_id=None, message=None):
        self.biz_id = biz_id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class FinishDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishDemandResponseBody, self).to_map()
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


class FinishDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FinishDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FinishDemandResponse, self).to_map()
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
            temp_model = FinishDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntlDomainDownloadUrlResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, dynamic_code=None, dynamic_message=None, error_args=None,
                 error_code=None, error_msg=None, http_status_code=None, request_id=None, success=None, url=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_args = error_args  # type: list[any]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntlDomainDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetIntlDomainDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIntlDomainDownloadUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIntlDomainDownloadUrlResponse, self).to_map()
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
            temp_model = GetIntlDomainDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReserveDomainUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None):
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReserveDomainUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetReserveDomainUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetReserveDomainUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReserveDomainUrlResponse, self).to_map()
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
            temp_model = GetReserveDomainUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseIntlDomainRequest(TeaModel):
    def __init__(self, auction_id=None, currency=None, price=None):
        self.auction_id = auction_id  # type: str
        self.currency = currency  # type: str
        self.price = price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseIntlDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class PurchaseIntlDomainResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, auction_id=None, dynamic_code=None, dynamic_message=None,
                 error_args=None, error_code=None, error_msg=None, http_status_code=None, request_id=None, success=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.auction_id = auction_id  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_args = error_args  # type: list[any]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseIntlDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PurchaseIntlDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurchaseIntlDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PurchaseIntlDomainResponse, self).to_map()
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
            temp_model = PurchaseIntlDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAuctionDetailRequest(TeaModel):
    def __init__(self, auction_id=None):
        self.auction_id = auction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAuctionDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        return self


class QueryAuctionDetailResponseBody(TeaModel):
    def __init__(self, auction_end_time=None, auction_id=None, book_end_time=None, booked_partner=None,
                 currency=None, delivery_time=None, domain_name=None, domain_type=None, fail_code=None, high_bid=None,
                 high_bidder=None, next_valid_bid=None, partner_type=None, pay_end_time=None, pay_price=None, pay_status=None,
                 produce_status=None, request_id=None, reserve_met=None, reserve_price=None, status=None, transfer_in_price=None,
                 your_current_bid=None, your_max_bid=None):
        self.auction_end_time = auction_end_time  # type: long
        self.auction_id = auction_id  # type: str
        self.book_end_time = book_end_time  # type: long
        self.booked_partner = booked_partner  # type: str
        self.currency = currency  # type: str
        self.delivery_time = delivery_time  # type: long
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.fail_code = fail_code  # type: str
        self.high_bid = high_bid  # type: float
        self.high_bidder = high_bidder  # type: str
        self.next_valid_bid = next_valid_bid  # type: float
        self.partner_type = partner_type  # type: str
        self.pay_end_time = pay_end_time  # type: long
        self.pay_price = pay_price  # type: float
        self.pay_status = pay_status  # type: str
        self.produce_status = produce_status  # type: str
        self.request_id = request_id  # type: str
        self.reserve_met = reserve_met  # type: bool
        self.reserve_price = reserve_price  # type: float
        self.status = status  # type: str
        self.transfer_in_price = transfer_in_price  # type: float
        self.your_current_bid = your_current_bid  # type: float
        self.your_max_bid = your_max_bid  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAuctionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.booked_partner is not None:
            result['BookedPartner'] = self.booked_partner
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.high_bid is not None:
            result['HighBid'] = self.high_bid
        if self.high_bidder is not None:
            result['HighBidder'] = self.high_bidder
        if self.next_valid_bid is not None:
            result['NextValidBid'] = self.next_valid_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.pay_end_time is not None:
            result['PayEndTime'] = self.pay_end_time
        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.produce_status is not None:
            result['ProduceStatus'] = self.produce_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserve_met is not None:
            result['ReserveMet'] = self.reserve_met
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        if self.your_current_bid is not None:
            result['YourCurrentBid'] = self.your_current_bid
        if self.your_max_bid is not None:
            result['YourMaxBid'] = self.your_max_bid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BookedPartner') is not None:
            self.booked_partner = m.get('BookedPartner')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('HighBid') is not None:
            self.high_bid = m.get('HighBid')
        if m.get('HighBidder') is not None:
            self.high_bidder = m.get('HighBidder')
        if m.get('NextValidBid') is not None:
            self.next_valid_bid = m.get('NextValidBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('PayEndTime') is not None:
            self.pay_end_time = m.get('PayEndTime')
        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('ProduceStatus') is not None:
            self.produce_status = m.get('ProduceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReserveMet') is not None:
            self.reserve_met = m.get('ReserveMet')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        if m.get('YourCurrentBid') is not None:
            self.your_current_bid = m.get('YourCurrentBid')
        if m.get('YourMaxBid') is not None:
            self.your_max_bid = m.get('YourMaxBid')
        return self


class QueryAuctionDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAuctionDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAuctionDetailResponse, self).to_map()
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
            temp_model = QueryAuctionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAuctionsRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, status=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAuctionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryAuctionsResponseBodyData(TeaModel):
    def __init__(self, auction_end_time=None, auction_id=None, book_end_time=None, booked_partner=None,
                 currency=None, delivery_time=None, domain_name=None, domain_type=None, fail_code=None, high_bid=None,
                 high_bidder=None, next_valid_bid=None, partner_type=None, pay_end_time=None, pay_price=None, pay_status=None,
                 produce_status=None, reserve_max=None, reserve_met=None, reserve_min=None, reserve_price=None, status=None,
                 transfer_in_price=None, your_current_bid=None, your_max_bid=None):
        self.auction_end_time = auction_end_time  # type: long
        self.auction_id = auction_id  # type: str
        self.book_end_time = book_end_time  # type: long
        self.booked_partner = booked_partner  # type: str
        self.currency = currency  # type: str
        self.delivery_time = delivery_time  # type: long
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str
        self.fail_code = fail_code  # type: str
        self.high_bid = high_bid  # type: float
        self.high_bidder = high_bidder  # type: str
        self.next_valid_bid = next_valid_bid  # type: float
        self.partner_type = partner_type  # type: str
        self.pay_end_time = pay_end_time  # type: long
        self.pay_price = pay_price  # type: float
        self.pay_status = pay_status  # type: str
        self.produce_status = produce_status  # type: str
        self.reserve_max = reserve_max  # type: long
        self.reserve_met = reserve_met  # type: bool
        self.reserve_min = reserve_min  # type: long
        self.reserve_price = reserve_price  # type: long
        self.status = status  # type: str
        self.transfer_in_price = transfer_in_price  # type: float
        self.your_current_bid = your_current_bid  # type: float
        self.your_max_bid = your_max_bid  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAuctionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.booked_partner is not None:
            result['BookedPartner'] = self.booked_partner
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.high_bid is not None:
            result['HighBid'] = self.high_bid
        if self.high_bidder is not None:
            result['HighBidder'] = self.high_bidder
        if self.next_valid_bid is not None:
            result['NextValidBid'] = self.next_valid_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.pay_end_time is not None:
            result['PayEndTime'] = self.pay_end_time
        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.produce_status is not None:
            result['ProduceStatus'] = self.produce_status
        if self.reserve_max is not None:
            result['ReserveMax'] = self.reserve_max
        if self.reserve_met is not None:
            result['ReserveMet'] = self.reserve_met
        if self.reserve_min is not None:
            result['ReserveMin'] = self.reserve_min
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        if self.your_current_bid is not None:
            result['YourCurrentBid'] = self.your_current_bid
        if self.your_max_bid is not None:
            result['YourMaxBid'] = self.your_max_bid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BookedPartner') is not None:
            self.booked_partner = m.get('BookedPartner')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('HighBid') is not None:
            self.high_bid = m.get('HighBid')
        if m.get('HighBidder') is not None:
            self.high_bidder = m.get('HighBidder')
        if m.get('NextValidBid') is not None:
            self.next_valid_bid = m.get('NextValidBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('PayEndTime') is not None:
            self.pay_end_time = m.get('PayEndTime')
        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('ProduceStatus') is not None:
            self.produce_status = m.get('ProduceStatus')
        if m.get('ReserveMax') is not None:
            self.reserve_max = m.get('ReserveMax')
        if m.get('ReserveMet') is not None:
            self.reserve_met = m.get('ReserveMet')
        if m.get('ReserveMin') is not None:
            self.reserve_min = m.get('ReserveMin')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        if m.get('YourCurrentBid') is not None:
            self.your_current_bid = m.get('YourCurrentBid')
        if m.get('YourMaxBid') is not None:
            self.your_max_bid = m.get('YourMaxBid')
        return self


class QueryAuctionsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[QueryAuctionsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAuctionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAuctionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryAuctionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAuctionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAuctionsResponse, self).to_map()
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
            temp_model = QueryAuctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBidRecordsRequest(TeaModel):
    def __init__(self, auction_id=None, current_page=None, page_size=None):
        self.auction_id = auction_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBidRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBidRecordsResponseBodyData(TeaModel):
    def __init__(self, bid=None, bid_time=None, bidder=None, currency=None, domain_name=None):
        self.bid = bid  # type: float
        self.bid_time = bid_time  # type: long
        self.bidder = bidder  # type: str
        self.currency = currency  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBidRecordsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.bid_time is not None:
            result['BidTime'] = self.bid_time
        if self.bidder is not None:
            result['Bidder'] = self.bidder
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BidTime') is not None:
            self.bid_time = m.get('BidTime')
        if m.get('Bidder') is not None:
            self.bidder = m.get('Bidder')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryBidRecordsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[QueryBidRecordsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBidRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBidRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBidRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBidRecordsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBidRecordsResponse, self).to_map()
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
            temp_model = QueryBidRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBookingDomainInfoRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBookingDomainInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryBookingDomainInfoResponseBody(TeaModel):
    def __init__(self, auction_id=None, book_end_time=None, currency=None, max_bid=None, partner_type=None,
                 request_id=None, transfer_in_price=None):
        self.auction_id = auction_id  # type: int
        self.book_end_time = book_end_time  # type: long
        self.currency = currency  # type: str
        self.max_bid = max_bid  # type: float
        self.partner_type = partner_type  # type: str
        self.request_id = request_id  # type: str
        self.transfer_in_price = transfer_in_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBookingDomainInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        return self


class QueryBookingDomainInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBookingDomainInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBookingDomainInfoResponse, self).to_map()
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
            temp_model = QueryBookingDomainInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBrokerDemandRequest(TeaModel):
    def __init__(self, biz_id=None, current_page=None, page_size=None, status=None):
        self.biz_id = biz_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBrokerDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryBrokerDemandResponseBodyData(TeaModel):
    def __init__(self, audit_status=None, bargain_seller_mobile=None, bargain_seller_price=None, biz_id=None,
                 demand_domain=None, demand_price=None, description=None, mobile=None, order_type=None, partner_domain=None,
                 pay_domain=None, pay_price=None, pay_time=None, produce_type=None, publish_time=None, purchase_status=None,
                 service_pay_price=None, status=None):
        self.audit_status = audit_status  # type: int
        self.bargain_seller_mobile = bargain_seller_mobile  # type: str
        self.bargain_seller_price = bargain_seller_price  # type: float
        self.biz_id = biz_id  # type: str
        self.demand_domain = demand_domain  # type: str
        self.demand_price = demand_price  # type: float
        self.description = description  # type: str
        self.mobile = mobile  # type: str
        self.order_type = order_type  # type: int
        self.partner_domain = partner_domain  # type: str
        self.pay_domain = pay_domain  # type: str
        self.pay_price = pay_price  # type: float
        self.pay_time = pay_time  # type: long
        self.produce_type = produce_type  # type: int
        self.publish_time = publish_time  # type: long
        self.purchase_status = purchase_status  # type: int
        self.service_pay_price = service_pay_price  # type: float
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBrokerDemandResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.bargain_seller_mobile is not None:
            result['BargainSellerMobile'] = self.bargain_seller_mobile
        if self.bargain_seller_price is not None:
            result['BargainSellerPrice'] = self.bargain_seller_price
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.demand_domain is not None:
            result['DemandDomain'] = self.demand_domain
        if self.demand_price is not None:
            result['DemandPrice'] = self.demand_price
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.partner_domain is not None:
            result['PartnerDomain'] = self.partner_domain
        if self.pay_domain is not None:
            result['PayDomain'] = self.pay_domain
        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.purchase_status is not None:
            result['PurchaseStatus'] = self.purchase_status
        if self.service_pay_price is not None:
            result['ServicePayPrice'] = self.service_pay_price
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BargainSellerMobile') is not None:
            self.bargain_seller_mobile = m.get('BargainSellerMobile')
        if m.get('BargainSellerPrice') is not None:
            self.bargain_seller_price = m.get('BargainSellerPrice')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DemandDomain') is not None:
            self.demand_domain = m.get('DemandDomain')
        if m.get('DemandPrice') is not None:
            self.demand_price = m.get('DemandPrice')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PartnerDomain') is not None:
            self.partner_domain = m.get('PartnerDomain')
        if m.get('PayDomain') is not None:
            self.pay_domain = m.get('PayDomain')
        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PurchaseStatus') is not None:
            self.purchase_status = m.get('PurchaseStatus')
        if m.get('ServicePayPrice') is not None:
            self.service_pay_price = m.get('ServicePayPrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryBrokerDemandResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[QueryBrokerDemandResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBrokerDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBrokerDemandResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBrokerDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBrokerDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBrokerDemandResponse, self).to_map()
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
            temp_model = QueryBrokerDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBrokerDemandRecordRequest(TeaModel):
    def __init__(self, biz_id=None, current_page=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBrokerDemandRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord(TeaModel):
    def __init__(self, biz_id=None, create_time=None, description=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class QueryBrokerDemandRecordResponseBodyData(TeaModel):
    def __init__(self, broker_demand_record=None):
        self.broker_demand_record = broker_demand_record  # type: list[QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord]

    def validate(self):
        if self.broker_demand_record:
            for k in self.broker_demand_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBrokerDemandRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BrokerDemandRecord'] = []
        if self.broker_demand_record is not None:
            for k in self.broker_demand_record:
                result['BrokerDemandRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.broker_demand_record = []
        if m.get('BrokerDemandRecord') is not None:
            for k in m.get('BrokerDemandRecord'):
                temp_model = QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord()
                self.broker_demand_record.append(temp_model.from_map(k))
        return self


class QueryBrokerDemandRecordResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryBrokerDemandRecordResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryBrokerDemandRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryBrokerDemandRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBrokerDemandRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBrokerDemandRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBrokerDemandRecordResponse, self).to_map()
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
            temp_model = QueryBrokerDemandRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainTransferStatusRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainTransferStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryDomainTransferStatusResponseBodyDomainTransferStatus(TeaModel):
    def __init__(self, domain_name=None, domain_status_description=None):
        self.domain_name = domain_name  # type: str
        self.domain_status_description = domain_status_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainTransferStatusResponseBodyDomainTransferStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status_description is not None:
            result['DomainStatusDescription'] = self.domain_status_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatusDescription') is not None:
            self.domain_status_description = m.get('DomainStatusDescription')
        return self


class QueryDomainTransferStatusResponseBody(TeaModel):
    def __init__(self, domain_transfer_status=None, request_id=None):
        self.domain_transfer_status = domain_transfer_status  # type: list[QueryDomainTransferStatusResponseBodyDomainTransferStatus]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_transfer_status:
            for k in self.domain_transfer_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDomainTransferStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainTransferStatus'] = []
        if self.domain_transfer_status is not None:
            for k in self.domain_transfer_status:
                result['DomainTransferStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_transfer_status = []
        if m.get('DomainTransferStatus') is not None:
            for k in m.get('DomainTransferStatus'):
                temp_model = QueryDomainTransferStatusResponseBodyDomainTransferStatus()
                self.domain_transfer_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDomainTransferStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainTransferStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainTransferStatusResponse, self).to_map()
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
            temp_model = QueryDomainTransferStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedDomainsRequest(TeaModel):
    def __init__(self, current_page=None, domain_name=None, end_operation_time=None, op_time_order=None,
                 operation_status=None, page_size=None, product_type=None, start_operation_time=None, update_time_order=None):
        self.current_page = current_page  # type: int
        self.domain_name = domain_name  # type: str
        self.end_operation_time = end_operation_time  # type: str
        self.op_time_order = op_time_order  # type: bool
        self.operation_status = operation_status  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: int
        self.start_operation_time = start_operation_time  # type: str
        self.update_time_order = update_time_order  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_operation_time is not None:
            result['EndOperationTime'] = self.end_operation_time
        if self.op_time_order is not None:
            result['OpTimeOrder'] = self.op_time_order
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.start_operation_time is not None:
            result['StartOperationTime'] = self.start_operation_time
        if self.update_time_order is not None:
            result['UpdateTimeOrder'] = self.update_time_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndOperationTime') is not None:
            self.end_operation_time = m.get('EndOperationTime')
        if m.get('OpTimeOrder') is not None:
            self.op_time_order = m.get('OpTimeOrder')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('StartOperationTime') is not None:
            self.start_operation_time = m.get('StartOperationTime')
        if m.get('UpdateTimeOrder') is not None:
            self.update_time_order = m.get('UpdateTimeOrder')
        return self


class QueryPurchasedDomainsResponseBodyData(TeaModel):
    def __init__(self, delivery_time=None, domain_name=None, operation_status=None, operation_time=None,
                 product_type=None, trade_money=None):
        self.delivery_time = delivery_time  # type: str
        self.domain_name = domain_name  # type: str
        self.operation_status = operation_status  # type: str
        self.operation_time = operation_time  # type: str
        self.product_type = product_type  # type: str
        self.trade_money = trade_money  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedDomainsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.trade_money is not None:
            result['TradeMoney'] = self.trade_money
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TradeMoney') is not None:
            self.trade_money = m.get('TradeMoney')
        return self


class QueryPurchasedDomainsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[QueryPurchasedDomainsResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPurchasedDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryPurchasedDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryPurchasedDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPurchasedDomainsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPurchasedDomainsResponse, self).to_map()
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
            temp_model = QueryPurchasedDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordDemandRequest(TeaModel):
    def __init__(self, biz_id=None, message=None):
        self.biz_id = biz_id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecordDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordDemandResponseBody, self).to_map()
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


class RecordDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecordDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecordDemandResponse, self).to_map()
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
            temp_model = RecordDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseDemandRequest(TeaModel):
    def __init__(self, biz_id=None, message=None):
        self.biz_id = biz_id  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RefuseDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseDemandResponseBody, self).to_map()
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


class RefuseDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefuseDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefuseDemandResponse, self).to_map()
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
            temp_model = RefuseDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestPayDemandRequest(TeaModel):
    def __init__(self, biz_id=None, domain_name=None, message=None, price=None, produce_type=None):
        self.biz_id = biz_id  # type: str
        self.domain_name = domain_name  # type: str
        self.message = message  # type: str
        self.price = price  # type: float
        self.produce_type = produce_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestPayDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        return self


class RequestPayDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestPayDemandResponseBody, self).to_map()
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


class RequestPayDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestPayDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestPayDemandResponse, self).to_map()
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
            temp_model = RequestPayDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveDomainRequest(TeaModel):
    def __init__(self, channels=None, domain_name=None):
        self.channels = channels  # type: list[str]
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReserveDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ReserveDomainResponseBody(TeaModel):
    def __init__(self, auction_id=None, request_id=None):
        self.auction_id = auction_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReserveDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReserveDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReserveDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReserveDomainResponse, self).to_map()
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
            temp_model = ReserveDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveIntlDomainRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReserveIntlDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ReserveIntlDomainResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, auction_id=None, dynamic_code=None, dynamic_message=None,
                 error_args=None, error_code=None, error_msg=None, http_status_code=None, request_id=None, success=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.auction_id = auction_id  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_args = error_args  # type: list[any]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReserveIntlDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReserveIntlDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReserveIntlDomainResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReserveIntlDomainResponse, self).to_map()
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
            temp_model = ReserveIntlDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectedDomainListRequest(TeaModel):
    def __init__(self, list_date=None):
        self.list_date = list_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectedDomainListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_date is not None:
            result['ListDate'] = self.list_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListDate') is not None:
            self.list_date = m.get('ListDate')
        return self


class SelectedDomainListResponseBodyModule(TeaModel):
    def __init__(self, download_url=None):
        self.download_url = download_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectedDomainListResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class SelectedDomainListResponseBody(TeaModel):
    def __init__(self, error_code=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.module = module  # type: SelectedDomainListResponseBodyModule
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(SelectedDomainListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Module') is not None:
            temp_model = SelectedDomainListResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectedDomainListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SelectedDomainListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SelectedDomainListResponse, self).to_map()
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
            temp_model = SelectedDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPurchaseInfoRequest(TeaModel):
    def __init__(self, biz_id=None, purchase_currency=None, purchase_price=None, purchase_proofs=None):
        self.biz_id = biz_id  # type: str
        self.purchase_currency = purchase_currency  # type: str
        self.purchase_price = purchase_price  # type: float
        self.purchase_proofs = purchase_proofs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPurchaseInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.purchase_currency is not None:
            result['PurchaseCurrency'] = self.purchase_currency
        if self.purchase_price is not None:
            result['PurchasePrice'] = self.purchase_price
        if self.purchase_proofs is not None:
            result['PurchaseProofs'] = self.purchase_proofs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PurchaseCurrency') is not None:
            self.purchase_currency = m.get('PurchaseCurrency')
        if m.get('PurchasePrice') is not None:
            self.purchase_price = m.get('PurchasePrice')
        if m.get('PurchaseProofs') is not None:
            self.purchase_proofs = m.get('PurchaseProofs')
        return self


class SubmitPurchaseInfoResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, dynamic_code=None, dynamic_message=None, error_args=None,
                 error_code=None, error_msg=None, http_status_code=None, module=None, request_id=None, success=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_args = error_args  # type: list[any]
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.module = module  # type: any
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPurchaseInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitPurchaseInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitPurchaseInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitPurchaseInfoResponse, self).to_map()
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
            temp_model = SubmitPurchaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePartnerReservePriceRequest(TeaModel):
    def __init__(self, bidding_id=None, domain_name=None, partner_type=None, reserve_price=None):
        self.bidding_id = bidding_id  # type: int
        self.domain_name = domain_name  # type: str
        self.partner_type = partner_type  # type: str
        self.reserve_price = reserve_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePartnerReservePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bidding_id is not None:
            result['BiddingId'] = self.bidding_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BiddingId') is not None:
            self.bidding_id = m.get('BiddingId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        return self


class UpdatePartnerReservePriceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePartnerReservePriceResponseBody, self).to_map()
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


class UpdatePartnerReservePriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePartnerReservePriceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePartnerReservePriceResponse, self).to_map()
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
            temp_model = UpdatePartnerReservePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


