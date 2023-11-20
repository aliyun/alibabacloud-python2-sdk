# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchBindDeviceRequestDeviceList(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDeviceRequestDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class BatchBindDeviceRequest(TeaModel):
    def __init__(self, device_list=None, identity_id=None, open_id=None, open_id_app_key=None):
        self.device_list = device_list  # type: list[BatchBindDeviceRequestDeviceList]
        self.identity_id = identity_id  # type: str
        self.open_id = open_id  # type: str
        self.open_id_app_key = open_id_app_key  # type: str

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.open_id_app_key is not None:
            result['OpenIdAppKey'] = self.open_id_app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = BatchBindDeviceRequestDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('OpenIdAppKey') is not None:
            self.open_id_app_key = m.get('OpenIdAppKey')
        return self


class BatchBindDeviceResponseBodyDataBindDeviceList(TeaModel):
    def __init__(self, bind_result_code=None, bind_result_message=None, device_name=None, iot_id=None,
                 product_key=None):
        self.bind_result_code = bind_result_code  # type: int
        self.bind_result_message = bind_result_message  # type: str
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDeviceResponseBodyDataBindDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_result_code is not None:
            result['BindResultCode'] = self.bind_result_code
        if self.bind_result_message is not None:
            result['BindResultMessage'] = self.bind_result_message
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindResultCode') is not None:
            self.bind_result_code = m.get('BindResultCode')
        if m.get('BindResultMessage') is not None:
            self.bind_result_message = m.get('BindResultMessage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class BatchBindDeviceResponseBodyData(TeaModel):
    def __init__(self, bind_device_list=None):
        self.bind_device_list = bind_device_list  # type: list[BatchBindDeviceResponseBodyDataBindDeviceList]

    def validate(self):
        if self.bind_device_list:
            for k in self.bind_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindDeviceList'] = []
        if self.bind_device_list is not None:
            for k in self.bind_device_list:
                result['BindDeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bind_device_list = []
        if m.get('BindDeviceList') is not None:
            for k in m.get('BindDeviceList'):
                temp_model = BatchBindDeviceResponseBodyDataBindDeviceList()
                self.bind_device_list.append(temp_model.from_map(k))
        return self


class BatchBindDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: BatchBindDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchBindDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = BatchBindDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchBindDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchBindDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindDeviceResponse, self).to_map()
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
            temp_model = BatchBindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindStorageOrderRequest(TeaModel):
    def __init__(self, device_name=None, enable_default_plan=None, event_record_duration=None,
                 event_record_prolong=None, iot_id=None, max_record_file_duration=None, order_id=None, pre_record_duration=None,
                 product_key=None, user_id=None, user_name=None):
        self.device_name = device_name  # type: str
        self.enable_default_plan = enable_default_plan  # type: bool
        self.event_record_duration = event_record_duration  # type: int
        self.event_record_prolong = event_record_prolong  # type: bool
        self.iot_id = iot_id  # type: str
        self.max_record_file_duration = max_record_file_duration  # type: int
        self.order_id = order_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.product_key = product_key  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.max_record_file_duration is not None:
            result['MaxRecordFileDuration'] = self.max_record_file_duration
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MaxRecordFileDuration') is not None:
            self.max_record_file_duration = m.get('MaxRecordFileDuration')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: BindStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BindStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = BindStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindStorageOrderResponse, self).to_map()
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
            temp_model = BindStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFreeStorageValidRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFreeStorageValidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class CheckFreeStorageValidResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFreeStorageValidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFreeStorageValidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckFreeStorageValidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckFreeStorageValidResponse, self).to_map()
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
            temp_model = CheckFreeStorageValidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsumeFreeStorageRequest(TeaModel):
    def __init__(self, device_name=None, enable_default_plan=None, event_record_duration=None,
                 event_record_prolong=None, immediate_use=None, iot_id=None, pre_record_duration=None, product_key=None, quota=None):
        self.device_name = device_name  # type: str
        self.enable_default_plan = enable_default_plan  # type: bool
        self.event_record_duration = event_record_duration  # type: int
        self.event_record_prolong = event_record_prolong  # type: bool
        self.immediate_use = immediate_use  # type: bool
        self.iot_id = iot_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.product_key = product_key  # type: str
        self.quota = quota  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConsumeFreeStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.quota is not None:
            result['Quota'] = self.quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        return self


class ConsumeFreeStorageResponseBodyData(TeaModel):
    def __init__(self, consumed=None, end_time=None, end_time_utc=None, expired=None, lifecycle=None, months=None,
                 remain_quota=None, start_time=None, start_time_utc=None, type=None):
        self.consumed = consumed  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.expired = expired  # type: int
        self.lifecycle = lifecycle  # type: int
        self.months = months  # type: int
        self.remain_quota = remain_quota  # type: int
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConsumeFreeStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ConsumeFreeStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ConsumeFreeStorageResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ConsumeFreeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = ConsumeFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConsumeFreeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConsumeFreeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConsumeFreeStorageResponse, self).to_map()
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
            temp_model = ConsumeFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndPayStorageOrderRequest(TeaModel):
    def __init__(self, commodity_code=None, copies=None, device_name=None, device_no_owner=None,
                 enable_default_plan=None, event_record_duration=None, event_record_prolong=None, immediate_use=None, iot_id=None,
                 max_record_file_duration=None, pre_record_duration=None, product_key=None, specification=None, user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.device_name = device_name  # type: str
        self.device_no_owner = device_no_owner  # type: bool
        self.enable_default_plan = enable_default_plan  # type: bool
        self.event_record_duration = event_record_duration  # type: int
        self.event_record_prolong = event_record_prolong  # type: bool
        self.immediate_use = immediate_use  # type: bool
        self.iot_id = iot_id  # type: str
        self.max_record_file_duration = max_record_file_duration  # type: int
        self.pre_record_duration = pre_record_duration  # type: int
        self.product_key = product_key  # type: str
        self.specification = specification  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAndPayStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.max_record_file_duration is not None:
            result['MaxRecordFileDuration'] = self.max_record_file_duration
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MaxRecordFileDuration') is not None:
            self.max_record_file_duration = m.get('MaxRecordFileDuration')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAndPayStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAndPayStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAndPayStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateAndPayStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAndPayStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateAndPayStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAndPayStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAndPayStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAndPayStorageOrderResponse, self).to_map()
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
            temp_model = CreateAndPayStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFreeStorageRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableFreeStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableFreeStorageResponseBodyData(TeaModel):
    def __init__(self, consumed=None, end_time=None, end_time_utc=None, expired=None, lifecycle=None, months=None,
                 remain_quota=None, start_time=None, start_time_utc=None, type=None):
        self.consumed = consumed  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.expired = expired  # type: int
        self.lifecycle = lifecycle  # type: int
        self.months = months  # type: int
        self.remain_quota = remain_quota  # type: int
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableFreeStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EnableFreeStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: EnableFreeStorageResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnableFreeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableFreeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableFreeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableFreeStorageResponse, self).to_map()
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
            temp_model = EnableFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableStorageOrderRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, order_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class EnableStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: EnableStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnableStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableStorageOrderResponse, self).to_map()
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
            temp_model = EnableStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeFreeStorageRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreezeFreeStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class FreezeFreeStorageResponseBodyData(TeaModel):
    def __init__(self, consumed=None, end_time=None, end_time_utc=None, expired=None, lifecycle=None, months=None,
                 remain_quota=None, start_time=None, start_time_utc=None, type=None):
        self.consumed = consumed  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.expired = expired  # type: int
        self.lifecycle = lifecycle  # type: int
        self.months = months  # type: int
        self.remain_quota = remain_quota  # type: int
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreezeFreeStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FreezeFreeStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: FreezeFreeStorageResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FreezeFreeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = FreezeFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FreezeFreeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FreezeFreeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FreezeFreeStorageResponse, self).to_map()
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
            temp_model = FreezeFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeStorageOrderRequest(TeaModel):
    def __init__(self, device_name=None, device_no_owner=None, iot_id=None, order_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.device_no_owner = device_no_owner  # type: bool
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreezeStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class FreezeStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FreezeStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FreezeStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: FreezeStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FreezeStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = FreezeStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FreezeStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FreezeStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FreezeStorageOrderResponse, self).to_map()
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
            temp_model = FreezeStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDeviceRequest(TeaModel):
    def __init__(self, amount=None, product_key=None, project_id=None):
        self.amount = amount  # type: long
        self.product_key = product_key  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GenerateDeviceResponseBodyData(TeaModel):
    def __init__(self, batch_id=None):
        self.batch_id = batch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class GenerateDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GenerateDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GenerateDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateDeviceResponse, self).to_map()
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
            temp_model = GenerateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDeviceByBatchIdRequest(TeaModel):
    def __init__(self, batch_id=None, product_key=None, project_id=None):
        self.batch_id = batch_id  # type: str
        self.product_key = product_key  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDeviceByBatchIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GenerateDeviceByBatchIdResponseBodyData(TeaModel):
    def __init__(self, batch_id=None):
        self.batch_id = batch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateDeviceByBatchIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class GenerateDeviceByBatchIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GenerateDeviceByBatchIdResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateDeviceByBatchIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GenerateDeviceByBatchIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateDeviceByBatchIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateDeviceByBatchIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateDeviceByBatchIdResponse, self).to_map()
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
            temp_model = GenerateDeviceByBatchIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountByIdRequest(TeaModel):
    def __init__(self, identity_id=None, open_id=None, open_id_app_key=None):
        self.identity_id = identity_id  # type: str
        self.open_id = open_id  # type: str
        self.open_id_app_key = open_id_app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.open_id_app_key is not None:
            result['OpenIdAppKey'] = self.open_id_app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('OpenIdAppKey') is not None:
            self.open_id_app_key = m.get('OpenIdAppKey')
        return self


class GetAccountByIdResponseBodyData(TeaModel):
    def __init__(self, email=None, gmt_create=None, gmt_modified=None, identity_id=None, last_login_time=None,
                 login_name=None, nick_name=None, phone=None):
        self.email = email  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.identity_id = identity_id  # type: str
        self.last_login_time = last_login_time  # type: long
        self.login_name = login_name  # type: str
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountByIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetAccountByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetAccountByIdResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAccountByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GetAccountByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccountByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountByIdResponse, self).to_map()
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
            temp_model = GetAccountByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDeviceStatusResponseBodyData(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeviceStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDeviceStatusResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GetDeviceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDeviceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceStatusResponse, self).to_map()
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
            temp_model = GetDeviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubDeviceListRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, page_no=None, page_size=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubDeviceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetSubDeviceListResponseBodyDataSubDeviceList(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubDeviceListResponseBodyDataSubDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetSubDeviceListResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, sub_device_list=None, total=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sub_device_list = sub_device_list  # type: list[GetSubDeviceListResponseBodyDataSubDeviceList]
        self.total = total  # type: long

    def validate(self):
        if self.sub_device_list:
            for k in self.sub_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSubDeviceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['SubDeviceList'] = []
        if self.sub_device_list is not None:
            for k in self.sub_device_list:
                result['SubDeviceList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.sub_device_list = []
        if m.get('SubDeviceList') is not None:
            for k in m.get('SubDeviceList'):
                temp_model = GetSubDeviceListResponseBodyDataSubDeviceList()
                self.sub_device_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSubDeviceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetSubDeviceListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSubDeviceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GetSubDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubDeviceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubDeviceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubDeviceListResponse, self).to_map()
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
            temp_model = GetSubDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThingEventSnapshotRequest(TeaModel):
    def __init__(self, device_name=None, identifier=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.identifier = identifier  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThingEventSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetThingEventSnapshotResponseBodyData(TeaModel):
    def __init__(self, event_body=None, event_code=None, event_type=None, identifier=None, iot_id=None,
                 timestamp=None):
        self.event_body = event_body  # type: str
        self.event_code = event_code  # type: str
        self.event_type = event_type  # type: str
        self.identifier = identifier  # type: str
        self.iot_id = iot_id  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThingEventSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_body is not None:
            result['EventBody'] = self.event_body
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBody') is not None:
            self.event_body = m.get('EventBody')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetThingEventSnapshotResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetThingEventSnapshotResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetThingEventSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetThingEventSnapshotResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetThingEventSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetThingEventSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetThingEventSnapshotResponse, self).to_map()
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
            temp_model = GetThingEventSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetThingPropertySnapshotRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThingPropertySnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetThingPropertySnapshotResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetThingPropertySnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetThingPropertySnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetThingPropertySnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetThingPropertySnapshotResponse, self).to_map()
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
            temp_model = GetThingPropertySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeThingServiceRequest(TeaModel):
    def __init__(self, args=None, device_name=None, identifier=None, iot_id=None, product_key=None):
        self.args = args  # type: str
        self.device_name = device_name  # type: str
        self.identifier = identifier  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeThingServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class InvokeThingServiceResponseBodyData(TeaModel):
    def __init__(self, data=None, message_id=None):
        self.data = data  # type: str
        self.message_id = message_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeThingServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class InvokeThingServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InvokeThingServiceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InvokeThingServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = InvokeThingServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvokeThingServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InvokeThingServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvokeThingServiceResponse, self).to_map()
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
            temp_model = InvokeThingServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingAccountByDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, owned=None, page_no=None, page_size=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.owned = owned  # type: int
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingAccountByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.owned is not None:
            result['Owned'] = self.owned
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('Owned') is not None:
            self.owned = m.get('Owned')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListBindingAccountByDeviceResponseBodyDataAccountList(TeaModel):
    def __init__(self, bind_time=None, identity_alias=None, identity_id=None):
        self.bind_time = bind_time  # type: long
        self.identity_alias = identity_alias  # type: str
        self.identity_id = identity_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingAccountByDeviceResponseBodyDataAccountList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        if self.identity_alias is not None:
            result['IdentityAlias'] = self.identity_alias
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        if m.get('IdentityAlias') is not None:
            self.identity_alias = m.get('IdentityAlias')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        return self


class ListBindingAccountByDeviceResponseBodyData(TeaModel):
    def __init__(self, account_list=None, page_no=None, page_size=None, total=None):
        self.account_list = account_list  # type: list[ListBindingAccountByDeviceResponseBodyDataAccountList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.account_list:
            for k in self.account_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindingAccountByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountList'] = []
        if self.account_list is not None:
            for k in self.account_list:
                result['AccountList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_list = []
        if m.get('AccountList') is not None:
            for k in m.get('AccountList'):
                temp_model = ListBindingAccountByDeviceResponseBodyDataAccountList()
                self.account_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBindingAccountByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListBindingAccountByDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListBindingAccountByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = ListBindingAccountByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBindingAccountByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindingAccountByDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindingAccountByDeviceResponse, self).to_map()
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
            temp_model = ListBindingAccountByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingDeviceByAccountRequest(TeaModel):
    def __init__(self, identity_id=None, open_id=None, open_id_app_key=None, page_no=None, page_size=None,
                 sub_device=None):
        self.identity_id = identity_id  # type: str
        self.open_id = open_id  # type: str
        self.open_id_app_key = open_id_app_key  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sub_device = sub_device  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingDeviceByAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.open_id_app_key is not None:
            result['OpenIdAppKey'] = self.open_id_app_key
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_device is not None:
            result['SubDevice'] = self.sub_device
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('OpenIdAppKey') is not None:
            self.open_id_app_key = m.get('OpenIdAppKey')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubDevice') is not None:
            self.sub_device = m.get('SubDevice')
        return self


class ListBindingDeviceByAccountResponseBodyDataDeviceList(TeaModel):
    def __init__(self, bind_time=None, device_name=None, iot_id=None, node_type=None, owned=None, product_key=None):
        self.bind_time = bind_time  # type: long
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.node_type = node_type  # type: str
        self.owned = owned  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingDeviceByAccountResponseBodyDataDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owned is not None:
            result['Owned'] = self.owned
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Owned') is not None:
            self.owned = m.get('Owned')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListBindingDeviceByAccountResponseBodyData(TeaModel):
    def __init__(self, device_list=None, page_count=None, page_no=None, page_size=None, total=None):
        self.device_list = device_list  # type: list[ListBindingDeviceByAccountResponseBodyDataDeviceList]
        self.page_count = page_count  # type: int
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindingDeviceByAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = ListBindingDeviceByAccountResponseBodyDataDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListBindingDeviceByAccountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListBindingDeviceByAccountResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListBindingDeviceByAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = ListBindingDeviceByAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBindingDeviceByAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindingDeviceByAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindingDeviceByAccountResponse, self).to_map()
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
            temp_model = ListBindingDeviceByAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBatchStatusRequest(TeaModel):
    def __init__(self, batch_id=None, product_key=None, project_id=None):
        self.batch_id = batch_id  # type: str
        self.product_key = product_key  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBatchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryBatchStatusResponseBodyDataInvalidDetailList(TeaModel):
    def __init__(self, device_name=None, error_msg=None):
        self.device_name = device_name  # type: str
        self.error_msg = error_msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBatchStatusResponseBodyDataInvalidDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class QueryBatchStatusResponseBodyData(TeaModel):
    def __init__(self, invalid_detail_list=None, invalid_list=None, status=None, valid_list=None):
        self.invalid_detail_list = invalid_detail_list  # type: list[QueryBatchStatusResponseBodyDataInvalidDetailList]
        self.invalid_list = invalid_list  # type: list[str]
        self.status = status  # type: str
        self.valid_list = valid_list  # type: list[str]

    def validate(self):
        if self.invalid_detail_list:
            for k in self.invalid_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBatchStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvalidDetailList'] = []
        if self.invalid_detail_list is not None:
            for k in self.invalid_detail_list:
                result['InvalidDetailList'].append(k.to_map() if k else None)
        if self.invalid_list is not None:
            result['InvalidList'] = self.invalid_list
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_list is not None:
            result['ValidList'] = self.valid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invalid_detail_list = []
        if m.get('InvalidDetailList') is not None:
            for k in m.get('InvalidDetailList'):
                temp_model = QueryBatchStatusResponseBodyDataInvalidDetailList()
                self.invalid_detail_list.append(temp_model.from_map(k))
        if m.get('InvalidList') is not None:
            self.invalid_list = m.get('InvalidList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidList') is not None:
            self.valid_list = m.get('ValidList')
        return self


class QueryBatchStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryBatchStatusResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryBatchStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryBatchStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBatchStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBatchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBatchStatusResponse, self).to_map()
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
            temp_model = QueryBatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceDetailRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None, project_id=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryDeviceDetailResponseBodyData(TeaModel):
    def __init__(self, active_time=None, create_time=None, device_name=None, device_secret=None,
                 firmware_version=None, iot_id=None, ip_address=None, nickname=None, node_type=None, online_time=None,
                 product_key=None, product_name=None, region=None, status=None):
        self.active_time = active_time  # type: long
        self.create_time = create_time  # type: long
        self.device_name = device_name  # type: str
        self.device_secret = device_secret  # type: str
        self.firmware_version = firmware_version  # type: str
        self.iot_id = iot_id  # type: str
        self.ip_address = ip_address  # type: str
        self.nickname = nickname  # type: str
        self.node_type = node_type  # type: int
        self.online_time = online_time  # type: long
        self.product_key = product_key  # type: str
        self.product_name = product_name  # type: str
        self.region = region  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_secret is not None:
            result['DeviceSecret'] = self.device_secret
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.online_time is not None:
            result['OnlineTime'] = self.online_time
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSecret') is not None:
            self.device_secret = m.get('DeviceSecret')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OnlineTime') is not None:
            self.online_time = m.get('OnlineTime')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDeviceDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDeviceDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDeviceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceDetailResponse, self).to_map()
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
            temp_model = QueryDeviceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesDownloadUrlRequest(TeaModel):
    def __init__(self, batch_id=None, product_key=None):
        self.batch_id = batch_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicesDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDevicesDownloadUrlResponseBodyData(TeaModel):
    def __init__(self, oss_download_url=None):
        self.oss_download_url = oss_download_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicesDownloadUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_download_url is not None:
            result['OssDownloadUrl'] = self.oss_download_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssDownloadUrl') is not None:
            self.oss_download_url = m.get('OssDownloadUrl')
        return self


class QueryDevicesDownloadUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDevicesDownloadUrlResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDevicesDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicesDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicesDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDevicesDownloadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDevicesDownloadUrlResponse, self).to_map()
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
            temp_model = QueryDevicesDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFreeStorageRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFreeStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryFreeStorageResponseBodyData(TeaModel):
    def __init__(self, consumed=None, end_time=None, end_time_utc=None, expired=None, lifecycle=None, months=None,
                 remain_quota=None, start_time=None, start_time_utc=None, type=None):
        self.consumed = consumed  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.expired = expired  # type: int
        self.lifecycle = lifecycle  # type: int
        self.months = months  # type: int
        self.remain_quota = remain_quota  # type: int
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFreeStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryFreeStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFreeStorageResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFreeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFreeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFreeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFreeStorageResponse, self).to_map()
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
            temp_model = QueryFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGenerateDevicesInfoListRequest(TeaModel):
    def __init__(self, batch_id=None, page_no=None, page_size=None, project_id=None):
        self.batch_id = batch_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGenerateDevicesInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryGenerateDevicesInfoListResponseBodyDataListData(TeaModel):
    def __init__(self, device_name=None, device_secret=None, iot_id=None):
        self.device_name = device_name  # type: str
        self.device_secret = device_secret  # type: str
        self.iot_id = iot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGenerateDevicesInfoListResponseBodyDataListData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_secret is not None:
            result['DeviceSecret'] = self.device_secret
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSecret') is not None:
            self.device_secret = m.get('DeviceSecret')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryGenerateDevicesInfoListResponseBodyData(TeaModel):
    def __init__(self, list_data=None, page_no=None, page_size=None, total=None):
        self.list_data = list_data  # type: list[QueryGenerateDevicesInfoListResponseBodyDataListData]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list_data:
            for k in self.list_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesInfoListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListData'] = []
        if self.list_data is not None:
            for k in self.list_data:
                result['ListData'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_data = []
        if m.get('ListData') is not None:
            for k in m.get('ListData'):
                temp_model = QueryGenerateDevicesInfoListResponseBodyDataListData()
                self.list_data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGenerateDevicesInfoListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryGenerateDevicesInfoListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGenerateDevicesInfoListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGenerateDevicesInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryGenerateDevicesInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesInfoListResponse, self).to_map()
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
            temp_model = QueryGenerateDevicesInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGenerateDevicesRecordRequest(TeaModel):
    def __init__(self, end_time=None, page_no=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGenerateDevicesRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryGenerateDevicesRecordResponseBodyDataListData(TeaModel):
    def __init__(self, apply_device_count=None, batch_id=None, batch_status=None, create_time=None,
                 network_type=None, operate_uid=None, product_key=None, product_name=None, spec_code=None, success_count=None):
        self.apply_device_count = apply_device_count  # type: long
        self.batch_id = batch_id  # type: str
        self.batch_status = batch_status  # type: str
        self.create_time = create_time  # type: long
        self.network_type = network_type  # type: str
        self.operate_uid = operate_uid  # type: long
        self.product_key = product_key  # type: str
        self.product_name = product_name  # type: str
        self.spec_code = spec_code  # type: str
        self.success_count = success_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGenerateDevicesRecordResponseBodyDataListData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_device_count is not None:
            result['ApplyDeviceCount'] = self.apply_device_count
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.batch_status is not None:
            result['BatchStatus'] = self.batch_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.operate_uid is not None:
            result['OperateUid'] = self.operate_uid
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyDeviceCount') is not None:
            self.apply_device_count = m.get('ApplyDeviceCount')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('BatchStatus') is not None:
            self.batch_status = m.get('BatchStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OperateUid') is not None:
            self.operate_uid = m.get('OperateUid')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryGenerateDevicesRecordResponseBodyData(TeaModel):
    def __init__(self, list_data=None, page_no=None, page_size=None, total=None):
        self.list_data = list_data  # type: list[QueryGenerateDevicesRecordResponseBodyDataListData]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list_data:
            for k in self.list_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListData'] = []
        if self.list_data is not None:
            for k in self.list_data:
                result['ListData'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_data = []
        if m.get('ListData') is not None:
            for k in m.get('ListData'):
                temp_model = QueryGenerateDevicesRecordResponseBodyDataListData()
                self.list_data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGenerateDevicesRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryGenerateDevicesRecordResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGenerateDevicesRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGenerateDevicesRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryGenerateDevicesRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGenerateDevicesRecordResponse, self).to_map()
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
            temp_model = QueryGenerateDevicesRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageCommodityListResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, commodity_name=None, lifecycle=None, months=None, price=None,
                 record_type=None, specification=None):
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.lifecycle = lifecycle  # type: int
        self.months = months  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStorageCommodityListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class QueryStorageCommodityListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryStorageCommodityListResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryStorageCommodityListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryStorageCommodityListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageCommodityListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStorageCommodityListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStorageCommodityListResponse, self).to_map()
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
            temp_model = QueryStorageCommodityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageOrderRequest(TeaModel):
    def __init__(self, device_name=None, device_no_owner=None, iot_id=None, order_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.device_no_owner = device_no_owner  # type: bool
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStorageOrderResponse, self).to_map()
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
            temp_model = QueryStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageOrderListRequest(TeaModel):
    def __init__(self, device_name=None, device_no_owner=None, iot_id=None, page_no=None, page_size=None,
                 product_key=None):
        self.device_name = device_name  # type: str
        self.device_no_owner = device_no_owner  # type: bool
        self.iot_id = iot_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStorageOrderListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStorageOrderListResponseBodyDataStorageOrderList(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStorageOrderListResponseBodyDataStorageOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryStorageOrderListResponseBodyData(TeaModel):
    def __init__(self, page_count=None, page_no=None, page_size=None, storage_order_list=None, total=None):
        self.page_count = page_count  # type: int
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.storage_order_list = storage_order_list  # type: list[QueryStorageOrderListResponseBodyDataStorageOrderList]
        self.total = total  # type: int

    def validate(self):
        if self.storage_order_list:
            for k in self.storage_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryStorageOrderListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['StorageOrderList'] = []
        if self.storage_order_list is not None:
            for k in self.storage_order_list:
                result['StorageOrderList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.storage_order_list = []
        if m.get('StorageOrderList') is not None:
            for k in m.get('StorageOrderList'):
                temp_model = QueryStorageOrderListResponseBodyDataStorageOrderList()
                self.storage_order_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryStorageOrderListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryStorageOrderListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryStorageOrderListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStorageOrderListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageOrderListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStorageOrderListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStorageOrderListResponse, self).to_map()
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
            temp_model = QueryStorageOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetThingPropertyRequest(TeaModel):
    def __init__(self, args=None, device_name=None, iot_id=None, product_key=None):
        self.args = args  # type: str
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetThingPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class SetThingPropertyResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetThingPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetThingPropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetThingPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetThingPropertyResponse, self).to_map()
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
            temp_model = SetThingPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferStorageOrderRequest(TeaModel):
    def __init__(self, dst_iot_id=None, enable_default_plan=None, event_record_duration=None,
                 event_record_prolong=None, immediate_use=None, pre_record_duration=None, src_iot_id=None, src_order_id=None,
                 support_cross_identity_transfer=None, user_id=None, user_name=None):
        self.dst_iot_id = dst_iot_id  # type: str
        self.enable_default_plan = enable_default_plan  # type: bool
        self.event_record_duration = event_record_duration  # type: int
        self.event_record_prolong = event_record_prolong  # type: bool
        self.immediate_use = immediate_use  # type: bool
        self.pre_record_duration = pre_record_duration  # type: int
        self.src_iot_id = src_iot_id  # type: str
        self.src_order_id = src_order_id  # type: str
        self.support_cross_identity_transfer = support_cross_identity_transfer  # type: bool
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferStorageOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_iot_id is not None:
            result['DstIotId'] = self.dst_iot_id
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.src_iot_id is not None:
            result['SrcIotId'] = self.src_iot_id
        if self.src_order_id is not None:
            result['SrcOrderId'] = self.src_order_id
        if self.support_cross_identity_transfer is not None:
            result['SupportCrossIdentityTransfer'] = self.support_cross_identity_transfer
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstIotId') is not None:
            self.dst_iot_id = m.get('DstIotId')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('SrcIotId') is not None:
            self.src_iot_id = m.get('SrcIotId')
        if m.get('SrcOrderId') is not None:
            self.src_order_id = m.get('SrcOrderId')
        if m.get('SupportCrossIdentityTransfer') is not None:
            self.support_cross_identity_transfer = m.get('SupportCrossIdentityTransfer')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class TransferStorageOrderResponseBodyData(TeaModel):
    def __init__(self, commodity_code=None, copies=None, end_time=None, end_time_utc=None, identity_id=None,
                 iot_id=None, order_id=None, order_type=None, out_order_no=None, payment_status=None, pre_consume=None,
                 price=None, record_type=None, specification=None, start_time=None, start_time_utc=None, status=None,
                 user_id=None, user_name=None):
        self.commodity_code = commodity_code  # type: str
        self.copies = copies  # type: int
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: int
        self.out_order_no = out_order_no  # type: str
        self.payment_status = payment_status  # type: int
        self.pre_consume = pre_consume  # type: int
        self.price = price  # type: str
        self.record_type = record_type  # type: int
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferStorageOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class TransferStorageOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: TransferStorageOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TransferStorageOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = TransferStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferStorageOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferStorageOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferStorageOrderResponse, self).to_map()
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
            temp_model = TransferStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAllUserByDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None, unbind_sub_device=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.unbind_sub_device = unbind_sub_device  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindAllUserByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.unbind_sub_device is not None:
            result['UnbindSubDevice'] = self.unbind_sub_device
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UnbindSubDevice') is not None:
            self.unbind_sub_device = m.get('UnbindSubDevice')
        return self


class UnbindAllUserByDeviceResponseBodyDataSubDeviceUnbindResult(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None, unbind_result_code=None,
                 unbind_result_message=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.unbind_result_code = unbind_result_code  # type: int
        self.unbind_result_message = unbind_result_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindAllUserByDeviceResponseBodyDataSubDeviceUnbindResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.unbind_result_code is not None:
            result['UnbindResultCode'] = self.unbind_result_code
        if self.unbind_result_message is not None:
            result['UnbindResultMessage'] = self.unbind_result_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UnbindResultCode') is not None:
            self.unbind_result_code = m.get('UnbindResultCode')
        if m.get('UnbindResultMessage') is not None:
            self.unbind_result_message = m.get('UnbindResultMessage')
        return self


class UnbindAllUserByDeviceResponseBodyData(TeaModel):
    def __init__(self, sub_device_unbind_result=None):
        self.sub_device_unbind_result = sub_device_unbind_result  # type: list[UnbindAllUserByDeviceResponseBodyDataSubDeviceUnbindResult]

    def validate(self):
        if self.sub_device_unbind_result:
            for k in self.sub_device_unbind_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnbindAllUserByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubDeviceUnbindResult'] = []
        if self.sub_device_unbind_result is not None:
            for k in self.sub_device_unbind_result:
                result['SubDeviceUnbindResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sub_device_unbind_result = []
        if m.get('SubDeviceUnbindResult') is not None:
            for k in m.get('SubDeviceUnbindResult'):
                temp_model = UnbindAllUserByDeviceResponseBodyDataSubDeviceUnbindResult()
                self.sub_device_unbind_result.append(temp_model.from_map(k))
        return self


class UnbindAllUserByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UnbindAllUserByDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UnbindAllUserByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UnbindAllUserByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindAllUserByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindAllUserByDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindAllUserByDeviceResponse, self).to_map()
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
            temp_model = UnbindAllUserByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceRequest(TeaModel):
    def __init__(self, device_name=None, identity_id=None, iot_id=None, open_id=None, open_id_app_key=None,
                 product_key=None, unbind_sub_device=None):
        self.device_name = device_name  # type: str
        self.identity_id = identity_id  # type: str
        self.iot_id = iot_id  # type: str
        self.open_id = open_id  # type: str
        self.open_id_app_key = open_id_app_key  # type: str
        self.product_key = product_key  # type: str
        self.unbind_sub_device = unbind_sub_device  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.open_id_app_key is not None:
            result['OpenIdAppKey'] = self.open_id_app_key
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.unbind_sub_device is not None:
            result['UnbindSubDevice'] = self.unbind_sub_device
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('OpenIdAppKey') is not None:
            self.open_id_app_key = m.get('OpenIdAppKey')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UnbindSubDevice') is not None:
            self.unbind_sub_device = m.get('UnbindSubDevice')
        return self


class UnbindDeviceResponseBodyDataSubDeviceUnbindResult(TeaModel):
    def __init__(self, device_name=None, iot_id=None, product_key=None, unbind_result_code=None,
                 unbind_result_message=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.unbind_result_code = unbind_result_code  # type: int
        self.unbind_result_message = unbind_result_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDeviceResponseBodyDataSubDeviceUnbindResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.unbind_result_code is not None:
            result['UnbindResultCode'] = self.unbind_result_code
        if self.unbind_result_message is not None:
            result['UnbindResultMessage'] = self.unbind_result_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UnbindResultCode') is not None:
            self.unbind_result_code = m.get('UnbindResultCode')
        if m.get('UnbindResultMessage') is not None:
            self.unbind_result_message = m.get('UnbindResultMessage')
        return self


class UnbindDeviceResponseBodyData(TeaModel):
    def __init__(self, sub_device_unbind_result=None):
        self.sub_device_unbind_result = sub_device_unbind_result  # type: list[UnbindDeviceResponseBodyDataSubDeviceUnbindResult]

    def validate(self):
        if self.sub_device_unbind_result:
            for k in self.sub_device_unbind_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnbindDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubDeviceUnbindResult'] = []
        if self.sub_device_unbind_result is not None:
            for k in self.sub_device_unbind_result:
                result['SubDeviceUnbindResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sub_device_unbind_result = []
        if m.get('SubDeviceUnbindResult') is not None:
            for k in m.get('SubDeviceUnbindResult'):
                temp_model = UnbindDeviceResponseBodyDataSubDeviceUnbindResult()
                self.sub_device_unbind_result.append(temp_model.from_map(k))
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UnbindDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UnbindDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UnbindDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindDeviceResponse, self).to_map()
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
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceNameListRequest(TeaModel):
    def __init__(self, device_names=None, product_key=None, project_id=None):
        self.device_names = device_names  # type: list[str]
        self.product_key = product_key  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDeviceNameListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_names is not None:
            result['DeviceNames'] = self.device_names
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNames') is not None:
            self.device_names = m.get('DeviceNames')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UploadDeviceNameListResponseBodyDataInvalidDetailList(TeaModel):
    def __init__(self, device_name=None, error_msg=None):
        self.device_name = device_name  # type: str
        self.error_msg = error_msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDeviceNameListResponseBodyDataInvalidDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class UploadDeviceNameListResponseBodyData(TeaModel):
    def __init__(self, batch_id=None, invalid_detail_list=None, invalid_device_name_list=None,
                 repeated_device_name_list=None):
        self.batch_id = batch_id  # type: str
        self.invalid_detail_list = invalid_detail_list  # type: list[UploadDeviceNameListResponseBodyDataInvalidDetailList]
        self.invalid_device_name_list = invalid_device_name_list  # type: list[str]
        self.repeated_device_name_list = repeated_device_name_list  # type: list[str]

    def validate(self):
        if self.invalid_detail_list:
            for k in self.invalid_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadDeviceNameListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        result['InvalidDetailList'] = []
        if self.invalid_detail_list is not None:
            for k in self.invalid_detail_list:
                result['InvalidDetailList'].append(k.to_map() if k else None)
        if self.invalid_device_name_list is not None:
            result['InvalidDeviceNameList'] = self.invalid_device_name_list
        if self.repeated_device_name_list is not None:
            result['RepeatedDeviceNameList'] = self.repeated_device_name_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        self.invalid_detail_list = []
        if m.get('InvalidDetailList') is not None:
            for k in m.get('InvalidDetailList'):
                temp_model = UploadDeviceNameListResponseBodyDataInvalidDetailList()
                self.invalid_detail_list.append(temp_model.from_map(k))
        if m.get('InvalidDeviceNameList') is not None:
            self.invalid_device_name_list = m.get('InvalidDeviceNameList')
        if m.get('RepeatedDeviceNameList') is not None:
            self.repeated_device_name_list = m.get('RepeatedDeviceNameList')
        return self


class UploadDeviceNameListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UploadDeviceNameListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UploadDeviceNameListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UploadDeviceNameListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDeviceNameListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadDeviceNameListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadDeviceNameListResponse, self).to_map()
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
            temp_model = UploadDeviceNameListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


