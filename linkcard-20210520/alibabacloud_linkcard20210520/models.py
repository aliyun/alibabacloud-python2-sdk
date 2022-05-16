# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CardStatisticsResponseBodyDataErrorStopStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataErrorStopStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataExhaustStopStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataExhaustStopStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataExpireStopStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataExpireStopStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataFlowOutStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataFlowOutStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataManageStopStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataManageStopStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataRiskWaringStatisticsDTO(TeaModel):
    def __init__(self, stop_count=None, waring_total_count=None, warning_count=None):
        self.stop_count = stop_count  # type: long
        self.waring_total_count = waring_total_count  # type: long
        self.warning_count = warning_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataRiskWaringStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stop_count is not None:
            result['StopCount'] = self.stop_count
        if self.waring_total_count is not None:
            result['WaringTotalCount'] = self.waring_total_count
        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StopCount') is not None:
            self.stop_count = m.get('StopCount')
        if m.get('WaringTotalCount') is not None:
            self.waring_total_count = m.get('WaringTotalCount')
        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')
        return self


class CardStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataUnbindResumeStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataUnbindResumeStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyDataWeekWarnStatisticsDTO(TeaModel):
    def __init__(self, pool_count=None, same_flow_card_count=None, single_card_count=None, total_count=None):
        self.pool_count = pool_count  # type: long
        self.same_flow_card_count = same_flow_card_count  # type: long
        self.single_card_count = single_card_count  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardStatisticsResponseBodyDataWeekWarnStatisticsDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count
        if self.same_flow_card_count is not None:
            result['SameFlowCardCount'] = self.same_flow_card_count
        if self.single_card_count is not None:
            result['SingleCardCount'] = self.single_card_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')
        if m.get('SameFlowCardCount') is not None:
            self.same_flow_card_count = m.get('SameFlowCardCount')
        if m.get('SingleCardCount') is not None:
            self.single_card_count = m.get('SingleCardCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CardStatisticsResponseBodyData(TeaModel):
    def __init__(self, error_stop_statistics_dto=None, exhaust_stop_statistics_dto=None,
                 expire_stop_statistics_dto=None, flow_out_statistics_dto=None, manage_stop_statistics_dto=None,
                 risk_waring_statistics_dto=None, un_certified_stop_statistics_dto=None, unbind_resume_statistics_dto=None,
                 week_warn_statistics_dto=None):
        self.error_stop_statistics_dto = error_stop_statistics_dto  # type: CardStatisticsResponseBodyDataErrorStopStatisticsDTO
        self.exhaust_stop_statistics_dto = exhaust_stop_statistics_dto  # type: CardStatisticsResponseBodyDataExhaustStopStatisticsDTO
        self.expire_stop_statistics_dto = expire_stop_statistics_dto  # type: CardStatisticsResponseBodyDataExpireStopStatisticsDTO
        self.flow_out_statistics_dto = flow_out_statistics_dto  # type: CardStatisticsResponseBodyDataFlowOutStatisticsDTO
        self.manage_stop_statistics_dto = manage_stop_statistics_dto  # type: CardStatisticsResponseBodyDataManageStopStatisticsDTO
        self.risk_waring_statistics_dto = risk_waring_statistics_dto  # type: CardStatisticsResponseBodyDataRiskWaringStatisticsDTO
        self.un_certified_stop_statistics_dto = un_certified_stop_statistics_dto  # type: CardStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO
        self.unbind_resume_statistics_dto = unbind_resume_statistics_dto  # type: CardStatisticsResponseBodyDataUnbindResumeStatisticsDTO
        self.week_warn_statistics_dto = week_warn_statistics_dto  # type: CardStatisticsResponseBodyDataWeekWarnStatisticsDTO

    def validate(self):
        if self.error_stop_statistics_dto:
            self.error_stop_statistics_dto.validate()
        if self.exhaust_stop_statistics_dto:
            self.exhaust_stop_statistics_dto.validate()
        if self.expire_stop_statistics_dto:
            self.expire_stop_statistics_dto.validate()
        if self.flow_out_statistics_dto:
            self.flow_out_statistics_dto.validate()
        if self.manage_stop_statistics_dto:
            self.manage_stop_statistics_dto.validate()
        if self.risk_waring_statistics_dto:
            self.risk_waring_statistics_dto.validate()
        if self.un_certified_stop_statistics_dto:
            self.un_certified_stop_statistics_dto.validate()
        if self.unbind_resume_statistics_dto:
            self.unbind_resume_statistics_dto.validate()
        if self.week_warn_statistics_dto:
            self.week_warn_statistics_dto.validate()

    def to_map(self):
        _map = super(CardStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_stop_statistics_dto is not None:
            result['ErrorStopStatisticsDTO'] = self.error_stop_statistics_dto.to_map()
        if self.exhaust_stop_statistics_dto is not None:
            result['ExhaustStopStatisticsDTO'] = self.exhaust_stop_statistics_dto.to_map()
        if self.expire_stop_statistics_dto is not None:
            result['ExpireStopStatisticsDTO'] = self.expire_stop_statistics_dto.to_map()
        if self.flow_out_statistics_dto is not None:
            result['FlowOutStatisticsDTO'] = self.flow_out_statistics_dto.to_map()
        if self.manage_stop_statistics_dto is not None:
            result['ManageStopStatisticsDTO'] = self.manage_stop_statistics_dto.to_map()
        if self.risk_waring_statistics_dto is not None:
            result['RiskWaringStatisticsDTO'] = self.risk_waring_statistics_dto.to_map()
        if self.un_certified_stop_statistics_dto is not None:
            result['UnCertifiedStopStatisticsDTO'] = self.un_certified_stop_statistics_dto.to_map()
        if self.unbind_resume_statistics_dto is not None:
            result['UnbindResumeStatisticsDTO'] = self.unbind_resume_statistics_dto.to_map()
        if self.week_warn_statistics_dto is not None:
            result['WeekWarnStatisticsDTO'] = self.week_warn_statistics_dto.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorStopStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataErrorStopStatisticsDTO()
            self.error_stop_statistics_dto = temp_model.from_map(m['ErrorStopStatisticsDTO'])
        if m.get('ExhaustStopStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataExhaustStopStatisticsDTO()
            self.exhaust_stop_statistics_dto = temp_model.from_map(m['ExhaustStopStatisticsDTO'])
        if m.get('ExpireStopStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataExpireStopStatisticsDTO()
            self.expire_stop_statistics_dto = temp_model.from_map(m['ExpireStopStatisticsDTO'])
        if m.get('FlowOutStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataFlowOutStatisticsDTO()
            self.flow_out_statistics_dto = temp_model.from_map(m['FlowOutStatisticsDTO'])
        if m.get('ManageStopStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataManageStopStatisticsDTO()
            self.manage_stop_statistics_dto = temp_model.from_map(m['ManageStopStatisticsDTO'])
        if m.get('RiskWaringStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataRiskWaringStatisticsDTO()
            self.risk_waring_statistics_dto = temp_model.from_map(m['RiskWaringStatisticsDTO'])
        if m.get('UnCertifiedStopStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataUnCertifiedStopStatisticsDTO()
            self.un_certified_stop_statistics_dto = temp_model.from_map(m['UnCertifiedStopStatisticsDTO'])
        if m.get('UnbindResumeStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataUnbindResumeStatisticsDTO()
            self.unbind_resume_statistics_dto = temp_model.from_map(m['UnbindResumeStatisticsDTO'])
        if m.get('WeekWarnStatisticsDTO') is not None:
            temp_model = CardStatisticsResponseBodyDataWeekWarnStatisticsDTO()
            self.week_warn_statistics_dto = temp_model.from_map(m['WeekWarnStatisticsDTO'])
        return self


class CardStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: CardStatisticsResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CardStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = CardStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CardStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CardStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CardStatisticsResponse, self).to_map()
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
            temp_model = CardStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceActivationRequest(TeaModel):
    def __init__(self, date_type=None, iccid=None):
        self.date_type = date_type  # type: str
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceActivationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_type is not None:
            result['DateType'] = self.date_type
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DateType') is not None:
            self.date_type = m.get('DateType')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class ForceActivationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceActivationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ForceActivationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ForceActivationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForceActivationResponse, self).to_map()
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
            temp_model = ForceActivationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardDetailRequest(TeaModel):
    def __init__(self, destroy_card=None, iccid=None, instance_id=None, show_psim=None):
        self.destroy_card = destroy_card  # type: bool
        self.iccid = iccid  # type: str
        self.instance_id = instance_id  # type: str
        self.show_psim = show_psim  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destroy_card is not None:
            result['DestroyCard'] = self.destroy_card
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.show_psim is not None:
            result['ShowPsim'] = self.show_psim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestroyCard') is not None:
            self.destroy_card = m.get('DestroyCard')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ShowPsim') is not None:
            self.show_psim = m.get('ShowPsim')
        return self


class GetCardDetailResponseBodyDataListPsimCards(TeaModel):
    def __init__(self, apn_name=None, certify_status=None, iccid=None, imsi=None, ip=None, msisdn=None, open_sms=None,
                 os_status=None, period_add_flow=None, period_sms_use=None, private_network_segment=None, status=None,
                 vendor=None):
        self.apn_name = apn_name  # type: str
        self.certify_status = certify_status  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: list[str]
        self.ip = ip  # type: list[str]
        self.msisdn = msisdn  # type: list[str]
        self.open_sms = open_sms  # type: bool
        self.os_status = os_status  # type: str
        self.period_add_flow = period_add_flow  # type: str
        self.period_sms_use = period_sms_use  # type: str
        self.private_network_segment = private_network_segment  # type: str
        self.status = status  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataListPsimCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.open_sms is not None:
            result['OpenSms'] = self.open_sms
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.status is not None:
            result['Status'] = self.status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('OpenSms') is not None:
            self.open_sms = m.get('OpenSms')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardDetailResponseBodyDataVsimCardInfoTagList(TeaModel):
    def __init__(self, id=None, tag_name=None):
        self.id = id  # type: long
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataVsimCardInfoTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetCardDetailResponseBodyDataVsimCardInfo(TeaModel):
    def __init__(self, active_time=None, active_type=None, ali_fee=None, aliyun_order_id=None, apn_name=None,
                 auto_limit_resume=None, auto_rebind_reuse=None, card_limit_speed_threshold=None, card_limit_stop_threshold=None,
                 certify_status=None, certify_type=None, credential_instance_id=None, credential_limit_speed_threshold=None,
                 credential_limit_stop_threshold=None, credential_no=None, credential_type=None, data_level=None, data_type=None, device_imei=None,
                 directional_group_id=None, directional_group_name=None, expire_time=None, flow_threshold_unit=None, iccid=None,
                 imsi=None, ip=None, is_auto_recharge=None, msisdn=None, notify_id=None, open_account_time=None,
                 open_sms=None, os_status=None, period=None, period_add_flow=None, period_rest_flow=None,
                 period_sms_use=None, private_network_segment=None, sim_type=None, status=None, tag_list=None, vendor=None,
                 vsim_instance_id=None):
        self.active_time = active_time  # type: str
        self.active_type = active_type  # type: str
        self.ali_fee = ali_fee  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apn_name = apn_name  # type: str
        self.auto_limit_resume = auto_limit_resume  # type: bool
        self.auto_rebind_reuse = auto_rebind_reuse  # type: bool
        self.card_limit_speed_threshold = card_limit_speed_threshold  # type: int
        self.card_limit_stop_threshold = card_limit_stop_threshold  # type: int
        self.certify_status = certify_status  # type: str
        self.certify_type = certify_type  # type: str
        self.credential_instance_id = credential_instance_id  # type: str
        self.credential_limit_speed_threshold = credential_limit_speed_threshold  # type: int
        self.credential_limit_stop_threshold = credential_limit_stop_threshold  # type: int
        self.credential_no = credential_no  # type: str
        self.credential_type = credential_type  # type: str
        self.data_level = data_level  # type: str
        self.data_type = data_type  # type: str
        self.device_imei = device_imei  # type: str
        self.directional_group_id = directional_group_id  # type: str
        self.directional_group_name = directional_group_name  # type: str
        self.expire_time = expire_time  # type: str
        self.flow_threshold_unit = flow_threshold_unit  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: list[str]
        self.ip = ip  # type: list[str]
        self.is_auto_recharge = is_auto_recharge  # type: bool
        self.msisdn = msisdn  # type: list[str]
        self.notify_id = notify_id  # type: str
        self.open_account_time = open_account_time  # type: str
        self.open_sms = open_sms  # type: bool
        self.os_status = os_status  # type: str
        self.period = period  # type: str
        self.period_add_flow = period_add_flow  # type: str
        self.period_rest_flow = period_rest_flow  # type: str
        self.period_sms_use = period_sms_use  # type: str
        self.private_network_segment = private_network_segment  # type: str
        self.sim_type = sim_type  # type: str
        self.status = status  # type: str
        self.tag_list = tag_list  # type: list[GetCardDetailResponseBodyDataVsimCardInfoTagList]
        self.vendor = vendor  # type: str
        self.vsim_instance_id = vsim_instance_id  # type: int

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataVsimCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.active_type is not None:
            result['ActiveType'] = self.active_type
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.auto_limit_resume is not None:
            result['AutoLimitResume'] = self.auto_limit_resume
        if self.auto_rebind_reuse is not None:
            result['AutoRebindReuse'] = self.auto_rebind_reuse
        if self.card_limit_speed_threshold is not None:
            result['CardLimitSpeedThreshold'] = self.card_limit_speed_threshold
        if self.card_limit_stop_threshold is not None:
            result['CardLimitStopThreshold'] = self.card_limit_stop_threshold
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_limit_speed_threshold is not None:
            result['CredentialLimitSpeedThreshold'] = self.credential_limit_speed_threshold
        if self.credential_limit_stop_threshold is not None:
            result['CredentialLimitStopThreshold'] = self.credential_limit_stop_threshold
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.device_imei is not None:
            result['DeviceImei'] = self.device_imei
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.directional_group_name is not None:
            result['DirectionalGroupName'] = self.directional_group_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.flow_threshold_unit is not None:
            result['FlowThresholdUnit'] = self.flow_threshold_unit
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.open_account_time is not None:
            result['OpenAccountTime'] = self.open_account_time
        if self.open_sms is not None:
            result['OpenSms'] = self.open_sms
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period is not None:
            result['Period'] = self.period
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_rest_flow is not None:
            result['PeriodRestFlow'] = self.period_rest_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vsim_instance_id is not None:
            result['VsimInstanceId'] = self.vsim_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('ActiveType') is not None:
            self.active_type = m.get('ActiveType')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('AutoLimitResume') is not None:
            self.auto_limit_resume = m.get('AutoLimitResume')
        if m.get('AutoRebindReuse') is not None:
            self.auto_rebind_reuse = m.get('AutoRebindReuse')
        if m.get('CardLimitSpeedThreshold') is not None:
            self.card_limit_speed_threshold = m.get('CardLimitSpeedThreshold')
        if m.get('CardLimitStopThreshold') is not None:
            self.card_limit_stop_threshold = m.get('CardLimitStopThreshold')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialLimitSpeedThreshold') is not None:
            self.credential_limit_speed_threshold = m.get('CredentialLimitSpeedThreshold')
        if m.get('CredentialLimitStopThreshold') is not None:
            self.credential_limit_stop_threshold = m.get('CredentialLimitStopThreshold')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DeviceImei') is not None:
            self.device_imei = m.get('DeviceImei')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('DirectionalGroupName') is not None:
            self.directional_group_name = m.get('DirectionalGroupName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FlowThresholdUnit') is not None:
            self.flow_threshold_unit = m.get('FlowThresholdUnit')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OpenAccountTime') is not None:
            self.open_account_time = m.get('OpenAccountTime')
        if m.get('OpenSms') is not None:
            self.open_sms = m.get('OpenSms')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodRestFlow') is not None:
            self.period_rest_flow = m.get('PeriodRestFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = GetCardDetailResponseBodyDataVsimCardInfoTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VsimInstanceId') is not None:
            self.vsim_instance_id = m.get('VsimInstanceId')
        return self


class GetCardDetailResponseBodyData(TeaModel):
    def __init__(self, list_psim_cards=None, vsim_card_info=None):
        self.list_psim_cards = list_psim_cards  # type: list[GetCardDetailResponseBodyDataListPsimCards]
        self.vsim_card_info = vsim_card_info  # type: GetCardDetailResponseBodyDataVsimCardInfo

    def validate(self):
        if self.list_psim_cards:
            for k in self.list_psim_cards:
                if k:
                    k.validate()
        if self.vsim_card_info:
            self.vsim_card_info.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListPsimCards'] = []
        if self.list_psim_cards is not None:
            for k in self.list_psim_cards:
                result['ListPsimCards'].append(k.to_map() if k else None)
        if self.vsim_card_info is not None:
            result['VsimCardInfo'] = self.vsim_card_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_psim_cards = []
        if m.get('ListPsimCards') is not None:
            for k in m.get('ListPsimCards'):
                temp_model = GetCardDetailResponseBodyDataListPsimCards()
                self.list_psim_cards.append(temp_model.from_map(k))
        if m.get('VsimCardInfo') is not None:
            temp_model = GetCardDetailResponseBodyDataVsimCardInfo()
            self.vsim_card_info = temp_model.from_map(m['VsimCardInfo'])
        return self


class GetCardDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCardDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = GetCardDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCardDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardDetailResponse, self).to_map()
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
            temp_model = GetCardDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardFlowInfoRequest(TeaModel):
    def __init__(self, date_list=None, iccid=None):
        self.date_list = date_list  # type: list[str]
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_list is not None:
            result['DateList'] = self.date_list
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DateList') is not None:
            self.date_list = m.get('DateList')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow(TeaModel):
    def __init__(self, day=None, flow=None):
        self.day = day  # type: str
        self.flow = flow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlow(TeaModel):
    def __init__(self, flow_count=None, list_day_flow=None, month=None):
        self.flow_count = flow_count  # type: str
        self.list_day_flow = list_day_flow  # type: list[GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow]
        self.month = month  # type: str

    def validate(self):
        if self.list_day_flow:
            for k in self.list_day_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListCardMonthFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_count is not None:
            result['FlowCount'] = self.flow_count
        result['ListDayFlow'] = []
        if self.list_day_flow is not None:
            for k in self.list_day_flow:
                result['ListDayFlow'].append(k.to_map() if k else None)
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCount') is not None:
            self.flow_count = m.get('FlowCount')
        self.list_day_flow = []
        if m.get('ListDayFlow') is not None:
            for k in m.get('ListDayFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow()
                self.list_day_flow.append(temp_model.from_map(k))
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetCardFlowInfoResponseBodyDataListPackageDTO(TeaModel):
    def __init__(self, effective_time=None, expire_time=None, package_name=None, remark=None):
        self.effective_time = effective_time  # type: str
        self.expire_time = expire_time  # type: str
        self.package_name = package_name  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListPackageDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class GetCardFlowInfoResponseBodyDataListVendorDetail(TeaModel):
    def __init__(self, net_work_delay=None, ratio=None, signal_strength=None, used_flow=None, vendor=None):
        self.net_work_delay = net_work_delay  # type: str
        self.ratio = ratio  # type: str
        self.signal_strength = signal_strength  # type: str
        self.used_flow = used_flow  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListVendorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_work_delay is not None:
            result['NetWorkDelay'] = self.net_work_delay
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.signal_strength is not None:
            result['SignalStrength'] = self.signal_strength
        if self.used_flow is not None:
            result['UsedFlow'] = self.used_flow
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetWorkDelay') is not None:
            self.net_work_delay = m.get('NetWorkDelay')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('SignalStrength') is not None:
            self.signal_strength = m.get('SignalStrength')
        if m.get('UsedFlow') is not None:
            self.used_flow = m.get('UsedFlow')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardFlowInfoResponseBodyData(TeaModel):
    def __init__(self, list_card_month_flow=None, list_package_dto=None, list_vendor_detail=None):
        self.list_card_month_flow = list_card_month_flow  # type: list[GetCardFlowInfoResponseBodyDataListCardMonthFlow]
        self.list_package_dto = list_package_dto  # type: list[GetCardFlowInfoResponseBodyDataListPackageDTO]
        self.list_vendor_detail = list_vendor_detail  # type: list[GetCardFlowInfoResponseBodyDataListVendorDetail]

    def validate(self):
        if self.list_card_month_flow:
            for k in self.list_card_month_flow:
                if k:
                    k.validate()
        if self.list_package_dto:
            for k in self.list_package_dto:
                if k:
                    k.validate()
        if self.list_vendor_detail:
            for k in self.list_vendor_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListCardMonthFlow'] = []
        if self.list_card_month_flow is not None:
            for k in self.list_card_month_flow:
                result['ListCardMonthFlow'].append(k.to_map() if k else None)
        result['ListPackageDTO'] = []
        if self.list_package_dto is not None:
            for k in self.list_package_dto:
                result['ListPackageDTO'].append(k.to_map() if k else None)
        result['ListVendorDetail'] = []
        if self.list_vendor_detail is not None:
            for k in self.list_vendor_detail:
                result['ListVendorDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_card_month_flow = []
        if m.get('ListCardMonthFlow') is not None:
            for k in m.get('ListCardMonthFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlow()
                self.list_card_month_flow.append(temp_model.from_map(k))
        self.list_package_dto = []
        if m.get('ListPackageDTO') is not None:
            for k in m.get('ListPackageDTO'):
                temp_model = GetCardFlowInfoResponseBodyDataListPackageDTO()
                self.list_package_dto.append(temp_model.from_map(k))
        self.list_vendor_detail = []
        if m.get('ListVendorDetail') is not None:
            for k in m.get('ListVendorDetail'):
                temp_model = GetCardFlowInfoResponseBodyDataListVendorDetail()
                self.list_vendor_detail.append(temp_model.from_map(k))
        return self


class GetCardFlowInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCardFlowInfoResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = GetCardFlowInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardFlowInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCardFlowInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponse, self).to_map()
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
            temp_model = GetCardFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialPoolStatisticsRequest(TeaModel):
    def __init__(self, credential_no=None, date=None):
        self.credential_no = credential_no  # type: str
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetCredentialPoolStatisticsResponseBodyData(TeaModel):
    def __init__(self, card_active_num=None, card_total_num=None, credential_instance_id=None, credential_no=None,
                 credential_type=None, effective_available_flow=None, effective_total_flow=None, month_feature_fee=None,
                 pool_avaiable=None, pool_grand_total=None, pool_grand_total_used=None, pool_out_used=None, pool_used=None,
                 sms_used=None):
        self.card_active_num = card_active_num  # type: long
        self.card_total_num = card_total_num  # type: long
        self.credential_instance_id = credential_instance_id  # type: str
        self.credential_no = credential_no  # type: str
        self.credential_type = credential_type  # type: str
        self.effective_available_flow = effective_available_flow  # type: str
        self.effective_total_flow = effective_total_flow  # type: str
        self.month_feature_fee = month_feature_fee  # type: long
        self.pool_avaiable = pool_avaiable  # type: str
        self.pool_grand_total = pool_grand_total  # type: str
        self.pool_grand_total_used = pool_grand_total_used  # type: str
        self.pool_out_used = pool_out_used  # type: str
        self.pool_used = pool_used  # type: str
        self.sms_used = sms_used  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_active_num is not None:
            result['CardActiveNum'] = self.card_active_num
        if self.card_total_num is not None:
            result['CardTotalNum'] = self.card_total_num
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.effective_available_flow is not None:
            result['EffectiveAvailableFlow'] = self.effective_available_flow
        if self.effective_total_flow is not None:
            result['EffectiveTotalFlow'] = self.effective_total_flow
        if self.month_feature_fee is not None:
            result['MonthFeatureFee'] = self.month_feature_fee
        if self.pool_avaiable is not None:
            result['PoolAvaiable'] = self.pool_avaiable
        if self.pool_grand_total is not None:
            result['PoolGrandTotal'] = self.pool_grand_total
        if self.pool_grand_total_used is not None:
            result['PoolGrandTotalUsed'] = self.pool_grand_total_used
        if self.pool_out_used is not None:
            result['PoolOutUsed'] = self.pool_out_used
        if self.pool_used is not None:
            result['PoolUsed'] = self.pool_used
        if self.sms_used is not None:
            result['SmsUsed'] = self.sms_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardActiveNum') is not None:
            self.card_active_num = m.get('CardActiveNum')
        if m.get('CardTotalNum') is not None:
            self.card_total_num = m.get('CardTotalNum')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('EffectiveAvailableFlow') is not None:
            self.effective_available_flow = m.get('EffectiveAvailableFlow')
        if m.get('EffectiveTotalFlow') is not None:
            self.effective_total_flow = m.get('EffectiveTotalFlow')
        if m.get('MonthFeatureFee') is not None:
            self.month_feature_fee = m.get('MonthFeatureFee')
        if m.get('PoolAvaiable') is not None:
            self.pool_avaiable = m.get('PoolAvaiable')
        if m.get('PoolGrandTotal') is not None:
            self.pool_grand_total = m.get('PoolGrandTotal')
        if m.get('PoolGrandTotalUsed') is not None:
            self.pool_grand_total_used = m.get('PoolGrandTotalUsed')
        if m.get('PoolOutUsed') is not None:
            self.pool_out_used = m.get('PoolOutUsed')
        if m.get('PoolUsed') is not None:
            self.pool_used = m.get('PoolUsed')
        if m.get('SmsUsed') is not None:
            self.sms_used = m.get('SmsUsed')
        return self


class GetCredentialPoolStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCredentialPoolStatisticsResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponseBody, self).to_map()
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
            temp_model = GetCredentialPoolStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCredentialPoolStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCredentialPoolStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponse, self).to_map()
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
            temp_model = GetCredentialPoolStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCardInfoRequest(TeaModel):
    def __init__(self, active_time_end=None, active_time_start=None, ali_fee=None, aliyun_order_id=None,
                 apn_name=None, certify_type=None, credential_no=None, data_level=None, data_type=None,
                 directional_group_id=None, expire_time_end=None, expire_time_start=None, iccid=None, imsi=None, is_auto_recharge=None,
                 msisdn=None, notify_id=None, os_status=None, page_no=None, page_size=None, period=None, pool_id=None,
                 sim_type=None, status=None, tag_name=None, vendor=None):
        self.active_time_end = active_time_end  # type: str
        self.active_time_start = active_time_start  # type: str
        self.ali_fee = ali_fee  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apn_name = apn_name  # type: str
        self.certify_type = certify_type  # type: str
        self.credential_no = credential_no  # type: str
        self.data_level = data_level  # type: str
        self.data_type = data_type  # type: str
        self.directional_group_id = directional_group_id  # type: str
        self.expire_time_end = expire_time_end  # type: str
        self.expire_time_start = expire_time_start  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: str
        self.is_auto_recharge = is_auto_recharge  # type: bool
        self.msisdn = msisdn  # type: str
        self.notify_id = notify_id  # type: str
        self.os_status = os_status  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.period = period  # type: str
        self.pool_id = pool_id  # type: str
        self.sim_type = sim_type  # type: str
        self.status = status  # type: str
        self.tag_name = tag_name  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCardInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time_end is not None:
            result['ActiveTimeEnd'] = self.active_time_end
        if self.active_time_start is not None:
            result['ActiveTimeStart'] = self.active_time_start
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.expire_time_end is not None:
            result['ExpireTimeEnd'] = self.expire_time_end
        if self.expire_time_start is not None:
            result['ExpireTimeStart'] = self.expire_time_start
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.period is not None:
            result['Period'] = self.period
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTimeEnd') is not None:
            self.active_time_end = m.get('ActiveTimeEnd')
        if m.get('ActiveTimeStart') is not None:
            self.active_time_start = m.get('ActiveTimeStart')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('ExpireTimeEnd') is not None:
            self.expire_time_end = m.get('ExpireTimeEnd')
        if m.get('ExpireTimeStart') is not None:
            self.expire_time_start = m.get('ExpireTimeStart')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ListCardInfoResponseBodyDataListTagList(TeaModel):
    def __init__(self, id=None, tag_name=None):
        self.id = id  # type: long
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCardInfoResponseBodyDataListTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListCardInfoResponseBodyDataList(TeaModel):
    def __init__(self, active_time=None, active_type=None, ali_fee=None, aliyun_order_id=None, apn_name=None,
                 certify_type=None, credential_instance_id=None, credential_no=None, credential_type=None, data_level=None,
                 data_type=None, directional_group_name=None, expire_time=None, iccid=None, imsi=None, is_auto_recharge=None,
                 msisdn=None, notify_id=None, open_account_time=None, os_status=None, period=None, period_add_flow=None,
                 period_rest_flow=None, period_sms_use=None, private_network_segment=None, remark=None, sim_type=None, status=None,
                 tag_list=None, vendor=None, vsim_instance_id=None):
        self.active_time = active_time  # type: str
        self.active_type = active_type  # type: str
        self.ali_fee = ali_fee  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apn_name = apn_name  # type: str
        self.certify_type = certify_type  # type: str
        self.credential_instance_id = credential_instance_id  # type: str
        self.credential_no = credential_no  # type: str
        self.credential_type = credential_type  # type: str
        self.data_level = data_level  # type: str
        self.data_type = data_type  # type: str
        self.directional_group_name = directional_group_name  # type: str
        self.expire_time = expire_time  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: list[str]
        self.is_auto_recharge = is_auto_recharge  # type: bool
        self.msisdn = msisdn  # type: list[str]
        self.notify_id = notify_id  # type: str
        self.open_account_time = open_account_time  # type: str
        self.os_status = os_status  # type: str
        self.period = period  # type: str
        self.period_add_flow = period_add_flow  # type: str
        self.period_rest_flow = period_rest_flow  # type: str
        self.period_sms_use = period_sms_use  # type: str
        self.private_network_segment = private_network_segment  # type: str
        self.remark = remark  # type: str
        self.sim_type = sim_type  # type: str
        self.status = status  # type: str
        self.tag_list = tag_list  # type: list[ListCardInfoResponseBodyDataListTagList]
        self.vendor = vendor  # type: str
        self.vsim_instance_id = vsim_instance_id  # type: long

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCardInfoResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.active_type is not None:
            result['ActiveType'] = self.active_type
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directional_group_name is not None:
            result['DirectionalGroupName'] = self.directional_group_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.open_account_time is not None:
            result['OpenAccountTime'] = self.open_account_time
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period is not None:
            result['Period'] = self.period
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_rest_flow is not None:
            result['PeriodRestFlow'] = self.period_rest_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vsim_instance_id is not None:
            result['VsimInstanceId'] = self.vsim_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('ActiveType') is not None:
            self.active_type = m.get('ActiveType')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DirectionalGroupName') is not None:
            self.directional_group_name = m.get('DirectionalGroupName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OpenAccountTime') is not None:
            self.open_account_time = m.get('OpenAccountTime')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodRestFlow') is not None:
            self.period_rest_flow = m.get('PeriodRestFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ListCardInfoResponseBodyDataListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VsimInstanceId') is not None:
            self.vsim_instance_id = m.get('VsimInstanceId')
        return self


class ListCardInfoResponseBodyData(TeaModel):
    def __init__(self, list=None, page_count=None, page_no=None, page_size=None, total=None):
        self.list = list  # type: list[ListCardInfoResponseBodyDataList]
        self.page_count = page_count  # type: int
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCardInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListCardInfoResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCardInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: ListCardInfoResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCardInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = ListCardInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCardInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCardInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCardInfoResponse, self).to_map()
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
            temp_model = ListCardInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrderRequest(TeaModel):
    def __init__(self, end_date=None, order_id=None, order_status=None, order_type=None, page_no=None,
                 page_size=None, start_date=None):
        self.end_date = end_date  # type: str
        self.order_id = order_id  # type: str
        self.order_status = order_status  # type: str
        self.order_type = order_type  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
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
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ListOrderResponseBodyDataListDeliveryInfo(TeaModel):
    def __init__(self, address=None, buyer_message=None, mail=None, receiver=None, zip_code=None):
        self.address = address  # type: str
        self.buyer_message = buyer_message  # type: str
        self.mail = mail  # type: str
        self.receiver = receiver  # type: str
        self.zip_code = zip_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrderResponseBodyDataListDeliveryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.buyer_message is not None:
            result['BuyerMessage'] = self.buyer_message
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BuyerMessage') is not None:
            self.buyer_message = m.get('BuyerMessage')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class ListOrderResponseBodyDataList(TeaModel):
    def __init__(self, ali_fee=None, billing_cycle=None, buy_num=None, card_pay_count=None, credential_no=None,
                 credential_package=None, data_level=None, delivery_info=None, express_no_list=None, flow_type=None, function_fee=None,
                 order_detail_url=None, order_id=None, order_info=None, order_status=None, order_type=None, pay_duration=None,
                 pay_time=None, pool_capacity=None, pool_capacity_unit=None, pool_no=None, vendor=None):
        self.ali_fee = ali_fee  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.buy_num = buy_num  # type: int
        self.card_pay_count = card_pay_count  # type: int
        self.credential_no = credential_no  # type: str
        self.credential_package = credential_package  # type: str
        self.data_level = data_level  # type: str
        self.delivery_info = delivery_info  # type: ListOrderResponseBodyDataListDeliveryInfo
        self.express_no_list = express_no_list  # type: list[str]
        self.flow_type = flow_type  # type: str
        self.function_fee = function_fee  # type: int
        self.order_detail_url = order_detail_url  # type: str
        self.order_id = order_id  # type: str
        self.order_info = order_info  # type: str
        self.order_status = order_status  # type: str
        self.order_type = order_type  # type: str
        self.pay_duration = pay_duration  # type: str
        self.pay_time = pay_time  # type: str
        self.pool_capacity = pool_capacity  # type: str
        self.pool_capacity_unit = pool_capacity_unit  # type: str
        self.pool_no = pool_no  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        if self.delivery_info:
            self.delivery_info.validate()

    def to_map(self):
        _map = super(ListOrderResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.buy_num is not None:
            result['BuyNum'] = self.buy_num
        if self.card_pay_count is not None:
            result['CardPayCount'] = self.card_pay_count
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_package is not None:
            result['CredentialPackage'] = self.credential_package
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.delivery_info is not None:
            result['DeliveryInfo'] = self.delivery_info.to_map()
        if self.express_no_list is not None:
            result['ExpressNoList'] = self.express_no_list
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.function_fee is not None:
            result['FunctionFee'] = self.function_fee
        if self.order_detail_url is not None:
            result['OrderDetailUrl'] = self.order_detail_url
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pay_duration is not None:
            result['PayDuration'] = self.pay_duration
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.pool_capacity is not None:
            result['PoolCapacity'] = self.pool_capacity
        if self.pool_capacity_unit is not None:
            result['PoolCapacityUnit'] = self.pool_capacity_unit
        if self.pool_no is not None:
            result['PoolNo'] = self.pool_no
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('BuyNum') is not None:
            self.buy_num = m.get('BuyNum')
        if m.get('CardPayCount') is not None:
            self.card_pay_count = m.get('CardPayCount')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialPackage') is not None:
            self.credential_package = m.get('CredentialPackage')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DeliveryInfo') is not None:
            temp_model = ListOrderResponseBodyDataListDeliveryInfo()
            self.delivery_info = temp_model.from_map(m['DeliveryInfo'])
        if m.get('ExpressNoList') is not None:
            self.express_no_list = m.get('ExpressNoList')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('FunctionFee') is not None:
            self.function_fee = m.get('FunctionFee')
        if m.get('OrderDetailUrl') is not None:
            self.order_detail_url = m.get('OrderDetailUrl')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PayDuration') is not None:
            self.pay_duration = m.get('PayDuration')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PoolCapacity') is not None:
            self.pool_capacity = m.get('PoolCapacity')
        if m.get('PoolCapacityUnit') is not None:
            self.pool_capacity_unit = m.get('PoolCapacityUnit')
        if m.get('PoolNo') is not None:
            self.pool_no = m.get('PoolNo')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ListOrderResponseBodyData(TeaModel):
    def __init__(self, list=None, page_count=None, page_no=None, page_size=None, total=None):
        self.list = list  # type: list[ListOrderResponseBodyDataList]
        self.page_count = page_count  # type: int
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
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
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListOrderResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: ListOrderResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = ListOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrderResponse, self).to_map()
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
            temp_model = ListOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebindResumeSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RebindResumeSingleCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebindResumeSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebindResumeSingleCardResponse, self).to_map()
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
            temp_model = RebindResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewRequest(TeaModel):
    def __init__(self, api_product=None, api_revision=None, buy_num=None, iccid=None, offer_code=None,
                 recharge_type=None, serial_no=None):
        self.api_product = api_product  # type: str
        self.api_revision = api_revision  # type: str
        self.buy_num = buy_num  # type: int
        self.iccid = iccid  # type: str
        self.offer_code = offer_code  # type: str
        self.recharge_type = recharge_type  # type: str
        self.serial_no = serial_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_product is not None:
            result['ApiProduct'] = self.api_product
        if self.api_revision is not None:
            result['ApiRevision'] = self.api_revision
        if self.buy_num is not None:
            result['BuyNum'] = self.buy_num
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.offer_code is not None:
            result['OfferCode'] = self.offer_code
        if self.recharge_type is not None:
            result['RechargeType'] = self.recharge_type
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiProduct') is not None:
            self.api_product = m.get('ApiProduct')
        if m.get('ApiRevision') is not None:
            self.api_revision = m.get('ApiRevision')
        if m.get('BuyNum') is not None:
            self.buy_num = m.get('BuyNum')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OfferCode') is not None:
            self.offer_code = m.get('OfferCode')
        if m.get('RechargeType') is not None:
            self.recharge_type = m.get('RechargeType')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RenewResponseBodyData(TeaModel):
    def __init__(self, order_no=None, serial_no=None):
        self.order_no = order_no  # type: str
        self.serial_no = serial_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RenewResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: RenewResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RenewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
            temp_model = RenewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewResponse, self).to_map()
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
            temp_model = RenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class ResumeSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class ResumeSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeSingleCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeSingleCardResponse, self).to_map()
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
            temp_model = ResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCardStopRuleRequest(TeaModel):
    def __init__(self, auto_restore=None, flow_limit=None, iccid=None):
        self.auto_restore = auto_restore  # type: bool
        self.flow_limit = flow_limit  # type: long
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCardStopRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_restore is not None:
            result['AutoRestore'] = self.auto_restore
        if self.flow_limit is not None:
            result['FlowLimit'] = self.flow_limit
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRestore') is not None:
            self.auto_restore = m.get('AutoRestore')
        if m.get('FlowLimit') is not None:
            self.flow_limit = m.get('FlowLimit')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class SetCardStopRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCardStopRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetCardStopRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetCardStopRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCardStopRuleResponse, self).to_map()
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
            temp_model = SetCardStopRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class StopSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class StopSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopSingleCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopSingleCardResponse, self).to_map()
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
            temp_model = StopSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoRechargeSwitchRequest(TeaModel):
    def __init__(self, iccid=None, open=None):
        self.iccid = iccid  # type: str
        self.open = open  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoRechargeSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.open is not None:
            result['Open'] = self.open
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        return self


class UpdateAutoRechargeSwitchResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoRechargeSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
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
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoRechargeSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAutoRechargeSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAutoRechargeSwitchResponse, self).to_map()
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
            temp_model = UpdateAutoRechargeSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


