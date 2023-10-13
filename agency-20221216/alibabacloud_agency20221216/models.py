# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelSubscriptionBillRequest(TeaModel):
    def __init__(self, subscribe_type=None):
        # The type of the bill to which you want to cancel the subscription. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        self.subscribe_type = subscribe_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelSubscriptionBillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        return self


class CancelSubscriptionBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: str
        # The data that is returned.
        self.data = data  # type: bool
        # The message that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelSubscriptionBillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelSubscriptionBillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelSubscriptionBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelSubscriptionBillResponse, self).to_map()
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
            temp_model = CancelSubscriptionBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomerRequest(TeaModel):
    def __init__(self, customer_name=None, customer_source=None, customer_sub_trade=None, customer_trade=None,
                 nation=None):
        self.customer_name = customer_name  # type: str
        self.customer_source = customer_source  # type: str
        self.customer_sub_trade = customer_sub_trade  # type: str
        self.customer_trade = customer_trade  # type: str
        self.nation = nation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.customer_source is not None:
            result['CustomerSource'] = self.customer_source
        if self.customer_sub_trade is not None:
            result['CustomerSubTrade'] = self.customer_sub_trade
        if self.customer_trade is not None:
            result['CustomerTrade'] = self.customer_trade
        if self.nation is not None:
            result['Nation'] = self.nation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('CustomerSource') is not None:
            self.customer_source = m.get('CustomerSource')
        if m.get('CustomerSubTrade') is not None:
            self.customer_sub_trade = m.get('CustomerSubTrade')
        if m.get('CustomerTrade') is not None:
            self.customer_trade = m.get('CustomerTrade')
        if m.get('Nation') is not None:
            self.nation = m.get('Nation')
        return self


class CreateCustomerResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCustomerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomerResponse, self).to_map()
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
            temp_model = CreateCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeductOutstandingBalanceRequest(TeaModel):
    def __init__(self, deduct_amount=None, uid=None):
        self.deduct_amount = deduct_amount  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeductOutstandingBalanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deduct_amount is not None:
            result['DeductAmount'] = self.deduct_amount
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeductAmount') is not None:
            self.deduct_amount = m.get('DeductAmount')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DeductOutstandingBalanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeductOutstandingBalanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeductOutstandingBalanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeductOutstandingBalanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeductOutstandingBalanceResponse, self).to_map()
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
            temp_model = DeductOutstandingBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditEndUserStatusRequest(TeaModel):
    def __init__(self, credit_status=None, uid=None):
        self.credit_status = credit_status  # type: str
        # uid
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditEndUserStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_status is not None:
            result['CreditStatus'] = self.credit_status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreditStatus') is not None:
            self.credit_status = m.get('CreditStatus')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditEndUserStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditEndUserStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditEndUserStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditEndUserStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditEndUserStatusResponse, self).to_map()
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
            temp_model = EditEndUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditNewBuyStatusRequest(TeaModel):
    def __init__(self, new_buy_status=None, uid=None):
        self.new_buy_status = new_buy_status  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditNewBuyStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditNewBuyStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditNewBuyStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditNewBuyStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditNewBuyStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditNewBuyStatusResponse, self).to_map()
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
            temp_model = EditNewBuyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditZeroCreditShutdownRequest(TeaModel):
    def __init__(self, shutdown_policy=None, uid=None):
        self.shutdown_policy = shutdown_policy  # type: str
        # uid
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditZeroCreditShutdownRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shutdown_policy is not None:
            result['ShutdownPolicy'] = self.shutdown_policy
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShutdownPolicy') is not None:
            self.shutdown_policy = m.get('ShutdownPolicy')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditZeroCreditShutdownResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditZeroCreditShutdownResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditZeroCreditShutdownResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditZeroCreditShutdownResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditZeroCreditShutdownResponse, self).to_map()
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
            temp_model = EditZeroCreditShutdownResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountInfoRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, uid=None, user_type=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.uid = uid  # type: long
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetAccountInfoResponseBodyAccountInfoListAccountInfo(TeaModel):
    def __init__(self, account_nickname=None, aliyun_id=None, association_success_time=None, cid=None, email=None,
                 mobile=None, remark=None, sub_account_type=None, uid=None):
        self.account_nickname = account_nickname  # type: str
        self.aliyun_id = aliyun_id  # type: str
        self.association_success_time = association_success_time  # type: str
        self.cid = cid  # type: long
        self.email = email  # type: str
        self.mobile = mobile  # type: str
        self.remark = remark  # type: str
        self.sub_account_type = sub_account_type  # type: int
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountInfoResponseBodyAccountInfoListAccountInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.association_success_time is not None:
            result['AssociationSuccessTime'] = self.association_success_time
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('AssociationSuccessTime') is not None:
            self.association_success_time = m.get('AssociationSuccessTime')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetAccountInfoResponseBodyAccountInfoList(TeaModel):
    def __init__(self, account_info=None):
        self.account_info = account_info  # type: list[GetAccountInfoResponseBodyAccountInfoListAccountInfo]

    def validate(self):
        if self.account_info:
            for k in self.account_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAccountInfoResponseBodyAccountInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountInfo'] = []
        if self.account_info is not None:
            for k in self.account_info:
                result['AccountInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_info = []
        if m.get('AccountInfo') is not None:
            for k in m.get('AccountInfo'):
                temp_model = GetAccountInfoResponseBodyAccountInfoListAccountInfo()
                self.account_info.append(temp_model.from_map(k))
        return self


class GetAccountInfoResponseBodyPageInfo(TeaModel):
    def __init__(self, page=None, page_size=None, total=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountInfoResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAccountInfoResponseBody(TeaModel):
    def __init__(self, account_info_list=None, code=None, message=None, page_info=None, request_id=None,
                 success=None):
        self.account_info_list = account_info_list  # type: GetAccountInfoResponseBodyAccountInfoList
        self.code = code  # type: str
        # message
        self.message = message  # type: str
        self.page_info = page_info  # type: GetAccountInfoResponseBodyPageInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.account_info_list:
            self.account_info_list.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetAccountInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info_list is not None:
            result['AccountInfoList'] = self.account_info_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountInfoList') is not None:
            temp_model = GetAccountInfoResponseBodyAccountInfoList()
            self.account_info_list = temp_model.from_map(m['AccountInfoList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetAccountInfoResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccountInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountInfoResponse, self).to_map()
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
            temp_model = GetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreditInfoRequest(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCreditInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetCreditInfoResponseBodyData(TeaModel):
    def __init__(self, account_status=None, alarm_threshold=None, available_credit=None, credit_line=None,
                 outstanding_balance=None, zero_credit_shutdown_policy=None, new_buy_status=None):
        self.account_status = account_status  # type: str
        self.alarm_threshold = alarm_threshold  # type: str
        self.available_credit = available_credit  # type: str
        self.credit_line = credit_line  # type: str
        self.outstanding_balance = outstanding_balance  # type: str
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy  # type: str
        self.new_buy_status = new_buy_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCreditInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.alarm_threshold is not None:
            result['AlarmThreshold'] = self.alarm_threshold
        if self.available_credit is not None:
            result['AvailableCredit'] = self.available_credit
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.outstanding_balance is not None:
            result['OutstandingBalance'] = self.outstanding_balance
        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy
        if self.new_buy_status is not None:
            result['newBuyStatus'] = self.new_buy_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AlarmThreshold') is not None:
            self.alarm_threshold = m.get('AlarmThreshold')
        if m.get('AvailableCredit') is not None:
            self.available_credit = m.get('AvailableCredit')
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('OutstandingBalance') is not None:
            self.outstanding_balance = m.get('OutstandingBalance')
        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')
        if m.get('newBuyStatus') is not None:
            self.new_buy_status = m.get('newBuyStatus')
        return self


class GetCreditInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCreditInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCreditInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCreditInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCreditInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCreditInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCreditInfoResponse, self).to_map()
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
            temp_model = GetCreditInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDailyBillRequest(TeaModel):
    def __init__(self, bill_owner=None, bill_type=None, date=None):
        self.bill_owner = bill_owner  # type: str
        self.bill_type = bill_type  # type: str
        # Billing date. Format YYYY-MM-DD
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDailyBillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetDailyBillResponseBodyData(TeaModel):
    def __init__(self, bill_link_csv=None, bill_link_xlsx=None, bill_owner=None, bill_type=None, spending_time=None):
        self.bill_link_csv = bill_link_csv  # type: str
        self.bill_link_xlsx = bill_link_xlsx  # type: str
        self.bill_owner = bill_owner  # type: str
        self.bill_type = bill_type  # type: str
        self.spending_time = spending_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDailyBillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_link_csv is not None:
            result['BillLinkCSV'] = self.bill_link_csv
        if self.bill_link_xlsx is not None:
            result['BillLinkXLSX'] = self.bill_link_xlsx
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.spending_time is not None:
            result['SpendingTime'] = self.spending_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillLinkCSV') is not None:
            self.bill_link_csv = m.get('BillLinkCSV')
        if m.get('BillLinkXLSX') is not None:
            self.bill_link_xlsx = m.get('BillLinkXLSX')
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('SpendingTime') is not None:
            self.spending_time = m.get('SpendingTime')
        return self


class GetDailyBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDailyBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDailyBillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDailyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDailyBillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDailyBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDailyBillResponse, self).to_map()
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
            temp_model = GetDailyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInviteStatusRequestInviteStatusList(TeaModel):
    def __init__(self, invite_id=None):
        self.invite_id = invite_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInviteStatusRequestInviteStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        return self


class GetInviteStatusRequest(TeaModel):
    def __init__(self, invite_status_list=None):
        # inviteId list
        self.invite_status_list = invite_status_list  # type: list[GetInviteStatusRequestInviteStatusList]

    def validate(self):
        if self.invite_status_list:
            for k in self.invite_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInviteStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteStatusList'] = []
        if self.invite_status_list is not None:
            for k in self.invite_status_list:
                result['InviteStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invite_status_list = []
        if m.get('InviteStatusList') is not None:
            for k in m.get('InviteStatusList'):
                temp_model = GetInviteStatusRequestInviteStatusList()
                self.invite_status_list.append(temp_model.from_map(k))
        return self


class GetInviteStatusResponseBodyDataInviteStatusInviteStatusList(TeaModel):
    def __init__(self, association_success_time=None, cid=None, gmt_create=None, parent_id=None, status=None,
                 sub_account_type=None, uid=None):
        self.association_success_time = association_success_time  # type: str
        self.cid = cid  # type: long
        self.gmt_create = gmt_create  # type: str
        self.parent_id = parent_id  # type: str
        self.status = status  # type: int
        self.sub_account_type = sub_account_type  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInviteStatusResponseBodyDataInviteStatusInviteStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_success_time is not None:
            result['AssociationSuccessTime'] = self.association_success_time
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationSuccessTime') is not None:
            self.association_success_time = m.get('AssociationSuccessTime')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetInviteStatusResponseBodyDataInviteStatus(TeaModel):
    def __init__(self, code=None, invite_status_list=None, message=None, success=None):
        self.code = code  # type: str
        self.invite_status_list = invite_status_list  # type: GetInviteStatusResponseBodyDataInviteStatusInviteStatusList
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.invite_status_list:
            self.invite_status_list.validate()

    def to_map(self):
        _map = super(GetInviteStatusResponseBodyDataInviteStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.invite_status_list is not None:
            result['InviteStatusList'] = self.invite_status_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InviteStatusList') is not None:
            temp_model = GetInviteStatusResponseBodyDataInviteStatusInviteStatusList()
            self.invite_status_list = temp_model.from_map(m['InviteStatusList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInviteStatusResponseBodyData(TeaModel):
    def __init__(self, invite_status=None):
        self.invite_status = invite_status  # type: list[GetInviteStatusResponseBodyDataInviteStatus]

    def validate(self):
        if self.invite_status:
            for k in self.invite_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInviteStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteStatus'] = []
        if self.invite_status is not None:
            for k in self.invite_status:
                result['InviteStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invite_status = []
        if m.get('InviteStatus') is not None:
            for k in m.get('InviteStatus'):
                temp_model = GetInviteStatusResponseBodyDataInviteStatus()
                self.invite_status.append(temp_model.from_map(k))
        return self


class GetInviteStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInviteStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInviteStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetInviteStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInviteStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInviteStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInviteStatusResponse, self).to_map()
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
            temp_model = GetInviteStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonthlyBillRequest(TeaModel):
    def __init__(self, bill_owner=None, bill_type=None, month=None):
        # Bill Owner type.
        # 
        #  Value range:
        # 
        # 1: Master account 
        # 
        # 2: Sub account
        self.bill_owner = bill_owner  # type: str
        # Value Range:
        # 
        # MonthlyInvoice
        # 
        # MonthRefundInvoice
        # 
        # MonthlySummary
        # 
        # MonthlyInstanceAddAdjustBill 
        # 
        # MonthlyInstanceRefundBill
        # 
        # MonthlyAddAdjustInvoce
        # 
        # MonthlyRefundAdjustInvoce 
        # 
        # MonthlyInstanceConsumeV2 
        # 
        # MarginReportV2
        self.bill_type = bill_type  # type: str
        # Billing Month, Format is YYYY-MM
        self.month = month  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMonthlyBillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetMonthlyBillResponseBodyData(TeaModel):
    def __init__(self, bill_link_csv=None, bill_link_xlsx=None, bill_owner=None, bill_type=None, invoice_link=None,
                 refund_invoice_flag=None, refund_invoice_link=None, spending_time=None):
        self.bill_link_csv = bill_link_csv  # type: str
        self.bill_link_xlsx = bill_link_xlsx  # type: str
        self.bill_owner = bill_owner  # type: str
        self.bill_type = bill_type  # type: str
        self.invoice_link = invoice_link  # type: str
        self.refund_invoice_flag = refund_invoice_flag  # type: bool
        self.refund_invoice_link = refund_invoice_link  # type: str
        self.spending_time = spending_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMonthlyBillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_link_csv is not None:
            result['BillLinkCSV'] = self.bill_link_csv
        if self.bill_link_xlsx is not None:
            result['BillLinkXLSX'] = self.bill_link_xlsx
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.invoice_link is not None:
            result['InvoiceLink'] = self.invoice_link
        if self.refund_invoice_flag is not None:
            result['RefundInvoiceFlag'] = self.refund_invoice_flag
        if self.refund_invoice_link is not None:
            result['RefundInvoiceLink'] = self.refund_invoice_link
        if self.spending_time is not None:
            result['SpendingTime'] = self.spending_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillLinkCSV') is not None:
            self.bill_link_csv = m.get('BillLinkCSV')
        if m.get('BillLinkXLSX') is not None:
            self.bill_link_xlsx = m.get('BillLinkXLSX')
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('InvoiceLink') is not None:
            self.invoice_link = m.get('InvoiceLink')
        if m.get('RefundInvoiceFlag') is not None:
            self.refund_invoice_flag = m.get('RefundInvoiceFlag')
        if m.get('RefundInvoiceLink') is not None:
            self.refund_invoice_link = m.get('RefundInvoiceLink')
        if m.get('SpendingTime') is not None:
            self.spending_time = m.get('SpendingTime')
        return self


class GetMonthlyBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetMonthlyBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMonthlyBillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetMonthlyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMonthlyBillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMonthlyBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMonthlyBillResponse, self).to_map()
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
            temp_model = GetMonthlyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnassociatedCustomerRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnassociatedCustomerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo(TeaModel):
    def __init__(self, account_nickname=None, email=None, gmt_create=None, invite_id=None, status=None):
        self.account_nickname = account_nickname  # type: str
        self.email = email  # type: str
        self.gmt_create = gmt_create  # type: str
        self.invite_id = invite_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.email is not None:
            result['Email'] = self.email
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUnassociatedCustomerResponseBodyInviteInfoList(TeaModel):
    def __init__(self, invite_info=None):
        self.invite_info = invite_info  # type: list[GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo]

    def validate(self):
        if self.invite_info:
            for k in self.invite_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUnassociatedCustomerResponseBodyInviteInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteInfo'] = []
        if self.invite_info is not None:
            for k in self.invite_info:
                result['InviteInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invite_info = []
        if m.get('InviteInfo') is not None:
            for k in m.get('InviteInfo'):
                temp_model = GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo()
                self.invite_info.append(temp_model.from_map(k))
        return self


class GetUnassociatedCustomerResponseBodyPageInfo(TeaModel):
    def __init__(self, page=None, page_size=None, total=None):
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUnassociatedCustomerResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetUnassociatedCustomerResponseBody(TeaModel):
    def __init__(self, code=None, invite_info_list=None, message=None, page_info=None, request_id=None, success=None):
        self.code = code  # type: str
        self.invite_info_list = invite_info_list  # type: GetUnassociatedCustomerResponseBodyInviteInfoList
        self.message = message  # type: str
        self.page_info = page_info  # type: GetUnassociatedCustomerResponseBodyPageInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.invite_info_list:
            self.invite_info_list.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetUnassociatedCustomerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.invite_info_list is not None:
            result['InviteInfoList'] = self.invite_info_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InviteInfoList') is not None:
            temp_model = GetUnassociatedCustomerResponseBodyInviteInfoList()
            self.invite_info_list = temp_model.from_map(m['InviteInfoList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetUnassociatedCustomerResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUnassociatedCustomerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUnassociatedCustomerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUnassociatedCustomerResponse, self).to_map()
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
            temp_model = GetUnassociatedCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InviteSubAccountRequestAccountInfoList(TeaModel):
    def __init__(self, account_nickname=None, credit_line=None, customer_id=None, email_address=None,
                 new_buy_status=None, remark=None, sub_account_type=None, zero_credit_shutdown_policy=None):
        self.account_nickname = account_nickname  # type: str
        self.credit_line = credit_line  # type: str
        self.customer_id = customer_id  # type: str
        self.email_address = email_address  # type: str
        self.new_buy_status = new_buy_status  # type: str
        self.remark = remark  # type: str
        self.sub_account_type = sub_account_type  # type: str
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InviteSubAccountRequestAccountInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')
        return self


class InviteSubAccountRequest(TeaModel):
    def __init__(self, account_info_list=None):
        self.account_info_list = account_info_list  # type: list[InviteSubAccountRequestAccountInfoList]

    def validate(self):
        if self.account_info_list:
            for k in self.account_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InviteSubAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountInfoList'] = []
        if self.account_info_list is not None:
            for k in self.account_info_list:
                result['AccountInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_info_list = []
        if m.get('AccountInfoList') is not None:
            for k in m.get('AccountInfoList'):
                temp_model = InviteSubAccountRequestAccountInfoList()
                self.account_info_list.append(temp_model.from_map(k))
        return self


class InviteSubAccountResponseBodyResultsResultResult(TeaModel):
    def __init__(self, days=None, invite_id=None, reg_url=None):
        self.days = days  # type: int
        self.invite_id = invite_id  # type: long
        self.reg_url = reg_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InviteSubAccountResponseBodyResultsResultResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        if self.reg_url is not None:
            result['RegUrl'] = self.reg_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        if m.get('RegUrl') is not None:
            self.reg_url = m.get('RegUrl')
        return self


class InviteSubAccountResponseBodyResultsResult(TeaModel):
    def __init__(self, code=None, message=None, result=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: InviteSubAccountResponseBodyResultsResultResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(InviteSubAccountResponseBodyResultsResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = InviteSubAccountResponseBodyResultsResultResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InviteSubAccountResponseBodyResults(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: list[InviteSubAccountResponseBodyResultsResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InviteSubAccountResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = InviteSubAccountResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class InviteSubAccountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, results=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.results = results  # type: InviteSubAccountResponseBodyResults
        self.success = success  # type: bool

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super(InviteSubAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = InviteSubAccountResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InviteSubAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InviteSubAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InviteSubAccountResponse, self).to_map()
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
            temp_model = InviteSubAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCountriesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCountriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCountriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCountriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCountriesResponse, self).to_map()
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
            temp_model = ListCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendEmailRequest(TeaModel):
    def __init__(self, invite_id=None):
        self.invite_id = invite_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        return self


class ResendEmailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResendEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResendEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResendEmailResponse, self).to_map()
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
            temp_model = ResendEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccountInfoRequest(TeaModel):
    def __init__(self, account_nickname=None, remark=None, uid=None):
        self.account_nickname = account_nickname  # type: str
        self.remark = remark  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccountInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SetAccountInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccountInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetAccountInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetAccountInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAccountInfoResponse, self).to_map()
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
            temp_model = SetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCreditLineRequest(TeaModel):
    def __init__(self, credit_line=None, uid=None):
        self.credit_line = credit_line  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCreditLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SetCreditLineResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCreditLineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetCreditLineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetCreditLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCreditLineResponse, self).to_map()
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
            temp_model = SetCreditLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWarningThresholdRequest(TeaModel):
    def __init__(self, uid=None, warning_value=None):
        self.uid = uid  # type: long
        self.warning_value = warning_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWarningThresholdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.warning_value is not None:
            result['WarningValue'] = self.warning_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('WarningValue') is not None:
            self.warning_value = m.get('WarningValue')
        return self


class SetWarningThresholdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWarningThresholdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetWarningThresholdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetWarningThresholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetWarningThresholdResponse, self).to_map()
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
            temp_model = SetWarningThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscriptionBillRequest(TeaModel):
    def __init__(self, begin_billing_cycle=None, bill_format=None, bucket_owner_id=None, subscribe_bucket=None,
                 subscribe_segment_size=None, subscribe_type=None):
        # The start month from which the bills are pushed. Specify the value in the yyyy-MM format.
        # 
        # After the subscription is generated, the system automatically pushes the bill data that is generated from the month that you specified to the current point in time. Data of up to six months can be pushed. The current month is included. If you subscribe to the bills for more than six months, the subscription is invalid.
        self.begin_billing_cycle = begin_billing_cycle  # type: str
        # The file format of the bill. Valid values: csv and parquet.
        # 
        # If you subscribe to the bills of multiple file formats, we recommend that you store the bills in different OSS buckets to prevent file overwriting.
        self.bill_format = bill_format  # type: str
        # The ID of the user to which the OSS bucket belongs.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of a subordinate partner account, you must set this parameter to the ID of the subordinate partner account and grant the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission to the subordinate partner account.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of your own account, your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        self.bucket_owner_id = bucket_owner_id  # type: long
        # The name of the Object Storage Service (OSS) bucket in which you want to store the bills.
        self.subscribe_bucket = subscribe_bucket  # type: str
        # The maximum rows in a single bill file. If the number of bill rows exceed the upper limit, the bill is automatically split into multiple files. The name of each split file is in the `uid_billType_billCycle_SquenceNo_fileNo` format.
        # 
        # Files whose names are the same except for the fileNo field are of the same type and belong to the same billing cycle.
        self.subscribe_segment_size = subscribe_segment_size  # type: int
        # The type of the bill to which you want to subscribe. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        self.subscribe_type = subscribe_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubscriptionBillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle
        if self.bill_format is not None:
            result['BillFormat'] = self.bill_format
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.subscribe_segment_size is not None:
            result['SubscribeSegmentSize'] = self.subscribe_segment_size
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')
        if m.get('BillFormat') is not None:
            self.bill_format = m.get('BillFormat')
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('SubscribeSegmentSize') is not None:
            self.subscribe_segment_size = m.get('SubscribeSegmentSize')
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        return self


class SubscriptionBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: str
        # The data that is returned.
        self.data = data  # type: bool
        # The message that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubscriptionBillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscriptionBillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubscriptionBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubscriptionBillResponse, self).to_map()
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
            temp_model = SubscriptionBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


