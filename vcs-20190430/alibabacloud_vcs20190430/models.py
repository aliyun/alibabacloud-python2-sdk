# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateComputeTaskRequest(TeaModel):
    def __init__(self, algorithm_code_list=None, device_code_list=None, project_id=None, region_id=None,
                 task_name=None, vcs_id=None):
        self.algorithm_code_list = algorithm_code_list  # type: str
        self.device_code_list = device_code_list  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.task_name = task_name  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_code_list is not None:
            result['AlgorithmCodeList'] = self.algorithm_code_list
        if self.device_code_list is not None:
            result['DeviceCodeList'] = self.device_code_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmCodeList') is not None:
            self.algorithm_code_list = m.get('AlgorithmCodeList')
        if m.get('DeviceCodeList') is not None:
            self.device_code_list = m.get('DeviceCodeList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class CreateComputeTaskResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateComputeTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateComputeTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateComputeTaskResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateComputeTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateComputeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateComputeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateComputeTaskResponse, self).to_map()
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
            temp_model = CreateComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, area_code=None, project_name=None, region_id=None, time_zone_code=None, vcs_id=None):
        self.area_code = area_code  # type: str
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.time_zone_code = time_zone_code  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.time_zone_code is not None:
            result['TimeZoneCode'] = self.time_zone_code
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TimeZoneCode') is not None:
            self.time_zone_code = m.get('TimeZoneCode')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateProjectResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComputeTasksRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, project_id=None, region_id=None, search_key=None, vcs_id=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.search_key = search_key  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComputeTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeComputeTasksResponseBodyData(TeaModel):
    def __init__(self, algorithm_name=None, device_num=None, image_size=None, runtime=None, structured_size=None,
                 task_id=None, task_name=None, task_status=None, vector_size=None):
        self.algorithm_name = algorithm_name  # type: str
        self.device_num = device_num  # type: int
        self.image_size = image_size  # type: float
        self.runtime = runtime  # type: str
        self.structured_size = structured_size  # type: float
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: str
        self.vector_size = vector_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComputeTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeComputeTasksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeComputeTasksResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeComputeTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeComputeTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeComputeTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeComputeTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComputeTasksResponse, self).to_map()
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
            temp_model = DescribeComputeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(self, filter_key=None, page_num=None, page_size=None, project_id=None, region_id=None,
                 search_key=None, vcs_id=None):
        self.filter_key = filter_key  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.search_key = search_key  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeDevicesResponseBodyData(TeaModel):
    def __init__(self, device_code=None, device_id=None, device_name=None, device_type=None, frame_rate=None,
                 image_size=None, location=None, owner=None, pull_stream_status=None, real_time_data_rate=None,
                 structured_size=None, vector_size=None):
        self.device_code = device_code  # type: str
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.frame_rate = frame_rate  # type: str
        self.image_size = image_size  # type: float
        self.location = location  # type: str
        self.owner = owner  # type: str
        self.pull_stream_status = pull_stream_status  # type: str
        self.real_time_data_rate = real_time_data_rate  # type: str
        self.structured_size = structured_size  # type: float
        self.vector_size = vector_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.location is not None:
            result['Location'] = self.location
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.pull_stream_status is not None:
            result['PullStreamStatus'] = self.pull_stream_status
        if self.real_time_data_rate is not None:
            result['RealTimeDataRate'] = self.real_time_data_rate
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PullStreamStatus') is not None:
            self.pull_stream_status = m.get('PullStreamStatus')
        if m.get('RealTimeDataRate') is not None:
            self.real_time_data_rate = m.get('RealTimeDataRate')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeDevicesResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDevicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponse, self).to_map()
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
            temp_model = DescribeDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, project_name=None, region_id=None, vcs_id=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class DescribeProjectsResponseBodyData(TeaModel):
    def __init__(self, algorithm_name=None, gb_id=None, gb_ip=None, gb_port=None, image_size=None,
                 package_pattern=None, project_code=None, project_id=None, project_name=None, protocol=None, status=None,
                 structured_size=None, vector_size=None):
        self.algorithm_name = algorithm_name  # type: str
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.gb_port = gb_port  # type: str
        self.image_size = image_size  # type: float
        self.package_pattern = package_pattern  # type: str
        self.project_code = project_code  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.structured_size = structured_size  # type: float
        self.vector_size = vector_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.package_pattern is not None:
            result['PackagePattern'] = self.package_pattern
        if self.project_code is not None:
            result['ProjectCode'] = self.project_code
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.structured_size is not None:
            result['StructuredSize'] = self.structured_size
        if self.vector_size is not None:
            result['VectorSize'] = self.vector_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('PackagePattern') is not None:
            self.package_pattern = m.get('PackagePattern')
        if m.get('ProjectCode') is not None:
            self.project_code = m.get('ProjectCode')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructuredSize') is not None:
            self.structured_size = m.get('StructuredSize')
        if m.get('VectorSize') is not None:
            self.vector_size = m.get('VectorSize')
        return self


class DescribeProjectsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, total_count=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeProjectsResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProjectsResponse, self).to_map()
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
            temp_model = DescribeProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureSearchResultsRequest(TeaModel):
    def __init__(self, algorithm_type=None, begin_time=None, device_list=None, end_time=None, page_num=None,
                 picture_contents=None, region_id=None, top_num=None, vcs_id=None):
        self.algorithm_type = algorithm_type  # type: str
        self.begin_time = begin_time  # type: str
        self.device_list = device_list  # type: str
        self.end_time = end_time  # type: str
        self.page_num = page_num  # type: int
        self.picture_contents = picture_contents  # type: str
        self.region_id = region_id  # type: str
        self.top_num = top_num  # type: int
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPictureSearchResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.picture_contents is not None:
            result['PictureContents'] = self.picture_contents
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.top_num is not None:
            result['TopNum'] = self.top_num
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PictureContents') is not None:
            self.picture_contents = m.get('PictureContents')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopNum') is not None:
            self.top_num = m.get('TopNum')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class GetPictureSearchResultsResponseBodyData(TeaModel):
    def __init__(self, device_id=None, left_upper_corner_xcoordinate=None, left_upper_corner_ycoordinate=None,
                 location_mark_time=None, picture_id_1=None, picture_id_2=None, picture_url_1=None, picture_url_2=None,
                 right_lower_corner_xcoordinate=None, right_lower_corner_ycoordinate=None, similarity=None):
        self.device_id = device_id  # type: str
        self.left_upper_corner_xcoordinate = left_upper_corner_xcoordinate  # type: str
        self.left_upper_corner_ycoordinate = left_upper_corner_ycoordinate  # type: str
        self.location_mark_time = location_mark_time  # type: str
        self.picture_id_1 = picture_id_1  # type: str
        self.picture_id_2 = picture_id_2  # type: str
        self.picture_url_1 = picture_url_1  # type: str
        self.picture_url_2 = picture_url_2  # type: str
        self.right_lower_corner_xcoordinate = right_lower_corner_xcoordinate  # type: str
        self.right_lower_corner_ycoordinate = right_lower_corner_ycoordinate  # type: str
        self.similarity = similarity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPictureSearchResultsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.left_upper_corner_xcoordinate is not None:
            result['LeftUpperCornerXCoordinate'] = self.left_upper_corner_xcoordinate
        if self.left_upper_corner_ycoordinate is not None:
            result['LeftUpperCornerYCoordinate'] = self.left_upper_corner_ycoordinate
        if self.location_mark_time is not None:
            result['LocationMarkTime'] = self.location_mark_time
        if self.picture_id_1 is not None:
            result['PictureId1'] = self.picture_id_1
        if self.picture_id_2 is not None:
            result['PictureId2'] = self.picture_id_2
        if self.picture_url_1 is not None:
            result['PictureUrl1'] = self.picture_url_1
        if self.picture_url_2 is not None:
            result['PictureUrl2'] = self.picture_url_2
        if self.right_lower_corner_xcoordinate is not None:
            result['RightLowerCornerXCoordinate'] = self.right_lower_corner_xcoordinate
        if self.right_lower_corner_ycoordinate is not None:
            result['RightLowerCornerYCoordinate'] = self.right_lower_corner_ycoordinate
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('LeftUpperCornerXCoordinate') is not None:
            self.left_upper_corner_xcoordinate = m.get('LeftUpperCornerXCoordinate')
        if m.get('LeftUpperCornerYCoordinate') is not None:
            self.left_upper_corner_ycoordinate = m.get('LeftUpperCornerYCoordinate')
        if m.get('LocationMarkTime') is not None:
            self.location_mark_time = m.get('LocationMarkTime')
        if m.get('PictureId1') is not None:
            self.picture_id_1 = m.get('PictureId1')
        if m.get('PictureId2') is not None:
            self.picture_id_2 = m.get('PictureId2')
        if m.get('PictureUrl1') is not None:
            self.picture_url_1 = m.get('PictureUrl1')
        if m.get('PictureUrl2') is not None:
            self.picture_url_2 = m.get('PictureUrl2')
        if m.get('RightLowerCornerXCoordinate') is not None:
            self.right_lower_corner_xcoordinate = m.get('RightLowerCornerXCoordinate')
        if m.get('RightLowerCornerYCoordinate') is not None:
            self.right_lower_corner_ycoordinate = m.get('RightLowerCornerYCoordinate')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class GetPictureSearchResultsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetPictureSearchResultsResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPictureSearchResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetPictureSearchResultsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPictureSearchResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPictureSearchResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPictureSearchResultsResponse, self).to_map()
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
            temp_model = GetPictureSearchResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportDevicesRequest(TeaModel):
    def __init__(self, device_list=None, project_id=None, region_id=None, vcs_id=None):
        self.device_list = device_list  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.vcs_id = vcs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcs_id is not None:
            result['VcsId'] = self.vcs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VcsId') is not None:
            self.vcs_id = m.get('VcsId')
        return self


class ImportDevicesResponseBodyDataFailure(TeaModel):
    def __init__(self, device_code=None, device_id=None):
        self.device_code = device_code  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportDevicesResponseBodyDataFailure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ImportDevicesResponseBodyDataSuccess(TeaModel):
    def __init__(self, device_code=None, device_id=None):
        self.device_code = device_code  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportDevicesResponseBodyDataSuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ImportDevicesResponseBodyData(TeaModel):
    def __init__(self, failure=None, success=None):
        self.failure = failure  # type: list[ImportDevicesResponseBodyDataFailure]
        self.success = success  # type: list[ImportDevicesResponseBodyDataSuccess]

    def validate(self):
        if self.failure:
            for k in self.failure:
                if k:
                    k.validate()
        if self.success:
            for k in self.success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportDevicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Failure'] = []
        if self.failure is not None:
            for k in self.failure:
                result['Failure'].append(k.to_map() if k else None)
        result['Success'] = []
        if self.success is not None:
            for k in self.success:
                result['Success'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failure = []
        if m.get('Failure') is not None:
            for k in m.get('Failure'):
                temp_model = ImportDevicesResponseBodyDataFailure()
                self.failure.append(temp_model.from_map(k))
        self.success = []
        if m.get('Success') is not None:
            for k in m.get('Success'):
                temp_model = ImportDevicesResponseBodyDataSuccess()
                self.success.append(temp_model.from_map(k))
        return self


class ImportDevicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ImportDevicesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImportDevicesResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImportDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportDevicesResponse, self).to_map()
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
            temp_model = ImportDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


