# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchDispatchGameSlotRequest(TeaModel):
    def __init__(self, queue_user_list=None):
        self.queue_user_list = queue_user_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDispatchGameSlotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_user_list is not None:
            result['QueueUserList'] = self.queue_user_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueueUserList') is not None:
            self.queue_user_list = m.get('QueueUserList')
        return self


class BatchDispatchGameSlotResponseBodyQueueResultList(TeaModel):
    def __init__(self, region_name=None, game_session=None, user_id=None, queue_state=None, message=None,
                 game_id=None, queue_code=None):
        self.region_name = region_name  # type: str
        self.game_session = game_session  # type: str
        self.user_id = user_id  # type: str
        self.queue_state = queue_state  # type: int
        self.message = message  # type: str
        self.game_id = game_id  # type: str
        self.queue_code = queue_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDispatchGameSlotResponseBodyQueueResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class BatchDispatchGameSlotResponseBody(TeaModel):
    def __init__(self, request_id=None, queue_result_list=None):
        self.request_id = request_id  # type: str
        self.queue_result_list = queue_result_list  # type: list[BatchDispatchGameSlotResponseBodyQueueResultList]

    def validate(self):
        if self.queue_result_list:
            for k in self.queue_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchDispatchGameSlotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['QueueResultList'] = []
        if self.queue_result_list is not None:
            for k in self.queue_result_list:
                result['QueueResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.queue_result_list = []
        if m.get('QueueResultList') is not None:
            for k in m.get('QueueResultList'):
                temp_model = BatchDispatchGameSlotResponseBodyQueueResultList()
                self.queue_result_list.append(temp_model.from_map(k))
        return self


class BatchDispatchGameSlotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDispatchGameSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDispatchGameSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopGameSessionsRequest(TeaModel):
    def __init__(self, project_id=None, game_id=None, token=None, reason=None, track_info=None, tags=None):
        self.project_id = project_id  # type: str
        self.game_id = game_id  # type: str
        self.token = token  # type: str
        self.reason = reason  # type: str
        self.track_info = track_info  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopGameSessionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.token is not None:
            result['Token'] = self.token
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class BatchStopGameSessionsResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, project_id=None, queue_state=None, message=None, game_id=None,
                 track_info=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.project_id = project_id  # type: str
        self.queue_state = queue_state  # type: int
        self.message = message  # type: str
        self.game_id = game_id  # type: str
        self.track_info = track_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopGameSessionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        return self


class BatchStopGameSessionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStopGameSessionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopGameSessionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchStopGameSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseOrderRequest(TeaModel):
    def __init__(self, buyer_account_id=None, order_id=None, account_domain=None):
        self.buyer_account_id = buyer_account_id  # type: str
        self.order_id = order_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CloseOrderResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(self, buyer_account_id=None, item_id=None, sku_id=None, origin_price=None, settlement_price=None,
                 amount=None, idempotent_code=None, account_domain=None):
        self.buyer_account_id = buyer_account_id  # type: str
        self.item_id = item_id  # type: str
        self.sku_id = sku_id  # type: str
        self.origin_price = origin_price  # type: long
        self.settlement_price = settlement_price  # type: long
        self.amount = amount  # type: long
        self.idempotent_code = idempotent_code  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.idempotent_code is not None:
            result['IdempotentCode'] = self.idempotent_code
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('IdempotentCode') is not None:
            self.idempotent_code = m.get('IdempotentCode')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(self, status=None, finish_time=None, create_time=None, auto_unlock_time=None,
                 apply_delivery_time=None, item_id=None, origin_price=None, buyer_account_id=None, amount=None, sku_id=None,
                 settlement_price=None, order_id=None, account_domain=None):
        self.status = status  # type: str
        self.finish_time = finish_time  # type: long
        self.create_time = create_time  # type: long
        self.auto_unlock_time = auto_unlock_time  # type: long
        self.apply_delivery_time = apply_delivery_time  # type: long
        self.item_id = item_id  # type: str
        self.origin_price = origin_price  # type: long
        self.buyer_account_id = buyer_account_id  # type: str
        self.amount = amount  # type: long
        self.sku_id = sku_id  # type: str
        self.settlement_price = settlement_price  # type: long
        self.order_id = order_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateOrderResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(self, session=None, current_token=None, client_token=None):
        self.session = session  # type: str
        self.current_token = current_token  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        if self.current_token is not None:
            result['CurrentToken'] = self.current_token
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        if m.get('CurrentToken') is not None:
            self.current_token = m.get('CurrentToken')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(self, token=None):
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateTokenResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeliveryOrderRequest(TeaModel):
    def __init__(self, buyer_account_id=None, order_id=None, account_domain=None):
        self.buyer_account_id = buyer_account_id  # type: str
        self.order_id = order_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliveryOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class DeliveryOrderResponseBodyData(TeaModel):
    def __init__(self, delivery_status=None):
        self.delivery_status = delivery_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliveryOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        return self


class DeliveryOrderResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: DeliveryOrderResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeliveryOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeliveryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DeliveryOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeliveryOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeliveryOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeliveryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DispatchGameSlotRequest(TeaModel):
    def __init__(self, game_id=None, access_key=None, region_name=None, user_id=None, biz_param=None, cancel=None,
                 game_session=None, game_start_param=None, game_command=None, system_info=None, client_ip=None, reconnect=None,
                 tags=None):
        self.game_id = game_id  # type: str
        self.access_key = access_key  # type: str
        self.region_name = region_name  # type: str
        self.user_id = user_id  # type: str
        self.biz_param = biz_param  # type: str
        self.cancel = cancel  # type: bool
        self.game_session = game_session  # type: str
        self.game_start_param = game_start_param  # type: str
        self.game_command = game_command  # type: str
        self.system_info = system_info  # type: str
        self.client_ip = client_ip  # type: str
        self.reconnect = reconnect  # type: bool
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DispatchGameSlotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.cancel is not None:
            result['Cancel'] = self.cancel
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.game_start_param is not None:
            result['GameStartParam'] = self.game_start_param
        if self.game_command is not None:
            result['GameCommand'] = self.game_command
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.reconnect is not None:
            result['Reconnect'] = self.reconnect
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('GameStartParam') is not None:
            self.game_start_param = m.get('GameStartParam')
        if m.get('GameCommand') is not None:
            self.game_command = m.get('GameCommand')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Reconnect') is not None:
            self.reconnect = m.get('Reconnect')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DispatchGameSlotResponseBody(TeaModel):
    def __init__(self, request_id=None, region_name=None, game_session=None, user_id=None, queue_state=None,
                 message=None, game_id=None, queue_code=None):
        self.request_id = request_id  # type: str
        self.region_name = region_name  # type: str
        self.game_session = game_session  # type: str
        self.user_id = user_id  # type: str
        self.queue_state = queue_state  # type: int
        self.message = message  # type: str
        self.game_id = game_id  # type: str
        self.queue_code = queue_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DispatchGameSlotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class DispatchGameSlotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DispatchGameSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DispatchGameSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameCcuRequest(TeaModel):
    def __init__(self, game_id=None, region_name=None, access_key=None):
        self.game_id = game_id  # type: str
        self.region_name = region_name  # type: str
        self.access_key = access_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGameCcuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetGameCcuResponseBodyDataList(TeaModel):
    def __init__(self, game_id=None, ccu=None, region_id=None):
        self.game_id = game_id  # type: str
        self.ccu = ccu  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGameCcuResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.ccu is not None:
            result['Ccu'] = self.ccu
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Ccu') is not None:
            self.ccu = m.get('Ccu')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetGameCcuResponseBody(TeaModel):
    def __init__(self, request_id=None, data_list=None):
        self.request_id = request_id  # type: str
        self.data_list = data_list  # type: list[GetGameCcuResponseBodyDataList]

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGameCcuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = GetGameCcuResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class GetGameCcuResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGameCcuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGameCcuResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGameCcuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameStockRequest(TeaModel):
    def __init__(self, game_id=None, access_key=None, user_level=None):
        self.game_id = game_id  # type: str
        self.access_key = access_key  # type: str
        self.user_level = user_level  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGameStockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        return self


class GetGameStockResponseBodyInstanceStockList(TeaModel):
    def __init__(self, available_slots=None, regin_name=None, instance_id=None, user_level=None, instance_spec=None):
        self.available_slots = available_slots  # type: long
        self.regin_name = regin_name  # type: str
        self.instance_id = instance_id  # type: str
        self.user_level = user_level  # type: long
        self.instance_spec = instance_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGameStockResponseBodyInstanceStockList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_slots is not None:
            result['AvailableSlots'] = self.available_slots
        if self.regin_name is not None:
            result['ReginName'] = self.regin_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableSlots') is not None:
            self.available_slots = m.get('AvailableSlots')
        if m.get('ReginName') is not None:
            self.regin_name = m.get('ReginName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        return self


class GetGameStockResponseBody(TeaModel):
    def __init__(self, message=None, game_id=None, request_id=None, instance_stock_list=None):
        self.message = message  # type: str
        self.game_id = game_id  # type: str
        self.request_id = request_id  # type: str
        self.instance_stock_list = instance_stock_list  # type: list[GetGameStockResponseBodyInstanceStockList]

    def validate(self):
        if self.instance_stock_list:
            for k in self.instance_stock_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGameStockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStockList'] = []
        if self.instance_stock_list is not None:
            for k in self.instance_stock_list:
                result['InstanceStockList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_stock_list = []
        if m.get('InstanceStockList') is not None:
            for k in m.get('InstanceStockList'):
                temp_model = GetGameStockResponseBodyInstanceStockList()
                self.instance_stock_list.append(temp_model.from_map(k))
        return self


class GetGameStockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGameStockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGameStockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGameStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemRequest(TeaModel):
    def __init__(self, item_id=None):
        self.item_id = item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetItemResponseBodyDataGames(TeaModel):
    def __init__(self, name=None, game_id=None):
        self.name = name  # type: str
        self.game_id = game_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetItemResponseBodyDataGames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class GetItemResponseBodyDataSkusSaleProps(TeaModel):
    def __init__(self, value=None, value_id=None, property_id=None, property_name=None):
        self.value = value  # type: str
        self.value_id = value_id  # type: long
        self.property_id = property_id  # type: long
        self.property_name = property_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetItemResponseBodyDataSkusSaleProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        return self


class GetItemResponseBodyDataSkus(TeaModel):
    def __init__(self, status=None, create_time=None, sku_id=None, item_id=None, sale_price=None, origin_price=None,
                 modify_time=None, sale_props=None):
        self.status = status  # type: int
        self.create_time = create_time  # type: long
        self.sku_id = sku_id  # type: str
        self.item_id = item_id  # type: str
        self.sale_price = sale_price  # type: long
        self.origin_price = origin_price  # type: long
        self.modify_time = modify_time  # type: long
        self.sale_props = sale_props  # type: list[GetItemResponseBodyDataSkusSaleProps]

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetItemResponseBodyDataSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = GetItemResponseBodyDataSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        return self


class GetItemResponseBodyData(TeaModel):
    def __init__(self, status=None, supplier=None, description=None, create_time=None, seller_id=None,
                 category_id=None, title=None, item_id=None, sale_price=None, origin_price=None, modify_time=None, games=None,
                 skus=None):
        self.status = status  # type: int
        self.supplier = supplier  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: long
        self.seller_id = seller_id  # type: str
        self.category_id = category_id  # type: long
        self.title = title  # type: str
        self.item_id = item_id  # type: str
        self.sale_price = sale_price  # type: long
        self.origin_price = origin_price  # type: long
        self.modify_time = modify_time  # type: long
        self.games = games  # type: list[GetItemResponseBodyDataGames]
        self.skus = skus  # type: list[GetItemResponseBodyDataSkus]

    def validate(self):
        if self.games:
            for k in self.games:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetItemResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.title is not None:
            result['Title'] = self.title
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = GetItemResponseBodyDataGames()
                self.games.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = GetItemResponseBodyDataSkus()
                self.skus.append(temp_model.from_map(k))
        return self


class GetItemResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: GetItemResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetItemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetItemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetItemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOutAccountBindDetailRequest(TeaModel):
    def __init__(self, out_account_type=None, account_id=None, account_domain=None):
        self.out_account_type = out_account_type  # type: str
        self.account_id = account_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOutAccountBindDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class GetOutAccountBindDetailResponseBodyData(TeaModel):
    def __init__(self, out_account_id=None, token=None, bind_status=None, token_expire_time=None,
                 out_account_type=None):
        self.out_account_id = out_account_id  # type: str
        self.token = token  # type: str
        self.bind_status = bind_status  # type: int
        self.token_expire_time = token_expire_time  # type: long
        self.out_account_type = out_account_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOutAccountBindDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_account_id is not None:
            result['OutAccountId'] = self.out_account_id
        if self.token is not None:
            result['Token'] = self.token
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutAccountId') is not None:
            self.out_account_id = m.get('OutAccountId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        return self


class GetOutAccountBindDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: GetOutAccountBindDetailResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOutAccountBindDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetOutAccountBindDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetOutAccountBindDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOutAccountBindDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOutAccountBindDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOutAccountBindDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionRequest(TeaModel):
    def __init__(self, token=None):
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetSessionResponseBodyData(TeaModel):
    def __init__(self, session=None):
        self.session = session  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        return self


class GetSessionResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: GetSessionResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSessionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSessionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStopGameTokenRequest(TeaModel):
    def __init__(self, game_id=None, access_key=None):
        self.game_id = game_id  # type: str
        self.access_key = access_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStopGameTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetStopGameTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None, expire_time=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: str
        self.expire_time = expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStopGameTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetStopGameTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStopGameTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStopGameTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetStopGameTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBoughtGamesRequest(TeaModel):
    def __init__(self, account_id=None, account_domain=None, page_number=None, page_size=None):
        self.account_id = account_id  # type: str
        self.account_domain = account_domain  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBoughtGamesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBoughtGamesResponseBodyItems(TeaModel):
    def __init__(self, end_time=None, start_time=None, game_id=None, game_name=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.game_id = game_id  # type: str
        self.game_name = game_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBoughtGamesResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_name is not None:
            result['GameName'] = self.game_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameName') is not None:
            self.game_name = m.get('GameName')
        return self


class ListBoughtGamesResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, items=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.items = items  # type: list[ListBoughtGamesResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBoughtGamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListBoughtGamesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListBoughtGamesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBoughtGamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBoughtGamesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBoughtGamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGameRequest(TeaModel):
    def __init__(self, project_id=None, page_no=None, page_size=None, tenant_id=None):
        self.project_id = project_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryGameResponseBodyData(TeaModel):
    def __init__(self, version=None, project_id=None, gmt_create=None, game_id=None, name=None, tenant_id=None):
        self.version = version  # type: str
        self.project_id = project_id  # type: long
        self.gmt_create = gmt_create  # type: str
        self.game_id = game_id  # type: long
        self.name = name  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryGameResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, data=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.data = data  # type: list[QueryGameResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryGameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryGameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryGameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryGameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryGameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryItemsResponseBodyDataItemsSkusSaleProps(TeaModel):
    def __init__(self, value=None, value_id=None, property_name=None, property_id=None):
        self.value = value  # type: str
        self.value_id = value_id  # type: long
        self.property_name = property_name  # type: str
        self.property_id = property_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemsResponseBodyDataItemsSkusSaleProps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class QueryItemsResponseBodyDataItemsSkus(TeaModel):
    def __init__(self, status=None, create_time=None, sku_id=None, item_id=None, sale_price=None, origin_price=None,
                 modify_time=None, sale_props=None):
        self.status = status  # type: int
        self.create_time = create_time  # type: long
        self.sku_id = sku_id  # type: str
        self.item_id = item_id  # type: str
        self.sale_price = sale_price  # type: long
        self.origin_price = origin_price  # type: long
        self.modify_time = modify_time  # type: long
        self.sale_props = sale_props  # type: list[QueryItemsResponseBodyDataItemsSkusSaleProps]

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemsResponseBodyDataItemsSkus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = QueryItemsResponseBodyDataItemsSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBodyDataItemsGames(TeaModel):
    def __init__(self, name=None, game_id=None):
        self.name = name  # type: str
        self.game_id = game_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemsResponseBodyDataItemsGames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class QueryItemsResponseBodyDataItems(TeaModel):
    def __init__(self, status=None, supplier=None, description=None, create_time=None, seller_id=None,
                 category_id=None, item_id=None, title=None, sale_price=None, origin_price=None, modify_time=None, skus=None,
                 games=None):
        self.status = status  # type: int
        self.supplier = supplier  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: long
        self.seller_id = seller_id  # type: str
        self.category_id = category_id  # type: long
        self.item_id = item_id  # type: str
        self.title = title  # type: str
        self.sale_price = sale_price  # type: long
        self.origin_price = origin_price  # type: long
        self.modify_time = modify_time  # type: long
        self.skus = skus  # type: list[QueryItemsResponseBodyDataItemsSkus]
        self.games = games  # type: list[QueryItemsResponseBodyDataItemsGames]

    def validate(self):
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()
        if self.games:
            for k in self.games:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemsResponseBodyDataItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.title is not None:
            result['Title'] = self.title
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = QueryItemsResponseBodyDataItemsSkus()
                self.skus.append(temp_model.from_map(k))
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = QueryItemsResponseBodyDataItemsGames()
                self.games.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, items=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long
        self.items = items  # type: list[QueryItemsResponseBodyDataItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryItemsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryItemsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBody(TeaModel):
    def __init__(self, http_status_code=None, request_id=None, success=None, data=None):
        self.http_status_code = http_status_code  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.data = data  # type: QueryItemsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = QueryItemsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryItemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderRequest(TeaModel):
    def __init__(self, buyer_account_id=None, order_id=None, account_domain=None):
        self.buyer_account_id = buyer_account_id  # type: str
        self.order_id = order_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOrderResponseBodyData(TeaModel):
    def __init__(self, status=None, finish_time=None, create_time=None, auto_unlock_time=None,
                 apply_delivery_time=None, item_id=None, origin_price=None, buyer_account_id=None, amount=None, sku_id=None,
                 settlement_price=None, order_id=None, account_domain=None):
        self.status = status  # type: str
        self.finish_time = finish_time  # type: long
        self.create_time = create_time  # type: long
        self.auto_unlock_time = auto_unlock_time  # type: long
        self.apply_delivery_time = apply_delivery_time  # type: long
        self.item_id = item_id  # type: str
        self.origin_price = origin_price  # type: long
        self.buyer_account_id = buyer_account_id  # type: str
        self.amount = amount  # type: long
        self.sku_id = sku_id  # type: str
        self.settlement_price = settlement_price  # type: long
        self.order_id = order_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOrderResponseBody(TeaModel):
    def __init__(self, delivery_status=None, request_id=None, refund_status=None, data=None):
        self.delivery_status = delivery_status  # type: str
        self.request_id = request_id  # type: str
        self.refund_status = refund_status  # type: str
        self.data = data  # type: QueryOrderResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('Data') is not None:
            temp_model = QueryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOutAccountBindStatusRequest(TeaModel):
    def __init__(self, account_id=None, game_id=None, account_domain=None):
        self.account_id = account_id  # type: str
        self.game_id = game_id  # type: str
        self.account_domain = account_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOutAccountBindStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOutAccountBindStatusResponseBodyData(TeaModel):
    def __init__(self, bind_status=None):
        self.bind_status = bind_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOutAccountBindStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        return self


class QueryOutAccountBindStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryOutAccountBindStatusResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOutAccountBindStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryOutAccountBindStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOutAccountBindStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOutAccountBindStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOutAccountBindStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOutAccountBindStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, project_id=None, tenant_id=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: long
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBodyData(TeaModel):
    def __init__(self, name=None, id=None, tenant_id=None):
        self.name = name  # type: str
        self.id = id  # type: long
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, data=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.data = data  # type: list[QueryProjectResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTenantRequest(TeaModel):
    def __init__(self, param=None, page_no=None, page_size=None):
        self.param = param  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTenantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTenantResponseBodyData(TeaModel):
    def __init__(self, gmt_create=None, name=None, tenant_id=None):
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTenantResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTenantResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, data=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.data = data  # type: list[QueryTenantResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTenantResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTenantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTenantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipTrialPolicyRequest(TeaModel):
    def __init__(self, game_session_id=None):
        self.game_session_id = game_session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkipTrialPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        return self


class SkipTrialPolicyResponseBodyData(TeaModel):
    def __init__(self, skip_result=None):
        self.skip_result = skip_result  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkipTrialPolicyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_result is not None:
            result['SkipResult'] = self.skip_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SkipResult') is not None:
            self.skip_result = m.get('SkipResult')
        return self


class SkipTrialPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: SkipTrialPolicyResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SkipTrialPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SkipTrialPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SkipTrialPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SkipTrialPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SkipTrialPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SkipTrialPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGameSessionRequest(TeaModel):
    def __init__(self, game_id=None, access_key=None, user_id=None, biz_param=None, game_session=None, reason=None):
        self.game_id = game_id  # type: str
        self.access_key = access_key  # type: str
        self.user_id = user_id  # type: str
        self.biz_param = biz_param  # type: str
        self.game_session = game_session  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopGameSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class StopGameSessionResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, game_session=None, queue_state=None, message=None,
                 game_id=None, queue_code=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.game_session = game_session  # type: str
        self.queue_state = queue_state  # type: int
        self.message = message  # type: str
        self.game_id = game_id  # type: str
        self.queue_code = queue_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopGameSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class StopGameSessionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopGameSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopGameSessionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopGameSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


