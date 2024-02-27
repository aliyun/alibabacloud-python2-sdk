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
        # Customer\"s name.
        self.customer_name = customer_name  # type: str
        # The source/channel that allow client to connected with us. Please enumerate with Customer Source.
        self.customer_source = customer_source  # type: str
        # The sub-industry that Customer\"s business belongs to. Please enumerate with Customer Trade.
        self.customer_sub_trade = customer_sub_trade  # type: str
        # The industry that Customer\"s business belongs to. Please enumerate with Customer Trade.
        self.customer_trade = customer_trade  # type: str
        # The region that Customer choose to launch the Cloud Service. Please use ListCountries to confirm the valid region list for current UID.
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
        # Code indicating whether the call was successful.
        self.code = code  # type: str
        # Data indicating whether a customer was successfully created. If it\"s "true", the Message contains CID.
        self.data = data  # type: bool
        # Massage indicating whether the call was successful.
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call it self was successful. It does not guarantee the success of subsequent business operations.
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


class CustomerQuotaRecordListRequest(TeaModel):
    def __init__(self, end_date=None, end_user_pk=None, language=None, operation_type=None, page_no=None,
                 page_size=None, start_date=None):
        # End Date Format: yyyy-MM-dd
        self.end_date = end_date  # type: str
        # Customer UID
        self.end_user_pk = end_user_pk  # type: long
        # Multilingual Parameters, the default language is English.</br>
        # en: English</br>
        # zh: Chinese</br>
        # ja: Japanese </br>
        self.language = language  # type: str
        # Operation Type Enum</br>
        # all All types</br>
        # quota_create Create quota</br>
        # quota_amount_adjust Adjust the amount of quota</br>
        self.operation_type = operation_type  # type: str
        # Pagination, current page number, starting from 1.
        self.page_no = page_no  # type: int
        # Pagination, record number on each page. Maximum 100.
        self.page_size = page_size  # type: int
        # Start Date Format: yyyy-MM-dd
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CustomerQuotaRecordListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.end_user_pk is not None:
            result['EndUserPk'] = self.end_user_pk
        if self.language is not None:
            result['Language'] = self.language
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EndUserPk') is not None:
            self.end_user_pk = m.get('EndUserPk')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class CustomerQuotaRecordListResponseBodyData(TeaModel):
    def __init__(self, operation_submit_type=None, operation_time=None, operation_type_code=None,
                 operation_type_desc=None, operation_uid=None, update_after_amount=None, update_amount=None, update_before_amount=None):
        # The way to submit the quota adjustment operation. API/ACPN
        self.operation_submit_type = operation_submit_type  # type: str
        # The time of submit the quota adjustment operation.
        self.operation_time = operation_time  # type: str
        # Operation Type Enum</br>
        # all All types</br>
        # quota_create Create quota</br>
        # quota_amount_adjust Adjust the amount of quota</br>
        self.operation_type_code = operation_type_code  # type: str
        # The description of submitted quota adjustment operation.
        self.operation_type_desc = operation_type_desc  # type: str
        # The UID of operator(Partner\"s UID).
        self.operation_uid = operation_uid  # type: str
        # Updated quota amount
        self.update_after_amount = update_after_amount  # type: str
        # The difference amount between updated quota and original quota.
        self.update_amount = update_amount  # type: str
        # Original quota amount
        self.update_before_amount = update_before_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CustomerQuotaRecordListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_submit_type is not None:
            result['OperationSubmitType'] = self.operation_submit_type
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type_code is not None:
            result['OperationTypeCode'] = self.operation_type_code
        if self.operation_type_desc is not None:
            result['OperationTypeDesc'] = self.operation_type_desc
        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid
        if self.update_after_amount is not None:
            result['UpdateAfterAmount'] = self.update_after_amount
        if self.update_amount is not None:
            result['UpdateAmount'] = self.update_amount
        if self.update_before_amount is not None:
            result['UpdateBeforeAmount'] = self.update_before_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationSubmitType') is not None:
            self.operation_submit_type = m.get('OperationSubmitType')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationTypeCode') is not None:
            self.operation_type_code = m.get('OperationTypeCode')
        if m.get('OperationTypeDesc') is not None:
            self.operation_type_desc = m.get('OperationTypeDesc')
        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')
        if m.get('UpdateAfterAmount') is not None:
            self.update_after_amount = m.get('UpdateAfterAmount')
        if m.get('UpdateAmount') is not None:
            self.update_amount = m.get('UpdateAmount')
        if m.get('UpdateBeforeAmount') is not None:
            self.update_before_amount = m.get('UpdateBeforeAmount')
        return self


class CustomerQuotaRecordListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, page_no=None, page_size=None, request_id=None, total=None):
        # Status code of returning result, 200 means success.
        self.code = code  # type: str
        # Listed data of returning result
        self.data = data  # type: list[CustomerQuotaRecordListResponseBodyData]
        # Description of returning data
        self.msg = msg  # type: str
        # Current page number
        self.page_no = page_no  # type: int
        # Record number on each page
        self.page_size = page_size  # type: int
        # ID of request
        self.request_id = request_id  # type: str
        # Total volume
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CustomerQuotaRecordListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CustomerQuotaRecordListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class CustomerQuotaRecordListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CustomerQuotaRecordListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CustomerQuotaRecordListResponse, self).to_map()
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
            temp_model = CustomerQuotaRecordListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeductOutstandingBalanceRequest(TeaModel):
    def __init__(self, deduct_amount=None, uid=None):
        # The Deducted Credit to be offset.
        self.deduct_amount = deduct_amount  # type: str
        # Account UID of Distribution Customer.
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
        # Result Code. Value Range:
        # - 200 OK
        # - 1109 System Error
        self.code = code  # type: str
        # Same as Code Parameter Value.
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Shutdown Status</br>
        # 
        # - postPayFreeze, the account have been blocked</br>
        # 
        # - postPayThaw, the account have been unlocked</br>
        self.credit_status = credit_status  # type: str
        # UID
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
        # Status Code</br>
        self.code = code  # type: str
        # Success or not</br>
        self.data = data  # type: str
        # Message</br>
        self.message = message  # type: str
        # Message</br>
        self.msg = msg  # type: str
        # Request ID</br>
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
        # New Purchase Status</br>
        # 
        # - cancelBan: Cancel the restriction for New Purchase request</br>
        # 
        # - ban: ban the New Purchase request</br>
        self.new_buy_status = new_buy_status  # type: str
        # Customer UID
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
        # Status Code</br>
        self.code = code  # type: str
        # Success or not</br>
        self.data = data  # type: str
        # Message</br>
        self.message = message  # type: str
        # Message</br>
        self.msg = msg  # type: str
        # Request ID</br>
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
        # UID
        self.shutdown_policy = shutdown_policy  # type: str
        # No Change History
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
        # Success or not</br>
        self.code = code  # type: str
        # Request ID</br>
        self.data = data  # type: str
        # Message</br>
        self.message = message  # type: str
        # NO_STOP
        self.msg = msg  # type: str
        # success
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


class ExportCustomerQuotaRecordRequest(TeaModel):
    def __init__(self, end_date=None, end_user_pk=None, language=None, operation_type=None, start_date=None):
        # End Date Format:  yyyy-MM-dd
        self.end_date = end_date  # type: str
        # Customer UID
        self.end_user_pk = end_user_pk  # type: long
        # Multilingual Parameters, the default language is English.</br>
        # en: English</br>
        # zh: Chinese</br>
        # ja: Japanese </br>
        self.language = language  # type: str
        # Operation Type Enum</br>
        # all All types</br>
        # quota_create Create quota</br>
        # quota_amount_adjust Adjust the amount of quota</br>
        self.operation_type = operation_type  # type: str
        # Start Date Format:  yyyy-MM-dd
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportCustomerQuotaRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.end_user_pk is not None:
            result['EndUserPk'] = self.end_user_pk
        if self.language is not None:
            result['Language'] = self.language
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EndUserPk') is not None:
            self.end_user_pk = m.get('EndUserPk')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportCustomerQuotaRecordResponseBodyData(TeaModel):
    def __init__(self, cost=None, id=None):
        # Estimated duration, in minutes.
        self.cost = cost  # type: int
        # ID of Export task
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportCustomerQuotaRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ExportCustomerQuotaRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        # Code
        self.code = code  # type: str
        # Data
        self.data = data  # type: ExportCustomerQuotaRecordResponseBodyData
        # Description
        self.msg = msg  # type: str
        # ID of the Request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExportCustomerQuotaRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ExportCustomerQuotaRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportCustomerQuotaRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportCustomerQuotaRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportCustomerQuotaRecordResponse, self).to_map()
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
            temp_model = ExportCustomerQuotaRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountInfoRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, uid=None, user_type=None):
        # Pagination, current page.
        self.current_page = current_page  # type: int
        # Pagination, record number on each page, maximum 20.
        self.page_size = page_size  # type: int
        # Account UID of Distribution Customer. This parameter and the UserType parameter must have one filled. If this parameter is empty, then check all Distribution Customer accounts of the selected UserType.
        self.uid = uid  # type: long
        # Distribution Customer\"s Account Type:
        # - 1 End User
        # - 2 Enterprise
        # - 3 T2 Partner
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
        # The name of Sub Account:
        # 1.	Use the official name of Company, if Sub Account is an enterprise.
        # 2.	Use the official name of Partner, if Sub Account is a T2 reseller.
        self.account_nickname = account_nickname  # type: str
        # Alibaba Cloud Login name of Distribution Customer.
        self.aliyun_id = aliyun_id  # type: str
        # The time that Distribution Customer successfully associated with Distributor.
        self.association_success_time = association_success_time  # type: str
        # Account CID of Distribution Customer.
        self.cid = cid  # type: long
        # The E-mail of Distribution Customer.
        self.email = email  # type: str
        # Valid mobile number of Distribution Customer.
        self.mobile = mobile  # type: str
        # Description of Distribution Customer.
        self.remark = remark  # type: str
        # Account Type:
        # - 1 Agency\"s End User
        # - 2 Reseller\"s End User
        # - 3 Enterprise
        # - 4 T2 Agency Partner
        # - 5 T2 Reseller Partner
        # - 6 T2 Agency+Reseller Partner
        self.sub_account_type = sub_account_type  # type: int
        # Account UID of Distribution Customer.
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
        # Pagination, current page.
        self.page = page  # type: int
        # Pagination, record number on each page.
        self.page_size = page_size  # type: int
        # Pagination, page volume in total.
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
        # List of Account Information
        self.account_info_list = account_info_list  # type: GetAccountInfoResponseBodyAccountInfoList
        # Result Code - Error Code. Value Range:
        # - 200 OK
        # - 1109 System Error
        # - 3029: Invalid UID
        # - 3062: UID and UserType are both empty.
        # - 3063: UserType value out of range.
        self.code = code  # type: str
        # Message
        self.message = message  # type: str
        # Pagination Information
        self.page_info = page_info  # type: GetAccountInfoResponseBodyPageInfo
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Sub Account UID
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
    def __init__(self, account_status=None, alarm_threshold=None, available_credit=None,
                 consumed_undeducted_value=None, credit_line=None, outstanding_balance=None, zero_credit_shutdown_policy=None,
                 new_buy_status=None):
        # The Credit Control status, Value Range:</br>
        # 1. normal - Sub Account status is running as usual.
        # 2. arrearsNotShutdown - Sub Account status is running as usual, but have outstanding bill(s).
        # 3. shutdown -  Sub Account status is down.
        self.account_status = account_status  # type: str
        # Percentage value, when the available credit limit is lower than this credit limit percentage, a notification E-mail will be sent to the main account.
        self.alarm_threshold = alarm_threshold  # type: str
        # The Credit available to consume.
        self.available_credit = available_credit  # type: str
        # Obtain total unpaid amount on demo bill before simulated deduction.
        self.consumed_undeducted_value = consumed_undeducted_value  # type: str
        # The Credit Line of Sub Account
        self.credit_line = credit_line  # type: str
        # The Credit have been consumed by Sub Account, and haven\"t be paid.
        self.outstanding_balance = outstanding_balance  # type: str
        # The systematic controlling policy for resource management, specifically when the available Credit of Sub Account falls to 0 or less.</br>
        # 
        # - 1: delayStop. The account have Shutdown-delay Privilege,  After Shutdown-delay Credit is ran out, Alibaba Cloud will take over resources and keep the instance for 15 days. In addition, the instance will be released if Sub Account failed to pay the bill within these 15 days.</br>
        # - 2: noStop. Partner will manually manage Shutdown Status for Sub Account. Meanwhile, System would not manage the resource\"s life-circle of Sub Account.</br>
        # - 3: immediatelyStop. Once valid quota of Sub Account falls below 0 and be identified as defaulting account, it will trigger the instance shutdown immediately.</br>
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy  # type: str
        # Manage order operation.
        # - ban：Ban the new purchase action.
        # - normal：The account could raise new purchase order as usual.
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
        if self.consumed_undeducted_value is not None:
            result['ConsumedUndeductedValue'] = self.consumed_undeducted_value
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
        if m.get('ConsumedUndeductedValue') is not None:
            self.consumed_undeducted_value = m.get('ConsumedUndeductedValue')
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
        # Result Code:
        # - 200 OK
        # - 1109 System Error
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetCreditInfoResponseBodyData
        # Message Information
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Bill Owner type. Value Range:</br>
        # 1: Master account</br>
        # 2: Sub account</br>
        self.bill_owner = bill_owner  # type: str
        # BillType. Value Range:</br>
        # 
        # - DailyOrder(Deprecated)
        # - DailyBill (Deprecated)
        # - DailyInstanceBill (Deprecated)
        # - DailyInstanceBillV2
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
        # The link to download CSV file, please use HTTP Protocol.
        self.bill_link_csv = bill_link_csv  # type: str
        # The link to download XLSX file, please use HTTP Protocol.
        self.bill_link_xlsx = bill_link_xlsx  # type: str
        # Same as inserted parameter BillOwner.
        self.bill_owner = bill_owner  # type: str
        # Same as inserted parameter BillType.
        self.bill_type = bill_type  # type: str
        # Spending Time, refer to the exact time of costuming.
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
        # Result Code:
        # * 200 OK
        # * 1109 System error
        # * 3050 Bill Type can only be DailyOrder, DailyBill or DailyInstanceBill.
        # * 3049 Incorrect format of Spending Time.
        # * 3048 Bill Owner can only be 1 or 2.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetDailyBillResponseBodyData
        # Same as Code parameters.
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Invitation ID, From interface InviteSubAccount
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
        # inviteId list</br>
        # `Sub-levels <= 5`
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
        # The time that Distribution Customer successfully associated with Distributor.</br>
        # This value will be empty if there is no existing association.
        self.association_success_time = association_success_time  # type: str
        # Distribution Customer\"s CID
        self.cid = cid  # type: long
        # The time of email been sent out.
        self.gmt_create = gmt_create  # type: str
        # The parent organization ID.
        self.parent_id = parent_id  # type: str
        # Invitation Status:
        # * 0 No visit on registration URL
        # * 1 Successful Registration
        # * 2 Unsuccessful Registration
        # * 3 Registration URL have been visited, but no submitted sheet/ticket.
        self.status = status  # type: int
        # Account Type:
        # - 1 Agency\"s End User
        # - 2 Reseller\"s End User
        # - 5 T2 Reseller Partner
        self.sub_account_type = sub_account_type  # type: str
        # Distribution Customer\"s UID
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
        # Result Code. Value Range:
        # *   200 OK
        # *   1109 system error
        self.code = code  # type: str
        # List of Invitation Status result
        self.invite_status_list = invite_status_list  # type: GetInviteStatusResponseBodyDataInviteStatusInviteStatusList
        # The message returned.
        self.message = message  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Status Code. Error Code:
        # 
        # - 3057 InviteId is empty
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetInviteStatusResponseBodyData
        # The message returned.
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Bill Owner type. Value Range:</br>
        # 1: Master account</br>
        # 2: Sub account</br>
        self.bill_owner = bill_owner  # type: str
        # Value Range:
        # 
        # - MonthlyInvoice
        # - MonthRefundInvoice
        # - MonthlySummary
        # - MonthlyInstanceAddAdjustBill 
        # - MonthlyInstanceRefundBill
        # - MonthlyAddAdjustInvoce
        # - MonthlyRefundAdjustInvoce 
        # - MonthlyInstanceConsumeV2 
        # - MarginReportV2
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
        # The link to download CSV file, please use HTTP Protocol.
        self.bill_link_csv = bill_link_csv  # type: str
        # The link to download XLSX file, please use HTTP Protocol.
        self.bill_link_xlsx = bill_link_xlsx  # type: str
        # Same as inserted parameter BillOwner.
        self.bill_owner = bill_owner  # type: str
        # Same as inserted parameter BillType.
        self.bill_type = bill_type  # type: str
        # The URL to download invoice.
        self.invoice_link = invoice_link  # type: str
        # It states the existence of refund invoice. </br>
        # Candidate Values: True/False
        self.refund_invoice_flag = refund_invoice_flag  # type: bool
        # The URL to download refund invoice.
        self.refund_invoice_link = refund_invoice_link  # type: str
        # Spending Time, refer to the exact time of costuming.
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
        # Result Code:
        # * 200 OK
        # * 1109 System error
        # * 3030 Sub Account Nickname exceeds maximum length, maximum length 150 bytes.
        # * 3031 Remark exceeds maximum length, maximum length 3000 bytes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetMonthlyBillResponseBodyData
        # Same as Code parameters.
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Pagination, current page.
        self.current_page = current_page  # type: int
        # Pagination, record number on each page.
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
        # The name of Customer who are to be invited.
        self.account_nickname = account_nickname  # type: str
        # The Email of Customer who are to be invited.
        self.email = email  # type: str
        # The time of email been sent out.
        self.gmt_create = gmt_create  # type: str
        # Invitation ID
        self.invite_id = invite_id  # type: long
        # Invitation Status:
        # * 0 No visit on registration URL
        # * 1 Successful Registration
        # * 2 Unsuccessful Registration
        # * 3 Registration URL have been visited, but no submitted sheet/ticket.
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
        # Pagination, current page.
        self.page = page  # type: int
        # Pagination, record number on each page.
        self.page_size = page_size  # type: int
        # Pagination, page volume in total.
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
        # Error Code, Candidate Value：
        # * 200: OK
        # * 1109: System error
        self.code = code  # type: str
        # List of Invitation Information
        self.invite_info_list = invite_info_list  # type: GetUnassociatedCustomerResponseBodyInviteInfoList
        # Message information
        self.message = message  # type: str
        # Pagination Information
        self.page_info = page_info  # type: GetUnassociatedCustomerResponseBodyPageInfo
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # The name of Sub Account:</br>
        # 1. Use the official name of Company, if Sub Account is an enterprise.</br>
        # 2. Use the official name of Partner, if Sub Account is a T2 reseller.</br>
        self.account_nickname = account_nickname  # type: str
        # The total budget Credit of Sub Account that distributed by Partner.
        self.credit_line = credit_line  # type: str
        # Customer ID, Returning ID from CreateCustomer API.
        self.customer_id = customer_id  # type: str
        # The email address of End User,  which will receive the invitation email.
        self.email_address = email_address  # type: str
        # Initial Order Status</br>
        # 1. ban：Ban the new purchase action--After End User finish registration and authorization, they can\"t issue Cloud Resource order immediately. Partner should manually update the "Order Control" settings as "Normal" to enable new order.</br>
        # 2. normal：Normal--After End User finished registration and authorization, they can issue Cloud Resource order immediately.</br>
        self.new_buy_status = new_buy_status  # type: str
        # Description of Sub Account.
        self.remark = remark  # type: str
        # The type of Sub Account</br>
        # 
        # 1 Agency\"s End User</br>
        # 2 Reseller\"s End user</br>
        # 5 Reseller\"s T2 Partner</br>
        self.sub_account_type = sub_account_type  # type: str
        # Partner\"s Shutdown Policy Management for Sub Account.</br>
        # 1: delayStop. The account have Shutdown-delay Privilege,  After Shutdown-delay Credit is ran out, Alibaba Cloud will take over resources and keep the instance for 15 days. In addition, the instance will be released if Sub Account failed to pay the bill within these 15 days.</br>
        # 2: noStop. Partner will manually manage Shutdown Status for Sub Account. Meanwhile, System would not manage the resource\"s life-circle of Sub Account.</br>
        # 3: immediatelyStop. Once valid quota of Sub Account falls below 0 and be identified as defaulting account, it will trigger the instance shutdown immediately.</br>
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
        # List of invited account information,  less than 5 accounts at a time.</br>
        # `Sub-levels <= 5`
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
        # Valid days of registration URL, count on daily basis.
        self.days = days  # type: int
        # Invitation ID, The invitation status tracking code.
        self.invite_id = invite_id  # type: long
        # URL for Partner Customer Registration.
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
        # Error Code, 200 OK
        self.code = code  # type: str
        # Message, Notes of Code
        self.message = message  # type: str
        # Returning Message of Invitation Results
        self.result = result  # type: InviteSubAccountResponseBodyResultsResultResult
        # Always true.
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
        # Error Code: </br>
        # • 200 OK</br>
        # • 1109 System Error</br>
        self.code = code  # type: str
        # Message</br>
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this ID.
        self.request_id = request_id  # type: str
        # List of invitation sending results
        self.results = results  # type: InviteSubAccountResponseBodyResults
        # Candidate Values: True/False, this value states if the current API calling action is successful. It does not guarantee the success of subsequent business operations.
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
        # Error Code
        # * 200: OK
        # * 1109: System error
        self.code = code  # type: str
        # List of Region Code
        self.data = data  # type: list[str]
        # Message information
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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


class QuotaListExportPagedRequest(TeaModel):
    def __init__(self, current_page=None, language=None, page_size=None):
        # Pagination, current page number, starting from 1.
        self.current_page = current_page  # type: int
        # Multilingual Parameters, the default language is English.</br>
        # en: English</br>
        # zh: Chinese</br>
        # ja: Japanese </br>
        self.language = language  # type: str
        # Pagination, record number on each page, maximum 100.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaListExportPagedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.language is not None:
            result['Language'] = self.language
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QuotaListExportPagedResponseBodyData(TeaModel):
    def __init__(self, create_time=None, file_name=None, message=None, status=None, status_code=None, url=None):
        # Create Time
        self.create_time = create_time  # type: str
        # File Name
        self.file_name = file_name  # type: str
        # Notification Message
        self.message = message  # type: str
        # Display of Task Status
        self.status = status  # type: str
        # Task Status Enum</br>
        # 2: Exporting</br>
        # 3: Export Success</br>
        # -1: Export Fail</br>
        self.status_code = status_code  # type: str
        # The link to download exported file.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuotaListExportPagedResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QuotaListExportPagedResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, page_no=None, page_size=None, request_id=None, total=None):
        # Status code of returning result, 200 means success.
        self.code = code  # type: str
        # Listed data of returning result
        self.data = data  # type: list[QuotaListExportPagedResponseBodyData]
        # Description of returning result
        self.msg = msg  # type: str
        # Current page number
        self.page_no = page_no  # type: int
        # Record number on each page
        self.page_size = page_size  # type: int
        # ID of the Request
        self.request_id = request_id  # type: str
        # Total volume
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuotaListExportPagedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuotaListExportPagedResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QuotaListExportPagedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuotaListExportPagedResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuotaListExportPagedResponse, self).to_map()
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
            temp_model = QuotaListExportPagedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendEmailRequest(TeaModel):
    def __init__(self, invite_id=None):
        # Invitation ID, from interface InviteSubAccount </br>
        # Note: This field type is Long, which may result in precision loss in serialization/deserialization process. Please ensure the value does not exceed 9007199254740991.
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
        # Result Code, Error code.</br>
        # Candidate Value: </br>
        # * 200: OK
        # * 1109: System error
        # * 3058: Frequent sending, the limit is 10 emails in every 5 minutes.
        # * 3057: InviteId is empty.
        # * 3060: Can\"t find sending record of given InviteId.
        # * 3061: Registration URL is expired, unable to resend.
        self.code = code  # type: str
        # Result message
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # Sub Account Nickname. 
        # * Use the official name of Company, if Sub Account is an enterprise.
        # * Use the official name of Partner, if Sub Account is a T2 reseller.
        self.account_nickname = account_nickname  # type: str
        # Description of Sub Account.
        self.remark = remark  # type: str
        # The UID of Sub Account.
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
        # Result Code:
        # *   200 OK
        # *   1109 System error
        # *   3030 Sub Account Nickname exceeds maximum length,  maximum length 150 bytes.
        # *   3031 Remark exceeds maximum length,  maximum length 3000 bytes.
        self.code = code  # type: str
        # Message information
        self.message = message  # type: str
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # New Credit Line
        self.credit_line = credit_line  # type: str
        # The UID of Sub Account.
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
        # Result Code:
        # *   200 OK
        # *   1109 system error
        # *   3040 Sub Account is in a frozen state and cannot be operated.
        # *   3041 Credit is not a proper number
        self.code = code  # type: str
        # Same as Code parameter value
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        # The UID of the partner‘s customer.
        self.uid = uid  # type: long
        # Percentage, 1 to 100. When the available credit limit is lower than the credit limit percentage, an email is sent to the main account.
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
        # Result Code:
        # * 200 OK
        # * 1109 System Error
        # * 3040 The Sub Account is frozen, the operation cannot be completed. 
        # * 3044 Alert proportion value is not a number.
        # * 3045 Alert proportion value should between 1 to 100.
        self.code = code  # type: str
        # Same as Code parameter value
        self.message = message  # type: str
        # Request ID, the unique request identifier generated by Alibaba Cloud.
        self.request_id = request_id  # type: str
        # Candidate Value: True or False, which indicates whether the current API call itself is successful. does not represent the success of subsequent business operations.
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


