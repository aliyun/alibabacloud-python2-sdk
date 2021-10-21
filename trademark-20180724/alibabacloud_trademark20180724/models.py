# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class QueryTradeProduceListRequest(TeaModel):
    def __init__(self, register_number=None, page_num=None, page_size=None, pre_order_id=None, buyer_status=None,
                 sort_order=None, sort_filed=None, biz_id=None):
        self.register_number = register_number  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.pre_order_id = pre_order_id  # type: str
        self.buyer_status = buyer_status  # type: int
        self.sort_order = sort_order  # type: str
        self.sort_filed = sort_filed  # type: str
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeProduceListResponseBodyDataTradeProduces(TeaModel):
    def __init__(self, update_time=None, pre_amount=None, create_time=None, user_id=None, biz_id=None, icon=None,
                 buyer_status=None, source=None, operate_note=None, pre_order_id=None, allow_cancel=None, register_number=None,
                 classification=None, final_amount=None, fail_reason=None):
        self.update_time = update_time  # type: long
        self.pre_amount = pre_amount  # type: float
        self.create_time = create_time  # type: long
        self.user_id = user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.icon = icon  # type: str
        self.buyer_status = buyer_status  # type: int
        self.source = source  # type: int
        self.operate_note = operate_note  # type: str
        self.pre_order_id = pre_order_id  # type: str
        self.allow_cancel = allow_cancel  # type: bool
        self.register_number = register_number  # type: str
        self.classification = classification  # type: str
        self.final_amount = final_amount  # type: float
        self.fail_reason = fail_reason  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBodyDataTradeProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.source is not None:
            result['Source'] = self.source
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryTradeProduceListResponseBodyData(TeaModel):
    def __init__(self, trade_produces=None):
        self.trade_produces = trade_produces  # type: list[QueryTradeProduceListResponseBodyDataTradeProduces]

    def validate(self):
        if self.trade_produces:
            for k in self.trade_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TradeProduces'] = []
        if self.trade_produces is not None:
            for k in self.trade_produces:
                result['TradeProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trade_produces = []
        if m.get('TradeProduces') is not None:
            for k in m.get('TradeProduces'):
                temp_model = QueryTradeProduceListResponseBodyDataTradeProduces()
                self.trade_produces.append(temp_model.from_map(k))
        return self


class QueryTradeProduceListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryTradeProduceListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeProduceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeProduceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponse, self).to_map()
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
            temp_model = QueryTradeProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorResultsRequest(TeaModel):
    def __init__(self, rule_id=None, action_type=None, procedure_status=None, tm_name=None, apply_year=None,
                 registration_number=None, classification=None, page_num=None, page_size=None):
        self.rule_id = rule_id  # type: long
        self.action_type = action_type  # type: int
        self.procedure_status = procedure_status  # type: int
        self.tm_name = tm_name  # type: str
        self.apply_year = apply_year  # type: str
        self.registration_number = registration_number  # type: str
        self.classification = classification  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.procedure_status is not None:
            result['ProcedureStatus'] = self.procedure_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.apply_year is not None:
            result['ApplyYear'] = self.apply_year
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ProcedureStatus') is not None:
            self.procedure_status = m.get('ProcedureStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('ApplyYear') is not None:
            self.apply_year = m.get('ApplyYear')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult(TeaModel):
    def __init__(self, tm_procedure_status_desc=None, wuxiao_end_date=None, user_id=None, owner_en_name=None,
                 tm_uid=None, owner_name=None, data_update_time=None, chesan_end_date=None, xuzhan_end_date=None,
                 rule_id=None, registration_number=None, tm_name=None, tm_image=None, data_create_time=None,
                 yiyi_end_date=None, classification=None, apply_date=None):
        self.tm_procedure_status_desc = tm_procedure_status_desc  # type: str
        self.wuxiao_end_date = wuxiao_end_date  # type: str
        self.user_id = user_id  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.tm_uid = tm_uid  # type: str
        self.owner_name = owner_name  # type: str
        self.data_update_time = data_update_time  # type: long
        self.chesan_end_date = chesan_end_date  # type: str
        self.xuzhan_end_date = xuzhan_end_date  # type: str
        self.rule_id = rule_id  # type: str
        self.registration_number = registration_number  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_image = tm_image  # type: str
        self.data_create_time = data_create_time  # type: long
        self.yiyi_end_date = yiyi_end_date  # type: str
        self.classification = classification  # type: str
        self.apply_date = apply_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_procedure_status_desc is not None:
            result['TmProcedureStatusDesc'] = self.tm_procedure_status_desc
        if self.wuxiao_end_date is not None:
            result['WuxiaoEndDate'] = self.wuxiao_end_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.tm_uid is not None:
            result['TmUid'] = self.tm_uid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.data_update_time is not None:
            result['DataUpdateTime'] = self.data_update_time
        if self.chesan_end_date is not None:
            result['ChesanEndDate'] = self.chesan_end_date
        if self.xuzhan_end_date is not None:
            result['XuzhanEndDate'] = self.xuzhan_end_date
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.data_create_time is not None:
            result['DataCreateTime'] = self.data_create_time
        if self.yiyi_end_date is not None:
            result['YiyiEndDate'] = self.yiyi_end_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TmProcedureStatusDesc') is not None:
            self.tm_procedure_status_desc = m.get('TmProcedureStatusDesc')
        if m.get('WuxiaoEndDate') is not None:
            self.wuxiao_end_date = m.get('WuxiaoEndDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('TmUid') is not None:
            self.tm_uid = m.get('TmUid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('DataUpdateTime') is not None:
            self.data_update_time = m.get('DataUpdateTime')
        if m.get('ChesanEndDate') is not None:
            self.chesan_end_date = m.get('ChesanEndDate')
        if m.get('XuzhanEndDate') is not None:
            self.xuzhan_end_date = m.get('XuzhanEndDate')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('DataCreateTime') is not None:
            self.data_create_time = m.get('DataCreateTime')
        if m.get('YiyiEndDate') is not None:
            self.yiyi_end_date = m.get('YiyiEndDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        return self


class QueryTrademarkMonitorResultsResponseBodyData(TeaModel):
    def __init__(self, tm_monitor_result=None):
        self.tm_monitor_result = tm_monitor_result  # type: list[QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult]

    def validate(self):
        if self.tm_monitor_result:
            for k in self.tm_monitor_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorResult'] = []
        if self.tm_monitor_result is not None:
            for k in self.tm_monitor_result:
                result['TmMonitorResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_monitor_result = []
        if m.get('TmMonitorResult') is not None:
            for k in m.get('TmMonitorResult'):
                temp_model = QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult()
                self.tm_monitor_result.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorResultsResponseBody(TeaModel):
    def __init__(self, next_page=None, request_id=None, pre_page=None, total_item_num=None, current_page_num=None,
                 total_page_num=None, page_size=None, data=None):
        self.next_page = next_page  # type: bool
        self.request_id = request_id  # type: str
        self.pre_page = pre_page  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: QueryTrademarkMonitorResultsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTrademarkMonitorResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTrademarkMonitorResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponse, self).to_map()
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
            temp_model = QueryTrademarkMonitorResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTradeOrderRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTradeOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class CancelTradeOrderResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTradeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CancelTradeOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelTradeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTradeOrderResponse, self).to_map()
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
            temp_model = CancelTradeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTmMonitorRuleRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTmMonitorRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTmMonitorRuleResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTmMonitorRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteTmMonitorRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTmMonitorRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTmMonitorRuleResponse, self).to_map()
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
            temp_model = DeleteTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadNotaryDataRequest(TeaModel):
    def __init__(self, notary_type=None, biz_order_no=None, upload_context=None):
        self.notary_type = notary_type  # type: int
        self.biz_order_no = biz_order_no  # type: str
        self.upload_context = upload_context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadNotaryDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.upload_context is not None:
            result['UploadContext'] = self.upload_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('UploadContext') is not None:
            self.upload_context = m.get('UploadContext')
        return self


class UploadNotaryDataResponseBody(TeaModel):
    def __init__(self, user_auth_url=None, request_id=None):
        self.user_auth_url = user_auth_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadNotaryDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_auth_url is not None:
            result['UserAuthUrl'] = self.user_auth_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserAuthUrl') is not None:
            self.user_auth_url = m.get('UserAuthUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadNotaryDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadNotaryDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadNotaryDataResponse, self).to_map()
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
            temp_model = UploadNotaryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyApplicantRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CopyApplicantResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyApplicantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyApplicantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CopyApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyApplicantResponse, self).to_map()
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
            temp_model = CopyApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PartnerUpdateTrademarkNameRequest(TeaModel):
    def __init__(self, tm_icon=None, aliyun_kp=None, type=None, biz_id=None, caller_type=None, caller_parent_id=None,
                 tm_comment=None, tm_name=None, bid=None, event_scene_type=None):
        # tmIcon
        self.tm_icon = tm_icon  # type: str
        # aliyunKp
        self.aliyun_kp = aliyun_kp  # type: str
        # type
        self.type = type  # type: int
        # bizId
        self.biz_id = biz_id  # type: str
        # callerType
        self.caller_type = caller_type  # type: str
        # callerParentId
        self.caller_parent_id = caller_parent_id  # type: long
        # tmComment
        self.tm_comment = tm_comment  # type: str
        # tmName
        self.tm_name = tm_name  # type: str
        # bid
        self.bid = bid  # type: str
        self.event_scene_type = event_scene_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        return self


class PartnerUpdateTrademarkNameResponseBody(TeaModel):
    def __init__(self, allow_retry=None, request_id=None, error_msg=None, http_status_code=None, dynamic_code=None,
                 error_code=None, dynamic_message=None, success=None, app_name=None):
        # allowRetry
        self.allow_retry = allow_retry  # type: bool
        # requestId
        self.request_id = request_id  # type: str
        # errorMsg
        self.error_msg = error_msg  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # dynamicCode
        self.dynamic_code = dynamic_code  # type: str
        # errorCode
        self.error_code = error_code  # type: str
        # dynamicMessage
        self.dynamic_message = dynamic_message  # type: str
        # success
        self.success = success  # type: bool
        # appName
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.success is not None:
            result['Success'] = self.success
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class PartnerUpdateTrademarkNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PartnerUpdateTrademarkNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameResponse, self).to_map()
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
            temp_model = PartnerUpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryIntentionDetailResponseBody(TeaModel):
    def __init__(self, status=None, type=None, update_time=None, relation_biz_id=None, create_time=None,
                 user_id=None, biz_id=None, partner_mobile=None, request_id=None, description=None, mobile=None,
                 register_number=None, classification=None, user_name=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.update_time = update_time  # type: long
        self.relation_biz_id = relation_biz_id  # type: str
        self.create_time = create_time  # type: long
        self.user_id = user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.partner_mobile = partner_mobile  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.mobile = mobile  # type: str
        self.register_number = register_number  # type: str
        self.classification = classification  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.relation_biz_id is not None:
            result['RelationBizId'] = self.relation_biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RelationBizId') is not None:
            self.relation_biz_id = m.get('RelationBizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryIntentionDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryIntentionDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionDetailResponse, self).to_map()
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
            temp_model = QueryIntentionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionPriceRequest(TeaModel):
    def __init__(self, intention_biz_id=None, channel=None):
        self.intention_biz_id = intention_biz_id  # type: str
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryIntentionPriceResponseBodyDataTmProduces(TeaModel):
    def __init__(self, type=None, status=None, order_price=None, update_time=None, material_name=None,
                 create_time=None, biz_id=None, service_price=None, tm_icon=None, tm_name=None, material_id=None,
                 supplement_id=None, loa_url=None, tm_number=None, note=None, supplement_status=None, total_price=None,
                 third_classification=None, first_classification=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.order_price = order_price  # type: float
        self.update_time = update_time  # type: long
        self.material_name = material_name  # type: str
        self.create_time = create_time  # type: long
        self.biz_id = biz_id  # type: str
        self.service_price = service_price  # type: float
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.material_id = material_id  # type: str
        self.supplement_id = supplement_id  # type: long
        self.loa_url = loa_url  # type: str
        self.tm_number = tm_number  # type: str
        self.note = note  # type: str
        self.supplement_status = supplement_status  # type: int
        self.total_price = total_price  # type: float
        self.third_classification = third_classification  # type: QueryIntentionPriceResponseBodyDataTmProducesThirdClassification
        self.first_classification = first_classification  # type: QueryIntentionPriceResponseBodyDataTmProducesFirstClassification

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.first_classification:
            self.first_classification.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        return self


class QueryIntentionPriceResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryIntentionPriceResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryIntentionPriceResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryIntentionPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryIntentionPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponse, self).to_map()
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
            temp_model = QueryIntentionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfficialFileCustomListRequest(TeaModel):
    def __init__(self, page_size=None, page_num=None):
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOfficialFileCustomListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class QueryOfficialFileCustomListResponseBodyDataCustomList(TeaModel):
    def __init__(self, status=None, expire_time=None, remark=None, download_url=None, create_time=None,
                 end_accept_time=None, start_accept_time=None):
        self.status = status  # type: str
        self.expire_time = expire_time  # type: long
        self.remark = remark  # type: str
        self.download_url = download_url  # type: str
        self.create_time = create_time  # type: long
        self.end_accept_time = end_accept_time  # type: long
        self.start_accept_time = start_accept_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBodyDataCustomList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class QueryOfficialFileCustomListResponseBodyData(TeaModel):
    def __init__(self, custom_list=None):
        self.custom_list = custom_list  # type: list[QueryOfficialFileCustomListResponseBodyDataCustomList]

    def validate(self):
        if self.custom_list:
            for k in self.custom_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomList'] = []
        if self.custom_list is not None:
            for k in self.custom_list:
                result['CustomList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_list = []
        if m.get('CustomList') is not None:
            for k in m.get('CustomList'):
                temp_model = QueryOfficialFileCustomListResponseBodyDataCustomList()
                self.custom_list.append(temp_model.from_map(k))
        return self


class QueryOfficialFileCustomListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryOfficialFileCustomListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryOfficialFileCustomListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOfficialFileCustomListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOfficialFileCustomListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponse, self).to_map()
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
            temp_model = QueryOfficialFileCustomListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkIconRequest(TeaModel):
    def __init__(self, trademark_icon_oss_key=None, event_scene_type=None):
        self.trademark_icon_oss_key = trademark_icon_oss_key  # type: str
        self.event_scene_type = event_scene_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkIconRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trademark_icon_oss_key is not None:
            result['TrademarkIconOssKey'] = self.trademark_icon_oss_key
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrademarkIconOssKey') is not None:
            self.trademark_icon_oss_key = m.get('TrademarkIconOssKey')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        return self


class CheckTrademarkIconResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkIconResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckTrademarkIconResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckTrademarkIconResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTrademarkIconResponse, self).to_map()
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
            temp_model = CheckTrademarkIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySupplementDetailRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySupplementDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QuerySupplementDetailResponseBodyFileTemplateUrls(TeaModel):
    def __init__(self, file_template_urls=None):
        self.file_template_urls = file_template_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySupplementDetailResponseBodyFileTemplateUrls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QuerySupplementDetailResponseBody(TeaModel):
    def __init__(self, operate_time=None, serial_number=None, status=None, type=None, sbj_dead_time=None,
                 accept_dead_time=None, send_time=None, accept_time=None, request_id=None, tm_number=None,
                 upload_file_template_url=None, content=None, id=None, file_template_urls=None):
        self.operate_time = operate_time  # type: long
        self.serial_number = serial_number  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.sbj_dead_time = sbj_dead_time  # type: long
        self.accept_dead_time = accept_dead_time  # type: long
        self.send_time = send_time  # type: long
        self.accept_time = accept_time  # type: long
        self.request_id = request_id  # type: str
        self.tm_number = tm_number  # type: str
        self.upload_file_template_url = upload_file_template_url  # type: str
        self.content = content  # type: str
        self.id = id  # type: long
        self.file_template_urls = file_template_urls  # type: QuerySupplementDetailResponseBodyFileTemplateUrls

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super(QuerySupplementDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QuerySupplementDetailResponseBodyFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        return self


class QuerySupplementDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySupplementDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySupplementDetailResponse, self).to_map()
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
            temp_model = QuerySupplementDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadTrademarkOnSaleRequest(TeaModel):
    def __init__(self, classification_code=None, tm_name=None, tm_icon=None, original_price=None, tm_number=None,
                 end_time=None, begin_time=None, description=None, label=None, reg_ann_date=None, owner_name=None,
                 owner_en_name=None, secondary_classification=None, third_classification=None, type=None, reason=None,
                 status=None):
        self.classification_code = classification_code  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.original_price = original_price  # type: float
        self.tm_number = tm_number  # type: str
        self.end_time = end_time  # type: long
        self.begin_time = begin_time  # type: long
        self.description = description  # type: str
        self.label = label  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.owner_name = owner_name  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.type = type  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadTrademarkOnSaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UploadTrademarkOnSaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadTrademarkOnSaleResponseBody, self).to_map()
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


class UploadTrademarkOnSaleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadTrademarkOnSaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadTrademarkOnSaleResponse, self).to_map()
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
            temp_model = UploadTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNotaryPostRequest(TeaModel):
    def __init__(self, notary_order_id=None, receiver_name=None, receiver_address=None, receiver_phone=None):
        self.notary_order_id = notary_order_id  # type: long
        self.receiver_name = receiver_name  # type: str
        self.receiver_address = receiver_address  # type: str
        self.receiver_phone = receiver_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNotaryPostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        return self


class ApplyNotaryPostResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNotaryPostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ApplyNotaryPostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyNotaryPostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyNotaryPostResponse, self).to_map()
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
            temp_model = ApplyNotaryPostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsByIntentionRequest(TeaModel):
    def __init__(self, intention_biz_id=None, channel=None, page_num=None, page_size=None, tm_produce_status=None):
        self.intention_biz_id = intention_biz_id  # type: str
        self.channel = channel  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.tm_produce_status = tm_produce_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tm_produce_status is not None:
            result['TmProduceStatus'] = self.tm_produce_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TmProduceStatus') is not None:
            self.tm_produce_status = m.get('TmProduceStatus')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces(TeaModel):
    def __init__(self, principal_description=None, type=None, status=None, order_price=None, update_time=None,
                 material_name=None, principal_value=None, create_time=None, biz_id=None, service_price=None, tm_icon=None,
                 tm_name=None, material_id=None, supplement_id=None, loa_url=None, tm_number=None, note=None,
                 supplement_status=None, total_price=None, third_classification=None, first_classification=None):
        self.principal_description = principal_description  # type: str
        self.type = type  # type: int
        self.status = status  # type: int
        self.order_price = order_price  # type: float
        self.update_time = update_time  # type: long
        self.material_name = material_name  # type: str
        self.principal_value = principal_value  # type: int
        self.create_time = create_time  # type: long
        self.biz_id = biz_id  # type: str
        self.service_price = service_price  # type: float
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.material_id = material_id  # type: str
        self.supplement_id = supplement_id  # type: long
        self.loa_url = loa_url  # type: str
        self.tm_number = tm_number  # type: str
        self.note = note  # type: str
        self.supplement_status = supplement_status  # type: int
        self.total_price = total_price  # type: float
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.first_classification:
            self.first_classification.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryTradeMarkApplicationsByIntentionResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationsByIntentionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeMarkApplicationsByIntentionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveExtensionAttributeRequest(TeaModel):
    def __init__(self, biz_id=None, attribute_key=None, attribute_value=None):
        self.biz_id = biz_id  # type: str
        self.attribute_key = attribute_key  # type: str
        self.attribute_value = attribute_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveExtensionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class SaveExtensionAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveExtensionAttributeResponseBody, self).to_map()
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


class SaveExtensionAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveExtensionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveExtensionAttributeResponse, self).to_map()
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
            temp_model = SaveExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptPartnerNotificationRequest(TeaModel):
    def __init__(self, biz_id=None, operation=None, material=None, remark=None):
        self.biz_id = biz_id  # type: str
        self.operation = operation  # type: str
        self.material = material  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptPartnerNotificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.material is not None:
            result['Material'] = self.material
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AcceptPartnerNotificationResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptPartnerNotificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class AcceptPartnerNotificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AcceptPartnerNotificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptPartnerNotificationResponse, self).to_map()
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
            temp_model = AcceptPartnerNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSupplementRequest(TeaModel):
    def __init__(self, id=None, upload_oss_key_list=None, content=None):
        self.id = id  # type: long
        self.upload_oss_key_list = upload_oss_key_list  # type: dict[str, any]
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.upload_oss_key_list is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list = m.get('UploadOssKeyList')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitSupplementShrinkRequest(TeaModel):
    def __init__(self, id=None, upload_oss_key_list_shrink=None, content=None):
        self.id = id  # type: long
        self.upload_oss_key_list_shrink = upload_oss_key_list_shrink  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.upload_oss_key_list_shrink is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list_shrink
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list_shrink = m.get('UploadOssKeyList')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitSupplementResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class SubmitSupplementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitSupplementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSupplementResponse, self).to_map()
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
            temp_model = SubmitSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceUploadTrademarkOnsaleRequest(TeaModel):
    def __init__(self, classification_code=None, tm_name=None, tm_icon=None, original_price=None, tm_number=None,
                 end_time=None, begin_time=None, description=None, label=None, reg_ann_date=None, owner_name=None,
                 owner_en_name=None, secondary_classification=None, third_classification=None, type=None, reason=None):
        self.classification_code = classification_code  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.original_price = original_price  # type: float
        self.tm_number = tm_number  # type: str
        self.end_time = end_time  # type: long
        self.begin_time = begin_time  # type: long
        self.description = description  # type: str
        self.label = label  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.owner_name = owner_name  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.type = type  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ForceUploadTrademarkOnsaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleResponseBody, self).to_map()
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


class ForceUploadTrademarkOnsaleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ForceUploadTrademarkOnsaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleResponse, self).to_map()
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
            temp_model = ForceUploadTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMaterialRequest(TeaModel):
    def __init__(self, material_id=None, biz_id=None, loa_oss_key=None, legal_notice_key=None):
        self.material_id = material_id  # type: str
        self.biz_id = biz_id  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.legal_notice_key = legal_notice_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        return self


class BindMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMaterialResponseBody, self).to_map()
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


class BindMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindMaterialResponse, self).to_map()
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
            temp_model = BindMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalResponseBody(TeaModel):
    def __init__(self, principal_description=None, principal_name=None, request_id=None, principal_value=None):
        self.principal_description = principal_description  # type: str
        self.principal_name = principal_name  # type: str
        self.request_id = request_id  # type: str
        self.principal_value = principal_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetDefaultPrincipalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDefaultPrincipalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultPrincipalResponse, self).to_map()
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
            temp_model = GetDefaultPrincipalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommunicationLogsRequest(TeaModel):
    def __init__(self, biz_id=None, type=None, page_num=None, page_size=None):
        self.biz_id = biz_id  # type: str
        self.type = type  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommunicationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCommunicationLogsResponseBodyDataTaskList(TeaModel):
    def __init__(self, note=None, biz_id=None, update_time=None, partner_code=None, create_time=None):
        self.note = note  # type: str
        self.biz_id = biz_id  # type: str
        self.update_time = update_time  # type: long
        self.partner_code = partner_code  # type: str
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class QueryCommunicationLogsResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryCommunicationLogsResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryCommunicationLogsResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryCommunicationLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryCommunicationLogsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBody, self).to_map()
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
            temp_model = QueryCommunicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCommunicationLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCommunicationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponse, self).to_map()
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
            temp_model = QueryCommunicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateQrCodeRequest(TeaModel):
    def __init__(self, uuid=None, oss_key=None, field_key=None):
        self.uuid = uuid  # type: str
        self.oss_key = oss_key  # type: str
        self.field_key = field_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateQrCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        return self


class GenerateQrCodeResponseBody(TeaModel):
    def __init__(self, uuid=None, request_id=None, expire_time=None, success=None, qrcode_url=None, field_key=None):
        self.uuid = uuid  # type: str
        self.request_id = request_id  # type: str
        self.expire_time = expire_time  # type: long
        self.success = success  # type: bool
        self.qrcode_url = qrcode_url  # type: str
        self.field_key = field_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateQrCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.success is not None:
            result['Success'] = self.success
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        return self


class GenerateQrCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateQrCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateQrCodeResponse, self).to_map()
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
            temp_model = GenerateQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDissentOriginalRequest(TeaModel):
    def __init__(self, biz_id=None, contact_name=None, contact_address=None, contact_number=None,
                 contact_province=None, contact_city=None, contact_district=None, contact_county=None):
        self.biz_id = biz_id  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_county = contact_county  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDissentOriginalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class ConfirmDissentOriginalResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDissentOriginalResponseBody, self).to_map()
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


class ConfirmDissentOriginalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfirmDissentOriginalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmDissentOriginalResponse, self).to_map()
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
            temp_model = ConfirmDissentOriginalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertImageToGrayRequest(TeaModel):
    def __init__(self, oss_key=None):
        self.oss_key = oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertImageToGrayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class ConvertImageToGrayResponseBody(TeaModel):
    def __init__(self, signature_url=None, request_id=None):
        self.signature_url = signature_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertImageToGrayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertImageToGrayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConvertImageToGrayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertImageToGrayResponse, self).to_map()
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
            temp_model = ConvertImageToGrayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionListRequest(TeaModel):
    def __init__(self, type=None, status=None, page_size=None, page_num=None, sort_filed=None, sort_order=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class QueryIntentionListResponseBodyDataIntention(TeaModel):
    def __init__(self, type=None, status=None, update_time=None, description=None, register_number=None,
                 create_time=None, user_id=None, biz_id=None, classification=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.update_time = update_time  # type: long
        self.description = description  # type: str
        self.register_number = register_number  # type: str
        self.create_time = create_time  # type: long
        self.user_id = user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionListResponseBodyDataIntention, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        return self


class QueryIntentionListResponseBodyData(TeaModel):
    def __init__(self, intention=None):
        self.intention = intention  # type: list[QueryIntentionListResponseBodyDataIntention]

    def validate(self):
        if self.intention:
            for k in self.intention:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intention'] = []
        if self.intention is not None:
            for k in self.intention:
                result['Intention'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.intention = []
        if m.get('Intention') is not None:
            for k in m.get('Intention'):
                temp_model = QueryIntentionListResponseBodyDataIntention()
                self.intention.append(temp_model.from_map(k))
        return self


class QueryIntentionListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryIntentionListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryIntentionListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryIntentionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponse, self).to_map()
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
            temp_model = QueryIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationLetterVersionRequest(TeaModel):
    def __init__(self, oss_key=None):
        self.oss_key = oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class GetAuthorizationLetterVersionResponseBody(TeaModel):
    def __init__(self, version=None, request_id=None):
        self.version = version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthorizationLetterVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuthorizationLetterVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionResponse, self).to_map()
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
            temp_model = GetAuthorizationLetterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkPriceRequest(TeaModel):
    def __init__(self, user_id=None, tm_name=None, tm_icon=None, type=None, order_data=None):
        self.user_id = user_id  # type: long
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.type = type  # type: int
        self.order_data = order_data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        return self


class QueryTrademarkPriceShrinkRequest(TeaModel):
    def __init__(self, user_id=None, tm_name=None, tm_icon=None, type=None, order_data_shrink=None):
        self.user_id = user_id  # type: long
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.type = type  # type: int
        self.order_data_shrink = order_data_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data_shrink is not None:
            result['OrderData'] = self.order_data_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data_shrink = m.get('OrderData')
        return self


class QueryTrademarkPriceResponseBodyPricesPrices(TeaModel):
    def __init__(self, original_price=None, discount_price=None, currency=None, trade_price=None,
                 classification_code=None):
        self.original_price = original_price  # type: float
        self.discount_price = discount_price  # type: float
        self.currency = currency  # type: str
        self.trade_price = trade_price  # type: float
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBodyPricesPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTrademarkPriceResponseBodyPrices(TeaModel):
    def __init__(self, prices=None):
        self.prices = prices  # type: list[QueryTrademarkPriceResponseBodyPricesPrices]

    def validate(self):
        if self.prices:
            for k in self.prices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBodyPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prices'] = []
        if self.prices is not None:
            for k in self.prices:
                result['Prices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prices = []
        if m.get('Prices') is not None:
            for k in m.get('Prices'):
                temp_model = QueryTrademarkPriceResponseBodyPricesPrices()
                self.prices.append(temp_model.from_map(k))
        return self


class QueryTrademarkPriceResponseBody(TeaModel):
    def __init__(self, original_price=None, request_id=None, discount_price=None, currency=None, trade_price=None,
                 prices=None):
        self.original_price = original_price  # type: float
        self.request_id = request_id  # type: str
        self.discount_price = discount_price  # type: float
        self.currency = currency  # type: str
        self.trade_price = trade_price  # type: float
        self.prices = prices  # type: QueryTrademarkPriceResponseBodyPrices

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Prices') is not None:
            temp_model = QueryTrademarkPriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
        return self


class QueryTrademarkPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTrademarkPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponse, self).to_map()
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
            temp_model = QueryTrademarkPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTmMonitorRuleRequest(TeaModel):
    def __init__(self, rule_source=None, rule_name=None, rule_type=None, rule_keyword=None, start_apply_date=None,
                 end_apply_date=None, classification=None, notify_status=None):
        self.rule_source = rule_source  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: int
        self.rule_keyword = rule_keyword  # type: str
        self.start_apply_date = start_apply_date  # type: str
        self.end_apply_date = end_apply_date  # type: str
        self.classification = classification  # type: dict[str, any]
        self.notify_status = notify_status  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        return self


class InsertTmMonitorRuleShrinkRequest(TeaModel):
    def __init__(self, rule_source=None, rule_name=None, rule_type=None, rule_keyword=None, start_apply_date=None,
                 end_apply_date=None, classification_shrink=None, notify_status_shrink=None):
        self.rule_source = rule_source  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: int
        self.rule_keyword = rule_keyword  # type: str
        self.start_apply_date = start_apply_date  # type: str
        self.end_apply_date = end_apply_date  # type: str
        self.classification_shrink = classification_shrink  # type: str
        self.notify_status_shrink = notify_status_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.classification_shrink is not None:
            result['Classification'] = self.classification_shrink
        if self.notify_status_shrink is not None:
            result['NotifyStatus'] = self.notify_status_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('Classification') is not None:
            self.classification_shrink = m.get('Classification')
        if m.get('NotifyStatus') is not None:
            self.notify_status_shrink = m.get('NotifyStatus')
        return self


class InsertTmMonitorRuleResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class InsertTmMonitorRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertTmMonitorRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertTmMonitorRuleResponse, self).to_map()
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
            temp_model = InsertTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorRulesRequest(TeaModel):
    def __init__(self, id=None, rule_name=None, notify_update=None, page_num=None, page_size=None):
        self.id = id  # type: str
        self.rule_name = rule_name  # type: str
        self.notify_update = notify_update  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule(TeaModel):
    def __init__(self, rule_status=None, last_finish_time=None, update_time=None, rule_type=None, create_time=None,
                 user_id=None, rule_extend=None, rule_name=None, end_time=None, start_time=None, rule_keyword=None,
                 last_run_time=None, version=None, rule_source=None, last_update_time=None, env=None, notify_update=None,
                 rule_detail=None, id=None):
        self.rule_status = rule_status  # type: str
        self.last_finish_time = last_finish_time  # type: str
        self.update_time = update_time  # type: str
        self.rule_type = rule_type  # type: int
        self.create_time = create_time  # type: str
        self.user_id = user_id  # type: str
        self.rule_extend = rule_extend  # type: str
        self.rule_name = rule_name  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.rule_keyword = rule_keyword  # type: str
        self.last_run_time = last_run_time  # type: str
        self.version = version  # type: int
        self.rule_source = rule_source  # type: str
        self.last_update_time = last_update_time  # type: str
        self.env = env  # type: str
        self.notify_update = notify_update  # type: int
        self.rule_detail = rule_detail  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rule_extend is not None:
            result['RuleExtend'] = self.rule_extend
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        if self.version is not None:
            result['Version'] = self.version
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.env is not None:
            result['Env'] = self.env
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RuleExtend') is not None:
            self.rule_extend = m.get('RuleExtend')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('RuleDetail') is not None:
            self.rule_detail = m.get('RuleDetail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryTrademarkMonitorRulesResponseBodyData(TeaModel):
    def __init__(self, tm_monitor_rule=None):
        self.tm_monitor_rule = tm_monitor_rule  # type: list[QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule]

    def validate(self):
        if self.tm_monitor_rule:
            for k in self.tm_monitor_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorRule'] = []
        if self.tm_monitor_rule is not None:
            for k in self.tm_monitor_rule:
                result['TmMonitorRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_monitor_rule = []
        if m.get('TmMonitorRule') is not None:
            for k in m.get('TmMonitorRule'):
                temp_model = QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule()
                self.tm_monitor_rule.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorRulesResponseBody(TeaModel):
    def __init__(self, next_page=None, request_id=None, pre_page=None, total_item_num=None, current_page_num=None,
                 total_page_num=None, page_size=None, data=None):
        self.next_page = next_page  # type: bool
        self.request_id = request_id  # type: str
        self.pre_page = pre_page  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: QueryTrademarkMonitorRulesResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTrademarkMonitorRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTrademarkMonitorRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponse, self).to_map()
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
            temp_model = QueryTrademarkMonitorRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DenySupplementRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DenySupplementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DenySupplementResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DenySupplementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DenySupplementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DenySupplementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DenySupplementResponse, self).to_map()
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
            temp_model = DenySupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialRequest(TeaModel):
    def __init__(self, id=None, query_unconfirmed_info=None):
        self.id = id  # type: long
        self.query_unconfirmed_info = query_unconfirmed_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query_unconfirmed_info is not None:
            result['QueryUnconfirmedInfo'] = self.query_unconfirmed_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueryUnconfirmedInfo') is not None:
            self.query_unconfirmed_info = m.get('QueryUnconfirmedInfo')
        return self


class QueryMaterialResponseBodyReviewAdditionalFiles(TeaModel):
    def __init__(self, review_additional_file=None):
        self.review_additional_file = review_additional_file  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialResponseBodyReviewAdditionalFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryMaterialResponseBody(TeaModel):
    def __init__(self, type=None, status=None, review_application_file=None, contact_district=None,
                 business_licence_url=None, passport_url=None, contact_province=None, legal_notice_url=None, city=None, eaddress=None,
                 contact_county=None, contact_email=None, request_id=None, contact_city=None, region=None, loa_url=None,
                 address=None, note=None, principal_name=None, name=None, principal_description=None, contact_number=None,
                 contact_address=None, contact_zipcode=None, contact_name=None, ename=None, valid_date=None, id_card_url=None,
                 expiration_date=None, card_number=None, country=None, town=None, loa_status=None, reason=None, id=None,
                 province=None, legal_notice_key=None, review_additional_files=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.review_application_file = review_application_file  # type: str
        self.contact_district = contact_district  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.passport_url = passport_url  # type: str
        self.contact_province = contact_province  # type: str
        self.legal_notice_url = legal_notice_url  # type: str
        self.city = city  # type: str
        self.eaddress = eaddress  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_email = contact_email  # type: str
        self.request_id = request_id  # type: str
        self.contact_city = contact_city  # type: str
        self.region = region  # type: int
        self.loa_url = loa_url  # type: str
        self.address = address  # type: str
        self.note = note  # type: str
        self.principal_name = principal_name  # type: int
        self.name = name  # type: str
        self.principal_description = principal_description  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.contact_name = contact_name  # type: str
        self.ename = ename  # type: str
        self.valid_date = valid_date  # type: long
        self.id_card_url = id_card_url  # type: str
        self.expiration_date = expiration_date  # type: long
        self.card_number = card_number  # type: str
        self.country = country  # type: str
        self.town = town  # type: str
        self.loa_status = loa_status  # type: int
        self.reason = reason  # type: str
        self.id = id  # type: long
        self.province = province  # type: str
        self.legal_notice_key = legal_notice_key  # type: str
        self.review_additional_files = review_additional_files  # type: QueryMaterialResponseBodyReviewAdditionalFiles

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super(QueryMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.city is not None:
            result['City'] = self.city
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.region is not None:
            result['Region'] = self.region
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.address is not None:
            result['Address'] = self.address
        if self.note is not None:
            result['Note'] = self.note
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.name is not None:
            result['Name'] = self.name
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ename is not None:
            result['EName'] = self.ename
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.country is not None:
            result['Country'] = self.country
        if self.town is not None:
            result['Town'] = self.town
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.id is not None:
            result['Id'] = self.id
        if self.province is not None:
            result['Province'] = self.province
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryMaterialResponseBodyReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        return self


class QueryMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMaterialResponse, self).to_map()
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
            temp_model = QueryMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrademarkOrderRequest(TeaModel):
    def __init__(self, user_id=None, tm_name=None, tm_icon=None, type=None, order_data=None, material_id=None,
                 loa_oss_key=None, is_black_icon=None, renew_info_id=None, root_code=None, channel=None, register_number=None,
                 tm_name_type=None, register_name=None, tm_comment=None, biz_id=None, uid=None, partner_code=None,
                 real_user_name=None, phone_num=None, principal_name=None, big_dipper_source=None, ua=None, legal_notice_key=None):
        self.user_id = user_id  # type: long
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.type = type  # type: int
        self.order_data = order_data  # type: str
        self.material_id = material_id  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.is_black_icon = is_black_icon  # type: bool
        self.renew_info_id = renew_info_id  # type: str
        self.root_code = root_code  # type: str
        self.channel = channel  # type: str
        self.register_number = register_number  # type: str
        self.tm_name_type = tm_name_type  # type: str
        self.register_name = register_name  # type: str
        self.tm_comment = tm_comment  # type: str
        self.biz_id = biz_id  # type: str
        self.uid = uid  # type: str
        self.partner_code = partner_code  # type: str
        self.real_user_name = real_user_name  # type: str
        self.phone_num = phone_num  # type: str
        self.principal_name = principal_name  # type: int
        self.big_dipper_source = big_dipper_source  # type: str
        self.ua = ua  # type: str
        self.legal_notice_key = legal_notice_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrademarkOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.big_dipper_source is not None:
            result['BigDipperSource'] = self.big_dipper_source
        if self.ua is not None:
            result['Ua'] = self.ua
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('BigDipperSource') is not None:
            self.big_dipper_source = m.get('BigDipperSource')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        return self


class CreateTrademarkOrderResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, order_id=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrademarkOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateTrademarkOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTrademarkOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrademarkOrderResponse, self).to_map()
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
            temp_model = CreateTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialListRequest(TeaModel):
    def __init__(self, name=None, type=None, region=None, status=None, page_num=None, page_size=None,
                 card_number=None, principal_name=None, material_id=None):
        self.name = name  # type: str
        self.type = type  # type: int
        self.region = region  # type: int
        self.status = status  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.card_number = card_number  # type: str
        self.principal_name = principal_name  # type: int
        self.material_id = material_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        return self


class QueryMaterialListResponseBodyDataTrademark(TeaModel):
    def __init__(self, principal_description=None, status=None, type=None, contact_name=None, card_number=None,
                 valid_date=None, region=None, principal_name=None, loa_status=None, name=None, loa_key=None, id=None,
                 reason=None):
        self.principal_description = principal_description  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.contact_name = contact_name  # type: str
        self.card_number = card_number  # type: str
        self.valid_date = valid_date  # type: long
        self.region = region  # type: int
        self.principal_name = principal_name  # type: int
        self.loa_status = loa_status  # type: int
        self.name = name  # type: str
        self.loa_key = loa_key  # type: str
        self.id = id  # type: long
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialListResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.region is not None:
            result['Region'] = self.region
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.name is not None:
            result['Name'] = self.name
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.id is not None:
            result['Id'] = self.id
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class QueryMaterialListResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[QueryMaterialListResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryMaterialListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryMaterialListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryMaterialListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryMaterialListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMaterialListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMaterialListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponse, self).to_map()
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
            temp_model = QueryMaterialListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkOrderRequest(TeaModel):
    def __init__(self, user_id=None, tm_name=None, tm_icon=None, type=None, order_data=None, material_id=None,
                 loa_oss_key=None, is_black_icon=None, renew_info_id=None, root_code=None, channel=None, register_number=None,
                 tm_name_type=None, register_name=None, tm_comment=None, biz_id=None, uid=None, partner_code=None,
                 real_user_name=None, phone_num=None, logo_goods_id=None):
        self.user_id = user_id  # type: long
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.type = type  # type: int
        self.order_data = order_data  # type: str
        self.material_id = material_id  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.is_black_icon = is_black_icon  # type: bool
        self.renew_info_id = renew_info_id  # type: str
        self.root_code = root_code  # type: str
        self.channel = channel  # type: str
        self.register_number = register_number  # type: str
        self.tm_name_type = tm_name_type  # type: str
        self.register_name = register_name  # type: str
        self.tm_comment = tm_comment  # type: str
        self.biz_id = biz_id  # type: str
        self.uid = uid  # type: str
        self.partner_code = partner_code  # type: str
        self.real_user_name = real_user_name  # type: str
        self.phone_num = phone_num  # type: str
        self.logo_goods_id = logo_goods_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        return self


class CheckTrademarkOrderResponseBody(TeaModel):
    def __init__(self, data=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: dict[str, any]
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckTrademarkOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckTrademarkOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTrademarkOrderResponse, self).to_map()
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
            temp_model = CheckTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsRequest(TeaModel):
    def __init__(self, tm_name=None, page_num=None, page_size=None, material_name=None, tm_number=None,
                 order_id=None, status=None, supplement_status=None, sort_order=None, type=None, biz_id=None,
                 intention_biz_id=None, hidden=None, product_type=None, logistics_no=None, classification_code=None, sort_filed=None):
        self.tm_name = tm_name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.material_name = material_name  # type: str
        self.tm_number = tm_number  # type: str
        self.order_id = order_id  # type: str
        self.status = status  # type: int
        self.supplement_status = supplement_status  # type: int
        self.sort_order = sort_order  # type: str
        self.type = type  # type: str
        self.biz_id = biz_id  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.hidden = hidden  # type: int
        self.product_type = product_type  # type: int
        self.logistics_no = logistics_no  # type: str
        self.classification_code = classification_code  # type: str
        self.sort_filed = sort_filed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags(TeaModel):
    def __init__(self, flags=None):
        self.flags = flags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_name=None, classification_code=None):
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse(TeaModel):
    def __init__(self, eng_name=None, register_time=None, eng_address=None, address=None, name=None,
                 submit_sbjtime=None):
        self.eng_name = eng_name  # type: str
        self.register_time = register_time  # type: long
        self.eng_address = eng_address  # type: str
        self.address = address  # type: str
        self.name = name  # type: str
        self.submit_sbjtime = submit_sbjtime  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProduces(TeaModel):
    def __init__(self, type=None, status=None, order_price=None, submit_audit_time=None, update_time=None,
                 material_name=None, remark=None, create_time=None, user_id=None, biz_id=None, service_price=None, tm_icon=None,
                 tm_name=None, material_id=None, supplement_id=None, loa_url=None, tm_number=None, note=None,
                 supplement_status=None, principal_name=None, total_price=None, submit_time=None, order_id=None,
                 third_classification=None, flags=None, first_classification=None, renew_response=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.order_price = order_price  # type: float
        self.submit_audit_time = submit_audit_time  # type: long
        self.update_time = update_time  # type: long
        self.material_name = material_name  # type: str
        self.remark = remark  # type: str
        self.create_time = create_time  # type: long
        self.user_id = user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.service_price = service_price  # type: float
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.material_id = material_id  # type: long
        self.supplement_id = supplement_id  # type: long
        self.loa_url = loa_url  # type: str
        self.tm_number = tm_number  # type: str
        self.note = note  # type: str
        self.supplement_status = supplement_status  # type: int
        self.principal_name = principal_name  # type: int
        self.total_price = total_price  # type: float
        self.submit_time = submit_time  # type: long
        self.order_id = order_id  # type: str
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification
        self.flags = flags  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification
        self.renew_response = renew_response  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.renew_response:
            self.renew_response.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        return self


class QueryTradeMarkApplicationsResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryTradeMarkApplicationsResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryTradeMarkApplicationsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeMarkApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicantContacterRequest(TeaModel):
    def __init__(self, contact_address=None, contact_name=None, contact_number=None, contact_email=None,
                 applicant_id=None, contact_zip_code=None, biz_id=None):
        self.contact_address = contact_address  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.applicant_id = applicant_id  # type: long
        self.contact_zip_code = contact_zip_code  # type: str
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicantContacterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class UpdateApplicantContacterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicantContacterResponseBody, self).to_map()
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


class UpdateApplicantContacterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateApplicantContacterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicantContacterResponse, self).to_map()
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
            temp_model = UpdateApplicantContacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskRequest(TeaModel):
    def __init__(self, request=None, biz_type=None):
        self.request = request  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class SaveTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskResponseBody, self).to_map()
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


class SaveTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskResponse, self).to_map()
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
            temp_model = SaveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTrademarkApplicationComplaintRequest(TeaModel):
    def __init__(self, biz_id=None, files=None, content=None):
        self.biz_id = biz_id  # type: str
        self.files = files  # type: dict[str, any]
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.files is not None:
            result['Files'] = self.files
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitTrademarkApplicationComplaintShrinkRequest(TeaModel):
    def __init__(self, biz_id=None, files_shrink=None, content=None):
        self.biz_id = biz_id  # type: str
        self.files_shrink = files_shrink  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitTrademarkApplicationComplaintResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintResponseBody, self).to_map()
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


class SubmitTrademarkApplicationComplaintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitTrademarkApplicationComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintResponse, self).to_map()
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
            temp_model = SubmitTrademarkApplicationComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteIntentionCommunicationLogRequest(TeaModel):
    def __init__(self, biz_id=None, note=None, reject=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str
        self.reject = reject  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.reject is not None:
            result['Reject'] = self.reject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Reject') is not None:
            self.reject = m.get('Reject')
        return self


class WriteIntentionCommunicationLogResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class WriteIntentionCommunicationLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WriteIntentionCommunicationLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogResponse, self).to_map()
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
            temp_model = WriteIntentionCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForOfficialFileCustomRequest(TeaModel):
    def __init__(self, end_accept_time=None, start_accept_time=None):
        self.end_accept_time = end_accept_time  # type: long
        self.start_accept_time = start_accept_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class SaveTaskForOfficialFileCustomResponseBody(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveTaskForOfficialFileCustomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveTaskForOfficialFileCustomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomResponse, self).to_map()
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
            temp_model = SaveTaskForOfficialFileCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeCombineTrademarkRequest(TeaModel):
    def __init__(self, registration_number=None, name=None, owner_name=None, products=None, accurate_match=None,
                 page_number=None, page_size=None, classification=None, similar_groups=None):
        self.registration_number = registration_number  # type: str
        self.name = name  # type: str
        self.owner_name = owner_name  # type: str
        self.products = products  # type: str
        self.accurate_match = accurate_match  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.classification = classification  # type: str
        self.similar_groups = similar_groups  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.products is not None:
            result['Products'] = self.products
        if self.accurate_match is not None:
            result['AccurateMatch'] = self.accurate_match
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('AccurateMatch') is not None:
            self.accurate_match = m.get('AccurateMatch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        return self


class DescirbeCombineTrademarkResponseBodyDataAnnouncementList(TeaModel):
    def __init__(self, image_url=None, ann_date=None, original_image_url=None, ann_type_name=None, ann_number=None,
                 ann_type_code=None):
        self.image_url = image_url  # type: str
        self.ann_date = ann_date  # type: str
        self.original_image_url = original_image_url  # type: str
        self.ann_type_name = ann_type_name  # type: str
        self.ann_number = ann_number  # type: str
        self.ann_type_code = ann_type_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyDataAnnouncementList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.ann_date is not None:
            result['AnnDate'] = self.ann_date
        if self.original_image_url is not None:
            result['OriginalImageUrl'] = self.original_image_url
        if self.ann_type_name is not None:
            result['AnnTypeName'] = self.ann_type_name
        if self.ann_number is not None:
            result['AnnNumber'] = self.ann_number
        if self.ann_type_code is not None:
            result['AnnTypeCode'] = self.ann_type_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('AnnDate') is not None:
            self.ann_date = m.get('AnnDate')
        if m.get('OriginalImageUrl') is not None:
            self.original_image_url = m.get('OriginalImageUrl')
        if m.get('AnnTypeName') is not None:
            self.ann_type_name = m.get('AnnTypeName')
        if m.get('AnnNumber') is not None:
            self.ann_number = m.get('AnnNumber')
        if m.get('AnnTypeCode') is not None:
            self.ann_type_code = m.get('AnnTypeCode')
        return self


class DescirbeCombineTrademarkResponseBodyDataProcedures(TeaModel):
    def __init__(self, procedure_step=None, procedure_result=None, procedure_code=None, procedure_date=None,
                 procedure_name=None):
        self.procedure_step = procedure_step  # type: str
        self.procedure_result = procedure_result  # type: str
        self.procedure_code = procedure_code  # type: str
        self.procedure_date = procedure_date  # type: str
        self.procedure_name = procedure_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyDataProcedures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.procedure_step is not None:
            result['ProcedureStep'] = self.procedure_step
        if self.procedure_result is not None:
            result['ProcedureResult'] = self.procedure_result
        if self.procedure_code is not None:
            result['ProcedureCode'] = self.procedure_code
        if self.procedure_date is not None:
            result['ProcedureDate'] = self.procedure_date
        if self.procedure_name is not None:
            result['ProcedureName'] = self.procedure_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProcedureStep') is not None:
            self.procedure_step = m.get('ProcedureStep')
        if m.get('ProcedureResult') is not None:
            self.procedure_result = m.get('ProcedureResult')
        if m.get('ProcedureCode') is not None:
            self.procedure_code = m.get('ProcedureCode')
        if m.get('ProcedureDate') is not None:
            self.procedure_date = m.get('ProcedureDate')
        if m.get('ProcedureName') is not None:
            self.procedure_name = m.get('ProcedureName')
        return self


class DescirbeCombineTrademarkResponseBodyData(TeaModel):
    def __init__(self, status=None, owner_address=None, pre_ann_date=None, pre_ann_number=None, intl_reg_date=None,
                 share=None, owner_en_name=None, subsequent_designation_date=None, index_id=None, reg_ann_number=None,
                 registration_number=None, second_anno_type=None, agency=None, owner_en_address=None, classification=None, name=None,
                 apply_date=None, priority_date=None, product_description=None, image=None, second_anno_number=None,
                 registration_type=None, first_anno_number=None, owner_name=None, reg_ann_date=None, similar_group=None, on_sale=None,
                 exclusive_date_limit=None, first_anno_type=None, last_procedure_status=None, law_final_status=None,
                 announcement_list=None, procedures=None):
        self.status = status  # type: str
        self.owner_address = owner_address  # type: str
        self.pre_ann_date = pre_ann_date  # type: str
        self.pre_ann_number = pre_ann_number  # type: str
        self.intl_reg_date = intl_reg_date  # type: str
        self.share = share  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.subsequent_designation_date = subsequent_designation_date  # type: str
        self.index_id = index_id  # type: str
        self.reg_ann_number = reg_ann_number  # type: str
        self.registration_number = registration_number  # type: str
        self.second_anno_type = second_anno_type  # type: str
        self.agency = agency  # type: str
        self.owner_en_address = owner_en_address  # type: str
        self.classification = classification  # type: str
        self.name = name  # type: str
        self.apply_date = apply_date  # type: str
        self.priority_date = priority_date  # type: str
        self.product_description = product_description  # type: str
        self.image = image  # type: str
        self.second_anno_number = second_anno_number  # type: str
        self.registration_type = registration_type  # type: str
        self.first_anno_number = first_anno_number  # type: str
        self.owner_name = owner_name  # type: str
        self.reg_ann_date = reg_ann_date  # type: str
        self.similar_group = similar_group  # type: str
        self.on_sale = on_sale  # type: int
        self.exclusive_date_limit = exclusive_date_limit  # type: str
        self.first_anno_type = first_anno_type  # type: str
        self.last_procedure_status = last_procedure_status  # type: str
        self.law_final_status = law_final_status  # type: str
        self.announcement_list = announcement_list  # type: list[DescirbeCombineTrademarkResponseBodyDataAnnouncementList]
        self.procedures = procedures  # type: list[DescirbeCombineTrademarkResponseBodyDataProcedures]

    def validate(self):
        if self.announcement_list:
            for k in self.announcement_list:
                if k:
                    k.validate()
        if self.procedures:
            for k in self.procedures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_number is not None:
            result['PreAnnNumber'] = self.pre_ann_number
        if self.intl_reg_date is not None:
            result['IntlRegDate'] = self.intl_reg_date
        if self.share is not None:
            result['Share'] = self.share
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.subsequent_designation_date is not None:
            result['SubsequentDesignationDate'] = self.subsequent_designation_date
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.reg_ann_number is not None:
            result['RegAnnNumber'] = self.reg_ann_number
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.second_anno_type is not None:
            result['SecondAnnoType'] = self.second_anno_type
        if self.agency is not None:
            result['Agency'] = self.agency
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.name is not None:
            result['Name'] = self.name
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.priority_date is not None:
            result['PriorityDate'] = self.priority_date
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.image is not None:
            result['Image'] = self.image
        if self.second_anno_number is not None:
            result['SecondAnnoNumber'] = self.second_anno_number
        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type
        if self.first_anno_number is not None:
            result['FirstAnnoNumber'] = self.first_anno_number
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.on_sale is not None:
            result['OnSale'] = self.on_sale
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.first_anno_type is not None:
            result['FirstAnnoType'] = self.first_anno_type
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.law_final_status is not None:
            result['LawFinalStatus'] = self.law_final_status
        result['AnnouncementList'] = []
        if self.announcement_list is not None:
            for k in self.announcement_list:
                result['AnnouncementList'].append(k.to_map() if k else None)
        result['Procedures'] = []
        if self.procedures is not None:
            for k in self.procedures:
                result['Procedures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNumber') is not None:
            self.pre_ann_number = m.get('PreAnnNumber')
        if m.get('IntlRegDate') is not None:
            self.intl_reg_date = m.get('IntlRegDate')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SubsequentDesignationDate') is not None:
            self.subsequent_designation_date = m.get('SubsequentDesignationDate')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('RegAnnNumber') is not None:
            self.reg_ann_number = m.get('RegAnnNumber')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('SecondAnnoType') is not None:
            self.second_anno_type = m.get('SecondAnnoType')
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('PriorityDate') is not None:
            self.priority_date = m.get('PriorityDate')
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('SecondAnnoNumber') is not None:
            self.second_anno_number = m.get('SecondAnnoNumber')
        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')
        if m.get('FirstAnnoNumber') is not None:
            self.first_anno_number = m.get('FirstAnnoNumber')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('OnSale') is not None:
            self.on_sale = m.get('OnSale')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('FirstAnnoType') is not None:
            self.first_anno_type = m.get('FirstAnnoType')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('LawFinalStatus') is not None:
            self.law_final_status = m.get('LawFinalStatus')
        self.announcement_list = []
        if m.get('AnnouncementList') is not None:
            for k in m.get('AnnouncementList'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataAnnouncementList()
                self.announcement_list.append(temp_model.from_map(k))
        self.procedures = []
        if m.get('Procedures') is not None:
            for k in m.get('Procedures'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataProcedures()
                self.procedures.append(temp_model.from_map(k))
        return self


class DescirbeCombineTrademarkResponseBody(TeaModel):
    def __init__(self, next_page=None, request_id=None, total_page_number=None, pre_page=None,
                 current_page_number=None, total_item_number=None, page_size=None, data=None):
        self.next_page = next_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_page_number = total_page_number  # type: int
        self.pre_page = pre_page  # type: bool
        self.current_page_number = current_page_number  # type: int
        self.total_item_number = total_item_number  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: list[DescirbeCombineTrademarkResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_number is not None:
            result['CurrentPageNumber'] = self.current_page_number
        if self.total_item_number is not None:
            result['TotalItemNumber'] = self.total_item_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNumber') is not None:
            self.current_page_number = m.get('CurrentPageNumber')
        if m.get('TotalItemNumber') is not None:
            self.total_item_number = m.get('TotalItemNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescirbeCombineTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class DescirbeCombineTrademarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescirbeCombineTrademarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponse, self).to_map()
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
            temp_model = DescirbeCombineTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotaryOrderRequest(TeaModel):
    def __init__(self, notary_order_id=None):
        self.notary_order_id = notary_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNotaryOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class GetNotaryOrderResponseBody(TeaModel):
    def __init__(self, type=None, order_price=None, legal_person_id_card=None, business_license_id=None,
                 notary_post_receipt=None, company_contact_name=None, notary_status=None, seller_back_of_id_card=None,
                 tm_register_change_certificate=None, request_id=None, legal_person_name=None, tm_image=None, notary_accept_date=None,
                 error_code=None, aliyun_order_id=None, notary_succeed_date=None, apply_post_status=None, error_msg=None,
                 name=None, business_license=None, receiver_name=None, order_date=None, company_contact_phone=None,
                 notary_type=None, notary_failed_date=None, tm_classification=None, success=None, biz_id=None,
                 notary_order_id=None, phone=None, receiver_phone=None, tm_register_certificate=None, tm_name=None,
                 tm_register_no=None, seller_company_name=None, tm_accept_certificate=None, receiver_postal_code=None,
                 notary_certificate=None, legal_person_phone=None, notary_failed_reason=None, seller_front_of_id_card=None,
                 receiver_address=None, notary_platform_name=None):
        self.type = type  # type: str
        self.order_price = order_price  # type: float
        self.legal_person_id_card = legal_person_id_card  # type: str
        self.business_license_id = business_license_id  # type: str
        self.notary_post_receipt = notary_post_receipt  # type: str
        self.company_contact_name = company_contact_name  # type: str
        self.notary_status = notary_status  # type: int
        self.seller_back_of_id_card = seller_back_of_id_card  # type: str
        self.tm_register_change_certificate = tm_register_change_certificate  # type: str
        self.request_id = request_id  # type: str
        self.legal_person_name = legal_person_name  # type: str
        self.tm_image = tm_image  # type: str
        self.notary_accept_date = notary_accept_date  # type: long
        self.error_code = error_code  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.notary_succeed_date = notary_succeed_date  # type: long
        self.apply_post_status = apply_post_status  # type: int
        self.error_msg = error_msg  # type: str
        self.name = name  # type: str
        self.business_license = business_license  # type: str
        self.receiver_name = receiver_name  # type: str
        self.order_date = order_date  # type: long
        self.company_contact_phone = company_contact_phone  # type: str
        self.notary_type = notary_type  # type: int
        self.notary_failed_date = notary_failed_date  # type: long
        self.tm_classification = tm_classification  # type: str
        self.success = success  # type: bool
        self.biz_id = biz_id  # type: str
        self.notary_order_id = notary_order_id  # type: long
        self.phone = phone  # type: str
        self.receiver_phone = receiver_phone  # type: str
        self.tm_register_certificate = tm_register_certificate  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_register_no = tm_register_no  # type: str
        self.seller_company_name = seller_company_name  # type: str
        self.tm_accept_certificate = tm_accept_certificate  # type: str
        self.receiver_postal_code = receiver_postal_code  # type: str
        self.notary_certificate = notary_certificate  # type: str
        self.legal_person_phone = legal_person_phone  # type: str
        self.notary_failed_reason = notary_failed_reason  # type: str
        self.seller_front_of_id_card = seller_front_of_id_card  # type: str
        self.receiver_address = receiver_address  # type: str
        self.notary_platform_name = notary_platform_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNotaryOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.legal_person_id_card is not None:
            result['LegalPersonIdCard'] = self.legal_person_id_card
        if self.business_license_id is not None:
            result['BusinessLicenseId'] = self.business_license_id
        if self.notary_post_receipt is not None:
            result['NotaryPostReceipt'] = self.notary_post_receipt
        if self.company_contact_name is not None:
            result['CompanyContactName'] = self.company_contact_name
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.seller_back_of_id_card is not None:
            result['SellerBackOfIdCard'] = self.seller_back_of_id_card
        if self.tm_register_change_certificate is not None:
            result['TmRegisterChangeCertificate'] = self.tm_register_change_certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.notary_accept_date is not None:
            result['NotaryAcceptDate'] = self.notary_accept_date
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.notary_succeed_date is not None:
            result['NotarySucceedDate'] = self.notary_succeed_date
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.name is not None:
            result['Name'] = self.name
        if self.business_license is not None:
            result['BusinessLicense'] = self.business_license
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.company_contact_phone is not None:
            result['CompanyContactPhone'] = self.company_contact_phone
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.notary_failed_date is not None:
            result['NotaryFailedDate'] = self.notary_failed_date
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.success is not None:
            result['Success'] = self.success
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.tm_register_certificate is not None:
            result['TmRegisterCertificate'] = self.tm_register_certificate
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.seller_company_name is not None:
            result['SellerCompanyName'] = self.seller_company_name
        if self.tm_accept_certificate is not None:
            result['TmAcceptCertificate'] = self.tm_accept_certificate
        if self.receiver_postal_code is not None:
            result['ReceiverPostalCode'] = self.receiver_postal_code
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.legal_person_phone is not None:
            result['LegalPersonPhone'] = self.legal_person_phone
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.seller_front_of_id_card is not None:
            result['SellerFrontOfIdCard'] = self.seller_front_of_id_card
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('LegalPersonIdCard') is not None:
            self.legal_person_id_card = m.get('LegalPersonIdCard')
        if m.get('BusinessLicenseId') is not None:
            self.business_license_id = m.get('BusinessLicenseId')
        if m.get('NotaryPostReceipt') is not None:
            self.notary_post_receipt = m.get('NotaryPostReceipt')
        if m.get('CompanyContactName') is not None:
            self.company_contact_name = m.get('CompanyContactName')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('SellerBackOfIdCard') is not None:
            self.seller_back_of_id_card = m.get('SellerBackOfIdCard')
        if m.get('TmRegisterChangeCertificate') is not None:
            self.tm_register_change_certificate = m.get('TmRegisterChangeCertificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('NotaryAcceptDate') is not None:
            self.notary_accept_date = m.get('NotaryAcceptDate')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('NotarySucceedDate') is not None:
            self.notary_succeed_date = m.get('NotarySucceedDate')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BusinessLicense') is not None:
            self.business_license = m.get('BusinessLicense')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('CompanyContactPhone') is not None:
            self.company_contact_phone = m.get('CompanyContactPhone')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('NotaryFailedDate') is not None:
            self.notary_failed_date = m.get('NotaryFailedDate')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('TmRegisterCertificate') is not None:
            self.tm_register_certificate = m.get('TmRegisterCertificate')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('SellerCompanyName') is not None:
            self.seller_company_name = m.get('SellerCompanyName')
        if m.get('TmAcceptCertificate') is not None:
            self.tm_accept_certificate = m.get('TmAcceptCertificate')
        if m.get('ReceiverPostalCode') is not None:
            self.receiver_postal_code = m.get('ReceiverPostalCode')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('LegalPersonPhone') is not None:
            self.legal_person_phone = m.get('LegalPersonPhone')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('SellerFrontOfIdCard') is not None:
            self.seller_front_of_id_card = m.get('SellerFrontOfIdCard')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        return self


class GetNotaryOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNotaryOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNotaryOrderResponse, self).to_map()
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
            temp_model = GetNotaryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmAdditionalMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmAdditionalMaterialResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ConfirmAdditionalMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfirmAdditionalMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialResponse, self).to_map()
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
            temp_model = ConfirmAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRenewInfoRequest(TeaModel):
    def __init__(self, name=None, eng_name=None, address=None, eng_address=None, register_time=None):
        self.name = name  # type: str
        self.eng_name = eng_name  # type: str
        self.address = address  # type: str
        self.eng_address = eng_address  # type: str
        self.register_time = register_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRenewInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        return self


class InsertRenewInfoResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None, id=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRenewInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class InsertRenewInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertRenewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertRenewInfoResponse, self).to_map()
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
            temp_model = InsertRenewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCredentialsInfoRequest(TeaModel):
    def __init__(self, oss_key=None, material_type=None, company_name=None):
        self.oss_key = oss_key  # type: str
        self.material_type = material_type  # type: str
        self.company_name = company_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCredentialsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        return self


class QueryCredentialsInfoResponseBodyCredentialsInfo(TeaModel):
    def __init__(self, card_number=None, address=None, person_name=None, province=None, company_name=None):
        self.card_number = card_number  # type: str
        self.address = address  # type: str
        self.person_name = person_name  # type: str
        self.province = province  # type: str
        self.company_name = company_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCredentialsInfoResponseBodyCredentialsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.address is not None:
            result['Address'] = self.address
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.province is not None:
            result['Province'] = self.province
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        return self


class QueryCredentialsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, credentials_info=None):
        self.request_id = request_id  # type: str
        self.credentials_info = credentials_info  # type: QueryCredentialsInfoResponseBodyCredentialsInfo

    def validate(self):
        if self.credentials_info:
            self.credentials_info.validate()

    def to_map(self):
        _map = super(QueryCredentialsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.credentials_info is not None:
            result['CredentialsInfo'] = self.credentials_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CredentialsInfo') is not None:
            temp_model = QueryCredentialsInfoResponseBodyCredentialsInfo()
            self.credentials_info = temp_model.from_map(m['CredentialsInfo'])
        return self


class QueryCredentialsInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCredentialsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCredentialsInfoResponse, self).to_map()
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
            temp_model = QueryCredentialsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTmOnsalesRequest(TeaModel):
    def __init__(self, keyword=None, classification=None, product_code=None, page_num=None, page_size=None,
                 register_number=None, tm_name=None, top_search=None, tag=None, order_price_left=None, order_price_right=None,
                 reg_left=None, reg_right=None, sort_name=None, sort_order=None, query_all=None):
        self.keyword = keyword  # type: str
        self.classification = classification  # type: str
        self.product_code = product_code  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.register_number = register_number  # type: str
        self.tm_name = tm_name  # type: str
        self.top_search = top_search  # type: str
        self.tag = tag  # type: str
        self.order_price_left = order_price_left  # type: long
        self.order_price_right = order_price_right  # type: long
        self.reg_left = reg_left  # type: int
        self.reg_right = reg_right  # type: int
        self.sort_name = sort_name  # type: str
        self.sort_order = sort_order  # type: str
        self.query_all = query_all  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTmOnsalesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.top_search is not None:
            result['TopSearch'] = self.top_search
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.order_price_left is not None:
            result['OrderPriceLeft'] = self.order_price_left
        if self.order_price_right is not None:
            result['OrderPriceRight'] = self.order_price_right
        if self.reg_left is not None:
            result['RegLeft'] = self.reg_left
        if self.reg_right is not None:
            result['RegRight'] = self.reg_right
        if self.sort_name is not None:
            result['SortName'] = self.sort_name
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.query_all is not None:
            result['QueryAll'] = self.query_all
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TopSearch') is not None:
            self.top_search = m.get('TopSearch')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('OrderPriceLeft') is not None:
            self.order_price_left = m.get('OrderPriceLeft')
        if m.get('OrderPriceRight') is not None:
            self.order_price_right = m.get('OrderPriceRight')
        if m.get('RegLeft') is not None:
            self.reg_left = m.get('RegLeft')
        if m.get('RegRight') is not None:
            self.reg_right = m.get('RegRight')
        if m.get('SortName') is not None:
            self.sort_name = m.get('SortName')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('QueryAll') is not None:
            self.query_all = m.get('QueryAll')
        return self


class SearchTmOnsalesResponseBodyTrademarks(TeaModel):
    def __init__(self, trademark_name=None, status=None, product_desc=None, registration_number=None, icon=None,
                 partner_code=None, classification=None, uid=None, product_code=None, order_price=None):
        self.trademark_name = trademark_name  # type: str
        self.status = status  # type: long
        self.product_desc = product_desc  # type: str
        self.registration_number = registration_number  # type: str
        self.icon = icon  # type: str
        self.partner_code = partner_code  # type: str
        self.classification = classification  # type: str
        self.uid = uid  # type: str
        self.product_code = product_code  # type: str
        self.order_price = order_price  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTmOnsalesResponseBodyTrademarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.status is not None:
            result['Status'] = self.status
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        return self


class SearchTmOnsalesResponseBody(TeaModel):
    def __init__(self, request_id=None, page_size=None, page_number=None, total_page_number=None, total_count=None,
                 trademarks=None):
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.total_page_number = total_page_number  # type: int
        self.total_count = total_count  # type: int
        self.trademarks = trademarks  # type: list[SearchTmOnsalesResponseBodyTrademarks]

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTmOnsalesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = SearchTmOnsalesResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class SearchTmOnsalesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchTmOnsalesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTmOnsalesResponse, self).to_map()
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
            temp_model = SearchTmOnsalesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(self, file_type=None, biz_id=None):
        self.file_type = file_type  # type: str
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(self, signature=None, host=None, request_id=None, expire_time=None, encoded_policy=None,
                 file_dir=None, access_id=None):
        self.signature = signature  # type: str
        self.host = host  # type: str
        self.request_id = request_id  # type: str
        self.expire_time = expire_time  # type: long
        self.encoded_policy = encoded_policy  # type: str
        self.file_dir = file_dir  # type: str
        self.access_id = access_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateUploadFilePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateUploadFilePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponse, self).to_map()
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
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteMaterialResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMaterialResponse, self).to_map()
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
            temp_model = DeleteMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteCommunicationLogRequest(TeaModel):
    def __init__(self, biz_id=None, note=None, target_id=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str
        self.target_id = target_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteCommunicationLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class WriteCommunicationLogResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteCommunicationLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class WriteCommunicationLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WriteCommunicationLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteCommunicationLogResponse, self).to_map()
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
            temp_model = WriteCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTradeIntentionUserRequest(TeaModel):
    def __init__(self, register_number=None, classification=None, type=None, mobile=None, vcode=None,
                 partner_code=None, user_name=None, description=None, channel=None, token=None, ua=None):
        self.register_number = register_number  # type: str
        self.classification = classification  # type: str
        self.type = type  # type: int
        self.mobile = mobile  # type: str
        self.vcode = vcode  # type: str
        self.partner_code = partner_code  # type: str
        self.user_name = user_name  # type: str
        self.description = description  # type: str
        self.channel = channel  # type: str
        self.token = token  # type: str
        self.ua = ua  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTradeIntentionUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.type is not None:
            result['Type'] = self.type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.vcode is not None:
            result['Vcode'] = self.vcode
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.token is not None:
            result['Token'] = self.token
        if self.ua is not None:
            result['Ua'] = self.ua
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Vcode') is not None:
            self.vcode = m.get('Vcode')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        return self


class InsertTradeIntentionUserResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTradeIntentionUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTradeIntentionUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertTradeIntentionUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertTradeIntentionUserResponse, self).to_map()
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
            temp_model = InsertTradeIntentionUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExtensionAttributeRequest(TeaModel):
    def __init__(self, biz_id=None, attribute_key=None):
        self.biz_id = biz_id  # type: str
        self.attribute_key = attribute_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExtensionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        return self


class QueryExtensionAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, attribute_value=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.attribute_value = attribute_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExtensionAttributeResponseBody, self).to_map()
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
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
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
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class QueryExtensionAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryExtensionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryExtensionAttributeResponse, self).to_map()
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
            temp_model = QueryExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkOnsaleRequest(TeaModel):
    def __init__(self, classification_code=None, tm_name=None, tm_icon=None, original_price=None, tm_number=None,
                 end_time=None, begin_time=None, description=None, label=None, reg_ann_date=None, owner_name=None,
                 owner_en_name=None, secondary_classification=None, third_classification=None, type=None, reason=None):
        self.classification_code = classification_code  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.original_price = original_price  # type: float
        self.tm_number = tm_number  # type: str
        self.end_time = end_time  # type: long
        self.begin_time = begin_time  # type: long
        self.description = description  # type: str
        self.label = label  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.owner_name = owner_name  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.type = type  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class UpdateTrademarkOnsaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleResponseBody, self).to_map()
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


class UpdateTrademarkOnsaleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTrademarkOnsaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleResponse, self).to_map()
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
            temp_model = UpdateTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeProduceDetailResponseBodyData(TeaModel):
    def __init__(self, update_time=None, third_code=None, share=None, pre_amount=None, create_time=None,
                 user_id=None, refund_amount=None, icon=None, biz_id=None, buyer_status=None, source=None,
                 confiscate_amount=None, operate_note=None, pre_order_id=None, extend=None, tm_name=None, exclusive_date_limit=None,
                 allow_cancel=None, register_number=None, final_amount=None, classification=None, paid_amount=None):
        self.update_time = update_time  # type: long
        self.third_code = third_code  # type: str
        self.share = share  # type: str
        self.pre_amount = pre_amount  # type: float
        self.create_time = create_time  # type: long
        self.user_id = user_id  # type: str
        self.refund_amount = refund_amount  # type: float
        self.icon = icon  # type: str
        self.biz_id = biz_id  # type: str
        self.buyer_status = buyer_status  # type: int
        self.source = source  # type: int
        self.confiscate_amount = confiscate_amount  # type: float
        self.operate_note = operate_note  # type: str
        self.pre_order_id = pre_order_id  # type: str
        self.extend = extend  # type: dict[str, any]
        self.tm_name = tm_name  # type: str
        self.exclusive_date_limit = exclusive_date_limit  # type: str
        self.allow_cancel = allow_cancel  # type: bool
        self.register_number = register_number  # type: str
        self.final_amount = final_amount  # type: float
        self.classification = classification  # type: str
        self.paid_amount = paid_amount  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.third_code is not None:
            result['ThirdCode'] = self.third_code
        if self.share is not None:
            result['Share'] = self.share
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.source is not None:
            result['Source'] = self.source
        if self.confiscate_amount is not None:
            result['ConfiscateAmount'] = self.confiscate_amount
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.paid_amount is not None:
            result['PaidAmount'] = self.paid_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ThirdCode') is not None:
            self.third_code = m.get('ThirdCode')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ConfiscateAmount') is not None:
            self.confiscate_amount = m.get('ConfiscateAmount')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PaidAmount') is not None:
            self.paid_amount = m.get('PaidAmount')
        return self


class QueryTradeProduceDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryTradeProduceDetailResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponseBody, self).to_map()
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
            temp_model = QueryTradeProduceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeProduceDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeProduceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponse, self).to_map()
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
            temp_model = QueryTradeProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQrCodeUploadStatusRequest(TeaModel):
    def __init__(self, oss_key=None, field_key=None, uuid=None):
        self.oss_key = oss_key  # type: str
        self.field_key = field_key  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryQrCodeUploadStatusResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, oss_url=None, oss_key=None, success=None):
        self.status = status  # type: int
        self.request_id = request_id  # type: str
        self.oss_url = oss_url  # type: str
        self.oss_key = oss_key  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryQrCodeUploadStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryQrCodeUploadStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusResponse, self).to_map()
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
            temp_model = QueryQrCodeUploadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApplicantRequest(TeaModel):
    def __init__(self, instance_id=None, note=None):
        self.instance_id = instance_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RejectApplicantResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApplicantResponseBody, self).to_map()
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


class RejectApplicantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RejectApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectApplicantResponse, self).to_map()
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
            temp_model = RejectApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeIntentionUserListRequest(TeaModel):
    def __init__(self, begin=None, end=None, page_size=None, page_num=None, biz_id=None, status=None):
        self.begin = begin  # type: long
        self.end = end  # type: long
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int
        self.biz_id = biz_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeIntentionUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTradeIntentionUserListResponseBodyDataTrademark(TeaModel):
    def __init__(self, type=None, status=None, description=None, mobile=None, register_number=None, biz_id=None,
                 classification=None, user_name=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.description = description  # type: str
        self.mobile = mobile  # type: str
        self.register_number = register_number  # type: str
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryTradeIntentionUserListResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[QueryTradeIntentionUserListResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTradeIntentionUserListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTradeIntentionUserListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryTradeIntentionUserListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeIntentionUserListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeIntentionUserListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeIntentionUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponse, self).to_map()
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
            temp_model = QueryTradeIntentionUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StoreMaterialTemporarilyRequest(TeaModel):
    def __init__(self, contact_zipcode=None, type=None, region=None, contact_name=None, contact_number=None,
                 contact_email=None, contact_address=None, loa_oss_key=None, name=None, card_number=None, province=None, city=None,
                 town=None, address=None, ename=None, eaddress=None, country=None, id_card_oss_key=None,
                 business_licence_oss_key=None, passport_oss_key=None, legal_notice_oss_key=None, principal_name=None,
                 contact_province=None, contact_city=None, contact_district=None, contact_county=None):
        self.contact_zipcode = contact_zipcode  # type: str
        self.type = type  # type: str
        self.region = region  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_address = contact_address  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.card_number = card_number  # type: str
        self.province = province  # type: str
        self.city = city  # type: str
        self.town = town  # type: str
        self.address = address  # type: str
        self.ename = ename  # type: str
        self.eaddress = eaddress  # type: str
        self.country = country  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.principal_name = principal_name  # type: int
        self.contact_province = contact_province  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_county = contact_county  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StoreMaterialTemporarilyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.country is not None:
            result['Country'] = self.country
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class StoreMaterialTemporarilyResponseBody(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StoreMaterialTemporarilyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StoreMaterialTemporarilyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StoreMaterialTemporarilyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StoreMaterialTemporarilyResponse, self).to_map()
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
            temp_model = StoreMaterialTemporarilyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseAdditionalMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseAdditionalMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseAdditionalMaterialResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseAdditionalMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefuseAdditionalMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefuseAdditionalMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefuseAdditionalMaterialResponse, self).to_map()
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
            temp_model = RefuseAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryInfosRequest(TeaModel):
    def __init__(self, notary_type=None, biz_order_no=None, token=None, page_num=None, page_size=None):
        self.notary_type = notary_type  # type: int
        self.biz_order_no = biz_order_no  # type: str
        self.token = token  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.token is not None:
            result['Token'] = self.token
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNotaryInfosResponseBodyDataNotaryInfo(TeaModel):
    def __init__(self, token=None, tm_register_no=None, tm_classification=None, notary_failed_reason=None,
                 gmt_modified=None, notary_status=None, biz_order_no=None):
        self.token = token  # type: str
        self.tm_register_no = tm_register_no  # type: str
        self.tm_classification = tm_classification  # type: str
        self.notary_failed_reason = notary_failed_reason  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.notary_status = notary_status  # type: int
        self.biz_order_no = biz_order_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryInfosResponseBodyDataNotaryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        return self


class ListNotaryInfosResponseBodyData(TeaModel):
    def __init__(self, notary_info=None):
        self.notary_info = notary_info  # type: list[ListNotaryInfosResponseBodyDataNotaryInfo]

    def validate(self):
        if self.notary_info:
            for k in self.notary_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryInfo'] = []
        if self.notary_info is not None:
            for k in self.notary_info:
                result['NotaryInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notary_info = []
        if m.get('NotaryInfo') is not None:
            for k in m.get('NotaryInfo'):
                temp_model = ListNotaryInfosResponseBodyDataNotaryInfo()
                self.notary_info.append(temp_model.from_map(k))
        return self


class ListNotaryInfosResponseBody(TeaModel):
    def __init__(self, next_page=None, request_id=None, success=None, error_code=None, total_item_num=None,
                 pre_page=None, current_page_num=None, error_msg=None, total_page_num=None, page_size=None, data=None):
        self.next_page = next_page  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.total_item_num = total_item_num  # type: int
        self.pre_page = pre_page  # type: bool
        self.current_page_num = current_page_num  # type: int
        self.error_msg = error_msg  # type: str
        self.total_page_num = total_page_num  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: ListNotaryInfosResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = ListNotaryInfosResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListNotaryInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNotaryInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponse, self).to_map()
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
            temp_model = ListNotaryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalNameRequest(TeaModel):
    def __init__(self, biz_type=None):
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class GetDefaultPrincipalNameResponseBody(TeaModel):
    def __init__(self, principal_name=None, request_id=None):
        self.principal_name = principal_name  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDefaultPrincipalNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultPrincipalNameResponse, self).to_map()
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
            temp_model = GetDefaultPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReceiptUrl(TeaModel):
    def __init__(self, receipt_url=None):
        self.receipt_url = receipt_url  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReceiptUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl(TeaModel):
    def __init__(self, judge_result_url=None):
        self.judge_result_url = judge_result_url  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JudgeResultUrl') is not None:
            self.judge_result_url = m.get('JudgeResultUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFlags(TeaModel):
    def __init__(self, flag=None):
        self.flag = flag  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        return self


class QueryTradeMarkApplicationDetailResponseBodyAdminUploads(TeaModel):
    def __init__(self, loa_pic_url=None, license_pic_url=None):
        self.loa_pic_url = loa_pic_url  # type: str
        self.license_pic_url = license_pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyAdminUploads, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loa_pic_url is not None:
            result['LoaPicUrl'] = self.loa_pic_url
        if self.license_pic_url is not None:
            result['LicensePicUrl'] = self.license_pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoaPicUrl') is not None:
            self.loa_pic_url = m.get('LoaPicUrl')
        if m.get('LicensePicUrl') is not None:
            self.license_pic_url = m.get('LicensePicUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFirstClassification(TeaModel):
    def __init__(self, name=None, code=None):
        self.name = name  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles(TeaModel):
    def __init__(self, review_additional_file=None):
        self.review_additional_file = review_additional_file  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(self, type=None, review_application_file=None, status=None, business_licence_url=None,
                 passport_url=None, city=None, legal_notice_url=None, eaddress=None, contact_email=None, region=None,
                 loa_url=None, address=None, principal_name=None, name=None, contact_number=None, contact_address=None,
                 contact_zipcode=None, contact_name=None, ename=None, card_number=None, expiration_date=None, id_card_url=None,
                 country=None, town=None, province=None, detailed_contact_address=None, review_additional_files=None):
        self.type = type  # type: int
        self.review_application_file = review_application_file  # type: str
        self.status = status  # type: int
        self.business_licence_url = business_licence_url  # type: str
        self.passport_url = passport_url  # type: str
        self.city = city  # type: str
        self.legal_notice_url = legal_notice_url  # type: str
        self.eaddress = eaddress  # type: str
        self.contact_email = contact_email  # type: str
        self.region = region  # type: int
        self.loa_url = loa_url  # type: str
        self.address = address  # type: str
        self.principal_name = principal_name  # type: int
        self.name = name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.contact_name = contact_name  # type: str
        self.ename = ename  # type: str
        self.card_number = card_number  # type: str
        self.expiration_date = expiration_date  # type: str
        self.id_card_url = id_card_url  # type: str
        self.country = country  # type: str
        self.town = town  # type: str
        self.province = province  # type: str
        # 详细收件地址
        self.detailed_contact_address = detailed_contact_address  # type: str
        self.review_additional_files = review_additional_files  # type: QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyMaterialDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.city is not None:
            result['City'] = self.city
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.region is not None:
            result['Region'] = self.region
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.address is not None:
            result['Address'] = self.address
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.name is not None:
            result['Name'] = self.name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ename is not None:
            result['EName'] = self.ename
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.country is not None:
            result['Country'] = self.country
        if self.town is not None:
            result['Town'] = self.town
        if self.province is not None:
            result['Province'] = self.province
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        return self


class QueryTradeMarkApplicationDetailResponseBodyRenewResponse(TeaModel):
    def __init__(self, eng_name=None, register_time=None, eng_address=None, address=None, name=None,
                 submit_sbjtime=None):
        self.eng_name = eng_name  # type: str
        self.register_time = register_time  # type: long
        self.eng_address = eng_address  # type: str
        self.address = address  # type: str
        self.name = name  # type: str
        self.submit_sbjtime = submit_sbjtime  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements(TeaModel):
    def __init__(self, review_supplement=None):
        self.review_supplement = review_supplement  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_supplement is not None:
            result['ReviewSupplement'] = self.review_supplement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewSupplement') is not None:
            self.review_supplement = m.get('ReviewSupplement')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles(TeaModel):
    def __init__(self, review_keep=None, review_audit=None, review_part=None, review_pass=None,
                 review_supplements=None):
        self.review_keep = review_keep  # type: str
        self.review_audit = review_audit  # type: str
        self.review_part = review_part  # type: str
        self.review_pass = review_pass  # type: str
        self.review_supplements = review_supplements  # type: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements

    def validate(self):
        if self.review_supplements:
            self.review_supplements.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_keep is not None:
            result['ReviewKeep'] = self.review_keep
        if self.review_audit is not None:
            result['ReviewAudit'] = self.review_audit
        if self.review_part is not None:
            result['ReviewPart'] = self.review_part
        if self.review_pass is not None:
            result['ReviewPass'] = self.review_pass
        if self.review_supplements is not None:
            result['ReviewSupplements'] = self.review_supplements.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewKeep') is not None:
            self.review_keep = m.get('ReviewKeep')
        if m.get('ReviewAudit') is not None:
            self.review_audit = m.get('ReviewAudit')
        if m.get('ReviewPart') is not None:
            self.review_part = m.get('ReviewPart')
        if m.get('ReviewPass') is not None:
            self.review_pass = m.get('ReviewPass')
        if m.get('ReviewSupplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements()
            self.review_supplements = temp_model.from_map(m['ReviewSupplements'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls(TeaModel):
    def __init__(self, file_template_urls=None):
        self.file_template_urls = file_template_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements(TeaModel):
    def __init__(self, type=None, operate_time=None, serial_number=None, status=None, sbj_dead_time=None,
                 accept_dead_time=None, send_time=None, batch_num=None, accept_time=None, tm_number=None,
                 upload_file_template_url=None, content=None, id=None, order_id=None, file_template_urls=None):
        self.type = type  # type: int
        self.operate_time = operate_time  # type: long
        self.serial_number = serial_number  # type: str
        self.status = status  # type: int
        self.sbj_dead_time = sbj_dead_time  # type: long
        self.accept_dead_time = accept_dead_time  # type: long
        self.send_time = send_time  # type: long
        self.batch_num = batch_num  # type: str
        self.accept_time = accept_time  # type: long
        self.tm_number = tm_number  # type: str
        self.upload_file_template_url = upload_file_template_url  # type: str
        self.content = content  # type: str
        self.id = id  # type: long
        self.order_id = order_id  # type: str
        self.file_template_urls = file_template_urls  # type: QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.batch_num is not None:
            result['BatchNum'] = self.batch_num
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('BatchNum') is not None:
            self.batch_num = m.get('BatchNum')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplements(TeaModel):
    def __init__(self, supplements=None):
        self.supplements = supplements  # type: list[QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements]

    def validate(self):
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements()
                self.supplements.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, name=None, code=None):
        self.name = name  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBody(TeaModel):
    def __init__(self, type=None, status=None, accept_url=None, order_price=None, submit_audit_time=None,
                 update_time=None, create_time=None, not_accept_url=None, send_time=None, service_price=None,
                 partner_mobile=None, recv_user_logistics=None, request_id=None, gray_icon_url=None, material_id=None,
                 send_sbj_logistics=None, send_user_logistics=None, loa_url=None, tm_number=None, note=None, principal_name=None,
                 partner_name=None, logistics_certificate_url=None, biz_id=None, partner_code=None, tm_name_type=None,
                 extend_info=None, tm_icon=None, tm_name=None, logistics_no=None, total_price=None, submit_time=None,
                 order_id=None, receipt_url=None, judge_result_url=None, flags=None, admin_uploads=None,
                 first_classification=None, material_detail=None, renew_response=None, review_official_files=None, supplements=None,
                 third_classification=None):
        self.type = type  # type: int
        self.status = status  # type: int
        self.accept_url = accept_url  # type: str
        self.order_price = order_price  # type: float
        self.submit_audit_time = submit_audit_time  # type: long
        self.update_time = update_time  # type: long
        self.create_time = create_time  # type: long
        self.not_accept_url = not_accept_url  # type: str
        self.send_time = send_time  # type: str
        self.service_price = service_price  # type: float
        self.partner_mobile = partner_mobile  # type: str
        self.recv_user_logistics = recv_user_logistics  # type: str
        self.request_id = request_id  # type: str
        self.gray_icon_url = gray_icon_url  # type: str
        self.material_id = material_id  # type: long
        self.send_sbj_logistics = send_sbj_logistics  # type: str
        self.send_user_logistics = send_user_logistics  # type: str
        self.loa_url = loa_url  # type: str
        self.tm_number = tm_number  # type: str
        self.note = note  # type: str
        self.principal_name = principal_name  # type: int
        self.partner_name = partner_name  # type: str
        self.logistics_certificate_url = logistics_certificate_url  # type: str
        self.biz_id = biz_id  # type: str
        self.partner_code = partner_code  # type: str
        self.tm_name_type = tm_name_type  # type: int
        self.extend_info = extend_info  # type: dict[str, any]
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.logistics_no = logistics_no  # type: str
        self.total_price = total_price  # type: float
        self.submit_time = submit_time  # type: long
        self.order_id = order_id  # type: str
        self.receipt_url = receipt_url  # type: QueryTradeMarkApplicationDetailResponseBodyReceiptUrl
        self.judge_result_url = judge_result_url  # type: QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl
        self.flags = flags  # type: QueryTradeMarkApplicationDetailResponseBodyFlags
        self.admin_uploads = admin_uploads  # type: QueryTradeMarkApplicationDetailResponseBodyAdminUploads
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationDetailResponseBodyFirstClassification
        self.material_detail = material_detail  # type: QueryTradeMarkApplicationDetailResponseBodyMaterialDetail
        self.renew_response = renew_response  # type: QueryTradeMarkApplicationDetailResponseBodyRenewResponse
        self.review_official_files = review_official_files  # type: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles
        self.supplements = supplements  # type: QueryTradeMarkApplicationDetailResponseBodySupplements
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationDetailResponseBodyThirdClassification

    def validate(self):
        if self.receipt_url:
            self.receipt_url.validate()
        if self.judge_result_url:
            self.judge_result_url.validate()
        if self.flags:
            self.flags.validate()
        if self.admin_uploads:
            self.admin_uploads.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.review_official_files:
            self.review_official_files.validate()
        if self.supplements:
            self.supplements.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.not_accept_url is not None:
            result['NotAcceptUrl'] = self.not_accept_url
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.logistics_certificate_url is not None:
            result['LogisticsCertificateUrl'] = self.logistics_certificate_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url.to_map()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.admin_uploads is not None:
            result['AdminUploads'] = self.admin_uploads.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.review_official_files is not None:
            result['ReviewOfficialFiles'] = self.review_official_files.to_map()
        if self.supplements is not None:
            result['Supplements'] = self.supplements.to_map()
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotAcceptUrl') is not None:
            self.not_accept_url = m.get('NotAcceptUrl')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('LogisticsCertificateUrl') is not None:
            self.logistics_certificate_url = m.get('LogisticsCertificateUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReceiptUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReceiptUrl()
            self.receipt_url = temp_model.from_map(m['ReceiptUrl'])
        if m.get('JudgeResultUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl()
            self.judge_result_url = temp_model.from_map(m['JudgeResultUrl'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('AdminUploads') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyAdminUploads()
            self.admin_uploads = temp_model.from_map(m['AdminUploads'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('ReviewOfficialFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles()
            self.review_official_files = temp_model.from_map(m['ReviewOfficialFiles'])
        if m.get('Supplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplements()
            self.supplements = temp_model.from_map(m['Supplements'])
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        return self


class QueryTradeMarkApplicationDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeMarkApplicationDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveClassificationConditionsRequest(TeaModel):
    def __init__(self, type=None, biz_id=None, condition=None):
        self.type = type  # type: int
        self.biz_id = biz_id  # type: str
        self.condition = condition  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveClassificationConditionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class SaveClassificationConditionsResponseBodyInvalidList(TeaModel):
    def __init__(self, parent_code=None, official_code=None, classification_name=None, classification_code=None):
        self.parent_code = parent_code  # type: str
        self.official_code = official_code  # type: str
        self.classification_name = classification_name  # type: str
        self.classification_code = classification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveClassificationConditionsResponseBodyInvalidList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        if self.official_code is not None:
            result['OfficialCode'] = self.official_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        if m.get('OfficialCode') is not None:
            self.official_code = m.get('OfficialCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class SaveClassificationConditionsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, tag_name=None, success=None, invalid_list=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.tag_name = tag_name  # type: str
        self.success = success  # type: bool
        self.invalid_list = invalid_list  # type: list[SaveClassificationConditionsResponseBodyInvalidList]

    def validate(self):
        if self.invalid_list:
            for k in self.invalid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveClassificationConditionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.success is not None:
            result['Success'] = self.success
        result['InvalidList'] = []
        if self.invalid_list is not None:
            for k in self.invalid_list:
                result['InvalidList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.invalid_list = []
        if m.get('InvalidList') is not None:
            for k in m.get('InvalidList'):
                temp_model = SaveClassificationConditionsResponseBodyInvalidList()
                self.invalid_list.append(temp_model.from_map(k))
        return self


class SaveClassificationConditionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveClassificationConditionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveClassificationConditionsResponse, self).to_map()
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
            temp_model = SaveClassificationConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FillLogisticsRequest(TeaModel):
    def __init__(self, biz_id=None, logistics=None):
        self.biz_id = biz_id  # type: str
        self.logistics = logistics  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FillLogisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.logistics is not None:
            result['Logistics'] = self.logistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')
        return self


class FillLogisticsResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FillLogisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class FillLogisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FillLogisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FillLogisticsResponse, self).to_map()
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
            temp_model = FillLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialRequest(TeaModel):
    def __init__(self, loa_id=None, contact_address=None, contact_name=None, contact_number=None,
                 contact_email=None, id=None, contact_zipcode=None, name=None, card_number=None, province=None, city=None,
                 town=None, address=None, ename=None, eaddress=None, id_card_oss_key=None, business_licence_oss_key=None,
                 passport_oss_key=None, loa_oss_key=None, legal_notice_oss_key=None, contact_province=None, contact_city=None,
                 contact_district=None, contact_county=None):
        self.loa_id = loa_id  # type: long
        self.contact_address = contact_address  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.id = id  # type: long
        self.contact_zipcode = contact_zipcode  # type: str
        self.name = name  # type: str
        self.card_number = card_number  # type: str
        self.province = province  # type: str
        self.city = city  # type: str
        self.town = town  # type: str
        self.address = address  # type: str
        self.ename = ename  # type: str
        self.eaddress = eaddress  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_county = contact_county  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.id is not None:
            result['Id'] = self.id
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class UpdateMaterialResponseBody(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMaterialResponse, self).to_map()
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
            temp_model = UpdateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationLogsRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationLogsResponseBodyDataData(TeaModel):
    def __init__(self, operate_time=None, operate_type=None, extend_content=None, biz_id=None, note=None,
                 biz_status=None):
        self.operate_time = operate_time  # type: long
        self.operate_type = operate_type  # type: int
        self.extend_content = extend_content  # type: str
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str
        self.biz_status = biz_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBodyDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        return self


class QueryTradeMarkApplicationLogsResponseBodyData(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[QueryTradeMarkApplicationLogsResponseBodyDataData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTradeMarkApplicationLogsResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryTradeMarkApplicationLogsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBody, self).to_map()
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
            temp_model = QueryTradeMarkApplicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTradeMarkApplicationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundProduceRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class RefundProduceResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefundProduceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefundProduceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundProduceResponse, self).to_map()
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
            temp_model = RefundProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncTrademarkRequest(TeaModel):
    def __init__(self, classification_code=None, tm_name=None, tm_icon=None, original_price=None, tm_number=None,
                 status=None, end_time=None, begin_time=None, description=None, label=None, reg_ann_date=None,
                 owner_name=None, owner_en_name=None, secondary_classification=None, third_classification=None, type=None,
                 reason=None):
        self.classification_code = classification_code  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_icon = tm_icon  # type: str
        self.original_price = original_price  # type: float
        self.tm_number = tm_number  # type: str
        self.status = status  # type: str
        self.end_time = end_time  # type: long
        self.begin_time = begin_time  # type: long
        self.description = description  # type: str
        self.label = label  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.owner_name = owner_name  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.type = type  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncTrademarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.status is not None:
            result['Status'] = self.status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class SyncTrademarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncTrademarkResponseBody, self).to_map()
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


class SyncTrademarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncTrademarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncTrademarkResponse, self).to_map()
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
            temp_model = SyncTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineLoaRequest(TeaModel):
    def __init__(self, material_id=None, trademark_name=None, material_name=None, nationality=None, address=None,
                 tm_produce_type=None, principal_name=None):
        self.material_id = material_id  # type: str
        self.trademark_name = trademark_name  # type: str
        self.material_name = material_name  # type: str
        self.nationality = nationality  # type: str
        self.address = address  # type: str
        self.tm_produce_type = tm_produce_type  # type: str
        self.principal_name = principal_name  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineLoaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.address is not None:
            result['Address'] = self.address
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class CombineLoaResponseBody(TeaModel):
    def __init__(self, template_combine_url=None, request_id=None):
        self.template_combine_url = template_combine_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineLoaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_combine_url is not None:
            result['TemplateCombineUrl'] = self.template_combine_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateCombineUrl') is not None:
            self.template_combine_url = m.get('TemplateCombineUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CombineLoaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CombineLoaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CombineLoaResponse, self).to_map()
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
            temp_model = CombineLoaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUnavailableCodesRequest(TeaModel):
    def __init__(self, codes=None):
        self.codes = codes  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesShrinkRequest(TeaModel):
    def __init__(self, codes_shrink=None):
        self.codes_shrink = codes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBodyData(TeaModel):
    def __init__(self, codes=None):
        self.codes = codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: FilterUnavailableCodesResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FilterUnavailableCodesResponseBody, self).to_map()
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
            temp_model = FilterUnavailableCodesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class FilterUnavailableCodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FilterUnavailableCodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FilterUnavailableCodesResponse, self).to_map()
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
            temp_model = FilterUnavailableCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertMaterialRequest(TeaModel):
    def __init__(self, contact_zipcode=None, type=None, region=None, contact_name=None, contact_number=None,
                 contact_email=None, contact_address=None, loa_oss_key=None, name=None, card_number=None, province=None, city=None,
                 town=None, address=None, ename=None, eaddress=None, country=None, id_card_oss_key=None,
                 business_licence_oss_key=None, passport_oss_key=None, legal_notice_oss_key=None, principal_name=None,
                 contact_province=None, contact_city=None, contact_district=None, contact_county=None):
        self.contact_zipcode = contact_zipcode  # type: str
        self.type = type  # type: int
        self.region = region  # type: int
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_address = contact_address  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.card_number = card_number  # type: str
        self.province = province  # type: str
        self.city = city  # type: str
        self.town = town  # type: str
        self.address = address  # type: str
        self.ename = ename  # type: str
        self.eaddress = eaddress  # type: str
        self.country = country  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.principal_name = principal_name  # type: int
        self.contact_province = contact_province  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_county = contact_county  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.country is not None:
            result['Country'] = self.country
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class InsertMaterialResponseBody(TeaModel):
    def __init__(self, success=None, request_id=None):
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InsertMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertMaterialResponse, self).to_map()
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
            temp_model = InsertMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTradeMarkReviewMaterialDetailRequest(TeaModel):
    def __init__(self, biz_id=None, type=None, region=None, country=None, contact_name=None, contact_number=None,
                 contact_email=None, contact_address=None, loa_oss_key=None, name=None, card_number=None, province=None,
                 address=None, eng_name=None, eng_address=None, id_card_oss_key=None, business_licence_oss_key=None,
                 passport_oss_key=None, legal_notice_oss_key=None, application_oss_key=None, additional_oss_key_list=None,
                 submit_type=None):
        self.biz_id = biz_id  # type: str
        self.type = type  # type: int
        self.region = region  # type: int
        self.country = country  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_address = contact_address  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.card_number = card_number  # type: str
        self.province = province  # type: str
        self.address = address  # type: str
        self.eng_name = eng_name  # type: str
        self.eng_address = eng_address  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.application_oss_key = application_oss_key  # type: str
        self.additional_oss_key_list = additional_oss_key_list  # type: dict[str, any]
        self.submit_type = submit_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.additional_oss_key_list is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list = m.get('AdditionalOssKeyList')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        return self


class SaveTradeMarkReviewMaterialDetailShrinkRequest(TeaModel):
    def __init__(self, biz_id=None, type=None, region=None, country=None, contact_name=None, contact_number=None,
                 contact_email=None, contact_address=None, loa_oss_key=None, name=None, card_number=None, province=None,
                 address=None, eng_name=None, eng_address=None, id_card_oss_key=None, business_licence_oss_key=None,
                 passport_oss_key=None, legal_notice_oss_key=None, application_oss_key=None, additional_oss_key_list_shrink=None,
                 submit_type=None):
        self.biz_id = biz_id  # type: str
        self.type = type  # type: int
        self.region = region  # type: int
        self.country = country  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_address = contact_address  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.card_number = card_number  # type: str
        self.province = province  # type: str
        self.address = address  # type: str
        self.eng_name = eng_name  # type: str
        self.eng_address = eng_address  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.application_oss_key = application_oss_key  # type: str
        self.additional_oss_key_list_shrink = additional_oss_key_list_shrink  # type: str
        self.submit_type = submit_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.additional_oss_key_list_shrink is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list_shrink
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list_shrink = m.get('AdditionalOssKeyList')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        return self


class SaveTradeMarkReviewMaterialDetailResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveTradeMarkReviewMaterialDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveTradeMarkReviewMaterialDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailResponse, self).to_map()
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
            temp_model = SaveTradeMarkReviewMaterialDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorKeywordsRequest(TeaModel):
    def __init__(self, rule_type=None, keywords=None):
        self.rule_type = rule_type  # type: int
        self.keywords = keywords  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorKeywordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBodyData(TeaModel):
    def __init__(self, keywords=None):
        self.keywords = keywords  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryMonitorKeywordsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponseBody, self).to_map()
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
            temp_model = QueryMonitorKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMonitorKeywordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMonitorKeywordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponse, self).to_map()
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
            temp_model = QueryMonitorKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(self, biz_type=None, page_size=None, page_num=None):
        self.biz_type = biz_type  # type: str
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class QueryTaskListResponseBodyDataTaskList(TeaModel):
    def __init__(self, task_type=None, result=None, task_status=None, complete_time=None, create_time=None,
                 err_msg=None, file_name=None):
        self.task_type = task_type  # type: str
        self.result = result  # type: str
        self.task_status = task_status  # type: str
        self.complete_time = complete_time  # type: long
        self.create_time = create_time  # type: long
        self.err_msg = err_msg  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.result is not None:
            result['Result'] = self.result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryTaskListResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryTaskListResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, total_page_num=None, request_id=None, page_size=None,
                 total_item_num=None, data=None):
        self.current_page_num = current_page_num  # type: int
        self.total_page_num = total_page_num  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_item_num = total_item_num  # type: int
        self.data = data  # type: QueryTaskListResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTaskListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskListResponse, self).to_map()
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
            temp_model = QueryTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkNameRequest(TeaModel):
    def __init__(self, client_token=None, biz_id=None, tm_name=None, tm_icon=None, tm_comment=None, type=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 业务id
        self.biz_id = biz_id  # type: str
        # 商标名称
        self.tm_name = tm_name  # type: str
        # 商标图片
        self.tm_icon = tm_icon  # type: str
        self.tm_comment = tm_comment  # type: str
        # 商标类型
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkNameResponseBody(TeaModel):
    def __init__(self, request_id=None, error_code=None, error_msg=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTrademarkNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTrademarkNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrademarkNameResponse, self).to_map()
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
            temp_model = UpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLoaFillRequest(TeaModel):
    def __init__(self, oss_key=None, type=None):
        self.oss_key = oss_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLoaFillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckLoaFillResponseBodyDataErrorMsgs(TeaModel):
    def __init__(self, error_msg=None):
        self.error_msg = error_msg  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLoaFillResponseBodyDataErrorMsgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CheckLoaFillResponseBodyData(TeaModel):
    def __init__(self, address_fill=None, template_url=None, country_fill=None, nationality_fill=None,
                 stamp_fill=None, trade_mark_name_fill=None, material_name_fill=None, error_msgs=None):
        self.address_fill = address_fill  # type: bool
        self.template_url = template_url  # type: str
        self.country_fill = country_fill  # type: bool
        self.nationality_fill = nationality_fill  # type: bool
        self.stamp_fill = stamp_fill  # type: bool
        self.trade_mark_name_fill = trade_mark_name_fill  # type: bool
        self.material_name_fill = material_name_fill  # type: bool
        self.error_msgs = error_msgs  # type: CheckLoaFillResponseBodyDataErrorMsgs

    def validate(self):
        if self.error_msgs:
            self.error_msgs.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_fill is not None:
            result['AddressFill'] = self.address_fill
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        if self.country_fill is not None:
            result['CountryFill'] = self.country_fill
        if self.nationality_fill is not None:
            result['NationalityFill'] = self.nationality_fill
        if self.stamp_fill is not None:
            result['StampFill'] = self.stamp_fill
        if self.trade_mark_name_fill is not None:
            result['TradeMarkNameFill'] = self.trade_mark_name_fill
        if self.material_name_fill is not None:
            result['MaterialNameFill'] = self.material_name_fill
        if self.error_msgs is not None:
            result['ErrorMsgs'] = self.error_msgs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressFill') is not None:
            self.address_fill = m.get('AddressFill')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        if m.get('CountryFill') is not None:
            self.country_fill = m.get('CountryFill')
        if m.get('NationalityFill') is not None:
            self.nationality_fill = m.get('NationalityFill')
        if m.get('StampFill') is not None:
            self.stamp_fill = m.get('StampFill')
        if m.get('TradeMarkNameFill') is not None:
            self.trade_mark_name_fill = m.get('TradeMarkNameFill')
        if m.get('MaterialNameFill') is not None:
            self.material_name_fill = m.get('MaterialNameFill')
        if m.get('ErrorMsgs') is not None:
            temp_model = CheckLoaFillResponseBodyDataErrorMsgs()
            self.error_msgs = temp_model.from_map(m['ErrorMsgs'])
        return self


class CheckLoaFillResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: CheckLoaFillResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponseBody, self).to_map()
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
            temp_model = CheckLoaFillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CheckLoaFillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckLoaFillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponse, self).to_map()
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
            temp_model = CheckLoaFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmApplicantRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmApplicantResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmApplicantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ConfirmApplicantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfirmApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmApplicantResponse, self).to_map()
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
            temp_model = ConfirmApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderRequest(TeaModel):
    def __init__(self, intention_biz_id=None, channel=None):
        self.intention_biz_id = intention_biz_id  # type: str
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class CreateIntentionOrderResponseBodyData(TeaModel):
    def __init__(self, order_ids=None):
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, data=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.data = data  # type: CreateIntentionOrderResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = CreateIntentionOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateIntentionOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIntentionOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderResponse, self).to_map()
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
            temp_model = CreateIntentionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOssResourcesRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOssResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryOssResourcesResponseBodyDataTaskList(TeaModel):
    def __init__(self, biz_id=None, update_time=None, oss_url=None, name=None, create_time=None):
        self.biz_id = biz_id  # type: str
        self.update_time = update_time  # type: long
        self.oss_url = oss_url  # type: str
        self.name = name  # type: str
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOssResourcesResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.name is not None:
            result['Name'] = self.name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class QueryOssResourcesResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryOssResourcesResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryOssResourcesResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryOssResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryOssResourcesResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponseBody, self).to_map()
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
            temp_model = QueryOssResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOssResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOssResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponse, self).to_map()
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
            temp_model = QueryOssResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseApplicantRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseApplicantResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseApplicantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefuseApplicantResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefuseApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefuseApplicantResponse, self).to_map()
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
            temp_model = RefuseApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderGeneratingPayRequest(TeaModel):
    def __init__(self, intention_biz_id=None, payment_callback=None, channel=None):
        self.intention_biz_id = intention_biz_id  # type: str
        self.payment_callback = payment_callback  # type: str
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.payment_callback is not None:
            result['PaymentCallback'] = self.payment_callback
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PaymentCallback') is not None:
            self.payment_callback = m.get('PaymentCallback')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class CreateIntentionOrderGeneratingPayResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, pay_url=None, success=None, order_ids=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.pay_url = pay_url  # type: str
        self.success = success  # type: bool
        self.order_ids = order_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url
        if self.success is not None:
            result['Success'] = self.success
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderGeneratingPayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIntentionOrderGeneratingPayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayResponse, self).to_map()
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
            temp_model = CreateIntentionOrderGeneratingPayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryOrdersRequest(TeaModel):
    def __init__(self, start_order_date=None, end_order_date=None, notary_status=None, aliyun_order_id=None,
                 sort_by_type=None, sort_key_type=None, page_num=None, page_size=None, biz_id=None, notary_type=None):
        self.start_order_date = start_order_date  # type: long
        self.end_order_date = end_order_date  # type: long
        self.notary_status = notary_status  # type: int
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.sort_by_type = sort_by_type  # type: str
        self.sort_key_type = sort_key_type  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.biz_id = biz_id  # type: str
        self.notary_type = notary_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_order_date is not None:
            result['StartOrderDate'] = self.start_order_date
        if self.end_order_date is not None:
            result['EndOrderDate'] = self.end_order_date
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.sort_by_type is not None:
            result['SortByType'] = self.sort_by_type
        if self.sort_key_type is not None:
            result['SortKeyType'] = self.sort_key_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartOrderDate') is not None:
            self.start_order_date = m.get('StartOrderDate')
        if m.get('EndOrderDate') is not None:
            self.end_order_date = m.get('EndOrderDate')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('SortByType') is not None:
            self.sort_by_type = m.get('SortByType')
        if m.get('SortKeyType') is not None:
            self.sort_key_type = m.get('SortKeyType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        return self


class ListNotaryOrdersResponseBodyDataNotaryOrder(TeaModel):
    def __init__(self, order_date=None, order_price=None, notary_type=None, tm_classification=None, biz_id=None,
                 gmt_modified=None, notary_status=None, notary_order_id=None, tm_name=None, tm_register_no=None, tm_image=None,
                 aliyun_order_id=None, apply_post_status=None, notary_certificate=None, notary_platform_name=None):
        self.order_date = order_date  # type: long
        self.order_price = order_price  # type: float
        self.notary_type = notary_type  # type: int
        self.tm_classification = tm_classification  # type: str
        self.biz_id = biz_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.notary_status = notary_status  # type: int
        self.notary_order_id = notary_order_id  # type: long
        self.tm_name = tm_name  # type: str
        self.tm_register_no = tm_register_no  # type: str
        self.tm_image = tm_image  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apply_post_status = apply_post_status  # type: str
        self.notary_certificate = notary_certificate  # type: str
        self.notary_platform_name = notary_platform_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBodyDataNotaryOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        return self


class ListNotaryOrdersResponseBodyData(TeaModel):
    def __init__(self, notary_order=None):
        self.notary_order = notary_order  # type: list[ListNotaryOrdersResponseBodyDataNotaryOrder]

    def validate(self):
        if self.notary_order:
            for k in self.notary_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryOrder'] = []
        if self.notary_order is not None:
            for k in self.notary_order:
                result['NotaryOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notary_order = []
        if m.get('NotaryOrder') is not None:
            for k in m.get('NotaryOrder'):
                temp_model = ListNotaryOrdersResponseBodyDataNotaryOrder()
                self.notary_order.append(temp_model.from_map(k))
        return self


class ListNotaryOrdersResponseBody(TeaModel):
    def __init__(self, next_page=None, request_id=None, success=None, error_code=None, total_item_num=None,
                 pre_page=None, current_page_num=None, error_msg=None, total_page_num=None, page_size=None, data=None):
        self.next_page = next_page  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str
        self.total_item_num = total_item_num  # type: int
        self.pre_page = pre_page  # type: bool
        self.current_page_num = current_page_num  # type: int
        self.error_msg = error_msg  # type: str
        self.total_page_num = total_page_num  # type: int
        self.page_size = page_size  # type: int
        self.data = data  # type: ListNotaryOrdersResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = ListNotaryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListNotaryOrdersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNotaryOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponse, self).to_map()
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
            temp_model = ListNotaryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportPrincipalNameResponseBodyPrincipals(TeaModel):
    def __init__(self, principal_description=None, default_principal=None, principal_value=None):
        self.principal_description = principal_description  # type: str
        self.default_principal = default_principal  # type: bool
        self.principal_value = principal_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponseBodyPrincipals, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.default_principal is not None:
            result['DefaultPrincipal'] = self.default_principal
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('DefaultPrincipal') is not None:
            self.default_principal = m.get('DefaultPrincipal')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetSupportPrincipalNameResponseBody(TeaModel):
    def __init__(self, request_id=None, principals=None):
        self.request_id = request_id  # type: str
        self.principals = principals  # type: list[GetSupportPrincipalNameResponseBodyPrincipals]

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = GetSupportPrincipalNameResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        return self


class GetSupportPrincipalNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSupportPrincipalNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponse, self).to_map()
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
            temp_model = GetSupportPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNotaryRequest(TeaModel):
    def __init__(self, notary_order_id=None):
        self.notary_order_id = notary_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNotaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class StartNotaryResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, notary_url=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.notary_url = notary_url  # type: str
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNotaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.notary_url is not None:
            result['NotaryUrl'] = self.notary_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NotaryUrl') is not None:
            self.notary_url = m.get('NotaryUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class StartNotaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartNotaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartNotaryResponse, self).to_map()
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
            temp_model = StartNotaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSendMaterialNumRequest(TeaModel):
    def __init__(self, biz_id=None, num=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.num = num  # type: str
        self.operate_type = operate_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSendMaterialNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.num is not None:
            result['Num'] = self.num
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateSendMaterialNumResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None, error_code=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSendMaterialNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateSendMaterialNumResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSendMaterialNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSendMaterialNumResponse, self).to_map()
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
            temp_model = UpdateSendMaterialNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrademarkApplicationRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrademarkApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DeleteTrademarkApplicationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrademarkApplicationResponseBody, self).to_map()
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


class DeleteTrademarkApplicationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTrademarkApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrademarkApplicationResponse, self).to_map()
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
            temp_model = DeleteTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


