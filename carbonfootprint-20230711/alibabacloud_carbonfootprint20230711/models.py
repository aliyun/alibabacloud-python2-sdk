# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllowResponseBody, self).to_map()
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


class AllowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllowResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllowResponse, self).to_map()
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
            temp_model = AllowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSummaryDataRequest(TeaModel):
    def __init__(self, end_time=None, group=None, start_time=None, uids=None):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-02-01 23:59:59.
        self.end_time = end_time  # type: str
        # The statistical dimension. A value of productCode specifies that statistics are collected based on cloud service. A value of region specifies that statistics are collected based on region. A value of subUid specifies that statistics are collected based on Resource Access Management (RAM) user. If you do not specify this parameter, statistics are collected based on Alibaba Cloud account.
        self.group = group  # type: str
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-01-01 00:00:00.
        self.start_time = start_time  # type: str
        # The list of Alibaba Cloud account IDs whose data needs to be queried.(used after enabling multi-account management).
        self.uids = uids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSummaryDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uids is not None:
            result['Uids'] = self.uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        return self


class GetSummaryDataShrinkRequest(TeaModel):
    def __init__(self, end_time=None, group=None, start_time=None, uids_shrink=None):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-02-01 23:59:59.
        self.end_time = end_time  # type: str
        # The statistical dimension. A value of productCode specifies that statistics are collected based on cloud service. A value of region specifies that statistics are collected based on region. A value of subUid specifies that statistics are collected based on Resource Access Management (RAM) user. If you do not specify this parameter, statistics are collected based on Alibaba Cloud account.
        self.group = group  # type: str
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-01-01 00:00:00.
        self.start_time = start_time  # type: str
        # The list of Alibaba Cloud account IDs whose data needs to be queried.(used after enabling multi-account management).
        self.uids_shrink = uids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSummaryDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uids_shrink is not None:
            result['Uids'] = self.uids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uids') is not None:
            self.uids_shrink = m.get('Uids')
        return self


class GetSummaryDataResponseBodyData(TeaModel):
    def __init__(self, aircraft_consumption_conversion=None, car_consumption_conversion=None,
                 last_month_consumption_conversion=None, last_year_consumption_conversion=None, last_year_consumption_conversion_sum=None,
                 latest_data_time=None, this_month_consumption_conversion=None, this_year_consumption_conversion=None,
                 total_carbon_consumption_conversion=None, tree_consumption_conversion=None):
        # Converted aircraft carbon emissions.
        self.aircraft_consumption_conversion = aircraft_consumption_conversion  # type: str
        # Converted car carbon emissions.
        self.car_consumption_conversion = car_consumption_conversion  # type: str
        # The carbon emissions in the previous month, in kgCO₂e.
        self.last_month_consumption_conversion = last_month_consumption_conversion  # type: str
        # The carbon emissions in the same month of the previous year, in kgCO₂e.
        self.last_year_consumption_conversion = last_year_consumption_conversion  # type: str
        # The carbon emissions of the previous year, in kgCO₂e.
        self.last_year_consumption_conversion_sum = last_year_consumption_conversion_sum  # type: str
        # The point in time at which the data is last updated.
        self.latest_data_time = latest_data_time  # type: str
        # The carbon emissions in this month, in kgCO₂e.
        self.this_month_consumption_conversion = this_month_consumption_conversion  # type: str
        # The carbon emissions in the year of this month, in kgCO₂e.
        self.this_year_consumption_conversion = this_year_consumption_conversion  # type: str
        # The total carbon emissions within the specified time range, in kgCO₂e.
        self.total_carbon_consumption_conversion = total_carbon_consumption_conversion  # type: str
        # Converted tree carbon absorption.
        self.tree_consumption_conversion = tree_consumption_conversion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSummaryDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aircraft_consumption_conversion is not None:
            result['AircraftConsumptionConversion'] = self.aircraft_consumption_conversion
        if self.car_consumption_conversion is not None:
            result['CarConsumptionConversion'] = self.car_consumption_conversion
        if self.last_month_consumption_conversion is not None:
            result['LastMonthConsumptionConversion'] = self.last_month_consumption_conversion
        if self.last_year_consumption_conversion is not None:
            result['LastYearConsumptionConversion'] = self.last_year_consumption_conversion
        if self.last_year_consumption_conversion_sum is not None:
            result['LastYearConsumptionConversionSum'] = self.last_year_consumption_conversion_sum
        if self.latest_data_time is not None:
            result['LatestDataTime'] = self.latest_data_time
        if self.this_month_consumption_conversion is not None:
            result['ThisMonthConsumptionConversion'] = self.this_month_consumption_conversion
        if self.this_year_consumption_conversion is not None:
            result['ThisYearConsumptionConversion'] = self.this_year_consumption_conversion
        if self.total_carbon_consumption_conversion is not None:
            result['TotalCarbonConsumptionConversion'] = self.total_carbon_consumption_conversion
        if self.tree_consumption_conversion is not None:
            result['TreeConsumptionConversion'] = self.tree_consumption_conversion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AircraftConsumptionConversion') is not None:
            self.aircraft_consumption_conversion = m.get('AircraftConsumptionConversion')
        if m.get('CarConsumptionConversion') is not None:
            self.car_consumption_conversion = m.get('CarConsumptionConversion')
        if m.get('LastMonthConsumptionConversion') is not None:
            self.last_month_consumption_conversion = m.get('LastMonthConsumptionConversion')
        if m.get('LastYearConsumptionConversion') is not None:
            self.last_year_consumption_conversion = m.get('LastYearConsumptionConversion')
        if m.get('LastYearConsumptionConversionSum') is not None:
            self.last_year_consumption_conversion_sum = m.get('LastYearConsumptionConversionSum')
        if m.get('LatestDataTime') is not None:
            self.latest_data_time = m.get('LatestDataTime')
        if m.get('ThisMonthConsumptionConversion') is not None:
            self.this_month_consumption_conversion = m.get('ThisMonthConsumptionConversion')
        if m.get('ThisYearConsumptionConversion') is not None:
            self.this_year_consumption_conversion = m.get('ThisYearConsumptionConversion')
        if m.get('TotalCarbonConsumptionConversion') is not None:
            self.total_carbon_consumption_conversion = m.get('TotalCarbonConsumptionConversion')
        if m.get('TreeConsumptionConversion') is not None:
            self.tree_consumption_conversion = m.get('TreeConsumptionConversion')
        return self


class GetSummaryDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: GetSummaryDataResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSummaryDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSummaryDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSummaryDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSummaryDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSummaryDataResponse, self).to_map()
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
            temp_model = GetSummaryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCarbonTrackRequest(TeaModel):
    def __init__(self, end_time=None, filter_rdaccount=None, group=None, start_time=None, top_num=None, uids=None,
                 use_code=None):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-02-01 23:59:59.
        self.end_time = end_time  # type: str
        # Whether to count the carbon emission details of multiple accounts. You can pass it in after opening the multi-account management. The default value and 0 is No and 1 is Yes.
        self.filter_rdaccount = filter_rdaccount  # type: int
        # The statistical dimension. A value of productCode specifies that statistics are collected based on cloud service. A value of region specifies that statistics are collected based on region. A value of subUid specifies that statistics are collected based on Resource Access Management (RAM) user. If you do not specify this parameter, statistics are collected based on Alibaba Cloud account.
        self.group = group  # type: str
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-01-01 00:00:00.
        self.start_time = start_time  # type: str
        # After sorting in reverse order according to the data value of the return value, only the first TopNum data will be returned. If no data is passed, all data will be returned by default.
        self.top_num = top_num  # type: int
        # The list of Alibaba Cloud account IDs whose data needs to be queried.(used after enabling multi-account management).
        self.uids = uids  # type: list[str]
        # Whether the return result uses code as the identifier(0 meas not used and 1 means used). If not passed, the default code is used.
        # 
        # For example, when the return result is to summarize carbon emissions according to the cloud product dimension, the identifier of ECS is "ecs" when 0 is passed, and "Elastic Compute Service" when 1 is passed.
        self.use_code = use_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCarbonTrackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_rdaccount is not None:
            result['FilterRDAccount'] = self.filter_rdaccount
        if self.group is not None:
            result['Group'] = self.group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_num is not None:
            result['TopNum'] = self.top_num
        if self.uids is not None:
            result['Uids'] = self.uids
        if self.use_code is not None:
            result['UseCode'] = self.use_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterRDAccount') is not None:
            self.filter_rdaccount = m.get('FilterRDAccount')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopNum') is not None:
            self.top_num = m.get('TopNum')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        if m.get('UseCode') is not None:
            self.use_code = m.get('UseCode')
        return self


class QueryCarbonTrackShrinkRequest(TeaModel):
    def __init__(self, end_time=None, filter_rdaccount=None, group=None, start_time=None, top_num=None,
                 uids_shrink=None, use_code=None):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-02-01 23:59:59.
        self.end_time = end_time  # type: str
        # Whether to count the carbon emission details of multiple accounts. You can pass it in after opening the multi-account management. The default value and 0 is No and 1 is Yes.
        self.filter_rdaccount = filter_rdaccount  # type: int
        # The statistical dimension. A value of productCode specifies that statistics are collected based on cloud service. A value of region specifies that statistics are collected based on region. A value of subUid specifies that statistics are collected based on Resource Access Management (RAM) user. If you do not specify this parameter, statistics are collected based on Alibaba Cloud account.
        self.group = group  # type: str
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. Example: 2023-01-01 00:00:00.
        self.start_time = start_time  # type: str
        # After sorting in reverse order according to the data value of the return value, only the first TopNum data will be returned. If no data is passed, all data will be returned by default.
        self.top_num = top_num  # type: int
        # The list of Alibaba Cloud account IDs whose data needs to be queried.(used after enabling multi-account management).
        self.uids_shrink = uids_shrink  # type: str
        # Whether the return result uses code as the identifier(0 meas not used and 1 means used). If not passed, the default code is used.
        # 
        # For example, when the return result is to summarize carbon emissions according to the cloud product dimension, the identifier of ECS is "ecs" when 0 is passed, and "Elastic Compute Service" when 1 is passed.
        self.use_code = use_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCarbonTrackShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_rdaccount is not None:
            result['FilterRDAccount'] = self.filter_rdaccount
        if self.group is not None:
            result['Group'] = self.group
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_num is not None:
            result['TopNum'] = self.top_num
        if self.uids_shrink is not None:
            result['Uids'] = self.uids_shrink
        if self.use_code is not None:
            result['UseCode'] = self.use_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterRDAccount') is not None:
            self.filter_rdaccount = m.get('FilterRDAccount')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopNum') is not None:
            self.top_num = m.get('TopNum')
        if m.get('Uids') is not None:
            self.uids_shrink = m.get('Uids')
        if m.get('UseCode') is not None:
            self.use_code = m.get('UseCode')
        return self


class QueryCarbonTrackResponseBodyData(TeaModel):
    def __init__(self, product_code=None, quota_value=None, region=None, statistics_date=None, sub_uid=None,
                 uid=None):
        # The service code.
        self.product_code = product_code  # type: str
        # The carbon emissions within the specified time range, in kgCO₂e.
        self.quota_value = quota_value  # type: float
        # The region in which the cloud service resides.
        self.region = region  # type: str
        # The date when the statistics are collected, which is a timestamp in milliseconds.
        self.statistics_date = statistics_date  # type: long
        # The ID of the RAM user.
        self.sub_uid = sub_uid  # type: str
        # The ID of the Alibaba Cloud account.
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCarbonTrackResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.region is not None:
            result['Region'] = self.region
        if self.statistics_date is not None:
            result['StatisticsDate'] = self.statistics_date
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StatisticsDate') is not None:
            self.statistics_date = m.get('StatisticsDate')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryCarbonTrackResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The data records.
        self.data = data  # type: list[QueryCarbonTrackResponseBodyData]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCarbonTrackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCarbonTrackResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCarbonTrackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCarbonTrackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCarbonTrackResponse, self).to_map()
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
            temp_model = QueryCarbonTrackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMultiAccountCarbonTrackRequest(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMultiAccountCarbonTrackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMultiAccountCarbonTrackResponseBodyData(TeaModel):
    def __init__(self, carbon_actual_emission=None, month=None, product_code=None, region=None, uid=None):
        self.carbon_actual_emission = carbon_actual_emission  # type: str
        self.month = month  # type: str
        self.product_code = product_code  # type: str
        self.region = region  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMultiAccountCarbonTrackResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_actual_emission is not None:
            result['CarbonActualEmission'] = self.carbon_actual_emission
        if self.month is not None:
            result['Month'] = self.month
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region is not None:
            result['Region'] = self.region
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CarbonActualEmission') is not None:
            self.carbon_actual_emission = m.get('CarbonActualEmission')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryMultiAccountCarbonTrackResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[QueryMultiAccountCarbonTrackResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMultiAccountCarbonTrackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryMultiAccountCarbonTrackResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMultiAccountCarbonTrackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMultiAccountCarbonTrackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMultiAccountCarbonTrackResponse, self).to_map()
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
            temp_model = QueryMultiAccountCarbonTrackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyResponseBodyDataAllMultiAccountUids(TeaModel):
    def __init__(self, account_id=None, display_name=None):
        self.account_id = account_id  # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyResponseBodyDataAllMultiAccountUids, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class VerifyResponseBodyData(TeaModel):
    def __init__(self, allowed_uids=None, account_type=None, all_multi_account_uids=None, code=None, message=None,
                 multi_accounts_allow=None):
        self.allowed_uids = allowed_uids  # type: list[str]
        self.account_type = account_type  # type: int
        self.all_multi_account_uids = all_multi_account_uids  # type: list[VerifyResponseBodyDataAllMultiAccountUids]
        self.code = code  # type: str
        self.message = message  # type: str
        self.multi_accounts_allow = multi_accounts_allow  # type: int

    def validate(self):
        if self.all_multi_account_uids:
            for k in self.all_multi_account_uids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_uids is not None:
            result['AllowedUids'] = self.allowed_uids
        if self.account_type is not None:
            result['accountType'] = self.account_type
        result['allMultiAccountUids'] = []
        if self.all_multi_account_uids is not None:
            for k in self.all_multi_account_uids:
                result['allMultiAccountUids'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.multi_accounts_allow is not None:
            result['multiAccountsAllow'] = self.multi_accounts_allow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedUids') is not None:
            self.allowed_uids = m.get('AllowedUids')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        self.all_multi_account_uids = []
        if m.get('allMultiAccountUids') is not None:
            for k in m.get('allMultiAccountUids'):
                temp_model = VerifyResponseBodyDataAllMultiAccountUids()
                self.all_multi_account_uids.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('multiAccountsAllow') is not None:
            self.multi_accounts_allow = m.get('multiAccountsAllow')
        return self


class VerifyResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: VerifyResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = VerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyResponse, self).to_map()
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
            temp_model = VerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


