# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetAliwareReportRequest(TeaModel):
    def __init__(self, report_id=None):
        self.report_id = report_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAliwareReportRequest, self).to_map()
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


class GetAliwareReportResponseBody(TeaModel):
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
        _map = super(GetAliwareReportResponseBody, self).to_map()
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


class GetAliwareReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAliwareReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAliwareReportResponse, self).to_map()
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
            temp_model = GetAliwareReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class StartSceneRequest(TeaModel):
    def __init__(self, scene_id=None, task_id=None, team_id=None, user_id=None):
        self.scene_id = scene_id  # type: long
        self.task_id = task_id  # type: long
        self.team_id = team_id  # type: long
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.team_id is not None:
            result['TeamId'] = self.team_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TeamId') is not None:
            self.team_id = m.get('TeamId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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


