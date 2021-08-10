# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ListSmartJobsRequest(TeaModel):
    def __init__(self, status=None, next_token=None, max_results=None, page_no=None, page_size=None, job_type=None,
                 sort_by=None, job_state=None):
        self.status = status  # type: long
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.job_type = job_type  # type: str
        self.sort_by = sort_by  # type: str
        self.job_state = job_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.job_state is not None:
            result['JobState'] = self.job_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        return self


class ListSmartJobsResponseBodySmartJobListInputConfig(TeaModel):
    def __init__(self, input_file=None, keyword=None):
        self.input_file = input_file  # type: str
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobListInputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListSmartJobsResponseBodySmartJobListOutputConfig(TeaModel):
    def __init__(self, bucket=None, object=None):
        self.bucket = bucket  # type: str
        self.object = object  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobListOutputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class ListSmartJobsResponseBodySmartJobList(TeaModel):
    def __init__(self, job_id=None, title=None, description=None, user_id=None, job_type=None, editing_config=None,
                 user_data=None, job_state=None, create_time=None, modified_time=None, input_config=None, output_config=None):
        self.job_id = job_id  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        self.user_id = user_id  # type: long
        self.job_type = job_type  # type: str
        self.editing_config = editing_config  # type: str
        self.user_data = user_data  # type: str
        self.job_state = job_state  # type: str
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.input_config = input_config  # type: ListSmartJobsResponseBodySmartJobListInputConfig
        self.output_config = output_config  # type: ListSmartJobsResponseBodySmartJobListOutputConfig

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('InputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('OutputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListOutputConfig()
            self.output_config = temp_model.from_map(m['OutputConfig'])
        return self


class ListSmartJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, smart_job_list=None, next_token=None, max_results=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.smart_job_list = smart_job_list  # type: list[ListSmartJobsResponseBodySmartJobList]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.smart_job_list:
            for k in self.smart_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmartJobList'] = []
        if self.smart_job_list is not None:
            for k in self.smart_job_list:
                result['SmartJobList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.smart_job_list = []
        if m.get('SmartJobList') is not None:
            for k in m.get('SmartJobList'):
                temp_model = ListSmartJobsResponseBodySmartJobList()
                self.smart_job_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSmartJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSmartJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponse, self).to_map()
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
            temp_model = ListSmartJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRelatedAuthorizationStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, ossauthorized=None, mtsauthorized=None, mnsauthorized=None, authorized=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.ossauthorized = ossauthorized  # type: bool
        self.mtsauthorized = mtsauthorized  # type: bool
        self.mnsauthorized = mnsauthorized  # type: bool
        self.authorized = authorized  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRelatedAuthorizationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ossauthorized is not None:
            result['OSSAuthorized'] = self.ossauthorized
        if self.mtsauthorized is not None:
            result['MTSAuthorized'] = self.mtsauthorized
        if self.mnsauthorized is not None:
            result['MNSAuthorized'] = self.mnsauthorized
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OSSAuthorized') is not None:
            self.ossauthorized = m.get('OSSAuthorized')
        if m.get('MTSAuthorized') is not None:
            self.mtsauthorized = m.get('MTSAuthorized')
        if m.get('MNSAuthorized') is not None:
            self.mnsauthorized = m.get('MNSAuthorized')
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        return self


class DescribeRelatedAuthorizationStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRelatedAuthorizationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRelatedAuthorizationStatusResponse, self).to_map()
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
            temp_model = DescribeRelatedAuthorizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmartJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteSmartJobResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None, job_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteSmartJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSmartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSmartJobResponse, self).to_map()
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
            temp_model = DeleteSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTemplateRequest(TeaModel):
    def __init__(self, name=None, type=None, config=None, cover_url=None, preview_media=None, status=None,
                 source=None, related_mediaids=None):
        # 模板名称
        self.name = name  # type: str
        # 模板类型，取值范围：Timeline
        self.type = type  # type: str
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板创建来源，默认OpenAPI
        self.source = source  # type: str
        # 模板相关素材，模板编辑器使用
        self.related_mediaids = related_mediaids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.source is not None:
            result['Source'] = self.source
        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')
        return self


class AddTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, template_id=None, name=None, type=None, config=None, cover_url=None, preview_media=None,
                 status=None, create_source=None, modified_source=None):
        # 模板Id
        self.template_id = template_id  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板类型
        self.type = type  # type: str
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板创建来源
        self.create_source = create_source  # type: str
        # 模板修改来源
        self.modified_source = modified_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        return self


class AddTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 模板信息
        self.template = template  # type: AddTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(AddTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = AddTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class AddTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTemplateResponse, self).to_map()
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
            temp_model = AddTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEditingProjectRequest(TeaModel):
    def __init__(self, title=None, description=None, timeline=None, cover_url=None, project_id=None):
        # 云剪辑工程标题
        self.title = title  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectResponseBody, self).to_map()
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


class UpdateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEditingProjectResponse, self).to_map()
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
            temp_model = UpdateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaProducingJobsRequest(TeaModel):
    def __init__(self, status=None):
        # 查询以下状态的合成任务，支持多值，以英文逗号分隔
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaProducingJobsRequest, self).to_map()
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


class ListMediaProducingJobsResponseBodyMediaProducingJobList(TeaModel):
    def __init__(self, job_id=None, project_id=None, media_id=None, media_url=None, template_id=None,
                 clips_param=None, duration=None, create_time=None, complete_time=None, modified_time=None, status=None,
                 code=None, message=None):
        self.job_id = job_id  # type: str
        self.project_id = project_id  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.template_id = template_id  # type: str
        self.clips_param = clips_param  # type: str
        self.duration = duration  # type: float
        self.create_time = create_time  # type: str
        self.complete_time = complete_time  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaProducingJobsResponseBodyMediaProducingJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListMediaProducingJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, media_producing_job_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.media_producing_job_list = media_producing_job_list  # type: list[ListMediaProducingJobsResponseBodyMediaProducingJobList]

    def validate(self):
        if self.media_producing_job_list:
            for k in self.media_producing_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMediaProducingJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaProducingJobList'] = []
        if self.media_producing_job_list is not None:
            for k in self.media_producing_job_list:
                result['MediaProducingJobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_producing_job_list = []
        if m.get('MediaProducingJobList') is not None:
            for k in m.get('MediaProducingJobList'):
                temp_model = ListMediaProducingJobsResponseBodyMediaProducingJobList()
                self.media_producing_job_list.append(temp_model.from_map(k))
        return self


class ListMediaProducingJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMediaProducingJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMediaProducingJobsResponse, self).to_map()
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
            temp_model = ListMediaProducingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, project_id=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsRequest, self).to_map()
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


class GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, snapshots=None, status=None,
                 transcode_status=None, create_time=None, modified_time=None, deleted_time=None, sprite_images=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 资源状态
        self.status = status  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo
        # FileInfos
        self.file_info_list = file_info_list  # type: list[GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class GetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None, project_id=None, media_infos=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.project_id = project_id  # type: str
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[GetEditingProjectMaterialsResponseBodyMediaInfos]

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class GetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = GetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(self, request_id=None, storage_type=None, bucket=None, path=None, status=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 存储类型
        self.storage_type = storage_type  # type: str
        # oss bucket 名称
        self.bucket = bucket  # type: str
        # 路径
        self.path = path  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultStorageLocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDefaultStorageLocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDefaultStorageLocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultStorageLocationResponse, self).to_map()
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
            temp_model = GetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMediaInfosRequest(TeaModel):
    def __init__(self, media_ids=None, input_urls=None):
        # ICE 媒资ID
        self.media_ids = media_ids  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_urls = input_urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMediaInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.input_urls is not None:
            result['InputURLs'] = self.input_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('InputURLs') is not None:
            self.input_urls = m.get('InputURLs')
        return self


class DeleteMediaInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, ignored_list=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 出现获取错误的ID或inputUr
        self.ignored_list = ignored_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMediaInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')
        return self


class DeleteMediaInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteMediaInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMediaInfosResponse, self).to_map()
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
            temp_model = DeleteMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEventCallbackRequest(TeaModel):
    def __init__(self, callback_queue_name=None, event_type_list=None):
        self.callback_queue_name = callback_queue_name  # type: str
        self.event_type_list = event_type_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEventCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class SetEventCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否设置成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEventCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetEventCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetEventCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetEventCallbackResponse, self).to_map()
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
            temp_model = SetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        # 模板Id
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, template_id=None, name=None, type=None, config=None, preview_media=None, status=None,
                 create_source=None, modified_source=None, preview_media_status=None, creation_time=None, modified_time=None,
                 cover_url=None, clips_param=None):
        # 模板ID
        self.template_id = template_id  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板类型
        self.type = type  # type: str
        # 模板配置
        self.config = config  # type: str
        # 预览素材
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 修改来源
        self.modified_source = modified_source  # type: str
        # 预览素材状态
        self.preview_media_status = preview_media_status  # type: str
        # 创建时间
        self.creation_time = creation_time  # type: str
        # 修改时间
        self.modified_time = modified_time  # type: str
        # 封面URL
        self.cover_url = cover_url  # type: str
        # 提交合成任务的ClipsParam参数
        self.clips_param = clips_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.template = template  # type: GetTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMediaInfoRequest(TeaModel):
    def __init__(self, input_url=None, media_type=None, business_type=None, title=None, description=None,
                 category=None, media_tags=None, cover_url=None, dynamic_meta_data_list=None, user_data=None, overwrite=None,
                 client_token=None, register_config=None):
        # 媒资媒体url
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 标题
        self.title = title  # type: str
        # 描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags  # type: str
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url  # type: str
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: str
        # 用户数据，最大1024字节
        self.user_data = user_data  # type: str
        # 是否覆盖已有媒资
        self.overwrite = overwrite  # type: bool
        # 客户端token
        self.client_token = client_token  # type: str
        # 注册媒资的配置
        self.register_config = register_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.register_config is not None:
            result['RegisterConfig'] = self.register_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegisterConfig') is not None:
            self.register_config = m.get('RegisterConfig')
        return self


class RegisterMediaInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, media_id=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # ICE媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class RegisterMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterMediaInfoResponse, self).to_map()
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
            temp_model = RegisterMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEditingProjectRequest(TeaModel):
    def __init__(self, title=None, description=None, timeline=None, cover_url=None, feextend=None):
        # 云剪辑工程标题
        self.title = title  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # FEExtend
        self.feextend = feextend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class CreateEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, project_id=None, title=None, description=None, timeline=None, cover_url=None, status=None,
                 status_name=None, create_time=None, modified_time=None, duration=None, create_source=None,
                 modified_source=None, template_type=None):
        self.project_id = project_id  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        self.timeline = timeline  # type: str
        self.cover_url = cover_url  # type: str
        self.status = status  # type: long
        self.status_name = status_name  # type: str
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.duration = duration  # type: float
        self.create_source = create_source  # type: str
        self.modified_source = modified_source  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, project=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.project = project  # type: CreateEditingProjectResponseBodyProject

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(CreateEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project is not None:
            result['Project'] = self.project.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Project') is not None:
            temp_model = CreateEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        return self


class CreateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEditingProjectResponse, self).to_map()
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
            temp_model = CreateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetMediaInfosRequest(TeaModel):
    def __init__(self, media_ids=None, addition_type=None):
        self.media_ids = media_ids  # type: str
        self.addition_type = addition_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, snapshots=None, status=None,
                 transcode_status=None, create_time=None, modified_time=None, deleted_time=None, sprite_images=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 资源状态
        self.status = status  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class BatchGetMediaInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo
        # FileInfos
        self.file_info_list = file_info_list  # type: list[BatchGetMediaInfosResponseBodyMediaInfosFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class BatchGetMediaInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, media_infos=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[BatchGetMediaInfosResponseBodyMediaInfos]

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class BatchGetMediaInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchGetMediaInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponse, self).to_map()
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
            temp_model = BatchGetMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultStorageLocationRequest(TeaModel):
    def __init__(self, storage_type=None, bucket=None, path=None):
        self.storage_type = storage_type  # type: str
        self.bucket = bucket  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultStorageLocationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class SetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultStorageLocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDefaultStorageLocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDefaultStorageLocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultStorageLocationResponse, self).to_map()
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
            temp_model = SetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMediaInfoRequest(TeaModel):
    def __init__(self, media_id=None, input_url=None, business_type=None, title=None, description=None,
                 category=None, media_tags=None, cover_url=None, dynamic_meta_data_list=None, user_data=None,
                 append_tags=None, append_dynamic_meta=None):
        # 媒资Id
        self.media_id = media_id  # type: str
        # 媒资媒体类型
        self.input_url = input_url  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 标题
        self.title = title  # type: str
        # 描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags  # type: str
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url  # type: str
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: str
        # 用户数据，最大1024字节
        self.user_data = user_data  # type: str
        # 是否以append的形式更新Tags字段
        self.append_tags = append_tags  # type: bool
        # 是否以append的形式更新DynamicMetaDataList字段
        self.append_dynamic_meta = append_dynamic_meta  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.append_tags is not None:
            result['AppendTags'] = self.append_tags
        if self.append_dynamic_meta is not None:
            result['AppendDynamicMeta'] = self.append_dynamic_meta
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')
        if m.get('AppendDynamicMeta') is not None:
            self.append_dynamic_meta = m.get('AppendDynamicMeta')
        return self


class UpdateMediaInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, media_id=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # ICE媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class UpdateMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMediaInfoResponse, self).to_map()
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
            temp_model = UpdateMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaProducingJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaProducingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetMediaProducingJobResponseBodyMediaProducingJob(TeaModel):
    def __init__(self, job_id=None, project_id=None, media_id=None, media_url=None, timeline=None, template_id=None,
                 clips_param=None, duration=None, create_time=None, complete_time=None, modified_time=None, status=None,
                 code=None, message=None):
        self.job_id = job_id  # type: str
        self.project_id = project_id  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.timeline = timeline  # type: str
        self.template_id = template_id  # type: str
        self.clips_param = clips_param  # type: str
        self.duration = duration  # type: float
        self.create_time = create_time  # type: str
        self.complete_time = complete_time  # type: str
        self.modified_time = modified_time  # type: str
        self.status = status  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaProducingJobResponseBodyMediaProducingJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetMediaProducingJobResponseBody(TeaModel):
    def __init__(self, request_id=None, media_producing_job=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.media_producing_job = media_producing_job  # type: GetMediaProducingJobResponseBodyMediaProducingJob

    def validate(self):
        if self.media_producing_job:
            self.media_producing_job.validate()

    def to_map(self):
        _map = super(GetMediaProducingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_producing_job is not None:
            result['MediaProducingJob'] = self.media_producing_job.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaProducingJob') is not None:
            temp_model = GetMediaProducingJobResponseBodyMediaProducingJob()
            self.media_producing_job = temp_model.from_map(m['MediaProducingJob'])
        return self


class GetMediaProducingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaProducingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaProducingJobResponse, self).to_map()
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
            temp_model = GetMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceProductStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, iceservice_avaliable=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.iceservice_avaliable = iceservice_avaliable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIceProductStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.iceservice_avaliable is not None:
            result['ICEServiceAvaliable'] = self.iceservice_avaliable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ICEServiceAvaliable') is not None:
            self.iceservice_avaliable = m.get('ICEServiceAvaliable')
        return self


class DescribeIceProductStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIceProductStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIceProductStatusResponse, self).to_map()
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
            temp_model = DescribeIceProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaBasicInfosRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, media_type=None, business_type=None, source=None,
                 category=None, status=None, next_token=None, max_results=None, sort_by=None, include_file_basic_info=None):
        # 创建时间
        self.start_time = start_time  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 分类
        self.category = category  # type: str
        # 资源状态
        self.status = status  # type: str
        # 页号
        self.next_token = next_token  # type: str
        # 分页大小
        self.max_results = max_results  # type: int
        # 排序
        self.sort_by = sort_by  # type: str
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.category is not None:
            result['Category'] = self.category
        if self.status is not None:
            result['Status'] = self.status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, snapshots=None, status=None,
                 transcode_status=None, create_time=None, modified_time=None, deleted_time=None, sprite_images=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 资源状态
        self.status = status  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo
        # FileInfos
        self.file_info_list = file_info_list  # type: list[ListMediaBasicInfosResponseBodyMediaInfosFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class ListMediaBasicInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, media_infos=None, next_token=None, max_results=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 符合要求的媒资总数
        self.total_count = total_count  # type: long
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[ListMediaBasicInfosResponseBodyMediaInfos]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListMediaBasicInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMediaBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponse, self).to_map()
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
            temp_model = ListMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSubtitleProduceJobRequest(TeaModel):
    def __init__(self, editing_config=None, type=None, output_config=None, input_config=None, is_async=None,
                 title=None, description=None, user_data=None):
        self.editing_config = editing_config  # type: str
        self.type = type  # type: str
        self.output_config = output_config  # type: str
        self.input_config = input_config  # type: str
        self.is_async = is_async  # type: long
        self.title = title  # type: str
        self.description = description  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.type is not None:
            result['Type'] = self.type
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitSubtitleProduceJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitSubtitleProduceJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitSubtitleProduceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobResponse, self).to_map()
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
            temp_model = SubmitSubtitleProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitKeyWordCutJobRequest(TeaModel):
    def __init__(self, keyword=None, input_file=None, user_data=None, title=None, description=None):
        self.keyword = keyword  # type: str
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitKeyWordCutJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitKeyWordCutJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitKeyWordCutJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitKeyWordCutJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitKeyWordCutJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitKeyWordCutJobResponse, self).to_map()
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
            temp_model = SubmitKeyWordCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, project_id=None, material_maps=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 素材ID
        self.material_maps = material_maps  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, snapshots=None, status=None,
                 transcode_status=None, create_time=None, modified_time=None, deleted_time=None, sprite_images=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 资源状态
        self.status = status  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo
        # FileInfos
        self.file_info_list = file_info_list  # type: list[AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class AddEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None, project_id=None, media_infos=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.project_id = project_id  # type: str
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[AddEditingProjectMaterialsResponseBodyMediaInfos]

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        return self


class AddEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = AddEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitASRJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None, start_time=None, duration=None):
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # 持续时间
        self.duration = duration  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitASRJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class SubmitASRJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitASRJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitASRJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitASRJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitASRJobResponse, self).to_map()
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
            temp_model = SubmitASRJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectRequest, self).to_map()
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


class GetEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, project_id=None, title=None, timeline=None, description=None, cover_url=None,
                 create_time=None, modified_time=None, duration=None, status=None, create_source=None, template_type=None,
                 modified_source=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str
        # 云剪辑工程时间线
        self.timeline = timeline  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程创建时间
        self.create_time = create_time  # type: str
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time  # type: str
        # 云剪辑工程总时长
        self.duration = duration  # type: long
        # 云剪辑工程状态
        self.status = status  # type: str
        # 云剪辑工程创建来源
        self.create_source = create_source  # type: str
        # 云剪辑工程模板类型
        self.template_type = template_type  # type: str
        # 云剪辑工程修改来源
        self.modified_source = modified_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        return self


class GetEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, project=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.project = project  # type: GetEditingProjectResponseBodyProject

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project is not None:
            result['Project'] = self.project.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Project') is not None:
            temp_model = GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        return self


class GetEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponse, self).to_map()
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
            temp_model = GetEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSysTemplatesRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, type=None):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSysTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSysTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, template_id=None, name=None, type=None, config=None):
        self.template_id = template_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSysTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ListSysTemplatesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, next_token=None, max_results=None, templates=None):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        self.templates = templates  # type: list[ListSysTemplatesResponseBodyTemplates]

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSysTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListSysTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListSysTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSysTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSysTemplatesResponse, self).to_map()
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
            temp_model = ListSysTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, template_ids=None):
        # 模板id，多个id用英文逗号隔开
        self.template_ids = template_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
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


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIRJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None):
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIRJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitIRJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitIRJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitIRJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitIRJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitIRJobResponse, self).to_map()
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
            temp_model = SubmitIRJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, project_id=None, material_ids=None, material_type=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 素材ID
        self.material_ids = material_ids  # type: str
        # 素材类型
        self.material_type = material_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        return self


class DeleteEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsResponseBody, self).to_map()
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


class DeleteEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = DeleteEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEditingProjectRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, status=None, sort_by=None, next_token=None, max_results=None,
                 create_source=None, template_type=None):
        # CreateTime（创建时间）的开始时间
        self.start_time = start_time  # type: str
        # CreationTime（创建时间）的结束时间
        self.end_time = end_time  # type: str
        # 云剪辑工程状态。多个用逗号分隔
        self.status = status  # type: str
        # 结果排序方式
        self.sort_by = sort_by  # type: str
        # 分页参数
        self.next_token = next_token  # type: str
        # 分页参数
        self.max_results = max_results  # type: long
        # 创建来源
        self.create_source = create_source  # type: str
        # 模板类型
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SearchEditingProjectResponseBodyProjectList(TeaModel):
    def __init__(self, project_id=None, title=None, timeline=None, description=None, cover_url=None,
                 create_time=None, modified_time=None, duration=None, status=None, error_code=None, error_message=None,
                 create_source=None, modified_source=None, template_type=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str
        # 云剪辑工程时间线
        self.timeline = timeline  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程创建时间
        self.create_time = create_time  # type: str
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time  # type: str
        # 云剪辑工程总时长
        self.duration = duration  # type: long
        # 云剪辑工程状态
        self.status = status  # type: str
        # 云剪辑工程合成失败的错误码
        self.error_code = error_code  # type: str
        # 云剪辑工程合成失败的消息
        self.error_message = error_message  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 最后一次修改来源
        self.modified_source = modified_source  # type: str
        # 模板类型
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectResponseBodyProjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SearchEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, project_list=None, max_results=None, total_count=None, next_token=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 云剪辑工程列表
        self.project_list = project_list  # type: list[SearchEditingProjectResponseBodyProjectList]
        # 云剪辑工程总数
        self.max_results = max_results  # type: long
        self.total_count = total_count  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k in m.get('ProjectList'):
                temp_model = SearchEditingProjectResponseBodyProjectList()
                self.project_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class SearchEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponse, self).to_map()
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
            temp_model = SearchEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, type=None, status=None, create_source=None, keyword=None, sort_type=None):
        # 模板类型
        self.type = type  # type: str
        # 模板状态
        self.status = status  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 搜索关键词，可以根据模板id和title搜索
        self.keyword = keyword  # type: str
        # 排序参数，默认根据创建时间倒序
        self.sort_type = sort_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, template_id=None, name=None, type=None, config=None, preview_media=None, status=None,
                 create_source=None, modified_source=None, preview_media_status=None, creation_time=None, modified_time=None,
                 cover_url=None, clips_param=None):
        # 模板ID
        self.template_id = template_id  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板类型
        self.type = type  # type: str
        # 模板配置
        self.config = config  # type: str
        # 预览素材
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 修改来源
        self.modified_source = modified_source  # type: str
        # 预览素材状态
        self.preview_media_status = preview_media_status  # type: str
        # 创建时间
        self.creation_time = creation_time  # type: str
        # 修改时间
        self.modified_time = modified_time  # type: str
        # 封面URL
        self.cover_url = cover_url  # type: str
        # ClipsParam
        self.clips_param = clips_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.config is not None:
            result['Config'] = self.config
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, templates=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 本次请求条件下的数据总量。
        self.total_count = total_count  # type: int
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectsRequest(TeaModel):
    def __init__(self, project_ids=None):
        # 云剪辑工程ID。支持多个云剪辑工程，以逗号分隔。
        self.project_ids = project_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class DeleteEditingProjectsResponseBody(TeaModel):
    def __init__(self, request_id=None, ignored_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.ignored_list = ignored_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')
        return self


class DeleteEditingProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEditingProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEditingProjectsResponse, self).to_map()
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
            temp_model = DeleteEditingProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaInfoRequest(TeaModel):
    def __init__(self, media_id=None, input_url=None, output_type=None):
        self.media_id = media_id  # type: str
        self.input_url = input_url  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetMediaInfoResponseBodyMediaInfoMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, status=None, create_time=None,
                 modified_time=None, deleted_time=None, sprite_images=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 资源状态
        self.status = status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        return self


class GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList(TeaModel):
    def __init__(self, in_=None, out=None, type=None, data=None):
        # 开始时间
        self.in_ = in_  # type: float
        # 结束时间
        self.out = out  # type: float
        # 类型
        self.type = type  # type: str
        # 元数据json string
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_ is not None:
            result['In'] = self.in_
        if self.out is not None:
            result['Out'] = self.out
        if self.type is not None:
            result['Type'] = self.type
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetMediaInfoResponseBodyMediaInfoAiRoughDataList(TeaModel):
    def __init__(self, type=None, result=None):
        # AI类型
        self.type = type  # type: str
        # AI原始结果
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoAiRoughDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList(TeaModel):
    def __init__(self, index=None, codec_name=None, codec_long_name=None, codec_time_base=None,
                 codec_tag_string=None, codec_tag=None, profile=None, sample_fmt=None, sample_rate=None, channels=None,
                 channel_layout=None, timebase=None, start_time=None, duration=None, bitrate=None, fps=None, num_frames=None,
                 lang=None):
        # 音频流序号
        self.index = index  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 编码预置
        self.profile = profile  # type: str
        # 采样格式
        self.sample_fmt = sample_fmt  # type: str
        # 采样率
        self.sample_rate = sample_rate  # type: str
        # 声道数
        self.channels = channels  # type: str
        # 声道输出样式
        self.channel_layout = channel_layout  # type: str
        # 时基
        self.timebase = timebase  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 音频帧率
        self.fps = fps  # type: str
        # 总帧数
        self.num_frames = num_frames  # type: str
        # 语言
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList(TeaModel):
    def __init__(self, index=None, codec_name=None, codec_long_name=None, profile=None, codec_time_base=None,
                 codec_tag_string=None, codec_tag=None, width=None, height=None, has_bframes=None, sar=None, dar=None, pix_fmt=None,
                 level=None, fps=None, avg_fps=None, timebase=None, start_time=None, duration=None, bitrate=None,
                 num_frames=None, lang=None, rotate=None, nb_frames=None):
        # 视频流序号
        self.index = index  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码预置
        self.profile = profile  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str
        # 是否有B帧
        self.has_bframes = has_bframes  # type: str
        # 编码信号分辨率比
        self.sar = sar  # type: str
        # 编码显示分辨率比
        self.dar = dar  # type: str
        # 像素格式
        self.pix_fmt = pix_fmt  # type: str
        # 编码等级
        self.level = level  # type: str
        # 视频帧率
        self.fps = fps  # type: str
        # 平均帧率
        self.avg_fps = avg_fps  # type: str
        # 时基
        self.timebase = timebase  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 总帧数
        self.num_frames = num_frames  # type: str
        # 语言
        self.lang = lang  # type: str
        # 旋转
        self.rotate = rotate  # type: str
        # 总帧数
        self.nb_frames = nb_frames  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.sar is not None:
            result['Sar'] = self.sar
        if self.dar is not None:
            result['Dar'] = self.dar
        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt
        if self.level is not None:
            result['Level'] = self.level
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.nb_frames is not None:
            result['Nb_frames'] = self.nb_frames
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Sar') is not None:
            self.sar = m.get('Sar')
        if m.get('Dar') is not None:
            self.dar = m.get('Dar')
        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Nb_frames') is not None:
            self.nb_frames = m.get('Nb_frames')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList(TeaModel):
    def __init__(self, index=None, codec_name=None, codec_long_name=None, codec_time_base=None,
                 codec_tag_string=None, codec_tag=None, timebase=None, start_time=None, duration=None, lang=None):
        # 音频流序号
        self.index = index  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 时基
        self.timebase = timebase  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时长
        self.duration = duration  # type: str
        # 语言
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None, audio_stream_info_list=None, video_stream_info_list=None,
                 subtitle_stream_info_list=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo
        # 音频流信息，一个媒资可能有多条音频流
        self.audio_stream_info_list = audio_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList]
        # 视频流信息，一个媒资可能有多条视频流
        self.video_stream_info_list = video_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList]
        # 字幕流信息，一个媒资可能有多条字幕流
        self.subtitle_stream_info_list = subtitle_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList]

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.audio_stream_info_list:
            for k in self.audio_stream_info_list:
                if k:
                    k.validate()
        if self.video_stream_info_list:
            for k in self.video_stream_info_list:
                if k:
                    k.validate()
        if self.subtitle_stream_info_list:
            for k in self.subtitle_stream_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        result['AudioStreamInfoList'] = []
        if self.audio_stream_info_list is not None:
            for k in self.audio_stream_info_list:
                result['AudioStreamInfoList'].append(k.to_map() if k else None)
        result['VideoStreamInfoList'] = []
        if self.video_stream_info_list is not None:
            for k in self.video_stream_info_list:
                result['VideoStreamInfoList'].append(k.to_map() if k else None)
        result['SubtitleStreamInfoList'] = []
        if self.subtitle_stream_info_list is not None:
            for k in self.subtitle_stream_info_list:
                result['SubtitleStreamInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        self.audio_stream_info_list = []
        if m.get('AudioStreamInfoList') is not None:
            for k in m.get('AudioStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k))
        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k in m.get('VideoStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k))
        self.subtitle_stream_info_list = []
        if m.get('SubtitleStreamInfoList') is not None:
            for k in m.get('SubtitleStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList()
                self.subtitle_stream_info_list.append(temp_model.from_map(k))
        return self


class GetMediaInfoResponseBodyMediaInfo(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, dynamic_meta_data_list=None, ai_rough_data_list=None,
                 file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: GetMediaInfoResponseBodyMediaInfoMediaBasicInfo
        # 其他元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: list[GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList]
        # AIMetadata
        self.ai_rough_data_list = ai_rough_data_list  # type: list[GetMediaInfoResponseBodyMediaInfoAiRoughDataList]
        # FileInfos
        self.file_info_list = file_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.dynamic_meta_data_list:
            for k in self.dynamic_meta_data_list:
                if k:
                    k.validate()
        if self.ai_rough_data_list:
            for k in self.ai_rough_data_list:
                if k:
                    k.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['DynamicMetaDataList'] = []
        if self.dynamic_meta_data_list is not None:
            for k in self.dynamic_meta_data_list:
                result['DynamicMetaDataList'].append(k.to_map() if k else None)
        result['AiRoughDataList'] = []
        if self.ai_rough_data_list is not None:
            for k in self.ai_rough_data_list:
                result['AiRoughDataList'].append(k.to_map() if k else None)
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.dynamic_meta_data_list = []
        if m.get('DynamicMetaDataList') is not None:
            for k in m.get('DynamicMetaDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList()
                self.dynamic_meta_data_list.append(temp_model.from_map(k))
        self.ai_rough_data_list = []
        if m.get('AiRoughDataList') is not None:
            for k in m.get('AiRoughDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoAiRoughDataList()
                self.ai_rough_data_list.append(temp_model.from_map(k))
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class GetMediaInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, media_info=None):
        # RequestId
        self.request_id = request_id  # type: str
        self.media_info = media_info  # type: GetMediaInfoResponseBodyMediaInfo

    def validate(self):
        if self.media_info:
            self.media_info.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfo()
            self.media_info = temp_model.from_map(m['MediaInfo'])
        return self


class GetMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponse, self).to_map()
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
            temp_model = GetMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSmartJobRequest(TeaModel):
    def __init__(self, editing_config=None, output_config=None, input_config=None, title=None, description=None,
                 user_data=None, job_type=None):
        self.editing_config = editing_config  # type: str
        self.output_config = output_config  # type: str
        self.input_config = input_config  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        self.user_data = user_data  # type: str
        self.job_type = job_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSmartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class SubmitSmartJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSmartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitSmartJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitSmartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSmartJobResponse, self).to_map()
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
            temp_model = SubmitSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDelogoJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None, output_config=None,
                 input_type=None, overwrite=None, output_media_target=None):
        # 输入文件
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: bool
        # 输出类型
        self.output_media_target = output_media_target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDelogoJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitDelogoJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDelogoJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitDelogoJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitDelogoJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDelogoJobResponse, self).to_map()
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
            temp_model = SubmitDelogoJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, template_id=None, name=None, config=None, cover_url=None, preview_media=None, status=None,
                 source=None):
        # 模板ID
        self.template_id = template_id  # type: str
        # 模板名称
        self.name = name  # type: str
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 修改来源，默认OpenAPI
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
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


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioProduceJobRequest(TeaModel):
    def __init__(self, editing_config=None, output_config=None, input_config=None, title=None, description=None,
                 user_data=None, overwrite=None):
        self.editing_config = editing_config  # type: str
        self.output_config = output_config  # type: str
        self.input_config = input_config  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        self.user_data = user_data  # type: str
        self.overwrite = overwrite  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioProduceJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        return self


class SubmitAudioProduceJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, state=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 任务ID
        self.job_id = job_id  # type: str
        # 任务状态
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioProduceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SubmitAudioProduceJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitAudioProduceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAudioProduceJobResponse, self).to_map()
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
            temp_model = SubmitAudioProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMediaProducingJobRequest(TeaModel):
    def __init__(self, project_id=None, timeline=None, template_id=None, clips_param=None, project_metadata=None,
                 output_media_target=None, output_media_config=None, user_data=None, client_token=None, source=None):
        self.project_id = project_id  # type: str
        self.timeline = timeline  # type: str
        self.template_id = template_id  # type: str
        self.clips_param = clips_param  # type: str
        self.project_metadata = project_metadata  # type: str
        self.output_media_target = output_media_target  # type: str
        self.output_media_config = output_media_config  # type: str
        self.user_data = user_data  # type: str
        self.client_token = client_token  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaProducingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.project_metadata is not None:
            result['ProjectMetadata'] = self.project_metadata
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('ProjectMetadata') is not None:
            self.project_metadata = m.get('ProjectMetadata')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SubmitMediaProducingJobResponseBody(TeaModel):
    def __init__(self, request_id=None, project_id=None, job_id=None, media_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 剪辑工程Id
        self.project_id = project_id  # type: str
        # 合成作业Id
        self.job_id = job_id  # type: str
        # 合成媒资Id
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaProducingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SubmitMediaProducingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitMediaProducingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitMediaProducingJobResponse, self).to_map()
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
            temp_model = SubmitMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmartJobRequest(TeaModel):
    def __init__(self, job_id=None, feextend=None):
        self.job_id = job_id  # type: str
        self.feextend = feextend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSmartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class UpdateSmartJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, feextend=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.feextend = feextend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSmartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        return self


class UpdateSmartJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSmartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSmartJobResponse, self).to_map()
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
            temp_model = UpdateSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllPublicMediaTagsRequest(TeaModel):
    def __init__(self, business_type=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllPublicMediaTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class ListAllPublicMediaTagsResponseBodyMediaTagList(TeaModel):
    def __init__(self, media_tag_id=None, media_tag_name_chinese=None, media_tag_name_english=None):
        # 素材标签id
        self.media_tag_id = media_tag_id  # type: str
        # 素材标签中文名
        self.media_tag_name_chinese = media_tag_name_chinese  # type: str
        # 素材标签英文名
        self.media_tag_name_english = media_tag_name_english  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponseBodyMediaTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.media_tag_name_chinese is not None:
            result['MediaTagNameChinese'] = self.media_tag_name_chinese
        if self.media_tag_name_english is not None:
            result['MediaTagNameEnglish'] = self.media_tag_name_english
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('MediaTagNameChinese') is not None:
            self.media_tag_name_chinese = m.get('MediaTagNameChinese')
        if m.get('MediaTagNameEnglish') is not None:
            self.media_tag_name_english = m.get('MediaTagNameEnglish')
        return self


class ListAllPublicMediaTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, media_tag_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 公共素材库标签列表
        self.media_tag_list = media_tag_list  # type: list[ListAllPublicMediaTagsResponseBodyMediaTagList]

    def validate(self):
        if self.media_tag_list:
            for k in self.media_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MediaTagList'] = []
        if self.media_tag_list is not None:
            for k in self.media_tag_list:
                result['MediaTagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.media_tag_list = []
        if m.get('MediaTagList') is not None:
            for k in m.get('MediaTagList'):
                temp_model = ListAllPublicMediaTagsResponseBodyMediaTagList()
                self.media_tag_list.append(temp_model.from_map(k))
        return self


class ListAllPublicMediaTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAllPublicMediaTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponse, self).to_map()
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
            temp_model = ListAllPublicMediaTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMattingJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None, output_config=None,
                 input_type=None, overwrite=None, output_media_target=None):
        # 输入文件
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: str
        # 输出类型
        self.output_media_target = output_media_target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMattingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitMattingJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMattingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitMattingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitMattingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitMattingJobResponse, self).to_map()
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
            temp_model = SubmitMattingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, callback_queue_name=None, event_type_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.callback_queue_name = callback_queue_name  # type: str
        self.event_type_list = event_type_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class GetEventCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEventCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEventCallbackResponse, self).to_map()
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
            temp_model = GetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicMediaBasicInfosRequest(TeaModel):
    def __init__(self, media_tag_id=None, next_token=None, max_results=None, include_file_basic_info=None):
        # 标签
        self.media_tag_id = media_tag_id  # type: str
        # 下一次读取的位置
        self.next_token = next_token  # type: str
        # 分页大小
        self.max_results = max_results  # type: int
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, media_id=None, input_url=None, media_type=None, business_type=None, source=None, title=None,
                 description=None, category=None, media_tags=None, cover_url=None, user_data=None, snapshots=None, status=None,
                 transcode_status=None, create_time=None, modified_time=None, deleted_time=None):
        # MediaId
        self.media_id = media_id  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 来源
        self.source = source  # type: str
        # 标题
        self.title = title  # type: str
        # 内容描述
        self.description = description  # type: str
        # 分类
        self.category = category  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 资源状态
        self.status = status  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, file_name=None, file_status=None, file_type=None, file_size=None, file_url=None, region=None,
                 format_name=None, duration=None, bitrate=None, width=None, height=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 时长
        self.duration = duration  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 宽
        self.width = width  # type: str
        # 高
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.region is not None:
            result['Region'] = self.region
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, media_id=None, media_basic_info=None, file_info_list=None):
        # 媒资ID
        self.media_id = media_id  # type: str
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo
        # FileInfos
        self.file_info_list = file_info_list  # type: list[ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList]

    def validate(self):
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        return self


class ListPublicMediaBasicInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, media_infos=None, next_token=None, max_results=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 符合要求的媒资总数
        self.total_count = total_count  # type: long
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[ListPublicMediaBasicInfosResponseBodyMediaInfos]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPublicMediaBasicInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPublicMediaBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponse, self).to_map()
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
            temp_model = ListPublicMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCoverJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None, output_config=None):
        # 输入文件
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCoverJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        return self


class SubmitCoverJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCoverJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitCoverJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitCoverJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitCoverJobResponse, self).to_map()
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
            temp_model = SubmitCoverJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmartHandleJobRequest(TeaModel):
    def __init__(self, job_id=None, with_ai_result=None):
        self.job_id = job_id  # type: str
        self.with_ai_result = with_ai_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSmartHandleJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.with_ai_result is not None:
            result['WithAiResult'] = self.with_ai_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('WithAiResult') is not None:
            self.with_ai_result = m.get('WithAiResult')
        return self


class GetSmartHandleJobResponseBodySmartJobInfoInputConfig(TeaModel):
    def __init__(self, input_file=None, job_parameters=None):
        self.input_file = input_file  # type: str
        self.job_parameters = job_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBodySmartJobInfoInputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')
        return self


class GetSmartHandleJobResponseBodySmartJobInfo(TeaModel):
    def __init__(self, title=None, description=None, user_id=None, editing_config=None, input_config=None,
                 output_config=None, create_time=None, modified_time=None, job_type=None):
        self.title = title  # type: str
        self.description = description  # type: str
        self.user_id = user_id  # type: str
        self.editing_config = editing_config  # type: str
        self.input_config = input_config  # type: GetSmartHandleJobResponseBodySmartJobInfoInputConfig
        self.output_config = output_config  # type: str
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.job_type = job_type  # type: str

    def validate(self):
        if self.input_config:
            self.input_config.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBodySmartJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.output_config is not None:
            result['outputConfig'] = self.output_config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfoInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('outputConfig') is not None:
            self.output_config = m.get('outputConfig')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class GetSmartHandleJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None, feextend=None,
                 smart_job_info=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str
        self.feextend = feextend  # type: str
        self.smart_job_info = smart_job_info  # type: GetSmartHandleJobResponseBodySmartJobInfo

    def validate(self):
        if self.smart_job_info:
            self.smart_job_info.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.smart_job_info is not None:
            result['SmartJobInfo'] = self.smart_job_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('SmartJobInfo') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfo()
            self.smart_job_info = temp_model.from_map(m['SmartJobInfo'])
        return self


class GetSmartHandleJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSmartHandleJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponse, self).to_map()
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
            temp_model = GetSmartHandleJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitH2VJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None, output_config=None,
                 input_type=None, overwrite=None, output_media_target=None):
        # 输入文件
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: bool
        # 输出类型
        self.output_media_target = output_media_target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitH2VJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        return self


class SubmitH2VJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitH2VJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitH2VJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitH2VJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitH2VJobResponse, self).to_map()
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
            temp_model = SubmitH2VJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPPTCutJobRequest(TeaModel):
    def __init__(self, input_file=None, user_data=None, title=None, description=None):
        self.input_file = input_file  # type: str
        self.user_data = user_data  # type: str
        self.title = title  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPPTCutJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitPPTCutJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None, output=None, state=None, user_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPPTCutJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitPPTCutJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitPPTCutJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitPPTCutJobResponse, self).to_map()
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
            temp_model = SubmitPPTCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


