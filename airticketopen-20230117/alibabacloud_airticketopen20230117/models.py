# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue(TeaModel):
    def __init__(self, baggage_amount=None, baggage_weight=None, baggage_weight_unit=None, is_all_weight=None,
                 carry_on_amount=None, carry_on_weight=None, carry_on_weight_unit=None, is_all_carry_on_weight=None):
        self.baggage_amount = baggage_amount  # type: int
        self.baggage_weight = baggage_weight  # type: int
        self.baggage_weight_unit = baggage_weight_unit  # type: str
        self.is_all_weight = is_all_weight  # type: bool
        self.carry_on_amount = carry_on_amount  # type: int
        self.carry_on_weight = carry_on_weight  # type: int
        self.carry_on_weight_unit = carry_on_weight_unit  # type: str
        self.is_all_carry_on_weight = is_all_carry_on_weight  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount
        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight
        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit
        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight
        if self.carry_on_amount is not None:
            result['carry_on_amount'] = self.carry_on_amount
        if self.carry_on_weight is not None:
            result['carry_on_weight'] = self.carry_on_weight
        if self.carry_on_weight_unit is not None:
            result['carry_on_weight_unit'] = self.carry_on_weight_unit
        if self.is_all_carry_on_weight is not None:
            result['is_all_carry_on_weight'] = self.is_all_carry_on_weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')
        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')
        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')
        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')
        if m.get('carry_on_amount') is not None:
            self.carry_on_amount = m.get('carry_on_amount')
        if m.get('carry_on_weight') is not None:
            self.carry_on_weight = m.get('carry_on_weight')
        if m.get('carry_on_weight_unit') is not None:
            self.carry_on_weight_unit = m.get('carry_on_weight_unit')
        if m.get('is_all_carry_on_weight') is not None:
            self.is_all_carry_on_weight = m.get('is_all_carry_on_weight')
        return self


class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue(TeaModel):
    def __init__(self, refund_rule_all_unused_list=None, refund_rule_part_unused_list=None,
                 change_rule_in_unused_list=None, change_rule_out_unused_list=None):
        self.refund_rule_all_unused_list = refund_rule_all_unused_list  # type: list[DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList]
        self.refund_rule_part_unused_list = refund_rule_part_unused_list  # type: list[DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList]
        self.change_rule_in_unused_list = change_rule_in_unused_list  # type: list[DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList]
        self.change_rule_out_unused_list = change_rule_out_unused_list  # type: list[DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList]

    def validate(self):
        if self.refund_rule_all_unused_list:
            for k in self.refund_rule_all_unused_list:
                if k:
                    k.validate()
        if self.refund_rule_part_unused_list:
            for k in self.refund_rule_part_unused_list:
                if k:
                    k.validate()
        if self.change_rule_in_unused_list:
            for k in self.change_rule_in_unused_list:
                if k:
                    k.validate()
        if self.change_rule_out_unused_list:
            for k in self.change_rule_out_unused_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_rule_all_unused_list'] = []
        if self.refund_rule_all_unused_list is not None:
            for k in self.refund_rule_all_unused_list:
                result['refund_rule_all_unused_list'].append(k.to_map() if k else None)
        result['refund_rule_part_unused_list'] = []
        if self.refund_rule_part_unused_list is not None:
            for k in self.refund_rule_part_unused_list:
                result['refund_rule_part_unused_list'].append(k.to_map() if k else None)
        result['change_rule_in_unused_list'] = []
        if self.change_rule_in_unused_list is not None:
            for k in self.change_rule_in_unused_list:
                result['change_rule_in_unused_list'].append(k.to_map() if k else None)
        result['change_rule_out_unused_list'] = []
        if self.change_rule_out_unused_list is not None:
            for k in self.change_rule_out_unused_list:
                result['change_rule_out_unused_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_rule_all_unused_list = []
        if m.get('refund_rule_all_unused_list') is not None:
            for k in m.get('refund_rule_all_unused_list'):
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList()
                self.refund_rule_all_unused_list.append(temp_model.from_map(k))
        self.refund_rule_part_unused_list = []
        if m.get('refund_rule_part_unused_list') is not None:
            for k in m.get('refund_rule_part_unused_list'):
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList()
                self.refund_rule_part_unused_list.append(temp_model.from_map(k))
        self.change_rule_in_unused_list = []
        if m.get('change_rule_in_unused_list') is not None:
            for k in m.get('change_rule_in_unused_list'):
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList()
                self.change_rule_in_unused_list.append(temp_model.from_map(k))
        self.change_rule_out_unused_list = []
        if m.get('change_rule_out_unused_list') is not None:
            for k in m.get('change_rule_out_unused_list'):
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList()
                self.change_rule_out_unused_list.append(temp_model.from_map(k))
        return self


class DataBaggageAllowanceMapValue(TeaModel):
    def __init__(self, baggage_amount=None, baggage_weight=None, baggage_weight_unit=None, is_all_weight=None,
                 carry_on_amount=None, carry_on_weight=None, carry_on_weight_unit=None, is_all_carry_on_weight=None):
        self.baggage_amount = baggage_amount  # type: int
        self.baggage_weight = baggage_weight  # type: int
        self.baggage_weight_unit = baggage_weight_unit  # type: str
        self.is_all_weight = is_all_weight  # type: bool
        self.carry_on_amount = carry_on_amount  # type: int
        self.carry_on_weight = carry_on_weight  # type: int
        self.carry_on_weight_unit = carry_on_weight_unit  # type: str
        self.is_all_carry_on_weight = is_all_carry_on_weight  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataBaggageAllowanceMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount
        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight
        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit
        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight
        if self.carry_on_amount is not None:
            result['carry_on_amount'] = self.carry_on_amount
        if self.carry_on_weight is not None:
            result['carry_on_weight'] = self.carry_on_weight
        if self.carry_on_weight_unit is not None:
            result['carry_on_weight_unit'] = self.carry_on_weight_unit
        if self.is_all_carry_on_weight is not None:
            result['is_all_carry_on_weight'] = self.is_all_carry_on_weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')
        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')
        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')
        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')
        if m.get('carry_on_amount') is not None:
            self.carry_on_amount = m.get('carry_on_amount')
        if m.get('carry_on_weight') is not None:
            self.carry_on_weight = m.get('carry_on_weight')
        if m.get('carry_on_weight_unit') is not None:
            self.carry_on_weight_unit = m.get('carry_on_weight_unit')
        if m.get('is_all_carry_on_weight') is not None:
            self.is_all_carry_on_weight = m.get('is_all_carry_on_weight')
        return self


class DataRefundChangeRuleMapValueRefundRuleAllUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRefundChangeRuleMapValueRefundRuleAllUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataRefundChangeRuleMapValueRefundRulePartUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRefundChangeRuleMapValueRefundRulePartUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataRefundChangeRuleMapValueChangeRuleInUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRefundChangeRuleMapValueChangeRuleInUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataRefundChangeRuleMapValueChangeRuleOutUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRefundChangeRuleMapValueChangeRuleOutUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataRefundChangeRuleMapValue(TeaModel):
    def __init__(self, refund_rule_all_unused_list=None, refund_rule_part_unused_list=None,
                 change_rule_in_unused_list=None, change_rule_out_unused_list=None):
        self.refund_rule_all_unused_list = refund_rule_all_unused_list  # type: list[DataRefundChangeRuleMapValueRefundRuleAllUnusedList]
        self.refund_rule_part_unused_list = refund_rule_part_unused_list  # type: list[DataRefundChangeRuleMapValueRefundRulePartUnusedList]
        self.change_rule_in_unused_list = change_rule_in_unused_list  # type: list[DataRefundChangeRuleMapValueChangeRuleInUnusedList]
        self.change_rule_out_unused_list = change_rule_out_unused_list  # type: list[DataRefundChangeRuleMapValueChangeRuleOutUnusedList]

    def validate(self):
        if self.refund_rule_all_unused_list:
            for k in self.refund_rule_all_unused_list:
                if k:
                    k.validate()
        if self.refund_rule_part_unused_list:
            for k in self.refund_rule_part_unused_list:
                if k:
                    k.validate()
        if self.change_rule_in_unused_list:
            for k in self.change_rule_in_unused_list:
                if k:
                    k.validate()
        if self.change_rule_out_unused_list:
            for k in self.change_rule_out_unused_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataRefundChangeRuleMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_rule_all_unused_list'] = []
        if self.refund_rule_all_unused_list is not None:
            for k in self.refund_rule_all_unused_list:
                result['refund_rule_all_unused_list'].append(k.to_map() if k else None)
        result['refund_rule_part_unused_list'] = []
        if self.refund_rule_part_unused_list is not None:
            for k in self.refund_rule_part_unused_list:
                result['refund_rule_part_unused_list'].append(k.to_map() if k else None)
        result['change_rule_in_unused_list'] = []
        if self.change_rule_in_unused_list is not None:
            for k in self.change_rule_in_unused_list:
                result['change_rule_in_unused_list'].append(k.to_map() if k else None)
        result['change_rule_out_unused_list'] = []
        if self.change_rule_out_unused_list is not None:
            for k in self.change_rule_out_unused_list:
                result['change_rule_out_unused_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_rule_all_unused_list = []
        if m.get('refund_rule_all_unused_list') is not None:
            for k in m.get('refund_rule_all_unused_list'):
                temp_model = DataRefundChangeRuleMapValueRefundRuleAllUnusedList()
                self.refund_rule_all_unused_list.append(temp_model.from_map(k))
        self.refund_rule_part_unused_list = []
        if m.get('refund_rule_part_unused_list') is not None:
            for k in m.get('refund_rule_part_unused_list'):
                temp_model = DataRefundChangeRuleMapValueRefundRulePartUnusedList()
                self.refund_rule_part_unused_list.append(temp_model.from_map(k))
        self.change_rule_in_unused_list = []
        if m.get('change_rule_in_unused_list') is not None:
            for k in m.get('change_rule_in_unused_list'):
                temp_model = DataRefundChangeRuleMapValueChangeRuleInUnusedList()
                self.change_rule_in_unused_list.append(temp_model.from_map(k))
        self.change_rule_out_unused_list = []
        if m.get('change_rule_out_unused_list') is not None:
            for k in m.get('change_rule_out_unused_list'):
                temp_model = DataRefundChangeRuleMapValueChangeRuleOutUnusedList()
                self.change_rule_out_unused_list.append(temp_model.from_map(k))
        return self


class DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue(TeaModel):
    def __init__(self, baggage_amount=None, baggage_weight=None, baggage_weight_unit=None, is_all_weight=None,
                 carry_on_amount=None, carry_on_weight=None, carry_on_weight_unit=None, is_all_carry_on_weight=None):
        self.baggage_amount = baggage_amount  # type: int
        self.baggage_weight = baggage_weight  # type: int
        self.baggage_weight_unit = baggage_weight_unit  # type: str
        self.is_all_weight = is_all_weight  # type: bool
        self.carry_on_amount = carry_on_amount  # type: int
        self.carry_on_weight = carry_on_weight  # type: int
        self.carry_on_weight_unit = carry_on_weight_unit  # type: str
        self.is_all_carry_on_weight = is_all_carry_on_weight  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount
        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight
        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit
        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight
        if self.carry_on_amount is not None:
            result['carry_on_amount'] = self.carry_on_amount
        if self.carry_on_weight is not None:
            result['carry_on_weight'] = self.carry_on_weight
        if self.carry_on_weight_unit is not None:
            result['carry_on_weight_unit'] = self.carry_on_weight_unit
        if self.is_all_carry_on_weight is not None:
            result['is_all_carry_on_weight'] = self.is_all_carry_on_weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')
        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')
        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')
        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')
        if m.get('carry_on_amount') is not None:
            self.carry_on_amount = m.get('carry_on_amount')
        if m.get('carry_on_weight') is not None:
            self.carry_on_weight = m.get('carry_on_weight')
        if m.get('carry_on_weight_unit') is not None:
            self.carry_on_weight_unit = m.get('carry_on_weight_unit')
        if m.get('is_all_carry_on_weight') is not None:
            self.is_all_carry_on_weight = m.get('is_all_carry_on_weight')
        return self


class DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_refund=None,
                 refund_fee=None, can_return_all_tax=None, return_part_tax_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_refund = can_refund  # type: bool
        self.refund_fee = refund_fee  # type: float
        self.can_return_all_tax = can_return_all_tax  # type: bool
        self.return_part_tax_fee = return_part_tax_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.can_return_all_tax is not None:
            result['can_return_all_tax'] = self.can_return_all_tax
        if self.return_part_tax_fee is not None:
            result['return_part_tax_fee'] = self.return_part_tax_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('can_return_all_tax') is not None:
            self.can_return_all_tax = m.get('can_return_all_tax')
        if m.get('return_part_tax_fee') is not None:
            self.return_part_tax_fee = m.get('return_part_tax_fee')
        return self


class DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList(TeaModel):
    def __init__(self, type=None, time_unit=None, rule_start_time=None, rule_end_time=None, can_change=None,
                 change_fee=None):
        self.type = type  # type: int
        self.time_unit = time_unit  # type: str
        self.rule_start_time = rule_start_time  # type: int
        self.rule_end_time = rule_end_time  # type: int
        self.can_change = can_change  # type: bool
        self.change_fee = change_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.time_unit is not None:
            result['time_unit'] = self.time_unit
        if self.rule_start_time is not None:
            result['rule_start_time'] = self.rule_start_time
        if self.rule_end_time is not None:
            result['rule_end_time'] = self.rule_end_time
        if self.can_change is not None:
            result['can_change'] = self.can_change
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('time_unit') is not None:
            self.time_unit = m.get('time_unit')
        if m.get('rule_start_time') is not None:
            self.rule_start_time = m.get('rule_start_time')
        if m.get('rule_end_time') is not None:
            self.rule_end_time = m.get('rule_end_time')
        if m.get('can_change') is not None:
            self.can_change = m.get('can_change')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        return self


class DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue(TeaModel):
    def __init__(self, refund_rule_all_unused_list=None, refund_rule_part_unused_list=None,
                 change_rule_in_unused_list=None, change_rule_out_unused_list=None):
        self.refund_rule_all_unused_list = refund_rule_all_unused_list  # type: list[DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList]
        self.refund_rule_part_unused_list = refund_rule_part_unused_list  # type: list[DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList]
        self.change_rule_in_unused_list = change_rule_in_unused_list  # type: list[DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList]
        self.change_rule_out_unused_list = change_rule_out_unused_list  # type: list[DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList]

    def validate(self):
        if self.refund_rule_all_unused_list:
            for k in self.refund_rule_all_unused_list:
                if k:
                    k.validate()
        if self.refund_rule_part_unused_list:
            for k in self.refund_rule_part_unused_list:
                if k:
                    k.validate()
        if self.change_rule_in_unused_list:
            for k in self.change_rule_in_unused_list:
                if k:
                    k.validate()
        if self.change_rule_out_unused_list:
            for k in self.change_rule_out_unused_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_rule_all_unused_list'] = []
        if self.refund_rule_all_unused_list is not None:
            for k in self.refund_rule_all_unused_list:
                result['refund_rule_all_unused_list'].append(k.to_map() if k else None)
        result['refund_rule_part_unused_list'] = []
        if self.refund_rule_part_unused_list is not None:
            for k in self.refund_rule_part_unused_list:
                result['refund_rule_part_unused_list'].append(k.to_map() if k else None)
        result['change_rule_in_unused_list'] = []
        if self.change_rule_in_unused_list is not None:
            for k in self.change_rule_in_unused_list:
                result['change_rule_in_unused_list'].append(k.to_map() if k else None)
        result['change_rule_out_unused_list'] = []
        if self.change_rule_out_unused_list is not None:
            for k in self.change_rule_out_unused_list:
                result['change_rule_out_unused_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_rule_all_unused_list = []
        if m.get('refund_rule_all_unused_list') is not None:
            for k in m.get('refund_rule_all_unused_list'):
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRuleAllUnusedList()
                self.refund_rule_all_unused_list.append(temp_model.from_map(k))
        self.refund_rule_part_unused_list = []
        if m.get('refund_rule_part_unused_list') is not None:
            for k in m.get('refund_rule_part_unused_list'):
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueRefundRulePartUnusedList()
                self.refund_rule_part_unused_list.append(temp_model.from_map(k))
        self.change_rule_in_unused_list = []
        if m.get('change_rule_in_unused_list') is not None:
            for k in m.get('change_rule_in_unused_list'):
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleInUnusedList()
                self.change_rule_in_unused_list.append(temp_model.from_map(k))
        self.change_rule_out_unused_list = []
        if m.get('change_rule_out_unused_list') is not None:
            for k in m.get('change_rule_out_unused_list'):
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValueChangeRuleOutUnusedList()
                self.change_rule_out_unused_list.append(temp_model.from_map(k))
        return self


class AccountFlowListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccountFlowListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class AccountFlowListRequest(TeaModel):
    def __init__(self, day_num=None, page_index=None, page_size=None, utc_begin_time=None):
        self.day_num = day_num  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.utc_begin_time = utc_begin_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccountFlowListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_num is not None:
            result['day_num'] = self.day_num
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.utc_begin_time is not None:
            result['utc_begin_time'] = self.utc_begin_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('day_num') is not None:
            self.day_num = m.get('day_num')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('utc_begin_time') is not None:
            self.utc_begin_time = m.get('utc_begin_time')
        return self


class AccountFlowListResponseBodyDataList(TeaModel):
    def __init__(self, after_available_amount=None, before_available_amount=None, change_order_num=None,
                 flow_id=None, gmt_create=None, gmt_modified=None, op_amount=None, op_type=None, order_num=None,
                 order_type=None, out_order_num=None, refund_order_num=None):
        self.after_available_amount = after_available_amount  # type: float
        self.before_available_amount = before_available_amount  # type: float
        self.change_order_num = change_order_num  # type: long
        self.flow_id = flow_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.op_amount = op_amount  # type: float
        self.op_type = op_type  # type: int
        self.order_num = order_num  # type: long
        self.order_type = order_type  # type: int
        self.out_order_num = out_order_num  # type: str
        self.refund_order_num = refund_order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccountFlowListResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_available_amount is not None:
            result['after_available_amount'] = self.after_available_amount
        if self.before_available_amount is not None:
            result['before_available_amount'] = self.before_available_amount
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.op_amount is not None:
            result['op_amount'] = self.op_amount
        if self.op_type is not None:
            result['op_type'] = self.op_type
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_type is not None:
            result['order_type'] = self.order_type
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('after_available_amount') is not None:
            self.after_available_amount = m.get('after_available_amount')
        if m.get('before_available_amount') is not None:
            self.before_available_amount = m.get('before_available_amount')
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('op_amount') is not None:
            self.op_amount = m.get('op_amount')
        if m.get('op_type') is not None:
            self.op_type = m.get('op_type')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')
        return self


class AccountFlowListResponseBodyDataPagination(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None, total_page=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccountFlowListResponseBodyDataPagination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['current_page'] = self.current_page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.total_page is not None:
            result['total_page'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')
        return self


class AccountFlowListResponseBodyData(TeaModel):
    def __init__(self, list=None, pagination=None):
        self.list = list  # type: list[AccountFlowListResponseBodyDataList]
        self.pagination = pagination  # type: AccountFlowListResponseBodyDataPagination

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super(AccountFlowListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = AccountFlowListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pagination') is not None:
            temp_model = AccountFlowListResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['pagination'])
        return self


class AccountFlowListResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: AccountFlowListResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AccountFlowListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = AccountFlowListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AccountFlowListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AccountFlowListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AccountFlowListResponse, self).to_map()
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
            temp_model = AccountFlowListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AncillarySuggestHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AncillarySuggestHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class AncillarySuggestRequest(TeaModel):
    def __init__(self, solution_id=None):
        self.solution_id = solution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AncillarySuggestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary(TeaModel):
    def __init__(self, baggage_amount=None, baggage_weight=None, baggage_weight_unit=None, is_all_weight=None,
                 price=None):
        # 行李件数 取值如：3、2、1、0、-2。 -2 表示计重
        self.baggage_amount = baggage_amount  # type: int
        # 行李重量，0-50。isAllWeght=true 时，表示所有件数总重量。
        self.baggage_weight = baggage_weight  # type: int
        # 行李重量单位
        self.baggage_weight_unit = baggage_weight_unit  # type: str
        # 是否所有行李重量
        self.is_all_weight = is_all_weight  # type: bool
        # 总价
        self.price = price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount
        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight
        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit
        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight
        if self.price is not None:
            result['price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')
        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')
        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')
        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')
        if m.get('price') is not None:
            self.price = m.get('price')
        return self


class AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary(TeaModel):
    def __init__(self, ancillary_id=None, ancillary_type=None, baggage_ancillary=None):
        self.ancillary_id = ancillary_id  # type: str
        self.ancillary_type = ancillary_type  # type: int
        # 行李辅营详情
        self.baggage_ancillary = baggage_ancillary  # type: AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary

    def validate(self):
        if self.baggage_ancillary:
            self.baggage_ancillary.validate()

    def to_map(self):
        _map = super(AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id
        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type
        if self.baggage_ancillary is not None:
            result['baggage_ancillary'] = self.baggage_ancillary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')
        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')
        if m.get('baggage_ancillary') is not None:
            temp_model = AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary()
            self.baggage_ancillary = temp_model.from_map(m['baggage_ancillary'])
        return self


class AncillarySuggestResponseBodyDataSegAncillaryMapList(TeaModel):
    def __init__(self, ancillary=None, segment_id_list=None):
        self.ancillary = ancillary  # type: AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.ancillary:
            self.ancillary.validate()

    def to_map(self):
        _map = super(AncillarySuggestResponseBodyDataSegAncillaryMapList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ancillary is not None:
            result['ancillary'] = self.ancillary.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ancillary') is not None:
            temp_model = AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary()
            self.ancillary = temp_model.from_map(m['ancillary'])
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class AncillarySuggestResponseBodyData(TeaModel):
    def __init__(self, seg_ancillary_map_list=None, solution_id=None):
        self.seg_ancillary_map_list = seg_ancillary_map_list  # type: list[AncillarySuggestResponseBodyDataSegAncillaryMapList]
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.seg_ancillary_map_list:
            for k in self.seg_ancillary_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AncillarySuggestResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['seg_ancillary_map_list'] = []
        if self.seg_ancillary_map_list is not None:
            for k in self.seg_ancillary_map_list:
                result['seg_ancillary_map_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.seg_ancillary_map_list = []
        if m.get('seg_ancillary_map_list') is not None:
            for k in m.get('seg_ancillary_map_list'):
                temp_model = AncillarySuggestResponseBodyDataSegAncillaryMapList()
                self.seg_ancillary_map_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class AncillarySuggestResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: AncillarySuggestResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AncillarySuggestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = AncillarySuggestResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AncillarySuggestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AncillarySuggestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AncillarySuggestResponse, self).to_map()
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
            temp_model = AncillarySuggestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BookHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class BookRequestContact(TeaModel):
    def __init__(self, email=None, first_name=None, last_name=None, mobile_country_code=None, mobile_phone_num=None):
        self.email = email  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_num = mobile_phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookRequestContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')
        return self


class BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem(TeaModel):
    def __init__(self, ancillary_id=None, ancillary_type=None):
        self.ancillary_id = ancillary_id  # type: str
        self.ancillary_type = ancillary_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id
        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')
        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')
        return self


class BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class BookRequestPassengerAncillaryPurchaseMapListPassengerList(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(BookRequestPassengerAncillaryPurchaseMapListPassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BookRequestPassengerAncillaryPurchaseMapList(TeaModel):
    def __init__(self, book_ancillary_req_item=None, passenger_list=None):
        self.book_ancillary_req_item = book_ancillary_req_item  # type: BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem
        self.passenger_list = passenger_list  # type: list[BookRequestPassengerAncillaryPurchaseMapListPassengerList]

    def validate(self):
        if self.book_ancillary_req_item:
            self.book_ancillary_req_item.validate()
        if self.passenger_list:
            for k in self.passenger_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BookRequestPassengerAncillaryPurchaseMapList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_ancillary_req_item is not None:
            result['book_ancillary_req_item'] = self.book_ancillary_req_item.to_map()
        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k in self.passenger_list:
                result['passenger_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('book_ancillary_req_item') is not None:
            temp_model = BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem()
            self.book_ancillary_req_item = temp_model.from_map(m['book_ancillary_req_item'])
        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k in m.get('passenger_list'):
                temp_model = BookRequestPassengerAncillaryPurchaseMapListPassengerList()
                self.passenger_list.append(temp_model.from_map(k))
        return self


class BookRequestPassengerListCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookRequestPassengerListCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class BookRequestPassengerList(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: BookRequestPassengerListCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(BookRequestPassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = BookRequestPassengerListCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BookRequest(TeaModel):
    def __init__(self, contact=None, out_order_num=None, passenger_ancillary_purchase_map_list=None,
                 passenger_list=None, solution_id=None):
        self.contact = contact  # type: BookRequestContact
        self.out_order_num = out_order_num  # type: str
        self.passenger_ancillary_purchase_map_list = passenger_ancillary_purchase_map_list  # type: list[BookRequestPassengerAncillaryPurchaseMapList]
        self.passenger_list = passenger_list  # type: list[BookRequestPassengerList]
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.passenger_ancillary_purchase_map_list:
            for k in self.passenger_ancillary_purchase_map_list:
                if k:
                    k.validate()
        if self.passenger_list:
            for k in self.passenger_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['contact'] = self.contact.to_map()
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        result['passenger_ancillary_purchase_map_list'] = []
        if self.passenger_ancillary_purchase_map_list is not None:
            for k in self.passenger_ancillary_purchase_map_list:
                result['passenger_ancillary_purchase_map_list'].append(k.to_map() if k else None)
        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k in self.passenger_list:
                result['passenger_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('contact') is not None:
            temp_model = BookRequestContact()
            self.contact = temp_model.from_map(m['contact'])
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        self.passenger_ancillary_purchase_map_list = []
        if m.get('passenger_ancillary_purchase_map_list') is not None:
            for k in m.get('passenger_ancillary_purchase_map_list'):
                temp_model = BookRequestPassengerAncillaryPurchaseMapList()
                self.passenger_ancillary_purchase_map_list.append(temp_model.from_map(k))
        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k in m.get('passenger_list'):
                temp_model = BookRequestPassengerList()
                self.passenger_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class BookShrinkRequest(TeaModel):
    def __init__(self, contact_shrink=None, out_order_num=None, passenger_ancillary_purchase_map_list_shrink=None,
                 passenger_list_shrink=None, solution_id=None):
        self.contact_shrink = contact_shrink  # type: str
        self.out_order_num = out_order_num  # type: str
        self.passenger_ancillary_purchase_map_list_shrink = passenger_ancillary_purchase_map_list_shrink  # type: str
        self.passenger_list_shrink = passenger_list_shrink  # type: str
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_shrink is not None:
            result['contact'] = self.contact_shrink
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        if self.passenger_ancillary_purchase_map_list_shrink is not None:
            result['passenger_ancillary_purchase_map_list'] = self.passenger_ancillary_purchase_map_list_shrink
        if self.passenger_list_shrink is not None:
            result['passenger_list'] = self.passenger_list_shrink
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('contact') is not None:
            self.contact_shrink = m.get('contact')
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        if m.get('passenger_ancillary_purchase_map_list') is not None:
            self.passenger_ancillary_purchase_map_list_shrink = m.get('passenger_ancillary_purchase_map_list')
        if m.get('passenger_list') is not None:
            self.passenger_list_shrink = m.get('passenger_list')
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class BookResponseBodyDataOrderList(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookResponseBodyDataOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class BookResponseBodyData(TeaModel):
    def __init__(self, order_list=None):
        self.order_list = order_list  # type: list[BookResponseBodyDataOrderList]

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['order_list'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['order_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_list = []
        if m.get('order_list') is not None:
            for k in m.get('order_list'):
                temp_model = BookResponseBodyDataOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class BookResponseBodyErrorDataOrderList(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BookResponseBodyErrorDataOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class BookResponseBodyErrorData(TeaModel):
    def __init__(self, order_list=None):
        self.order_list = order_list  # type: list[BookResponseBodyErrorDataOrderList]

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BookResponseBodyErrorData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['order_list'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['order_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order_list = []
        if m.get('order_list') is not None:
            for k in m.get('order_list'):
                temp_model = BookResponseBodyErrorDataOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class BookResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: BookResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: BookResponseBodyErrorData
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_data:
            self.error_data.validate()

    def to_map(self):
        _map = super(BookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data.to_map()
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = BookResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            temp_model = BookResponseBodyErrorData()
            self.error_data = temp_model.from_map(m['error_data'])
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BookResponse, self).to_map()
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
            temp_model = BookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class CancelRequest(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class CancelResponseBodyData(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class CancelResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: CancelResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CancelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = CancelResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CancelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelResponse, self).to_map()
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
            temp_model = CancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeApplyHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeApplyRequestChangePassengerList(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyRequestChangePassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeApplyRequestChangedJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrive_terminal=None, arrive_time=None,
                 code_share=None, departure_airport=None, departure_city=None, departure_date=None, departure_terminal=None,
                 departure_time=None, marketing_flight_no=None, operating_flight_no=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrive_terminal = arrive_terminal  # type: str
        self.arrive_time = arrive_time  # type: long
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_date = departure_date  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: long
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.operating_flight_no = operating_flight_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyRequestChangedJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrive_terminal is not None:
            result['arrive_terminal'] = self.arrive_terminal
        if self.arrive_time is not None:
            result['arrive_time'] = self.arrive_time
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_date is not None:
            result['departure_date'] = self.departure_date
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrive_terminal') is not None:
            self.arrive_terminal = m.get('arrive_terminal')
        if m.get('arrive_time') is not None:
            self.arrive_time = m.get('arrive_time')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        return self


class ChangeApplyRequestChangedJourneys(TeaModel):
    def __init__(self, segment_list=None):
        self.segment_list = segment_list  # type: list[ChangeApplyRequestChangedJourneysSegmentList]

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeApplyRequestChangedJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeApplyRequestChangedJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        return self


class ChangeApplyRequestContact(TeaModel):
    def __init__(self, email=None, mobile_country_code=None, mobile_phone_num=None):
        self.email = email  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_num = mobile_phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyRequestContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')
        return self


class ChangeApplyRequest(TeaModel):
    def __init__(self, change_passenger_list=None, changed_journeys=None, contact=None, order_num=None, remark=None,
                 type=None):
        self.change_passenger_list = change_passenger_list  # type: list[ChangeApplyRequestChangePassengerList]
        self.changed_journeys = changed_journeys  # type: list[ChangeApplyRequestChangedJourneys]
        self.contact = contact  # type: ChangeApplyRequestContact
        self.order_num = order_num  # type: long
        self.remark = remark  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.change_passenger_list:
            for k in self.change_passenger_list:
                if k:
                    k.validate()
        if self.changed_journeys:
            for k in self.changed_journeys:
                if k:
                    k.validate()
        if self.contact:
            self.contact.validate()

    def to_map(self):
        _map = super(ChangeApplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['change_passenger_list'] = []
        if self.change_passenger_list is not None:
            for k in self.change_passenger_list:
                result['change_passenger_list'].append(k.to_map() if k else None)
        result['changed_journeys'] = []
        if self.changed_journeys is not None:
            for k in self.changed_journeys:
                result['changed_journeys'].append(k.to_map() if k else None)
        if self.contact is not None:
            result['contact'] = self.contact.to_map()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.remark is not None:
            result['remark'] = self.remark
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_passenger_list = []
        if m.get('change_passenger_list') is not None:
            for k in m.get('change_passenger_list'):
                temp_model = ChangeApplyRequestChangePassengerList()
                self.change_passenger_list.append(temp_model.from_map(k))
        self.changed_journeys = []
        if m.get('changed_journeys') is not None:
            for k in m.get('changed_journeys'):
                temp_model = ChangeApplyRequestChangedJourneys()
                self.changed_journeys.append(temp_model.from_map(k))
        if m.get('contact') is not None:
            temp_model = ChangeApplyRequestContact()
            self.contact = temp_model.from_map(m['contact'])
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ChangeApplyShrinkRequest(TeaModel):
    def __init__(self, change_passenger_list_shrink=None, changed_journeys_shrink=None, contact_shrink=None,
                 order_num=None, remark=None, type=None):
        self.change_passenger_list_shrink = change_passenger_list_shrink  # type: str
        self.changed_journeys_shrink = changed_journeys_shrink  # type: str
        self.contact_shrink = contact_shrink  # type: str
        self.order_num = order_num  # type: long
        self.remark = remark  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_passenger_list_shrink is not None:
            result['change_passenger_list'] = self.change_passenger_list_shrink
        if self.changed_journeys_shrink is not None:
            result['changed_journeys'] = self.changed_journeys_shrink
        if self.contact_shrink is not None:
            result['contact'] = self.contact_shrink
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.remark is not None:
            result['remark'] = self.remark
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_passenger_list') is not None:
            self.change_passenger_list_shrink = m.get('change_passenger_list')
        if m.get('changed_journeys') is not None:
            self.changed_journeys_shrink = m.get('changed_journeys')
        if m.get('contact') is not None:
            self.contact_shrink = m.get('contact')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ChangeApplyResponseBodyDataChangeOrdersPassengers(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplyResponseBodyDataChangeOrdersPassengers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeApplyResponseBodyDataChangeOrders(TeaModel):
    def __init__(self, change_order_num=None, change_order_status=None, fail_reason=None, passengers=None):
        self.change_order_num = change_order_num  # type: long
        self.change_order_status = change_order_status  # type: int
        self.fail_reason = fail_reason  # type: str
        self.passengers = passengers  # type: list[ChangeApplyResponseBodyDataChangeOrdersPassengers]

    def validate(self):
        if self.passengers:
            for k in self.passengers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeApplyResponseBodyDataChangeOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        if self.change_order_status is not None:
            result['change_order_status'] = self.change_order_status
        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason
        result['passengers'] = []
        if self.passengers is not None:
            for k in self.passengers:
                result['passengers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        if m.get('change_order_status') is not None:
            self.change_order_status = m.get('change_order_status')
        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')
        self.passengers = []
        if m.get('passengers') is not None:
            for k in m.get('passengers'):
                temp_model = ChangeApplyResponseBodyDataChangeOrdersPassengers()
                self.passengers.append(temp_model.from_map(k))
        return self


class ChangeApplyResponseBodyData(TeaModel):
    def __init__(self, change_orders=None, order_num=None):
        self.change_orders = change_orders  # type: list[ChangeApplyResponseBodyDataChangeOrders]
        self.order_num = order_num  # type: long

    def validate(self):
        if self.change_orders:
            for k in self.change_orders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeApplyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['change_orders'] = []
        if self.change_orders is not None:
            for k in self.change_orders:
                result['change_orders'].append(k.to_map() if k else None)
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_orders = []
        if m.get('change_orders') is not None:
            for k in m.get('change_orders'):
                temp_model = ChangeApplyResponseBodyDataChangeOrders()
                self.change_orders.append(temp_model.from_map(k))
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class ChangeApplyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ChangeApplyResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeApplyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ChangeApplyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeApplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeApplyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeApplyResponse, self).to_map()
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
            temp_model = ChangeApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeCancelHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeCancelHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeCancelRequest(TeaModel):
    def __init__(self, change_order_num=None):
        self.change_order_num = change_order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeCancelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        return self


class ChangeCancelResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: any
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeCancelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeCancelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeCancelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeCancelResponse, self).to_map()
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
            temp_model = ChangeCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeConfirmHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeConfirmHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeConfirmRequest(TeaModel):
    def __init__(self, change_order_num=None):
        self.change_order_num = change_order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeConfirmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        return self


class ChangeConfirmResponseBodyData(TeaModel):
    def __init__(self, pay_amount=None, transaction_no=None):
        self.pay_amount = pay_amount  # type: float
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeConfirmResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class ChangeConfirmResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ChangeConfirmResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeConfirmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ChangeConfirmResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeConfirmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeConfirmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeConfirmResponse, self).to_map()
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
            temp_model = ChangeConfirmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeDetailRequest(TeaModel):
    def __init__(self, change_order_num=None):
        self.change_order_num = change_order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        return self


class ChangeDetailResponseBodyDataChangeFeeDetailsChangeFee(TeaModel):
    def __init__(self, service_fee=None, tax_fee=None, upgrade_fee=None):
        self.service_fee = service_fee  # type: float
        self.tax_fee = tax_fee  # type: float
        self.upgrade_fee = upgrade_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangeFeeDetailsChangeFee, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.tax_fee is not None:
            result['tax_fee'] = self.tax_fee
        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('tax_fee') is not None:
            self.tax_fee = m.get('tax_fee')
        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')
        return self


class ChangeDetailResponseBodyDataChangeFeeDetailsPassenger(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangeFeeDetailsPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeDetailResponseBodyDataChangeFeeDetails(TeaModel):
    def __init__(self, change_fee=None, passenger=None):
        self.change_fee = change_fee  # type: ChangeDetailResponseBodyDataChangeFeeDetailsChangeFee
        self.passenger = passenger  # type: ChangeDetailResponseBodyDataChangeFeeDetailsPassenger

    def validate(self):
        if self.change_fee:
            self.change_fee.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangeFeeDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee.to_map()
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_fee') is not None:
            temp_model = ChangeDetailResponseBodyDataChangeFeeDetailsChangeFee()
            self.change_fee = temp_model.from_map(m['change_fee'])
        if m.get('passenger') is not None:
            temp_model = ChangeDetailResponseBodyDataChangeFeeDetailsPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        return self


class ChangeDetailResponseBodyDataChangePassengers(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangePassengers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeDetailResponseBodyDataChangedJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangedJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailResponseBodyDataChangedJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailResponseBodyDataChangedJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataChangedJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailResponseBodyDataChangedJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailResponseBodyDataContact(TeaModel):
    def __init__(self, email=None, mobile_country_code=None, mobile_phone_num=None):
        self.email = email  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_num = mobile_phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')
        return self


class ChangeDetailResponseBodyDataLastJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataLastJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailResponseBodyDataLastJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailResponseBodyDataLastJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataLastJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailResponseBodyDataLastJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailResponseBodyDataOriginalJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataOriginalJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailResponseBodyDataOriginalJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailResponseBodyDataOriginalJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBodyDataOriginalJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailResponseBodyDataOriginalJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailResponseBodyData(TeaModel):
    def __init__(self, change_fee_details=None, change_order_num=None, change_passengers=None,
                 change_reason_type=None, changed_journeys=None, close_reason=None, close_utc_time=None, contact=None,
                 create_utc_time=None, last_confirm_utc_time=None, last_journeys=None, order_num=None, order_status=None,
                 original_journeys=None, pay_status=None, pay_success_utc_time=None, total_amount=None, transaction_no=None):
        self.change_fee_details = change_fee_details  # type: list[ChangeDetailResponseBodyDataChangeFeeDetails]
        self.change_order_num = change_order_num  # type: long
        self.change_passengers = change_passengers  # type: list[ChangeDetailResponseBodyDataChangePassengers]
        self.change_reason_type = change_reason_type  # type: int
        self.changed_journeys = changed_journeys  # type: list[ChangeDetailResponseBodyDataChangedJourneys]
        self.close_reason = close_reason  # type: str
        self.close_utc_time = close_utc_time  # type: long
        self.contact = contact  # type: ChangeDetailResponseBodyDataContact
        self.create_utc_time = create_utc_time  # type: long
        self.last_confirm_utc_time = last_confirm_utc_time  # type: long
        self.last_journeys = last_journeys  # type: list[ChangeDetailResponseBodyDataLastJourneys]
        self.order_num = order_num  # type: long
        self.order_status = order_status  # type: int
        self.original_journeys = original_journeys  # type: list[ChangeDetailResponseBodyDataOriginalJourneys]
        self.pay_status = pay_status  # type: int
        self.pay_success_utc_time = pay_success_utc_time  # type: long
        self.total_amount = total_amount  # type: float
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        if self.change_fee_details:
            for k in self.change_fee_details:
                if k:
                    k.validate()
        if self.change_passengers:
            for k in self.change_passengers:
                if k:
                    k.validate()
        if self.changed_journeys:
            for k in self.changed_journeys:
                if k:
                    k.validate()
        if self.contact:
            self.contact.validate()
        if self.last_journeys:
            for k in self.last_journeys:
                if k:
                    k.validate()
        if self.original_journeys:
            for k in self.original_journeys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['change_fee_details'] = []
        if self.change_fee_details is not None:
            for k in self.change_fee_details:
                result['change_fee_details'].append(k.to_map() if k else None)
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        result['change_passengers'] = []
        if self.change_passengers is not None:
            for k in self.change_passengers:
                result['change_passengers'].append(k.to_map() if k else None)
        if self.change_reason_type is not None:
            result['change_reason_type'] = self.change_reason_type
        result['changed_journeys'] = []
        if self.changed_journeys is not None:
            for k in self.changed_journeys:
                result['changed_journeys'].append(k.to_map() if k else None)
        if self.close_reason is not None:
            result['close_reason'] = self.close_reason
        if self.close_utc_time is not None:
            result['close_utc_time'] = self.close_utc_time
        if self.contact is not None:
            result['contact'] = self.contact.to_map()
        if self.create_utc_time is not None:
            result['create_utc_time'] = self.create_utc_time
        if self.last_confirm_utc_time is not None:
            result['last_confirm_utc_time'] = self.last_confirm_utc_time
        result['last_journeys'] = []
        if self.last_journeys is not None:
            for k in self.last_journeys:
                result['last_journeys'].append(k.to_map() if k else None)
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_status is not None:
            result['order_status'] = self.order_status
        result['original_journeys'] = []
        if self.original_journeys is not None:
            for k in self.original_journeys:
                result['original_journeys'].append(k.to_map() if k else None)
        if self.pay_status is not None:
            result['pay_status'] = self.pay_status
        if self.pay_success_utc_time is not None:
            result['pay_success_utc_time'] = self.pay_success_utc_time
        if self.total_amount is not None:
            result['total_amount'] = self.total_amount
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_fee_details = []
        if m.get('change_fee_details') is not None:
            for k in m.get('change_fee_details'):
                temp_model = ChangeDetailResponseBodyDataChangeFeeDetails()
                self.change_fee_details.append(temp_model.from_map(k))
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        self.change_passengers = []
        if m.get('change_passengers') is not None:
            for k in m.get('change_passengers'):
                temp_model = ChangeDetailResponseBodyDataChangePassengers()
                self.change_passengers.append(temp_model.from_map(k))
        if m.get('change_reason_type') is not None:
            self.change_reason_type = m.get('change_reason_type')
        self.changed_journeys = []
        if m.get('changed_journeys') is not None:
            for k in m.get('changed_journeys'):
                temp_model = ChangeDetailResponseBodyDataChangedJourneys()
                self.changed_journeys.append(temp_model.from_map(k))
        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')
        if m.get('close_utc_time') is not None:
            self.close_utc_time = m.get('close_utc_time')
        if m.get('contact') is not None:
            temp_model = ChangeDetailResponseBodyDataContact()
            self.contact = temp_model.from_map(m['contact'])
        if m.get('create_utc_time') is not None:
            self.create_utc_time = m.get('create_utc_time')
        if m.get('last_confirm_utc_time') is not None:
            self.last_confirm_utc_time = m.get('last_confirm_utc_time')
        self.last_journeys = []
        if m.get('last_journeys') is not None:
            for k in m.get('last_journeys'):
                temp_model = ChangeDetailResponseBodyDataLastJourneys()
                self.last_journeys.append(temp_model.from_map(k))
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        self.original_journeys = []
        if m.get('original_journeys') is not None:
            for k in m.get('original_journeys'):
                temp_model = ChangeDetailResponseBodyDataOriginalJourneys()
                self.original_journeys.append(temp_model.from_map(k))
        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')
        if m.get('pay_success_utc_time') is not None:
            self.pay_success_utc_time = m.get('pay_success_utc_time')
        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class ChangeDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ChangeDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ChangeDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeDetailResponse, self).to_map()
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
            temp_model = ChangeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeDetailListOfBuyerHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeDetailListOfBuyerRequest(TeaModel):
    def __init__(self, page_index=None, page_size=None, utc_create_begin=None, utc_create_end=None):
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.utc_create_begin = utc_create_begin  # type: long
        self.utc_create_end = utc_create_end  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.utc_create_begin is not None:
            result['utc_create_begin'] = self.utc_create_begin
        if self.utc_create_end is not None:
            result['utc_create_end'] = self.utc_create_end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('utc_create_begin') is not None:
            self.utc_create_begin = m.get('utc_create_begin')
        if m.get('utc_create_end') is not None:
            self.utc_create_end = m.get('utc_create_end')
        return self


class ChangeDetailListOfBuyerResponseBodyDataList(TeaModel):
    def __init__(self, change_order_num=None, order_num=None, order_status=None, pay_status=None,
                 transaction_no=None, utc_create_time=None):
        self.change_order_num = change_order_num  # type: long
        self.order_num = order_num  # type: long
        self.order_status = order_status  # type: int
        self.pay_status = pay_status  # type: int
        self.transaction_no = transaction_no  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.pay_status is not None:
            result['pay_status'] = self.pay_status
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        if self.utc_create_time is not None:
            result['utc_create_time'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        if m.get('utc_create_time') is not None:
            self.utc_create_time = m.get('utc_create_time')
        return self


class ChangeDetailListOfBuyerResponseBodyDataPagination(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None, total_page=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerResponseBodyDataPagination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['current_page'] = self.current_page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.total_page is not None:
            result['total_page'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')
        return self


class ChangeDetailListOfBuyerResponseBodyData(TeaModel):
    def __init__(self, list=None, pagination=None):
        self.list = list  # type: list[ChangeDetailListOfBuyerResponseBodyDataList]
        self.pagination = pagination  # type: ChangeDetailListOfBuyerResponseBodyDataPagination

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ChangeDetailListOfBuyerResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pagination') is not None:
            temp_model = ChangeDetailListOfBuyerResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['pagination'])
        return self


class ChangeDetailListOfBuyerResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ChangeDetailListOfBuyerResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ChangeDetailListOfBuyerResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeDetailListOfBuyerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeDetailListOfBuyerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfBuyerResponse, self).to_map()
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
            temp_model = ChangeDetailListOfBuyerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeDetailListOfOrderNumHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class ChangeDetailListOfOrderNumRequest(TeaModel):
    def __init__(self, order_num=None, page_index=None, page_size=None):
        self.order_num = order_num  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee(TeaModel):
    def __init__(self, service_fee=None, tax_fee=None, upgrade_fee=None):
        self.service_fee = service_fee  # type: float
        self.tax_fee = tax_fee  # type: float
        self.upgrade_fee = upgrade_fee  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.tax_fee is not None:
            result['tax_fee'] = self.tax_fee
        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('tax_fee') is not None:
            self.tax_fee = m.get('tax_fee')
        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails(TeaModel):
    def __init__(self, change_fee=None, passenger=None):
        self.change_fee = change_fee  # type: ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee
        self.passenger = passenger  # type: ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger

    def validate(self):
        if self.change_fee:
            self.change_fee.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee.to_map()
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_fee') is not None:
            temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee()
            self.change_fee = temp_model.from_map(m['change_fee'])
        if m.get('passenger') is not None:
            temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListContact(TeaModel):
    def __init__(self, email=None, mobile_country_code=None, mobile_phone_num=None):
        self.email = email  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_num = mobile_phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataList(TeaModel):
    def __init__(self, change_fee_details=None, change_order_num=None, change_passengers=None,
                 change_reason_type=None, changed_journeys=None, close_reason=None, close_utc_time=None, contact=None,
                 create_utc_time=None, last_confirm_utc_time=None, last_journeys=None, order_num=None, order_status=None,
                 original_journeys=None, pay_status=None, pay_success_utc_time=None, total_amount=None, transaction_no=None):
        self.change_fee_details = change_fee_details  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails]
        self.change_order_num = change_order_num  # type: long
        self.change_passengers = change_passengers  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers]
        self.change_reason_type = change_reason_type  # type: int
        self.changed_journeys = changed_journeys  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys]
        self.close_reason = close_reason  # type: str
        self.close_utc_time = close_utc_time  # type: long
        self.contact = contact  # type: ChangeDetailListOfOrderNumResponseBodyDataListContact
        self.create_utc_time = create_utc_time  # type: long
        self.last_confirm_utc_time = last_confirm_utc_time  # type: long
        self.last_journeys = last_journeys  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys]
        self.order_num = order_num  # type: long
        self.order_status = order_status  # type: int
        self.original_journeys = original_journeys  # type: list[ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys]
        self.pay_status = pay_status  # type: int
        self.pay_success_utc_time = pay_success_utc_time  # type: long
        self.total_amount = total_amount  # type: float
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        if self.change_fee_details:
            for k in self.change_fee_details:
                if k:
                    k.validate()
        if self.change_passengers:
            for k in self.change_passengers:
                if k:
                    k.validate()
        if self.changed_journeys:
            for k in self.changed_journeys:
                if k:
                    k.validate()
        if self.contact:
            self.contact.validate()
        if self.last_journeys:
            for k in self.last_journeys:
                if k:
                    k.validate()
        if self.original_journeys:
            for k in self.original_journeys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['change_fee_details'] = []
        if self.change_fee_details is not None:
            for k in self.change_fee_details:
                result['change_fee_details'].append(k.to_map() if k else None)
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num
        result['change_passengers'] = []
        if self.change_passengers is not None:
            for k in self.change_passengers:
                result['change_passengers'].append(k.to_map() if k else None)
        if self.change_reason_type is not None:
            result['change_reason_type'] = self.change_reason_type
        result['changed_journeys'] = []
        if self.changed_journeys is not None:
            for k in self.changed_journeys:
                result['changed_journeys'].append(k.to_map() if k else None)
        if self.close_reason is not None:
            result['close_reason'] = self.close_reason
        if self.close_utc_time is not None:
            result['close_utc_time'] = self.close_utc_time
        if self.contact is not None:
            result['contact'] = self.contact.to_map()
        if self.create_utc_time is not None:
            result['create_utc_time'] = self.create_utc_time
        if self.last_confirm_utc_time is not None:
            result['last_confirm_utc_time'] = self.last_confirm_utc_time
        result['last_journeys'] = []
        if self.last_journeys is not None:
            for k in self.last_journeys:
                result['last_journeys'].append(k.to_map() if k else None)
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_status is not None:
            result['order_status'] = self.order_status
        result['original_journeys'] = []
        if self.original_journeys is not None:
            for k in self.original_journeys:
                result['original_journeys'].append(k.to_map() if k else None)
        if self.pay_status is not None:
            result['pay_status'] = self.pay_status
        if self.pay_success_utc_time is not None:
            result['pay_success_utc_time'] = self.pay_success_utc_time
        if self.total_amount is not None:
            result['total_amount'] = self.total_amount
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_fee_details = []
        if m.get('change_fee_details') is not None:
            for k in m.get('change_fee_details'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails()
                self.change_fee_details.append(temp_model.from_map(k))
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')
        self.change_passengers = []
        if m.get('change_passengers') is not None:
            for k in m.get('change_passengers'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers()
                self.change_passengers.append(temp_model.from_map(k))
        if m.get('change_reason_type') is not None:
            self.change_reason_type = m.get('change_reason_type')
        self.changed_journeys = []
        if m.get('changed_journeys') is not None:
            for k in m.get('changed_journeys'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys()
                self.changed_journeys.append(temp_model.from_map(k))
        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')
        if m.get('close_utc_time') is not None:
            self.close_utc_time = m.get('close_utc_time')
        if m.get('contact') is not None:
            temp_model = ChangeDetailListOfOrderNumResponseBodyDataListContact()
            self.contact = temp_model.from_map(m['contact'])
        if m.get('create_utc_time') is not None:
            self.create_utc_time = m.get('create_utc_time')
        if m.get('last_confirm_utc_time') is not None:
            self.last_confirm_utc_time = m.get('last_confirm_utc_time')
        self.last_journeys = []
        if m.get('last_journeys') is not None:
            for k in m.get('last_journeys'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys()
                self.last_journeys.append(temp_model.from_map(k))
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        self.original_journeys = []
        if m.get('original_journeys') is not None:
            for k in m.get('original_journeys'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys()
                self.original_journeys.append(temp_model.from_map(k))
        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')
        if m.get('pay_success_utc_time') is not None:
            self.pay_success_utc_time = m.get('pay_success_utc_time')
        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class ChangeDetailListOfOrderNumResponseBodyDataPagination(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None, total_page=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyDataPagination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['current_page'] = self.current_page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.total_page is not None:
            result['total_page'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')
        return self


class ChangeDetailListOfOrderNumResponseBodyData(TeaModel):
    def __init__(self, list=None, pagination=None):
        self.list = list  # type: list[ChangeDetailListOfOrderNumResponseBodyDataList]
        self.pagination = pagination  # type: ChangeDetailListOfOrderNumResponseBodyDataPagination

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ChangeDetailListOfOrderNumResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pagination') is not None:
            temp_model = ChangeDetailListOfOrderNumResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['pagination'])
        return self


class ChangeDetailListOfOrderNumResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ChangeDetailListOfOrderNumResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ChangeDetailListOfOrderNumResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ChangeDetailListOfOrderNumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeDetailListOfOrderNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeDetailListOfOrderNumResponse, self).to_map()
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
            temp_model = ChangeDetailListOfOrderNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnrichHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrichHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class EnrichRequestJourneyParamListSegmentParamList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, cabin=None, child_cabin=None,
                 departure_airport=None, departure_city=None, departure_time=None, marketing_flight_no=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.cabin = cabin  # type: str
        self.child_cabin = child_cabin  # type: str
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_time = departure_time  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrichRequestJourneyParamListSegmentParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.child_cabin is not None:
            result['child_cabin'] = self.child_cabin
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('child_cabin') is not None:
            self.child_cabin = m.get('child_cabin')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        return self


class EnrichRequestJourneyParamList(TeaModel):
    def __init__(self, arrival_city=None, departure_city=None, departure_date=None, segment_param_list=None):
        self.arrival_city = arrival_city  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_date = departure_date  # type: str
        self.segment_param_list = segment_param_list  # type: list[EnrichRequestJourneyParamListSegmentParamList]

    def validate(self):
        if self.segment_param_list:
            for k in self.segment_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrichRequestJourneyParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_date is not None:
            result['departure_date'] = self.departure_date
        result['segment_param_list'] = []
        if self.segment_param_list is not None:
            for k in self.segment_param_list:
                result['segment_param_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')
        self.segment_param_list = []
        if m.get('segment_param_list') is not None:
            for k in m.get('segment_param_list'):
                temp_model = EnrichRequestJourneyParamListSegmentParamList()
                self.segment_param_list.append(temp_model.from_map(k))
        return self


class EnrichRequest(TeaModel):
    def __init__(self, adults=None, cabin_class=None, children=None, infants=None, journey_param_list=None,
                 solution_id=None):
        self.adults = adults  # type: int
        self.cabin_class = cabin_class  # type: str
        self.children = children  # type: int
        self.infants = infants  # type: int
        self.journey_param_list = journey_param_list  # type: list[EnrichRequestJourneyParamList]
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.journey_param_list:
            for k in self.journey_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrichRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adults is not None:
            result['adults'] = self.adults
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.children is not None:
            result['children'] = self.children
        if self.infants is not None:
            result['infants'] = self.infants
        result['journey_param_list'] = []
        if self.journey_param_list is not None:
            for k in self.journey_param_list:
                result['journey_param_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('infants') is not None:
            self.infants = m.get('infants')
        self.journey_param_list = []
        if m.get('journey_param_list') is not None:
            for k in m.get('journey_param_list'):
                temp_model = EnrichRequestJourneyParamList()
                self.journey_param_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class EnrichShrinkRequest(TeaModel):
    def __init__(self, adults=None, cabin_class=None, children=None, infants=None, journey_param_list_shrink=None,
                 solution_id=None):
        self.adults = adults  # type: int
        self.cabin_class = cabin_class  # type: str
        self.children = children  # type: int
        self.infants = infants  # type: int
        self.journey_param_list_shrink = journey_param_list_shrink  # type: str
        self.solution_id = solution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrichShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adults is not None:
            result['adults'] = self.adults
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.children is not None:
            result['children'] = self.children
        if self.infants is not None:
            result['infants'] = self.infants
        if self.journey_param_list_shrink is not None:
            result['journey_param_list'] = self.journey_param_list_shrink
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('infants') is not None:
            self.infants = m.get('infants')
        if m.get('journey_param_list') is not None:
            self.journey_param_list_shrink = m.get('journey_param_list')
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class EnrichResponseBodyDataSolutionListJourneyListSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionListJourneyListSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class EnrichResponseBodyDataSolutionListJourneyList(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[EnrichResponseBodyDataSolutionListJourneyListSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionListJourneyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = EnrichResponseBodyDataSolutionListJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class EnrichResponseBodyDataSolutionListSegmentBaggageCheckInInfoList(TeaModel):
    def __init__(self, luggage_direct_info_type=None, segment_id_list=None):
        self.luggage_direct_info_type = luggage_direct_info_type  # type: int
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionListSegmentBaggageCheckInInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.luggage_direct_info_type is not None:
            result['luggage_direct_info_type'] = self.luggage_direct_info_type
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('luggage_direct_info_type') is not None:
            self.luggage_direct_info_type = m.get('luggage_direct_info_type')
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class EnrichResponseBodyDataSolutionListSegmentBaggageMappingList(TeaModel):
    def __init__(self, passenger_baggage_allowance_mapping=None, segment_id_list=None):
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping  # type: dict[str, DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.passenger_baggage_allowance_mapping:
            for v in self.passenger_baggage_allowance_mapping.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionListSegmentBaggageMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['passenger_baggage_allowance_mapping'] = {}
        if self.passenger_baggage_allowance_mapping is not None:
            for k, v in self.passenger_baggage_allowance_mapping.items():
                result['passenger_baggage_allowance_mapping'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.passenger_baggage_allowance_mapping = {}
        if m.get('passenger_baggage_allowance_mapping') is not None:
            for k, v in m.get('passenger_baggage_allowance_mapping').items():
                temp_model = DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class EnrichResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList(TeaModel):
    def __init__(self, refund_change_rule_map=None, segment_id_list=None):
        self.refund_change_rule_map = refund_change_rule_map  # type: dict[str, DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.refund_change_rule_map:
            for v in self.refund_change_rule_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k, v in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k, v in m.get('refund_change_rule_map').items():
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class EnrichResponseBodyDataSolutionList(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None, journey_list=None, product_type_description=None, refund_ticket_coupon_description=None,
                 segment_baggage_check_in_info_list=None, segment_baggage_mapping_list=None, segment_refund_change_rule_mapping_list=None,
                 solution_id=None):
        self.adult_price = adult_price  # type: float
        self.adult_tax = adult_tax  # type: float
        self.child_price = child_price  # type: float
        self.child_tax = child_tax  # type: float
        self.infant_price = infant_price  # type: float
        self.infant_tax = infant_tax  # type: float
        self.journey_list = journey_list  # type: list[EnrichResponseBodyDataSolutionListJourneyList]
        self.product_type_description = product_type_description  # type: str
        self.refund_ticket_coupon_description = refund_ticket_coupon_description  # type: str
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list  # type: list[EnrichResponseBodyDataSolutionListSegmentBaggageCheckInInfoList]
        self.segment_baggage_mapping_list = segment_baggage_mapping_list  # type: list[EnrichResponseBodyDataSolutionListSegmentBaggageMappingList]
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list  # type: list[EnrichResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList]
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.journey_list:
            for k in self.journey_list:
                if k:
                    k.validate()
        if self.segment_baggage_check_in_info_list:
            for k in self.segment_baggage_check_in_info_list:
                if k:
                    k.validate()
        if self.segment_baggage_mapping_list:
            for k in self.segment_baggage_mapping_list:
                if k:
                    k.validate()
        if self.segment_refund_change_rule_mapping_list:
            for k in self.segment_refund_change_rule_mapping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrichResponseBodyDataSolutionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        result['journey_list'] = []
        if self.journey_list is not None:
            for k in self.journey_list:
                result['journey_list'].append(k.to_map() if k else None)
        if self.product_type_description is not None:
            result['product_type_description'] = self.product_type_description
        if self.refund_ticket_coupon_description is not None:
            result['refund_ticket_coupon_description'] = self.refund_ticket_coupon_description
        result['segment_baggage_check_in_info_list'] = []
        if self.segment_baggage_check_in_info_list is not None:
            for k in self.segment_baggage_check_in_info_list:
                result['segment_baggage_check_in_info_list'].append(k.to_map() if k else None)
        result['segment_baggage_mapping_list'] = []
        if self.segment_baggage_mapping_list is not None:
            for k in self.segment_baggage_mapping_list:
                result['segment_baggage_mapping_list'].append(k.to_map() if k else None)
        result['segment_refund_change_rule_mapping_list'] = []
        if self.segment_refund_change_rule_mapping_list is not None:
            for k in self.segment_refund_change_rule_mapping_list:
                result['segment_refund_change_rule_mapping_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        self.journey_list = []
        if m.get('journey_list') is not None:
            for k in m.get('journey_list'):
                temp_model = EnrichResponseBodyDataSolutionListJourneyList()
                self.journey_list.append(temp_model.from_map(k))
        if m.get('product_type_description') is not None:
            self.product_type_description = m.get('product_type_description')
        if m.get('refund_ticket_coupon_description') is not None:
            self.refund_ticket_coupon_description = m.get('refund_ticket_coupon_description')
        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k in m.get('segment_baggage_check_in_info_list'):
                temp_model = EnrichResponseBodyDataSolutionListSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k))
        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k in m.get('segment_baggage_mapping_list'):
                temp_model = EnrichResponseBodyDataSolutionListSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k))
        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = EnrichResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class EnrichResponseBodyData(TeaModel):
    def __init__(self, solution_list=None):
        self.solution_list = solution_list  # type: list[EnrichResponseBodyDataSolutionList]

    def validate(self):
        if self.solution_list:
            for k in self.solution_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrichResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['solution_list'] = []
        if self.solution_list is not None:
            for k in self.solution_list:
                result['solution_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.solution_list = []
        if m.get('solution_list') is not None:
            for k in m.get('solution_list'):
                temp_model = EnrichResponseBodyDataSolutionList()
                self.solution_list.append(temp_model.from_map(k))
        return self


class EnrichResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: EnrichResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnrichResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = EnrichResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class EnrichResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnrichResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnrichResponse, self).to_map()
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
            temp_model = EnrichResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileUploadHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileUploadHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class FileUploadRequest(TeaModel):
    def __init__(self, file_content=None, order_num=None):
        self.file_content = file_content  # type: str
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileUploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_content is not None:
            result['file_content'] = self.file_content
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('file_content') is not None:
            self.file_content = m.get('file_content')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class FileUploadResponseBodyData(TeaModel):
    def __init__(self, uploaded_file_url=None):
        self.uploaded_file_url = uploaded_file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileUploadResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uploaded_file_url is not None:
            result['uploaded_file_url'] = self.uploaded_file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uploaded_file_url') is not None:
            self.uploaded_file_url = m.get('uploaded_file_url')
        return self


class FileUploadResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: FileUploadResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FileUploadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = FileUploadResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FileUploadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FileUploadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FileUploadResponse, self).to_map()
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
            temp_model = FileUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlightChangeOfOrderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlightChangeOfOrderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class FlightChangeOfOrderRequest(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlightChangeOfOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class FlightChangeOfOrderResponseBodyDataFlightChangeDetail(TeaModel):
    def __init__(self, change_reason=None, change_time=None, change_type=None, new_arrival_airport=None,
                 new_arrival_time=None, new_departure_airport=None, new_departure_time=None, new_flight_no=None,
                 old_arrival_airport=None, old_arrival_time=None, old_departure_airport=None, old_departure_time=None,
                 old_flight_no=None):
        self.change_reason = change_reason  # type: str
        self.change_time = change_time  # type: str
        self.change_type = change_type  # type: int
        self.new_arrival_airport = new_arrival_airport  # type: str
        self.new_arrival_time = new_arrival_time  # type: str
        self.new_departure_airport = new_departure_airport  # type: str
        self.new_departure_time = new_departure_time  # type: str
        self.new_flight_no = new_flight_no  # type: str
        self.old_arrival_airport = old_arrival_airport  # type: str
        self.old_arrival_time = old_arrival_time  # type: str
        self.old_departure_airport = old_departure_airport  # type: str
        self.old_departure_time = old_departure_time  # type: str
        self.old_flight_no = old_flight_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlightChangeOfOrderResponseBodyDataFlightChangeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_reason is not None:
            result['change_reason'] = self.change_reason
        if self.change_time is not None:
            result['change_time'] = self.change_time
        if self.change_type is not None:
            result['change_type'] = self.change_type
        if self.new_arrival_airport is not None:
            result['new_arrival_airport'] = self.new_arrival_airport
        if self.new_arrival_time is not None:
            result['new_arrival_time'] = self.new_arrival_time
        if self.new_departure_airport is not None:
            result['new_departure_airport'] = self.new_departure_airport
        if self.new_departure_time is not None:
            result['new_departure_time'] = self.new_departure_time
        if self.new_flight_no is not None:
            result['new_flight_no'] = self.new_flight_no
        if self.old_arrival_airport is not None:
            result['old_arrival_airport'] = self.old_arrival_airport
        if self.old_arrival_time is not None:
            result['old_arrival_time'] = self.old_arrival_time
        if self.old_departure_airport is not None:
            result['old_departure_airport'] = self.old_departure_airport
        if self.old_departure_time is not None:
            result['old_departure_time'] = self.old_departure_time
        if self.old_flight_no is not None:
            result['old_flight_no'] = self.old_flight_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_reason') is not None:
            self.change_reason = m.get('change_reason')
        if m.get('change_time') is not None:
            self.change_time = m.get('change_time')
        if m.get('change_type') is not None:
            self.change_type = m.get('change_type')
        if m.get('new_arrival_airport') is not None:
            self.new_arrival_airport = m.get('new_arrival_airport')
        if m.get('new_arrival_time') is not None:
            self.new_arrival_time = m.get('new_arrival_time')
        if m.get('new_departure_airport') is not None:
            self.new_departure_airport = m.get('new_departure_airport')
        if m.get('new_departure_time') is not None:
            self.new_departure_time = m.get('new_departure_time')
        if m.get('new_flight_no') is not None:
            self.new_flight_no = m.get('new_flight_no')
        if m.get('old_arrival_airport') is not None:
            self.old_arrival_airport = m.get('old_arrival_airport')
        if m.get('old_arrival_time') is not None:
            self.old_arrival_time = m.get('old_arrival_time')
        if m.get('old_departure_airport') is not None:
            self.old_departure_airport = m.get('old_departure_airport')
        if m.get('old_departure_time') is not None:
            self.old_departure_time = m.get('old_departure_time')
        if m.get('old_flight_no') is not None:
            self.old_flight_no = m.get('old_flight_no')
        return self


class FlightChangeOfOrderResponseBodyData(TeaModel):
    def __init__(self, flight_change_detail=None, order_num=None):
        self.flight_change_detail = flight_change_detail  # type: FlightChangeOfOrderResponseBodyDataFlightChangeDetail
        self.order_num = order_num  # type: long

    def validate(self):
        if self.flight_change_detail:
            self.flight_change_detail.validate()

    def to_map(self):
        _map = super(FlightChangeOfOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flight_change_detail is not None:
            result['flight_change_detail'] = self.flight_change_detail.to_map()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flight_change_detail') is not None:
            temp_model = FlightChangeOfOrderResponseBodyDataFlightChangeDetail()
            self.flight_change_detail = temp_model.from_map(m['flight_change_detail'])
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class FlightChangeOfOrderResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[FlightChangeOfOrderResponseBodyData]
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FlightChangeOfOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FlightChangeOfOrderResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FlightChangeOfOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FlightChangeOfOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FlightChangeOfOrderResponse, self).to_map()
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
            temp_model = FlightChangeOfOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, app_key=None, app_secret=None):
        # appKey
        self.app_key = app_key  # type: str
        # appSecret
        self.app_secret = app_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['app_key'] = self.app_key
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app_key') is not None:
            self.app_key = m.get('app_key')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(self, expire_time=None, generate_time=None, token=None):
        self.expire_time = expire_time  # type: long
        self.generate_time = generate_time  # type: long
        # token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.generate_time is not None:
            result['generate_time'] = self.generate_time
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('generate_time') is not None:
            self.generate_time = m.get('generate_time')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: GetTokenResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTokenResponse, self).to_map()
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LuggageDirectHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LuggageDirectHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class LuggageDirectRequestFlightSegmentParamList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_terminal=None, arrival_time=None, code_share=None,
                 departure_airport=None, departure_terminal=None, departure_time=None, marketing_airline=None,
                 marketing_flight_no=None, operating_airline=None, stop_city_list=None, ticketing_airline=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: long
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: long
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.operating_airline = operating_airline  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.ticketing_airline = ticketing_airline  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LuggageDirectRequestFlightSegmentParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.ticketing_airline is not None:
            result['ticketing_airline'] = self.ticketing_airline
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('ticketing_airline') is not None:
            self.ticketing_airline = m.get('ticketing_airline')
        return self


class LuggageDirectRequest(TeaModel):
    def __init__(self, flight_segment_param_list=None):
        self.flight_segment_param_list = flight_segment_param_list  # type: list[LuggageDirectRequestFlightSegmentParamList]

    def validate(self):
        if self.flight_segment_param_list:
            for k in self.flight_segment_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LuggageDirectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['flight_segment_param_list'] = []
        if self.flight_segment_param_list is not None:
            for k in self.flight_segment_param_list:
                result['flight_segment_param_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flight_segment_param_list = []
        if m.get('flight_segment_param_list') is not None:
            for k in m.get('flight_segment_param_list'):
                temp_model = LuggageDirectRequestFlightSegmentParamList()
                self.flight_segment_param_list.append(temp_model.from_map(k))
        return self


class LuggageDirectShrinkRequest(TeaModel):
    def __init__(self, flight_segment_param_list_shrink=None):
        self.flight_segment_param_list_shrink = flight_segment_param_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LuggageDirectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flight_segment_param_list_shrink is not None:
            result['flight_segment_param_list'] = self.flight_segment_param_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flight_segment_param_list') is not None:
            self.flight_segment_param_list_shrink = m.get('flight_segment_param_list')
        return self


class LuggageDirectResponseBodyData(TeaModel):
    def __init__(self, city_code=None, direct_type=None):
        self.city_code = city_code  # type: str
        self.direct_type = direct_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(LuggageDirectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.direct_type is not None:
            result['direct_type'] = self.direct_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('direct_type') is not None:
            self.direct_type = m.get('direct_type')
        return self


class LuggageDirectResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[LuggageDirectResponseBodyData]
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LuggageDirectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = LuggageDirectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class LuggageDirectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LuggageDirectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LuggageDirectResponse, self).to_map()
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
            temp_model = LuggageDirectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class OrderDetailRequest(TeaModel):
    def __init__(self, order_num=None, out_order_num=None):
        self.order_num = order_num  # type: long
        self.out_order_num = out_order_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        return self


class OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary(TeaModel):
    def __init__(self, baggage_amount=None, baggage_weight=None, baggage_weight_unit=None, is_all_weight=None,
                 price=None):
        self.baggage_amount = baggage_amount  # type: int
        self.baggage_weight = baggage_weight  # type: int
        self.baggage_weight_unit = baggage_weight_unit  # type: str
        self.is_all_weight = is_all_weight  # type: bool
        self.price = price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount
        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight
        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit
        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight
        if self.price is not None:
            result['price'] = self.price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')
        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')
        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')
        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')
        if m.get('price') is not None:
            self.price = m.get('price')
        return self


class OrderDetailResponseBodyDataAncillaryItemDetailListAncillary(TeaModel):
    def __init__(self, ancillary_id=None, ancillary_type=None, baggage_ancillary=None):
        self.ancillary_id = ancillary_id  # type: str
        self.ancillary_type = ancillary_type  # type: int
        self.baggage_ancillary = baggage_ancillary  # type: OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary

    def validate(self):
        if self.baggage_ancillary:
            self.baggage_ancillary.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataAncillaryItemDetailListAncillary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id
        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type
        if self.baggage_ancillary is not None:
            result['baggage_ancillary'] = self.baggage_ancillary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')
        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')
        if m.get('baggage_ancillary') is not None:
            temp_model = OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary()
            self.baggage_ancillary = temp_model.from_map(m['baggage_ancillary'])
        return self


class OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class OrderDetailResponseBodyDataAncillaryItemDetailListPassenger(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataAncillaryItemDetailListPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OrderDetailResponseBodyDataAncillaryItemDetailList(TeaModel):
    def __init__(self, ancillary=None, passenger=None, segment_id_list=None):
        self.ancillary = ancillary  # type: OrderDetailResponseBodyDataAncillaryItemDetailListAncillary
        self.passenger = passenger  # type: OrderDetailResponseBodyDataAncillaryItemDetailListPassenger
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.ancillary:
            self.ancillary.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataAncillaryItemDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ancillary is not None:
            result['ancillary'] = self.ancillary.to_map()
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ancillary') is not None:
            temp_model = OrderDetailResponseBodyDataAncillaryItemDetailListAncillary()
            self.ancillary = temp_model.from_map(m['ancillary'])
        if m.get('passenger') is not None:
            temp_model = OrderDetailResponseBodyDataAncillaryItemDetailListPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class OrderDetailResponseBodyDataFlightItemDetailListFlightPrice(TeaModel):
    def __init__(self, sell_price=None, tax=None):
        self.sell_price = sell_price  # type: float
        self.tax = tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataFlightItemDetailListFlightPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sell_price is not None:
            result['sell_price'] = self.sell_price
        if self.tax is not None:
            result['tax'] = self.tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')
        if m.get('tax') is not None:
            self.tax = m.get('tax')
        return self


class OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation(TeaModel):
    def __init__(self, cabin=None, cabin_class=None, cabin_class_name=None, cabin_quantity=None, segment_id=None):
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.cabin_class_name = cabin_class_name  # type: str
        self.cabin_quantity = cabin_quantity  # type: str
        self.segment_id = segment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name
        if self.cabin_quantity is not None:
            result['cabin_quantity'] = self.cabin_quantity
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')
        if m.get('cabin_quantity') is not None:
            self.cabin_quantity = m.get('cabin_quantity')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        return self


class OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class OrderDetailResponseBodyDataFlightItemDetailListPassenger(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataFlightItemDetailListPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OrderDetailResponseBodyDataFlightItemDetailList(TeaModel):
    def __init__(self, b_pnr_list=None, c_pnr_list=None, flight_price=None, flight_segment_cabin_relation=None,
                 passenger=None, ticket_air_line=None, ticket_nos=None):
        self.b_pnr_list = b_pnr_list  # type: list[str]
        self.c_pnr_list = c_pnr_list  # type: list[str]
        self.flight_price = flight_price  # type: OrderDetailResponseBodyDataFlightItemDetailListFlightPrice
        self.flight_segment_cabin_relation = flight_segment_cabin_relation  # type: list[OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation]
        self.passenger = passenger  # type: OrderDetailResponseBodyDataFlightItemDetailListPassenger
        self.ticket_air_line = ticket_air_line  # type: str
        self.ticket_nos = ticket_nos  # type: list[str]

    def validate(self):
        if self.flight_price:
            self.flight_price.validate()
        if self.flight_segment_cabin_relation:
            for k in self.flight_segment_cabin_relation:
                if k:
                    k.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataFlightItemDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.b_pnr_list is not None:
            result['b_pnr_list'] = self.b_pnr_list
        if self.c_pnr_list is not None:
            result['c_pnr_list'] = self.c_pnr_list
        if self.flight_price is not None:
            result['flight_price'] = self.flight_price.to_map()
        result['flight_segment_cabin_relation'] = []
        if self.flight_segment_cabin_relation is not None:
            for k in self.flight_segment_cabin_relation:
                result['flight_segment_cabin_relation'].append(k.to_map() if k else None)
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        if self.ticket_air_line is not None:
            result['ticket_air_line'] = self.ticket_air_line
        if self.ticket_nos is not None:
            result['ticket_nos'] = self.ticket_nos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('b_pnr_list') is not None:
            self.b_pnr_list = m.get('b_pnr_list')
        if m.get('c_pnr_list') is not None:
            self.c_pnr_list = m.get('c_pnr_list')
        if m.get('flight_price') is not None:
            temp_model = OrderDetailResponseBodyDataFlightItemDetailListFlightPrice()
            self.flight_price = temp_model.from_map(m['flight_price'])
        self.flight_segment_cabin_relation = []
        if m.get('flight_segment_cabin_relation') is not None:
            for k in m.get('flight_segment_cabin_relation'):
                temp_model = OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation()
                self.flight_segment_cabin_relation.append(temp_model.from_map(k))
        if m.get('passenger') is not None:
            temp_model = OrderDetailResponseBodyDataFlightItemDetailListPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        if m.get('ticket_air_line') is not None:
            self.ticket_air_line = m.get('ticket_air_line')
        if m.get('ticket_nos') is not None:
            self.ticket_nos = m.get('ticket_nos')
        return self


class OrderDetailResponseBodyDataPassengerListCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataPassengerListCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class OrderDetailResponseBodyDataPassengerList(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: OrderDetailResponseBodyDataPassengerListCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataPassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = OrderDetailResponseBodyDataPassengerListCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OrderDetailResponseBodyDataSolutionJourneyListSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolutionJourneyListSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class OrderDetailResponseBodyDataSolutionJourneyList(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[OrderDetailResponseBodyDataSolutionJourneyListSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolutionJourneyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = OrderDetailResponseBodyDataSolutionJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList(TeaModel):
    def __init__(self, luggage_direct_info_type=None, segment_id_list=None):
        self.luggage_direct_info_type = luggage_direct_info_type  # type: int
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.luggage_direct_info_type is not None:
            result['luggage_direct_info_type'] = self.luggage_direct_info_type
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('luggage_direct_info_type') is not None:
            self.luggage_direct_info_type = m.get('luggage_direct_info_type')
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList(TeaModel):
    def __init__(self, passenger_baggage_allowance_mapping=None, segment_id_list=None):
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping  # type: dict[str, DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.passenger_baggage_allowance_mapping:
            for v in self.passenger_baggage_allowance_mapping.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['passenger_baggage_allowance_mapping'] = {}
        if self.passenger_baggage_allowance_mapping is not None:
            for k, v in self.passenger_baggage_allowance_mapping.items():
                result['passenger_baggage_allowance_mapping'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.passenger_baggage_allowance_mapping = {}
        if m.get('passenger_baggage_allowance_mapping') is not None:
            for k, v in m.get('passenger_baggage_allowance_mapping').items():
                temp_model = DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList(TeaModel):
    def __init__(self, refund_change_rule_map=None, segment_id_list=None):
        self.refund_change_rule_map = refund_change_rule_map  # type: dict[str, DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.refund_change_rule_map:
            for v in self.refund_change_rule_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k, v in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k, v in m.get('refund_change_rule_map').items():
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class OrderDetailResponseBodyDataSolution(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None, journey_list=None, product_type_description=None, refund_ticket_coupon_description=None,
                 segment_baggage_check_in_info_list=None, segment_baggage_mapping_list=None, segment_refund_change_rule_mapping_list=None,
                 solution_id=None):
        self.adult_price = adult_price  # type: float
        self.adult_tax = adult_tax  # type: float
        self.child_price = child_price  # type: float
        self.child_tax = child_tax  # type: float
        self.infant_price = infant_price  # type: float
        self.infant_tax = infant_tax  # type: float
        self.journey_list = journey_list  # type: list[OrderDetailResponseBodyDataSolutionJourneyList]
        self.product_type_description = product_type_description  # type: str
        self.refund_ticket_coupon_description = refund_ticket_coupon_description  # type: str
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list  # type: list[OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList]
        self.segment_baggage_mapping_list = segment_baggage_mapping_list  # type: list[OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList]
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list  # type: list[OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList]
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.journey_list:
            for k in self.journey_list:
                if k:
                    k.validate()
        if self.segment_baggage_check_in_info_list:
            for k in self.segment_baggage_check_in_info_list:
                if k:
                    k.validate()
        if self.segment_baggage_mapping_list:
            for k in self.segment_baggage_mapping_list:
                if k:
                    k.validate()
        if self.segment_refund_change_rule_mapping_list:
            for k in self.segment_refund_change_rule_mapping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyDataSolution, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        result['journey_list'] = []
        if self.journey_list is not None:
            for k in self.journey_list:
                result['journey_list'].append(k.to_map() if k else None)
        if self.product_type_description is not None:
            result['product_type_description'] = self.product_type_description
        if self.refund_ticket_coupon_description is not None:
            result['refund_ticket_coupon_description'] = self.refund_ticket_coupon_description
        result['segment_baggage_check_in_info_list'] = []
        if self.segment_baggage_check_in_info_list is not None:
            for k in self.segment_baggage_check_in_info_list:
                result['segment_baggage_check_in_info_list'].append(k.to_map() if k else None)
        result['segment_baggage_mapping_list'] = []
        if self.segment_baggage_mapping_list is not None:
            for k in self.segment_baggage_mapping_list:
                result['segment_baggage_mapping_list'].append(k.to_map() if k else None)
        result['segment_refund_change_rule_mapping_list'] = []
        if self.segment_refund_change_rule_mapping_list is not None:
            for k in self.segment_refund_change_rule_mapping_list:
                result['segment_refund_change_rule_mapping_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        self.journey_list = []
        if m.get('journey_list') is not None:
            for k in m.get('journey_list'):
                temp_model = OrderDetailResponseBodyDataSolutionJourneyList()
                self.journey_list.append(temp_model.from_map(k))
        if m.get('product_type_description') is not None:
            self.product_type_description = m.get('product_type_description')
        if m.get('refund_ticket_coupon_description') is not None:
            self.refund_ticket_coupon_description = m.get('refund_ticket_coupon_description')
        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k in m.get('segment_baggage_check_in_info_list'):
                temp_model = OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k))
        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k in m.get('segment_baggage_mapping_list'):
                temp_model = OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k))
        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class OrderDetailResponseBodyData(TeaModel):
    def __init__(self, ancillary_item_detail_list=None, baggage_allowance_map=None, book_time=None,
                 flight_item_detail_list=None, order_num=None, order_status=None, out_order_num=None, passenger_list=None, pay_status=None,
                 pay_time=None, promotion_price=None, real_pay_price=None, refund_change_rule_map=None, session_nick=None,
                 solution=None, succeed_time=None, total_price=None, transaction_no=None):
        self.ancillary_item_detail_list = ancillary_item_detail_list  # type: list[OrderDetailResponseBodyDataAncillaryItemDetailList]
        self.baggage_allowance_map = baggage_allowance_map  # type: dict[str, DataBaggageAllowanceMapValue]
        self.book_time = book_time  # type: long
        self.flight_item_detail_list = flight_item_detail_list  # type: list[OrderDetailResponseBodyDataFlightItemDetailList]
        self.order_num = order_num  # type: long
        self.order_status = order_status  # type: int
        self.out_order_num = out_order_num  # type: str
        self.passenger_list = passenger_list  # type: list[OrderDetailResponseBodyDataPassengerList]
        self.pay_status = pay_status  # type: int
        self.pay_time = pay_time  # type: long
        self.promotion_price = promotion_price  # type: float
        self.real_pay_price = real_pay_price  # type: float
        self.refund_change_rule_map = refund_change_rule_map  # type: dict[str, DataRefundChangeRuleMapValue]
        self.session_nick = session_nick  # type: str
        self.solution = solution  # type: OrderDetailResponseBodyDataSolution
        self.succeed_time = succeed_time  # type: long
        self.total_price = total_price  # type: float
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        if self.ancillary_item_detail_list:
            for k in self.ancillary_item_detail_list:
                if k:
                    k.validate()
        if self.baggage_allowance_map:
            for v in self.baggage_allowance_map.values():
                if v:
                    v.validate()
        if self.flight_item_detail_list:
            for k in self.flight_item_detail_list:
                if k:
                    k.validate()
        if self.passenger_list:
            for k in self.passenger_list:
                if k:
                    k.validate()
        if self.refund_change_rule_map:
            for v in self.refund_change_rule_map.values():
                if v:
                    v.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ancillary_item_detail_list'] = []
        if self.ancillary_item_detail_list is not None:
            for k in self.ancillary_item_detail_list:
                result['ancillary_item_detail_list'].append(k.to_map() if k else None)
        result['baggage_allowance_map'] = {}
        if self.baggage_allowance_map is not None:
            for k, v in self.baggage_allowance_map.items():
                result['baggage_allowance_map'][k] = v.to_map()
        if self.book_time is not None:
            result['book_time'] = self.book_time
        result['flight_item_detail_list'] = []
        if self.flight_item_detail_list is not None:
            for k in self.flight_item_detail_list:
                result['flight_item_detail_list'].append(k.to_map() if k else None)
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k in self.passenger_list:
                result['passenger_list'].append(k.to_map() if k else None)
        if self.pay_status is not None:
            result['pay_status'] = self.pay_status
        if self.pay_time is not None:
            result['pay_time'] = self.pay_time
        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price
        if self.real_pay_price is not None:
            result['real_pay_price'] = self.real_pay_price
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k, v in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k] = v.to_map()
        if self.session_nick is not None:
            result['session_nick'] = self.session_nick
        if self.solution is not None:
            result['solution'] = self.solution.to_map()
        if self.succeed_time is not None:
            result['succeed_time'] = self.succeed_time
        if self.total_price is not None:
            result['total_price'] = self.total_price
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ancillary_item_detail_list = []
        if m.get('ancillary_item_detail_list') is not None:
            for k in m.get('ancillary_item_detail_list'):
                temp_model = OrderDetailResponseBodyDataAncillaryItemDetailList()
                self.ancillary_item_detail_list.append(temp_model.from_map(k))
        self.baggage_allowance_map = {}
        if m.get('baggage_allowance_map') is not None:
            for k, v in m.get('baggage_allowance_map').items():
                temp_model = DataBaggageAllowanceMapValue()
                self.baggage_allowance_map[k] = temp_model.from_map(v)
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        self.flight_item_detail_list = []
        if m.get('flight_item_detail_list') is not None:
            for k in m.get('flight_item_detail_list'):
                temp_model = OrderDetailResponseBodyDataFlightItemDetailList()
                self.flight_item_detail_list.append(temp_model.from_map(k))
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k in m.get('passenger_list'):
                temp_model = OrderDetailResponseBodyDataPassengerList()
                self.passenger_list.append(temp_model.from_map(k))
        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')
        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')
        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')
        if m.get('real_pay_price') is not None:
            self.real_pay_price = m.get('real_pay_price')
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k, v in m.get('refund_change_rule_map').items():
                temp_model = DataRefundChangeRuleMapValue()
                self.refund_change_rule_map[k] = temp_model.from_map(v)
        if m.get('session_nick') is not None:
            self.session_nick = m.get('session_nick')
        if m.get('solution') is not None:
            temp_model = OrderDetailResponseBodyDataSolution()
            self.solution = temp_model.from_map(m['solution'])
        if m.get('succeed_time') is not None:
            self.succeed_time = m.get('succeed_time')
        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class OrderDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: OrderDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(OrderDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = OrderDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class OrderDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OrderDetailResponse, self).to_map()
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
            temp_model = OrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class OrderListRequest(TeaModel):
    def __init__(self, book_time_end=None, book_time_start=None, page_index=None, page_size=None, status=None):
        self.book_time_end = book_time_end  # type: long
        self.book_time_start = book_time_start  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_time_end is not None:
            result['book_time_end'] = self.book_time_end
        if self.book_time_start is not None:
            result['book_time_start'] = self.book_time_start
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('book_time_end') is not None:
            self.book_time_end = m.get('book_time_end')
        if m.get('book_time_start') is not None:
            self.book_time_start = m.get('book_time_start')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class OrderListResponseBodyDataListPassengerListCredential(TeaModel):
    def __init__(self, cert_issue_place=None, credential_num=None, credential_type=None, expire_date=None):
        self.cert_issue_place = cert_issue_place  # type: str
        self.credential_num = credential_num  # type: str
        self.credential_type = credential_type  # type: int
        self.expire_date = expire_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderListResponseBodyDataListPassengerListCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place
        if self.credential_num is not None:
            result['credential_num'] = self.credential_num
        if self.credential_type is not None:
            result['credential_type'] = self.credential_type
        if self.expire_date is not None:
            result['expire_date'] = self.expire_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')
        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')
        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')
        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')
        return self


class OrderListResponseBodyDataListPassengerList(TeaModel):
    def __init__(self, birthday=None, credential=None, first_name=None, gender=None, last_name=None,
                 mobile_country_code=None, mobile_phone_number=None, nationality=None, type=None):
        self.birthday = birthday  # type: str
        self.credential = credential  # type: OrderListResponseBodyDataListPassengerListCredential
        self.first_name = first_name  # type: str
        self.gender = gender  # type: int
        self.last_name = last_name  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.mobile_phone_number = mobile_phone_number  # type: str
        self.nationality = nationality  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(OrderListResponseBodyDataListPassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code
        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number
        if self.nationality is not None:
            result['nationality'] = self.nationality
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('credential') is not None:
            temp_model = OrderListResponseBodyDataListPassengerListCredential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')
        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')
        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OrderListResponseBodyDataList(TeaModel):
    def __init__(self, book_time=None, order_num=None, order_status=None, out_order_num=None, passenger_list=None,
                 pay_status=None, pay_time=None, promotion_price=None, real_pay_price=None, session_nick=None,
                 succeed_time=None, total_price=None, transaction_no=None):
        self.book_time = book_time  # type: long
        self.order_num = order_num  # type: long
        self.order_status = order_status  # type: str
        self.out_order_num = out_order_num  # type: str
        self.passenger_list = passenger_list  # type: list[OrderListResponseBodyDataListPassengerList]
        self.pay_status = pay_status  # type: str
        self.pay_time = pay_time  # type: long
        self.promotion_price = promotion_price  # type: float
        self.real_pay_price = real_pay_price  # type: float
        self.session_nick = session_nick  # type: str
        self.succeed_time = succeed_time  # type: long
        self.total_price = total_price  # type: float
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        if self.passenger_list:
            for k in self.passenger_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OrderListResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num
        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k in self.passenger_list:
                result['passenger_list'].append(k.to_map() if k else None)
        if self.pay_status is not None:
            result['pay_status'] = self.pay_status
        if self.pay_time is not None:
            result['pay_time'] = self.pay_time
        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price
        if self.real_pay_price is not None:
            result['real_pay_price'] = self.real_pay_price
        if self.session_nick is not None:
            result['session_nick'] = self.session_nick
        if self.succeed_time is not None:
            result['succeed_time'] = self.succeed_time
        if self.total_price is not None:
            result['total_price'] = self.total_price
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')
        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k in m.get('passenger_list'):
                temp_model = OrderListResponseBodyDataListPassengerList()
                self.passenger_list.append(temp_model.from_map(k))
        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')
        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')
        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')
        if m.get('real_pay_price') is not None:
            self.real_pay_price = m.get('real_pay_price')
        if m.get('session_nick') is not None:
            self.session_nick = m.get('session_nick')
        if m.get('succeed_time') is not None:
            self.succeed_time = m.get('succeed_time')
        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class OrderListResponseBodyDataPagination(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None, total_page=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderListResponseBodyDataPagination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['current_page'] = self.current_page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.total_page is not None:
            result['total_page'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')
        return self


class OrderListResponseBodyData(TeaModel):
    def __init__(self, list=None, pagination=None):
        self.list = list  # type: list[OrderListResponseBodyDataList]
        self.pagination = pagination  # type: OrderListResponseBodyDataPagination

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super(OrderListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = OrderListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pagination') is not None:
            temp_model = OrderListResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['pagination'])
        return self


class OrderListResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: OrderListResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(OrderListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = OrderListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class OrderListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OrderListResponse, self).to_map()
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
            temp_model = OrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PricingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class PricingRequest(TeaModel):
    def __init__(self, solution_id=None):
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class PricingResponseBodyDataChangedPriceInfo(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None):
        self.adult_price = adult_price  # type: float
        self.adult_tax = adult_tax  # type: float
        self.child_price = child_price  # type: float
        self.child_tax = child_tax  # type: float
        self.infant_price = infant_price  # type: float
        self.infant_tax = infant_tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingResponseBodyDataChangedPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        return self


class PricingResponseBodyDataOriginalPriceInfo(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None):
        # 成人单价
        self.adult_price = adult_price  # type: float
        # 成人税
        self.adult_tax = adult_tax  # type: float
        # 儿童单价
        self.child_price = child_price  # type: float
        # 儿童税
        self.child_tax = child_tax  # type: float
        # 婴儿单价
        self.infant_price = infant_price  # type: float
        # 婴儿税
        self.infant_tax = infant_tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingResponseBodyDataOriginalPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        return self


class PricingResponseBodyDataSolutionJourneyListSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingResponseBodyDataSolutionJourneyListSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class PricingResponseBodyDataSolutionJourneyList(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[PricingResponseBodyDataSolutionJourneyListSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PricingResponseBodyDataSolutionJourneyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = PricingResponseBodyDataSolutionJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList(TeaModel):
    def __init__(self, luggage_direct_info_type=None, segment_id_list=None):
        self.luggage_direct_info_type = luggage_direct_info_type  # type: int
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.luggage_direct_info_type is not None:
            result['luggage_direct_info_type'] = self.luggage_direct_info_type
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('luggage_direct_info_type') is not None:
            self.luggage_direct_info_type = m.get('luggage_direct_info_type')
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class PricingResponseBodyDataSolutionSegmentBaggageMappingList(TeaModel):
    def __init__(self, passenger_baggage_allowance_mapping=None, segment_id_list=None):
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping  # type: dict[str, DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.passenger_baggage_allowance_mapping:
            for v in self.passenger_baggage_allowance_mapping.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(PricingResponseBodyDataSolutionSegmentBaggageMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['passenger_baggage_allowance_mapping'] = {}
        if self.passenger_baggage_allowance_mapping is not None:
            for k, v in self.passenger_baggage_allowance_mapping.items():
                result['passenger_baggage_allowance_mapping'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.passenger_baggage_allowance_mapping = {}
        if m.get('passenger_baggage_allowance_mapping') is not None:
            for k, v in m.get('passenger_baggage_allowance_mapping').items():
                temp_model = DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList(TeaModel):
    def __init__(self, refund_change_rule_map=None, segment_id_list=None):
        self.refund_change_rule_map = refund_change_rule_map  # type: dict[str, DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.refund_change_rule_map:
            for v in self.refund_change_rule_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k, v in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k, v in m.get('refund_change_rule_map').items():
                temp_model = DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class PricingResponseBodyDataSolution(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None, journey_list=None, product_type_description=None, refund_ticket_coupon_description=None,
                 segment_baggage_check_in_info_list=None, segment_baggage_mapping_list=None, segment_refund_change_rule_mapping_list=None,
                 solution_id=None):
        self.adult_price = adult_price  # type: float
        self.adult_tax = adult_tax  # type: float
        self.child_price = child_price  # type: float
        self.child_tax = child_tax  # type: float
        self.infant_price = infant_price  # type: float
        self.infant_tax = infant_tax  # type: float
        self.journey_list = journey_list  # type: list[PricingResponseBodyDataSolutionJourneyList]
        self.product_type_description = product_type_description  # type: str
        self.refund_ticket_coupon_description = refund_ticket_coupon_description  # type: str
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list  # type: list[PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList]
        self.segment_baggage_mapping_list = segment_baggage_mapping_list  # type: list[PricingResponseBodyDataSolutionSegmentBaggageMappingList]
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list  # type: list[PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList]
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.journey_list:
            for k in self.journey_list:
                if k:
                    k.validate()
        if self.segment_baggage_check_in_info_list:
            for k in self.segment_baggage_check_in_info_list:
                if k:
                    k.validate()
        if self.segment_baggage_mapping_list:
            for k in self.segment_baggage_mapping_list:
                if k:
                    k.validate()
        if self.segment_refund_change_rule_mapping_list:
            for k in self.segment_refund_change_rule_mapping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PricingResponseBodyDataSolution, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        result['journey_list'] = []
        if self.journey_list is not None:
            for k in self.journey_list:
                result['journey_list'].append(k.to_map() if k else None)
        if self.product_type_description is not None:
            result['product_type_description'] = self.product_type_description
        if self.refund_ticket_coupon_description is not None:
            result['refund_ticket_coupon_description'] = self.refund_ticket_coupon_description
        result['segment_baggage_check_in_info_list'] = []
        if self.segment_baggage_check_in_info_list is not None:
            for k in self.segment_baggage_check_in_info_list:
                result['segment_baggage_check_in_info_list'].append(k.to_map() if k else None)
        result['segment_baggage_mapping_list'] = []
        if self.segment_baggage_mapping_list is not None:
            for k in self.segment_baggage_mapping_list:
                result['segment_baggage_mapping_list'].append(k.to_map() if k else None)
        result['segment_refund_change_rule_mapping_list'] = []
        if self.segment_refund_change_rule_mapping_list is not None:
            for k in self.segment_refund_change_rule_mapping_list:
                result['segment_refund_change_rule_mapping_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        self.journey_list = []
        if m.get('journey_list') is not None:
            for k in m.get('journey_list'):
                temp_model = PricingResponseBodyDataSolutionJourneyList()
                self.journey_list.append(temp_model.from_map(k))
        if m.get('product_type_description') is not None:
            self.product_type_description = m.get('product_type_description')
        if m.get('refund_ticket_coupon_description') is not None:
            self.refund_ticket_coupon_description = m.get('refund_ticket_coupon_description')
        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k in m.get('segment_baggage_check_in_info_list'):
                temp_model = PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k))
        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k in m.get('segment_baggage_mapping_list'):
                temp_model = PricingResponseBodyDataSolutionSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k))
        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class PricingResponseBodyData(TeaModel):
    def __init__(self, changed_price_info=None, is_changed=None, original_price_info=None, remain_seats=None,
                 solution=None):
        self.changed_price_info = changed_price_info  # type: PricingResponseBodyDataChangedPriceInfo
        self.is_changed = is_changed  # type: bool
        # 变价之前价格信息 isChanged = true 时，才有值
        self.original_price_info = original_price_info  # type: PricingResponseBodyDataOriginalPriceInfo
        self.remain_seats = remain_seats  # type: str
        # solution
        self.solution = solution  # type: PricingResponseBodyDataSolution

    def validate(self):
        if self.changed_price_info:
            self.changed_price_info.validate()
        if self.original_price_info:
            self.original_price_info.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        _map = super(PricingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changed_price_info is not None:
            result['changed_price_info'] = self.changed_price_info.to_map()
        if self.is_changed is not None:
            result['is_changed'] = self.is_changed
        if self.original_price_info is not None:
            result['original_price_info'] = self.original_price_info.to_map()
        if self.remain_seats is not None:
            result['remain_seats'] = self.remain_seats
        if self.solution is not None:
            result['solution'] = self.solution.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('changed_price_info') is not None:
            temp_model = PricingResponseBodyDataChangedPriceInfo()
            self.changed_price_info = temp_model.from_map(m['changed_price_info'])
        if m.get('is_changed') is not None:
            self.is_changed = m.get('is_changed')
        if m.get('original_price_info') is not None:
            temp_model = PricingResponseBodyDataOriginalPriceInfo()
            self.original_price_info = temp_model.from_map(m['original_price_info'])
        if m.get('remain_seats') is not None:
            self.remain_seats = m.get('remain_seats')
        if m.get('solution') is not None:
            temp_model = PricingResponseBodyDataSolution()
            self.solution = temp_model.from_map(m['solution'])
        return self


class PricingResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: PricingResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PricingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = PricingResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PricingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PricingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PricingResponse, self).to_map()
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
            temp_model = PricingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundApplyHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class RefundApplyRequestRefundJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, departure_airport=None, departure_city=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyRequestRefundJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        return self


class RefundApplyRequestRefundJourneys(TeaModel):
    def __init__(self, segment_list=None):
        self.segment_list = segment_list  # type: list[RefundApplyRequestRefundJourneysSegmentList]

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundApplyRequestRefundJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = RefundApplyRequestRefundJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        return self


class RefundApplyRequestRefundPassengerList(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyRequestRefundPassengerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class RefundApplyRequestRefundType(TeaModel):
    def __init__(self, file=None, refund_type_id=None, remark=None):
        self.file = file  # type: list[str]
        self.refund_type_id = refund_type_id  # type: int
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyRequestRefundType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file is not None:
            result['file'] = self.file
        if self.refund_type_id is not None:
            result['refund_type_id'] = self.refund_type_id
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('file') is not None:
            self.file = m.get('file')
        if m.get('refund_type_id') is not None:
            self.refund_type_id = m.get('refund_type_id')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class RefundApplyRequest(TeaModel):
    def __init__(self, order_num=None, refund_journeys=None, refund_passenger_list=None, refund_type=None):
        self.order_num = order_num  # type: long
        self.refund_journeys = refund_journeys  # type: list[RefundApplyRequestRefundJourneys]
        self.refund_passenger_list = refund_passenger_list  # type: list[RefundApplyRequestRefundPassengerList]
        self.refund_type = refund_type  # type: RefundApplyRequestRefundType

    def validate(self):
        if self.refund_journeys:
            for k in self.refund_journeys:
                if k:
                    k.validate()
        if self.refund_passenger_list:
            for k in self.refund_passenger_list:
                if k:
                    k.validate()
        if self.refund_type:
            self.refund_type.validate()

    def to_map(self):
        _map = super(RefundApplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        result['refund_journeys'] = []
        if self.refund_journeys is not None:
            for k in self.refund_journeys:
                result['refund_journeys'].append(k.to_map() if k else None)
        result['refund_passenger_list'] = []
        if self.refund_passenger_list is not None:
            for k in self.refund_passenger_list:
                result['refund_passenger_list'].append(k.to_map() if k else None)
        if self.refund_type is not None:
            result['refund_type'] = self.refund_type.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        self.refund_journeys = []
        if m.get('refund_journeys') is not None:
            for k in m.get('refund_journeys'):
                temp_model = RefundApplyRequestRefundJourneys()
                self.refund_journeys.append(temp_model.from_map(k))
        self.refund_passenger_list = []
        if m.get('refund_passenger_list') is not None:
            for k in m.get('refund_passenger_list'):
                temp_model = RefundApplyRequestRefundPassengerList()
                self.refund_passenger_list.append(temp_model.from_map(k))
        if m.get('refund_type') is not None:
            temp_model = RefundApplyRequestRefundType()
            self.refund_type = temp_model.from_map(m['refund_type'])
        return self


class RefundApplyShrinkRequest(TeaModel):
    def __init__(self, order_num=None, refund_journeys_shrink=None, refund_passenger_list_shrink=None,
                 refund_type_shrink=None):
        self.order_num = order_num  # type: long
        self.refund_journeys_shrink = refund_journeys_shrink  # type: str
        self.refund_passenger_list_shrink = refund_passenger_list_shrink  # type: str
        self.refund_type_shrink = refund_type_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.refund_journeys_shrink is not None:
            result['refund_journeys'] = self.refund_journeys_shrink
        if self.refund_passenger_list_shrink is not None:
            result['refund_passenger_list'] = self.refund_passenger_list_shrink
        if self.refund_type_shrink is not None:
            result['refund_type'] = self.refund_type_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('refund_journeys') is not None:
            self.refund_journeys_shrink = m.get('refund_journeys')
        if m.get('refund_passenger_list') is not None:
            self.refund_passenger_list_shrink = m.get('refund_passenger_list')
        if m.get('refund_type') is not None:
            self.refund_type_shrink = m.get('refund_type')
        return self


class RefundApplyResponseBodyDataRefundResultsRefundPassengers(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundApplyResponseBodyDataRefundResultsRefundPassengers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class RefundApplyResponseBodyDataRefundResults(TeaModel):
    def __init__(self, fail_reason=None, refund_order_num=None, refund_passengers=None, status=None):
        self.fail_reason = fail_reason  # type: str
        self.refund_order_num = refund_order_num  # type: long
        self.refund_passengers = refund_passengers  # type: list[RefundApplyResponseBodyDataRefundResultsRefundPassengers]
        self.status = status  # type: int

    def validate(self):
        if self.refund_passengers:
            for k in self.refund_passengers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundApplyResponseBodyDataRefundResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num
        result['refund_passengers'] = []
        if self.refund_passengers is not None:
            for k in self.refund_passengers:
                result['refund_passengers'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')
        self.refund_passengers = []
        if m.get('refund_passengers') is not None:
            for k in m.get('refund_passengers'):
                temp_model = RefundApplyResponseBodyDataRefundResultsRefundPassengers()
                self.refund_passengers.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class RefundApplyResponseBodyData(TeaModel):
    def __init__(self, order_num=None, refund_results=None):
        self.order_num = order_num  # type: long
        self.refund_results = refund_results  # type: list[RefundApplyResponseBodyDataRefundResults]

    def validate(self):
        if self.refund_results:
            for k in self.refund_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundApplyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        result['refund_results'] = []
        if self.refund_results is not None:
            for k in self.refund_results:
                result['refund_results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        self.refund_results = []
        if m.get('refund_results') is not None:
            for k in m.get('refund_results'):
                temp_model = RefundApplyResponseBodyDataRefundResults()
                self.refund_results.append(temp_model.from_map(k))
        return self


class RefundApplyResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        # 请求 RequestId
        self.request_id = request_id  # type: str
        self.data = data  # type: RefundApplyResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefundApplyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = RefundApplyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RefundApplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundApplyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundApplyResponse, self).to_map()
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
            temp_model = RefundApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundDetailHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class RefundDetailRequest(TeaModel):
    def __init__(self, refund_order_num=None):
        self.refund_order_num = refund_order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')
        return self


class RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails(TeaModel):
    def __init__(self, change_order_refund_fee=None, original_order_refund_fee=None, passenger=None):
        self.change_order_refund_fee = change_order_refund_fee  # type: float
        self.original_order_refund_fee = original_order_refund_fee  # type: float
        self.passenger = passenger  # type: RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger

    def validate(self):
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_refund_fee is not None:
            result['change_order_refund_fee'] = self.change_order_refund_fee
        if self.original_order_refund_fee is not None:
            result['original_order_refund_fee'] = self.original_order_refund_fee
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('change_order_refund_fee') is not None:
            self.change_order_refund_fee = m.get('change_order_refund_fee')
        if m.get('original_order_refund_fee') is not None:
            self.original_order_refund_fee = m.get('original_order_refund_fee')
        if m.get('passenger') is not None:
            temp_model = RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        return self


class RefundDetailResponseBodyDataMultiRefundDetails(TeaModel):
    def __init__(self, multi_refund_order_num=None, multi_refund_transaction_no=None,
                 passenger_multi_refund_details=None):
        self.multi_refund_order_num = multi_refund_order_num  # type: long
        self.multi_refund_transaction_no = multi_refund_transaction_no  # type: str
        self.passenger_multi_refund_details = passenger_multi_refund_details  # type: list[RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails]

    def validate(self):
        if self.passenger_multi_refund_details:
            for k in self.passenger_multi_refund_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataMultiRefundDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_refund_order_num is not None:
            result['multi_refund_order_num'] = self.multi_refund_order_num
        if self.multi_refund_transaction_no is not None:
            result['multi_refund_transaction_no'] = self.multi_refund_transaction_no
        result['passenger_multi_refund_details'] = []
        if self.passenger_multi_refund_details is not None:
            for k in self.passenger_multi_refund_details:
                result['passenger_multi_refund_details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('multi_refund_order_num') is not None:
            self.multi_refund_order_num = m.get('multi_refund_order_num')
        if m.get('multi_refund_transaction_no') is not None:
            self.multi_refund_transaction_no = m.get('multi_refund_transaction_no')
        self.passenger_multi_refund_details = []
        if m.get('passenger_multi_refund_details') is not None:
            for k in m.get('passenger_multi_refund_details'):
                temp_model = RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails()
                self.passenger_multi_refund_details.append(temp_model.from_map(k))
        return self


class RefundDetailResponseBodyDataPassengerRefundDetailsPassenger(TeaModel):
    def __init__(self, document=None, first_name=None, last_name=None):
        self.document = document  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataPassengerRefundDetailsPassenger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')
        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')
        return self


class RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee(TeaModel):
    def __init__(self, already_used_total_fee=None, modify_refund_to_buyer_money=None,
                 non_refundable_change_service_fee=None, non_refundable_change_upgrade_fee=None, non_refundable_tax_fee=None,
                 non_refundable_ticket_fee=None, refund_to_buyer_money=None):
        self.already_used_total_fee = already_used_total_fee  # type: float
        self.modify_refund_to_buyer_money = modify_refund_to_buyer_money  # type: float
        self.non_refundable_change_service_fee = non_refundable_change_service_fee  # type: float
        self.non_refundable_change_upgrade_fee = non_refundable_change_upgrade_fee  # type: float
        self.non_refundable_tax_fee = non_refundable_tax_fee  # type: float
        self.non_refundable_ticket_fee = non_refundable_ticket_fee  # type: float
        self.refund_to_buyer_money = refund_to_buyer_money  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_used_total_fee is not None:
            result['already_used_total_fee'] = self.already_used_total_fee
        if self.modify_refund_to_buyer_money is not None:
            result['modify_refund_to_buyer_money'] = self.modify_refund_to_buyer_money
        if self.non_refundable_change_service_fee is not None:
            result['non_refundable_change_service_fee'] = self.non_refundable_change_service_fee
        if self.non_refundable_change_upgrade_fee is not None:
            result['non_refundable_change_upgrade_fee'] = self.non_refundable_change_upgrade_fee
        if self.non_refundable_tax_fee is not None:
            result['non_refundable_tax_fee'] = self.non_refundable_tax_fee
        if self.non_refundable_ticket_fee is not None:
            result['non_refundable_ticket_fee'] = self.non_refundable_ticket_fee
        if self.refund_to_buyer_money is not None:
            result['refund_to_buyer_money'] = self.refund_to_buyer_money
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('already_used_total_fee') is not None:
            self.already_used_total_fee = m.get('already_used_total_fee')
        if m.get('modify_refund_to_buyer_money') is not None:
            self.modify_refund_to_buyer_money = m.get('modify_refund_to_buyer_money')
        if m.get('non_refundable_change_service_fee') is not None:
            self.non_refundable_change_service_fee = m.get('non_refundable_change_service_fee')
        if m.get('non_refundable_change_upgrade_fee') is not None:
            self.non_refundable_change_upgrade_fee = m.get('non_refundable_change_upgrade_fee')
        if m.get('non_refundable_tax_fee') is not None:
            self.non_refundable_tax_fee = m.get('non_refundable_tax_fee')
        if m.get('non_refundable_ticket_fee') is not None:
            self.non_refundable_ticket_fee = m.get('non_refundable_ticket_fee')
        if m.get('refund_to_buyer_money') is not None:
            self.refund_to_buyer_money = m.get('refund_to_buyer_money')
        return self


class RefundDetailResponseBodyDataPassengerRefundDetails(TeaModel):
    def __init__(self, passenger=None, refund_fee=None):
        self.passenger = passenger  # type: RefundDetailResponseBodyDataPassengerRefundDetailsPassenger
        self.refund_fee = refund_fee  # type: RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee

    def validate(self):
        if self.passenger:
            self.passenger.validate()
        if self.refund_fee:
            self.refund_fee.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataPassengerRefundDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('passenger') is not None:
            temp_model = RefundDetailResponseBodyDataPassengerRefundDetailsPassenger()
            self.passenger = temp_model.from_map(m['passenger'])
        if m.get('refund_fee') is not None:
            temp_model = RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee()
            self.refund_fee = temp_model.from_map(m['refund_fee'])
        return self


class RefundDetailResponseBodyDataRefundJourneysSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataRefundJourneysSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class RefundDetailResponseBodyDataRefundJourneys(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[RefundDetailResponseBodyDataRefundJourneysSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBodyDataRefundJourneys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = RefundDetailResponseBodyDataRefundJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class RefundDetailResponseBodyData(TeaModel):
    def __init__(self, contain_multi_refund=None, multi_refund_details=None, order_num=None,
                 passenger_refund_details=None, pay_success_utc_time=None, refund_attachment_urls=None, refund_journeys=None,
                 refund_order_num=None, refund_reason=None, refund_type=None, refuse_reason=None, status=None, transaction_no=None,
                 utc_create_time=None):
        self.contain_multi_refund = contain_multi_refund  # type: bool
        self.multi_refund_details = multi_refund_details  # type: list[RefundDetailResponseBodyDataMultiRefundDetails]
        self.order_num = order_num  # type: long
        self.passenger_refund_details = passenger_refund_details  # type: list[RefundDetailResponseBodyDataPassengerRefundDetails]
        self.pay_success_utc_time = pay_success_utc_time  # type: long
        self.refund_attachment_urls = refund_attachment_urls  # type: list[str]
        self.refund_journeys = refund_journeys  # type: list[RefundDetailResponseBodyDataRefundJourneys]
        self.refund_order_num = refund_order_num  # type: long
        self.refund_reason = refund_reason  # type: str
        self.refund_type = refund_type  # type: int
        self.refuse_reason = refuse_reason  # type: str
        self.status = status  # type: int
        self.transaction_no = transaction_no  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        if self.multi_refund_details:
            for k in self.multi_refund_details:
                if k:
                    k.validate()
        if self.passenger_refund_details:
            for k in self.passenger_refund_details:
                if k:
                    k.validate()
        if self.refund_journeys:
            for k in self.refund_journeys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_multi_refund is not None:
            result['contain_multi_refund'] = self.contain_multi_refund
        result['multi_refund_details'] = []
        if self.multi_refund_details is not None:
            for k in self.multi_refund_details:
                result['multi_refund_details'].append(k.to_map() if k else None)
        if self.order_num is not None:
            result['order_num'] = self.order_num
        result['passenger_refund_details'] = []
        if self.passenger_refund_details is not None:
            for k in self.passenger_refund_details:
                result['passenger_refund_details'].append(k.to_map() if k else None)
        if self.pay_success_utc_time is not None:
            result['pay_success_utc_time'] = self.pay_success_utc_time
        if self.refund_attachment_urls is not None:
            result['refund_attachment_urls'] = self.refund_attachment_urls
        result['refund_journeys'] = []
        if self.refund_journeys is not None:
            for k in self.refund_journeys:
                result['refund_journeys'].append(k.to_map() if k else None)
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num
        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason
        if self.refund_type is not None:
            result['refund_type'] = self.refund_type
        if self.refuse_reason is not None:
            result['refuse_reason'] = self.refuse_reason
        if self.status is not None:
            result['status'] = self.status
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        if self.utc_create_time is not None:
            result['utc_create_time'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('contain_multi_refund') is not None:
            self.contain_multi_refund = m.get('contain_multi_refund')
        self.multi_refund_details = []
        if m.get('multi_refund_details') is not None:
            for k in m.get('multi_refund_details'):
                temp_model = RefundDetailResponseBodyDataMultiRefundDetails()
                self.multi_refund_details.append(temp_model.from_map(k))
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        self.passenger_refund_details = []
        if m.get('passenger_refund_details') is not None:
            for k in m.get('passenger_refund_details'):
                temp_model = RefundDetailResponseBodyDataPassengerRefundDetails()
                self.passenger_refund_details.append(temp_model.from_map(k))
        if m.get('pay_success_utc_time') is not None:
            self.pay_success_utc_time = m.get('pay_success_utc_time')
        if m.get('refund_attachment_urls') is not None:
            self.refund_attachment_urls = m.get('refund_attachment_urls')
        self.refund_journeys = []
        if m.get('refund_journeys') is not None:
            for k in m.get('refund_journeys'):
                temp_model = RefundDetailResponseBodyDataRefundJourneys()
                self.refund_journeys.append(temp_model.from_map(k))
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')
        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')
        if m.get('refund_type') is not None:
            self.refund_type = m.get('refund_type')
        if m.get('refuse_reason') is not None:
            self.refuse_reason = m.get('refuse_reason')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        if m.get('utc_create_time') is not None:
            self.utc_create_time = m.get('utc_create_time')
        return self


class RefundDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: RefundDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefundDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = RefundDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RefundDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundDetailResponse, self).to_map()
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
            temp_model = RefundDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundDetailListHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailListHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class RefundDetailListRequest(TeaModel):
    def __init__(self, order_num=None, page_index=None, page_size=None, refund_create_begin_time=None,
                 refund_create_end_time=None):
        self.order_num = order_num  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.refund_create_begin_time = refund_create_begin_time  # type: long
        self.refund_create_end_time = refund_create_end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.refund_create_begin_time is not None:
            result['refund_create_begin_time'] = self.refund_create_begin_time
        if self.refund_create_end_time is not None:
            result['refund_create_end_time'] = self.refund_create_end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('refund_create_begin_time') is not None:
            self.refund_create_begin_time = m.get('refund_create_begin_time')
        if m.get('refund_create_end_time') is not None:
            self.refund_create_end_time = m.get('refund_create_end_time')
        return self


class RefundDetailListResponseBodyDataList(TeaModel):
    def __init__(self, is_multi_refund=None, order_num=None, refund_order_num=None, refund_order_status=None,
                 related_refund_order_num=None, transaction_no=None, utc_create_time=None):
        self.is_multi_refund = is_multi_refund  # type: bool
        self.order_num = order_num  # type: long
        self.refund_order_num = refund_order_num  # type: long
        self.refund_order_status = refund_order_status  # type: int
        self.related_refund_order_num = related_refund_order_num  # type: str
        self.transaction_no = transaction_no  # type: str
        self.utc_create_time = utc_create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailListResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_multi_refund is not None:
            result['is_multi_refund'] = self.is_multi_refund
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num
        if self.refund_order_status is not None:
            result['refund_order_status'] = self.refund_order_status
        if self.related_refund_order_num is not None:
            result['related_refund_order_num'] = self.related_refund_order_num
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        if self.utc_create_time is not None:
            result['utc_create_time'] = self.utc_create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('is_multi_refund') is not None:
            self.is_multi_refund = m.get('is_multi_refund')
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')
        if m.get('refund_order_status') is not None:
            self.refund_order_status = m.get('refund_order_status')
        if m.get('related_refund_order_num') is not None:
            self.related_refund_order_num = m.get('related_refund_order_num')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        if m.get('utc_create_time') is not None:
            self.utc_create_time = m.get('utc_create_time')
        return self


class RefundDetailListResponseBodyDataPagination(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None, total_page=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundDetailListResponseBodyDataPagination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['current_page'] = self.current_page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.total_page is not None:
            result['total_page'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')
        return self


class RefundDetailListResponseBodyData(TeaModel):
    def __init__(self, list=None, pagination=None):
        self.list = list  # type: list[RefundDetailListResponseBodyDataList]
        self.pagination = pagination  # type: RefundDetailListResponseBodyDataPagination

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        _map = super(RefundDetailListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = RefundDetailListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pagination') is not None:
            temp_model = RefundDetailListResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m['pagination'])
        return self


class RefundDetailListResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: RefundDetailListResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefundDetailListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = RefundDetailListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RefundDetailListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundDetailListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundDetailListResponse, self).to_map()
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
            temp_model = RefundDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class SearchRequestAirLegs(TeaModel):
    def __init__(self, arrival_airport_list=None, arrival_city=None, departure_airport_list=None,
                 departure_city=None, departure_date=None):
        self.arrival_airport_list = arrival_airport_list  # type: list[str]
        self.arrival_city = arrival_city  # type: str
        self.departure_airport_list = departure_airport_list  # type: list[str]
        self.departure_city = departure_city  # type: str
        self.departure_date = departure_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRequestAirLegs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport_list is not None:
            result['arrival_airport_list'] = self.arrival_airport_list
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.departure_airport_list is not None:
            result['departure_airport_list'] = self.departure_airport_list
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_date is not None:
            result['departure_date'] = self.departure_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport_list') is not None:
            self.arrival_airport_list = m.get('arrival_airport_list')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('departure_airport_list') is not None:
            self.departure_airport_list = m.get('departure_airport_list')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')
        return self


class SearchRequest(TeaModel):
    def __init__(self, adults=None, air_legs=None, cabin_class=None, children=None, infants=None):
        self.adults = adults  # type: int
        self.air_legs = air_legs  # type: list[SearchRequestAirLegs]
        self.cabin_class = cabin_class  # type: str
        self.children = children  # type: int
        self.infants = infants  # type: int

    def validate(self):
        if self.air_legs:
            for k in self.air_legs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adults is not None:
            result['adults'] = self.adults
        result['air_legs'] = []
        if self.air_legs is not None:
            for k in self.air_legs:
                result['air_legs'].append(k.to_map() if k else None)
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.children is not None:
            result['children'] = self.children
        if self.infants is not None:
            result['infants'] = self.infants
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')
        self.air_legs = []
        if m.get('air_legs') is not None:
            for k in m.get('air_legs'):
                temp_model = SearchRequestAirLegs()
                self.air_legs.append(temp_model.from_map(k))
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('infants') is not None:
            self.infants = m.get('infants')
        return self


class SearchShrinkRequest(TeaModel):
    def __init__(self, adults=None, air_legs_shrink=None, cabin_class=None, children=None, infants=None):
        self.adults = adults  # type: int
        self.air_legs_shrink = air_legs_shrink  # type: str
        self.cabin_class = cabin_class  # type: str
        self.children = children  # type: int
        self.infants = infants  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adults is not None:
            result['adults'] = self.adults
        if self.air_legs_shrink is not None:
            result['air_legs'] = self.air_legs_shrink
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.children is not None:
            result['children'] = self.children
        if self.infants is not None:
            result['infants'] = self.infants
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adults') is not None:
            self.adults = m.get('adults')
        if m.get('air_legs') is not None:
            self.air_legs_shrink = m.get('air_legs')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('children') is not None:
            self.children = m.get('children')
        if m.get('infants') is not None:
            self.infants = m.get('infants')
        return self


class SearchResponseBodyDataSolutionListJourneyListSegmentList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_city=None, arrival_terminal=None, arrival_time=None,
                 availability=None, cabin=None, cabin_class=None, code_share=None, departure_airport=None, departure_city=None,
                 departure_terminal=None, departure_time=None, equip_type=None, flight_duration=None, marketing_airline=None,
                 marketing_flight_no=None, marketing_flight_no_int=None, operating_airline=None, operating_flight_no=None,
                 segment_id=None, stop_city_list=None, stop_quantity=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_city = arrival_city  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: str
        self.availability = availability  # type: str
        self.cabin = cabin  # type: str
        self.cabin_class = cabin_class  # type: str
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_city = departure_city  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: str
        self.equip_type = equip_type  # type: str
        self.flight_duration = flight_duration  # type: int
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.marketing_flight_no_int = marketing_flight_no_int  # type: int
        self.operating_airline = operating_airline  # type: str
        self.operating_flight_no = operating_flight_no  # type: str
        self.segment_id = segment_id  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.stop_quantity = stop_quantity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionListJourneyListSegmentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.availability is not None:
            result['availability'] = self.availability
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_city is not None:
            result['departure_city'] = self.departure_city
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.equip_type is not None:
            result['equip_type'] = self.equip_type
        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no
        if self.segment_id is not None:
            result['segment_id'] = self.segment_id
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('availability') is not None:
            self.availability = m.get('availability')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')
        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')
        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')
        return self


class SearchResponseBodyDataSolutionListJourneyList(TeaModel):
    def __init__(self, segment_list=None, transfer_count=None):
        self.segment_list = segment_list  # type: list[SearchResponseBodyDataSolutionListJourneyListSegmentList]
        self.transfer_count = transfer_count  # type: int

    def validate(self):
        if self.segment_list:
            for k in self.segment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionListJourneyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['segment_list'] = []
        if self.segment_list is not None:
            for k in self.segment_list:
                result['segment_list'].append(k.to_map() if k else None)
        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k in m.get('segment_list'):
                temp_model = SearchResponseBodyDataSolutionListJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k))
        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')
        return self


class SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList(TeaModel):
    def __init__(self, luggage_direct_info_type=None, segment_id_list=None):
        self.luggage_direct_info_type = luggage_direct_info_type  # type: int
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.luggage_direct_info_type is not None:
            result['luggage_direct_info_type'] = self.luggage_direct_info_type
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('luggage_direct_info_type') is not None:
            self.luggage_direct_info_type = m.get('luggage_direct_info_type')
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class SearchResponseBodyDataSolutionListSegmentBaggageMappingList(TeaModel):
    def __init__(self, passenger_baggage_allowance_mapping=None, segment_id_list=None):
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping  # type: dict[str, DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.passenger_baggage_allowance_mapping:
            for v in self.passenger_baggage_allowance_mapping.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionListSegmentBaggageMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['passenger_baggage_allowance_mapping'] = {}
        if self.passenger_baggage_allowance_mapping is not None:
            for k, v in self.passenger_baggage_allowance_mapping.items():
                result['passenger_baggage_allowance_mapping'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.passenger_baggage_allowance_mapping = {}
        if m.get('passenger_baggage_allowance_mapping') is not None:
            for k, v in m.get('passenger_baggage_allowance_mapping').items():
                temp_model = DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList(TeaModel):
    def __init__(self, refund_change_rule_map=None, segment_id_list=None):
        self.refund_change_rule_map = refund_change_rule_map  # type: dict[str, DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue]
        self.segment_id_list = segment_id_list  # type: list[str]

    def validate(self):
        if self.refund_change_rule_map:
            for v in self.refund_change_rule_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k, v in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k] = v.to_map()
        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k, v in m.get('refund_change_rule_map').items():
                temp_model = DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k] = temp_model.from_map(v)
        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')
        return self


class SearchResponseBodyDataSolutionList(TeaModel):
    def __init__(self, adult_price=None, adult_tax=None, child_price=None, child_tax=None, infant_price=None,
                 infant_tax=None, journey_list=None, product_type_description=None, refund_ticket_coupon_description=None,
                 segment_baggage_check_in_info_list=None, segment_baggage_mapping_list=None, segment_refund_change_rule_mapping_list=None,
                 solution_id=None):
        self.adult_price = adult_price  # type: float
        self.adult_tax = adult_tax  # type: float
        self.child_price = child_price  # type: float
        self.child_tax = child_tax  # type: float
        self.infant_price = infant_price  # type: float
        self.infant_tax = infant_tax  # type: float
        self.journey_list = journey_list  # type: list[SearchResponseBodyDataSolutionListJourneyList]
        self.product_type_description = product_type_description  # type: str
        self.refund_ticket_coupon_description = refund_ticket_coupon_description  # type: str
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list  # type: list[SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList]
        self.segment_baggage_mapping_list = segment_baggage_mapping_list  # type: list[SearchResponseBodyDataSolutionListSegmentBaggageMappingList]
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list  # type: list[SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList]
        # solution_id
        self.solution_id = solution_id  # type: str

    def validate(self):
        if self.journey_list:
            for k in self.journey_list:
                if k:
                    k.validate()
        if self.segment_baggage_check_in_info_list:
            for k in self.segment_baggage_check_in_info_list:
                if k:
                    k.validate()
        if self.segment_baggage_mapping_list:
            for k in self.segment_baggage_mapping_list:
                if k:
                    k.validate()
        if self.segment_refund_change_rule_mapping_list:
            for k in self.segment_refund_change_rule_mapping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchResponseBodyDataSolutionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price
        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax
        if self.child_price is not None:
            result['child_price'] = self.child_price
        if self.child_tax is not None:
            result['child_tax'] = self.child_tax
        if self.infant_price is not None:
            result['infant_price'] = self.infant_price
        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax
        result['journey_list'] = []
        if self.journey_list is not None:
            for k in self.journey_list:
                result['journey_list'].append(k.to_map() if k else None)
        if self.product_type_description is not None:
            result['product_type_description'] = self.product_type_description
        if self.refund_ticket_coupon_description is not None:
            result['refund_ticket_coupon_description'] = self.refund_ticket_coupon_description
        result['segment_baggage_check_in_info_list'] = []
        if self.segment_baggage_check_in_info_list is not None:
            for k in self.segment_baggage_check_in_info_list:
                result['segment_baggage_check_in_info_list'].append(k.to_map() if k else None)
        result['segment_baggage_mapping_list'] = []
        if self.segment_baggage_mapping_list is not None:
            for k in self.segment_baggage_mapping_list:
                result['segment_baggage_mapping_list'].append(k.to_map() if k else None)
        result['segment_refund_change_rule_mapping_list'] = []
        if self.segment_refund_change_rule_mapping_list is not None:
            for k in self.segment_refund_change_rule_mapping_list:
                result['segment_refund_change_rule_mapping_list'].append(k.to_map() if k else None)
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')
        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')
        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')
        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')
        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')
        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')
        self.journey_list = []
        if m.get('journey_list') is not None:
            for k in m.get('journey_list'):
                temp_model = SearchResponseBodyDataSolutionListJourneyList()
                self.journey_list.append(temp_model.from_map(k))
        if m.get('product_type_description') is not None:
            self.product_type_description = m.get('product_type_description')
        if m.get('refund_ticket_coupon_description') is not None:
            self.refund_ticket_coupon_description = m.get('refund_ticket_coupon_description')
        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k in m.get('segment_baggage_check_in_info_list'):
                temp_model = SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k))
        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k in m.get('segment_baggage_mapping_list'):
                temp_model = SearchResponseBodyDataSolutionListSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k))
        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k))
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')
        return self


class SearchResponseBodyData(TeaModel):
    def __init__(self, solution_list=None):
        self.solution_list = solution_list  # type: list[SearchResponseBodyDataSolutionList]

    def validate(self):
        if self.solution_list:
            for k in self.solution_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['solution_list'] = []
        if self.solution_list is not None:
            for k in self.solution_list:
                result['solution_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.solution_list = []
        if m.get('solution_list') is not None:
            for k in m.get('solution_list'):
                temp_model = SearchResponseBodyDataSolutionList()
                self.solution_list.append(temp_model.from_map(k))
        return self


class SearchResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: SearchResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = SearchResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchResponse, self).to_map()
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
            temp_model = SearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TicketingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class TicketingRequest(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class TicketingResponseBodyData(TeaModel):
    def __init__(self, order_num=None, transaction_no=None):
        self.order_num = order_num  # type: long
        self.transaction_no = transaction_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')
        return self


class TicketingResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: TicketingResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TicketingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = TicketingResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class TicketingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TicketingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TicketingResponse, self).to_map()
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
            temp_model = TicketingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TicketingCheckHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingCheckHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class TicketingCheckRequest(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class TicketingCheckResponseBodyData(TeaModel):
    def __init__(self, order_num=None):
        self.order_num = order_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TicketingCheckResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_num is not None:
            result['order_num'] = self.order_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')
        return self


class TicketingCheckResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: TicketingCheckResponseBodyData
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TicketingCheckResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = TicketingCheckResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class TicketingCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TicketingCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TicketingCheckResponse, self).to_map()
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
            temp_model = TicketingCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransitVisaHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_airticket_access_token=None, x_acs_airticket_language=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # access_token
        self.x_acs_airticket_access_token = x_acs_airticket_access_token  # type: str
        self.x_acs_airticket_language = x_acs_airticket_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransitVisaHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['x-acs-airticket-access-token'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['x-acs-airticket-language'] = self.x_acs_airticket_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-airticket-access-token') is not None:
            self.x_acs_airticket_access_token = m.get('x-acs-airticket-access-token')
        if m.get('x-acs-airticket-language') is not None:
            self.x_acs_airticket_language = m.get('x-acs-airticket-language')
        return self


class TransitVisaRequestFlightSegmentParamList(TeaModel):
    def __init__(self, arrival_airport=None, arrival_terminal=None, arrival_time=None, code_share=None,
                 departure_airport=None, departure_terminal=None, departure_time=None, marketing_airline=None,
                 marketing_flight_no=None, operating_airline=None, stop_city_list=None, ticketing_airline=None):
        self.arrival_airport = arrival_airport  # type: str
        self.arrival_terminal = arrival_terminal  # type: str
        self.arrival_time = arrival_time  # type: long
        self.code_share = code_share  # type: bool
        self.departure_airport = departure_airport  # type: str
        self.departure_terminal = departure_terminal  # type: str
        self.departure_time = departure_time  # type: long
        self.marketing_airline = marketing_airline  # type: str
        self.marketing_flight_no = marketing_flight_no  # type: str
        self.operating_airline = operating_airline  # type: str
        self.stop_city_list = stop_city_list  # type: str
        self.ticketing_airline = ticketing_airline  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransitVisaRequestFlightSegmentParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport
        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal
        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time
        if self.code_share is not None:
            result['code_share'] = self.code_share
        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport
        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal
        if self.departure_time is not None:
            result['departure_time'] = self.departure_time
        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline
        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no
        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline
        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list
        if self.ticketing_airline is not None:
            result['ticketing_airline'] = self.ticketing_airline
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')
        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')
        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')
        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')
        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')
        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')
        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')
        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')
        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')
        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')
        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')
        if m.get('ticketing_airline') is not None:
            self.ticketing_airline = m.get('ticketing_airline')
        return self


class TransitVisaRequest(TeaModel):
    def __init__(self, flight_segment_param_list=None):
        self.flight_segment_param_list = flight_segment_param_list  # type: list[TransitVisaRequestFlightSegmentParamList]

    def validate(self):
        if self.flight_segment_param_list:
            for k in self.flight_segment_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TransitVisaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['flight_segment_param_list'] = []
        if self.flight_segment_param_list is not None:
            for k in self.flight_segment_param_list:
                result['flight_segment_param_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flight_segment_param_list = []
        if m.get('flight_segment_param_list') is not None:
            for k in m.get('flight_segment_param_list'):
                temp_model = TransitVisaRequestFlightSegmentParamList()
                self.flight_segment_param_list.append(temp_model.from_map(k))
        return self


class TransitVisaShrinkRequest(TeaModel):
    def __init__(self, flight_segment_param_list_shrink=None):
        self.flight_segment_param_list_shrink = flight_segment_param_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransitVisaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flight_segment_param_list_shrink is not None:
            result['flight_segment_param_list'] = self.flight_segment_param_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flight_segment_param_list') is not None:
            self.flight_segment_param_list_shrink = m.get('flight_segment_param_list')
        return self


class TransitVisaResponseBodyData(TeaModel):
    def __init__(self, city_code=None, visa_type=None):
        self.city_code = city_code  # type: str
        self.visa_type = visa_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransitVisaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.visa_type is not None:
            result['visa_type'] = self.visa_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('visa_type') is not None:
            self.visa_type = m.get('visa_type')
        return self


class TransitVisaResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, error_code=None, error_data=None, error_msg=None, status=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[TransitVisaResponseBodyData]
        self.error_code = error_code  # type: str
        self.error_data = error_data  # type: any
        self.error_msg = error_msg  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TransitVisaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_data is not None:
            result['error_data'] = self.error_data
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = TransitVisaResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class TransitVisaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransitVisaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransitVisaResponse, self).to_map()
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
            temp_model = TransitVisaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


