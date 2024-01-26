# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetReportRequest(TeaModel):
    def __init__(self, report_id=None):
        self.report_id = report_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetReportResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, snapshot=None, success=None, summary=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.snapshot = snapshot  # type: str
        self.success = success  # type: bool
        self.summary = summary  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.success is not None:
            result['Success'] = self.success
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReportResponse, self).to_map()
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
            temp_model = GetReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunnableScenesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRunnableScenesRequest, self).to_map()
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


class ListRunnableScenesResponseBodyScenesScene(TeaModel):
    def __init__(self, duration=None, modified_time=None, scene_id=None, scene_name=None):
        self.duration = duration  # type: int
        self.modified_time = modified_time  # type: long
        self.scene_id = scene_id  # type: long
        self.scene_name = scene_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRunnableScenesResponseBodyScenesScene, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ListRunnableScenesResponseBodyScenes(TeaModel):
    def __init__(self, scene=None):
        self.scene = scene  # type: list[ListRunnableScenesResponseBodyScenesScene]

    def validate(self):
        if self.scene:
            for k in self.scene:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRunnableScenesResponseBodyScenes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Scene'] = []
        if self.scene is not None:
            for k in self.scene:
                result['Scene'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.scene = []
        if m.get('Scene') is not None:
            for k in m.get('Scene'):
                temp_model = ListRunnableScenesResponseBodyScenesScene()
                self.scene.append(temp_model.from_map(k))
        return self


class ListRunnableScenesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, page_number=None, page_size=None, request_id=None, scenes=None,
                 success=None, total_count=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.scenes = scenes  # type: ListRunnableScenesResponseBodyScenes
        self.success = success  # type: bool
        self.total_count = total_count  # type: long

    def validate(self):
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        _map = super(ListRunnableScenesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scenes') is not None:
            temp_model = ListRunnableScenesResponseBodyScenes()
            self.scenes = temp_model.from_map(m['Scenes'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRunnableScenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRunnableScenesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRunnableScenesResponse, self).to_map()
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
            temp_model = ListRunnableScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPlanStatusRequest(TeaModel):
    def __init__(self, report_id=None, scene_id=None):
        self.report_id = report_id  # type: long
        self.scene_id = scene_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPlanStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class QueryPlanStatusResponseBodyAgentLocations(TeaModel):
    def __init__(self, agent_location=None):
        self.agent_location = agent_location  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPlanStatusResponseBodyAgentLocations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_location is not None:
            result['AgentLocation'] = self.agent_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentLocation') is not None:
            self.agent_location = m.get('AgentLocation')
        return self


class QueryPlanStatusResponseBodyMonitorData(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPlanStatusResponseBodyMonitorData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryPlanStatusResponseBody(TeaModel):
    def __init__(self, agent_locations=None, alive_agent_count=None, average_rt=None, bps_request=None,
                 bps_response=None, code=None, concurrency=None, concurrency_limit=None, current_time=None,
                 failed_business_count=None, failed_request_count=None, message=None, monitor_data=None, report_id=None,
                 request_count=None, request_id=None, seg_90rt=None, start_time=None, success=None, tips=None,
                 total_agent_count=None, tps=None, tps_limit=None, vum=None):
        self.agent_locations = agent_locations  # type: QueryPlanStatusResponseBodyAgentLocations
        self.alive_agent_count = alive_agent_count  # type: int
        self.average_rt = average_rt  # type: int
        self.bps_request = bps_request  # type: str
        self.bps_response = bps_response  # type: str
        self.code = code  # type: str
        self.concurrency = concurrency  # type: int
        self.concurrency_limit = concurrency_limit  # type: int
        self.current_time = current_time  # type: long
        self.failed_business_count = failed_business_count  # type: int
        self.failed_request_count = failed_request_count  # type: int
        self.message = message  # type: str
        self.monitor_data = monitor_data  # type: QueryPlanStatusResponseBodyMonitorData
        self.report_id = report_id  # type: long
        self.request_count = request_count  # type: str
        self.request_id = request_id  # type: str
        self.seg_90rt = seg_90rt  # type: int
        self.start_time = start_time  # type: long
        self.success = success  # type: bool
        self.tips = tips  # type: str
        self.total_agent_count = total_agent_count  # type: int
        self.tps = tps  # type: int
        self.tps_limit = tps_limit  # type: int
        self.vum = vum  # type: int

    def validate(self):
        if self.agent_locations:
            self.agent_locations.validate()
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        _map = super(QueryPlanStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_locations is not None:
            result['AgentLocations'] = self.agent_locations.to_map()
        if self.alive_agent_count is not None:
            result['AliveAgentCount'] = self.alive_agent_count
        if self.average_rt is not None:
            result['AverageRt'] = self.average_rt
        if self.bps_request is not None:
            result['BpsRequest'] = self.bps_request
        if self.bps_response is not None:
            result['BpsResponse'] = self.bps_response
        if self.code is not None:
            result['Code'] = self.code
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.concurrency_limit is not None:
            result['ConcurrencyLimit'] = self.concurrency_limit
        if self.current_time is not None:
            result['CurrentTime'] = self.current_time
        if self.failed_business_count is not None:
            result['FailedBusinessCount'] = self.failed_business_count
        if self.failed_request_count is not None:
            result['FailedRequestCount'] = self.failed_request_count
        if self.message is not None:
            result['Message'] = self.message
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.success is not None:
            result['Success'] = self.success
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_agent_count is not None:
            result['TotalAgentCount'] = self.total_agent_count
        if self.tps is not None:
            result['Tps'] = self.tps
        if self.tps_limit is not None:
            result['TpsLimit'] = self.tps_limit
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentLocations') is not None:
            temp_model = QueryPlanStatusResponseBodyAgentLocations()
            self.agent_locations = temp_model.from_map(m['AgentLocations'])
        if m.get('AliveAgentCount') is not None:
            self.alive_agent_count = m.get('AliveAgentCount')
        if m.get('AverageRt') is not None:
            self.average_rt = m.get('AverageRt')
        if m.get('BpsRequest') is not None:
            self.bps_request = m.get('BpsRequest')
        if m.get('BpsResponse') is not None:
            self.bps_response = m.get('BpsResponse')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        if m.get('CurrentTime') is not None:
            self.current_time = m.get('CurrentTime')
        if m.get('FailedBusinessCount') is not None:
            self.failed_business_count = m.get('FailedBusinessCount')
        if m.get('FailedRequestCount') is not None:
            self.failed_request_count = m.get('FailedRequestCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MonitorData') is not None:
            temp_model = QueryPlanStatusResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalAgentCount') is not None:
            self.total_agent_count = m.get('TotalAgentCount')
        if m.get('Tps') is not None:
            self.tps = m.get('Tps')
        if m.get('TpsLimit') is not None:
            self.tps_limit = m.get('TpsLimit')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class QueryPlanStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPlanStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPlanStatusResponse, self).to_map()
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
            temp_model = QueryPlanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSceneRequest(TeaModel):
    def __init__(self, scene_id=None):
        self.scene_id = scene_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StartSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, report_id=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.report_id = report_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.report_id is not None:
            result['ReportId'] = self.report_id
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
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartSceneResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartSceneResponse, self).to_map()
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
            temp_model = StartSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSceneRequest(TeaModel):
    def __init__(self, scene_id=None):
        self.scene_id = scene_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StopSceneResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSceneResponseBody, self).to_map()
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


class StopSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopSceneResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopSceneResponse, self).to_map()
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
            temp_model = StopSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


