# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchDeleteJobsRequest(TeaModel):
    def __init__(self, group_id=None, job_id_list=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the application ID on the **Application Management** page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The job IDs. Multiple job IDs are separated by commas (,).
        self.job_id_list = job_id_list  # type: list[long]
        # The ID of the namespace to which the job belongs. You can obtain the ID of the namespace on the **Namespace** page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region to which the job belongs.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchDeleteJobsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The additional information that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether jobs are deleted in batches. Valid values:
        # 
        # *   **true**: Jobs are deleted in batches.
        # *   **false**: Failed to delete jobs in batches.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteJobsResponseBody, self).to_map()
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


class BatchDeleteJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteJobsResponse, self).to_map()
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
            temp_model = BatchDeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDisableJobsRequest(TeaModel):
    def __init__(self, group_id=None, job_id_list=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the ID of the application on the **Application Management** page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The job IDs. Separate multiple job IDs with commas (,).
        self.job_id_list = job_id_list  # type: list[long]
        # The ID of the namespace to which the job belongs. You can obtain the ID of the namespace on the **Namespace** page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # Required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the job resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDisableJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchDisableJobsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The status code.
        self.code = code  # type: int
        # The additional information returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDisableJobsResponseBody, self).to_map()
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


class BatchDisableJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDisableJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDisableJobsResponse, self).to_map()
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
            temp_model = BatchDisableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchEnableJobsRequest(TeaModel):
    def __init__(self, group_id=None, job_id_list=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the ID of the application on the **Application Management** page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The job IDs. Separate multiple job IDs with commas (,).
        self.job_id_list = job_id_list  # type: list[long]
        # The ID of the namespace to which the job belongs. You can obtain the ID of the namespace on the **Namespace** page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # Required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the job resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchEnableJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchEnableJobsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The status code.
        self.code = code  # type: int
        # The additional information returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchEnableJobsResponseBody, self).to_map()
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


class BatchEnableJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchEnableJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchEnableJobsResponse, self).to_map()
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
            temp_model = BatchEnableJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupRequest(TeaModel):
    def __init__(self, app_key=None, app_name=None, description=None, group_id=None, max_jobs=None,
                 monitor_config_json=None, monitor_contacts_json=None, namespace=None, namespace_name=None, namespace_source=None,
                 region_id=None, schedule_busy_workers=None):
        # The AppKey for the application.
        self.app_key = app_key  # type: str
        # The name of the application.
        self.app_name = app_name  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The maximum number of jobs.
        self.max_jobs = max_jobs  # type: int
        # The configuration of the alert. The value is a JSON string. For more information about this parameter, see **Additional information about request parameters**.
        self.monitor_config_json = monitor_config_json  # type: str
        # The configuration of alert contacts. The value is a JSON string.
        self.monitor_contacts_json = monitor_contacts_json  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # The name of the namespace.
        self.namespace_name = namespace_name  # type: str
        # This parameter is not supported. You do not need to specify this parameter.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to schedule a busy worker.
        self.schedule_busy_workers = schedule_busy_workers  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_jobs is not None:
            result['MaxJobs'] = self.max_jobs
        if self.monitor_config_json is not None:
            result['MonitorConfigJson'] = self.monitor_config_json
        if self.monitor_contacts_json is not None:
            result['MonitorContactsJson'] = self.monitor_contacts_json
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schedule_busy_workers is not None:
            result['ScheduleBusyWorkers'] = self.schedule_busy_workers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxJobs') is not None:
            self.max_jobs = m.get('MaxJobs')
        if m.get('MonitorConfigJson') is not None:
            self.monitor_config_json = m.get('MonitorConfigJson')
        if m.get('MonitorContactsJson') is not None:
            self.monitor_contacts_json = m.get('MonitorContactsJson')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScheduleBusyWorkers') is not None:
            self.schedule_busy_workers = m.get('ScheduleBusyWorkers')
        return self


class CreateAppGroupResponseBodyData(TeaModel):
    def __init__(self, app_group_id=None, app_key=None):
        # The ID of the job group.
        self.app_group_id = app_group_id  # type: long
        # The AppKey for the application.
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The information about the job group.
        self.data = data  # type: CreateAppGroupResponseBodyData
        # The error message that is returned only if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the application is created. Valid values:
        # 
        # *   **true**: The application is created.
        # *   **false**: Failed to create the application.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAppGroupResponseBody, self).to_map()
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
            temp_model = CreateAppGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppGroupResponse, self).to_map()
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
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequestContactInfo(TeaModel):
    def __init__(self, ding=None, user_mail=None, user_name=None, user_phone=None):
        # The webhook URL of the DingTalk chatbot. For more information, see [DingTalk development documentation](https://open.dingtalk.com/document/org/application-types).
        self.ding = ding  # type: str
        # The email address of the alert contact.
        self.user_mail = user_mail  # type: str
        # The name of the alert contact.
        self.user_name = user_name  # type: str
        # The mobile phone number of the alert contact.
        self.user_phone = user_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobRequestContactInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class CreateJobRequest(TeaModel):
    def __init__(self, attempt_interval=None, calendar=None, class_name=None, consumer_size=None, contact_info=None,
                 content=None, data_offset=None, description=None, dispatcher_size=None, execute_mode=None,
                 fail_enable=None, fail_times=None, group_id=None, job_type=None, max_attempt=None, max_concurrency=None,
                 miss_worker_enable=None, name=None, namespace=None, namespace_source=None, page_size=None, parameters=None,
                 queue_size=None, region_id=None, send_channel=None, status=None, success_notice_enable=None,
                 task_attempt_interval=None, task_max_attempt=None, time_expression=None, time_type=None, timeout=None,
                 timeout_enable=None, timeout_kill_enable=None, xattrs=None):
        # The interval at which the system attempts to rerun a job. Default value: 30. Unit: seconds.
        self.attempt_interval = attempt_interval  # type: int
        # When the Time type parameter is set to cron, you can specify a custom calendar.
        self.calendar = calendar  # type: str
        # The full path of the job interface class.
        # 
        # This field is available only when you select a java job. In this case, you must enter a full path.
        self.class_name = class_name  # type: str
        # The number of threads that are triggered by a single worker at a time. Default value: 5. This parameter is an advanced configuration item of the MapReduce job.
        self.consumer_size = consumer_size  # type: int
        # The information of the job contact.
        self.contact_info = contact_info  # type: list[CreateJobRequestContactInfo]
        # The script code content that is required when you set the job type to **python**, **shell**, or **go**.
        self.content = content  # type: str
        # When the Time type parameter is set to cron, you can specify a time offset. Unit: seconds.
        self.data_offset = data_offset  # type: int
        # The description of the job.
        self.description = description  # type: str
        # Default value: 5. This parameter is an advanced configuration item of the MapReduce job.
        self.dispatcher_size = dispatcher_size  # type: int
        # The execution mode of the job. The following execution modes are supported:
        # 
        # *   **standalone**: The job runs in standalone mode.
        # *   **broadcast**: The job runs in broadcast mode.
        # *   **parallel**: The job runs in parallel computing mode.
        # *   **grid**: The job runs in memory grid mode.
        # *   **batch**: The job runs in grid computing mode.
        # *   **sharding**: The job runs in sharding mode.
        self.execute_mode = execute_mode  # type: str
        # Specifies whether to turn on Failure alarm. Valid values:
        # 
        # *   **true**: Turn on Failure alarm.
        # *   **false**: Turn off Failure alarm.
        self.fail_enable = fail_enable  # type: bool
        self.fail_times = fail_times  # type: int
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The type of the job. The following job types are supported:
        # 
        # *   java
        # *   python
        # *   shell
        # *   go
        # *   http
        # *   xxljob
        # *   dataworks
        # *   k8s
        # *   springschedule
        self.job_type = job_type  # type: str
        # The maximum number of attempts that the system can make when an error occurs on a job. You can specify this parameter based on your business requirements. Default value: 0.
        self.max_attempt = max_attempt  # type: int
        # The maximum number of instances that the system can run at the same time. Default value: 1. When you set this parameter to 1, if the current job does not end, the system will not run the next job even if the runtime is reached.
        self.max_concurrency = max_concurrency  # type: int
        # Specifies whether to turn on No machine alarm available.
        # 
        # *   **true**: Turn on No machine alarm available.
        # *   **false**: Turn off No machine alarm available.
        self.miss_worker_enable = miss_worker_enable  # type: bool
        # The name of the job.
        self.name = name  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The number of subtasks that can be pulled at a time. Default value: 100. This parameter is an advanced configuration item of MapReduce job.
        self.page_size = page_size  # type: int
        # The user-defined parameters that you can obtain when the job is running.
        self.parameters = parameters  # type: str
        # The maximum number of subtask queues that you can cache. Default value: 10000. This parameter is an advanced configuration item of the MapReduce job.
        self.queue_size = queue_size  # type: int
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The channel for sending alerts. Only SMS messages are supported. Set the value to sms.
        self.send_channel = send_channel  # type: str
        # 0: disabled. 1: enabled. Default value: 1.
        self.status = status  # type: int
        self.success_notice_enable = success_notice_enable  # type: bool
        # The interval at which the system can rerun the subtask when the subtask fails. Default value: 0. This parameter is an advanced configuration item of the MapReduce job.
        self.task_attempt_interval = task_attempt_interval  # type: int
        # The number of retries that the system can perform when the subtask fails. Default value: 0. This parameter is an advanced configuration item of the MapReduce job.
        self.task_max_attempt = task_max_attempt  # type: int
        # The time expression. You can set the time expression according to the selected time type.
        # 
        # *   **cron**: Specify a standard Cron expression. You can verify the expression online after you specify the expression.
        # *   **api**: No time expression is available.
        # *   **fixed_rate**: Specify a fixed frequency value. Unit: seconds. For example, if you set this parameter to 30, the system triggers a job every 30 seconds.
        # *   **second_delay**: Specify a delay after which you can run a job. You can specify a value from 1 to 60. Unit: seconds.
        # *   **one_time**: Specify a time in the format of yyyy-MM-dd HH:mm:ss or specify a timestamp in milliseconds. Example: 2022-10-10 10:10:00.
        self.time_expression = time_expression  # type: str
        # The type of time. The following time types are supported:
        # 
        # *   **cron**: 1
        # *   **fixed_rate**: 3
        # *   **second_delay**: 4
        # *   **one_time**: 5
        # *   **api**: 100
        self.time_type = time_type  # type: int
        # The timeout threshold. Default value: 7200. Unit: seconds.
        self.timeout = timeout  # type: long
        # Specifies whether to turn on Timeout alarm. Valid values:
        # 
        # *   **true**: Turn on Timeout alarm.
        # *   **false**: Turn off Timeout alarm.
        self.timeout_enable = timeout_enable  # type: bool
        # Specifies whether to turn on Timeout termination. Valid values:
        # 
        # *   **true**: Turn on Timeout termination.
        # *   **false**: Turn off Timeout termination.
        self.timeout_kill_enable = timeout_kill_enable  # type: bool
        # If the Task type parameter is set to k8s, this parameter is required. xxljob task: {"resource":"job"} shell task: {"image":"busybox","resource":"shell"}
        self.xattrs = xattrs  # type: str

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.description is not None:
            result['Description'] = self.description
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.status is not None:
            result['Status'] = self.status
        if self.success_notice_enable is not None:
            result['SuccessNoticeEnable'] = self.success_notice_enable
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = CreateJobRequestContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessNoticeEnable') is not None:
            self.success_notice_enable = m.get('SuccessNoticeEnable')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')
        return self


class CreateJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        # The ID of the job.
        self.job_id = job_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobResponseBodyData, self).to_map()
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


class CreateJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The details of the job.
        self.data = data  # type: CreateJobResponseBodyData
        # The additional information that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the job is created. Valid values:
        # 
        # *   **true**: The job is created.
        # *   **false**: Failed to create the job.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateJobResponseBody, self).to_map()
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
            temp_model = CreateJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateJobResponse, self).to_map()
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
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(self, description=None, name=None, region_id=None, uid=None):
        # The description of the namespace.
        self.description = description  # type: str
        # The name of the namespace.
        self.name = name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The UID of the namespace, which is globally unique. We recommend that you use the UUID to generate the UID.
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CreateNamespaceResponseBodyData(TeaModel):
    def __init__(self, namespace_uid=None):
        # The unique identifier of the namespace.
        self.namespace_uid = namespace_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_uid is not None:
            result['NamespaceUid'] = self.namespace_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceUid') is not None:
            self.namespace_uid = m.get('NamespaceUid')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The information of the namespace.
        self.data = data  # type: CreateNamespaceResponseBodyData
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether an application is created. Valid values:
        # 
        # *   **true**: The application is created.
        # *   **false**: Failed to create the application.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponseBody, self).to_map()
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
            temp_model = CreateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkflowRequest(TeaModel):
    def __init__(self, description=None, group_id=None, max_concurrency=None, name=None, namespace=None,
                 namespace_source=None, region_id=None, time_expression=None, time_type=None, timezone=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.max_concurrency = max_concurrency  # type: int
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.time_expression = time_expression  # type: str
        self.time_type = time_type  # type: int
        self.timezone = timezone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        return self


class CreateWorkflowResponseBodyData(TeaModel):
    def __init__(self, workflow_id=None):
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkflowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class CreateWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateWorkflowResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateWorkflowResponseBody, self).to_map()
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
            temp_model = CreateWorkflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWorkflowResponse, self).to_map()
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
            temp_model = CreateWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the application ID on the **Application Management** page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the ID on the **Task Management** page in Distributed Task Scheduling Platform.
        self.job_id = job_id  # type: long
        # The ID of the namespace. You can obtain the ID of the namespace on the **Namespace** page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The additional information that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the job is deleted.
        # 
        # *   **true**: The job is deleted.
        # *   **false**: Failed to delete the job.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobResponseBody, self).to_map()
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


class DeleteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobResponse, self).to_map()
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
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkflowRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, workflow_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class DeleteWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The unique ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the workflow is deleted. Valid values:
        # 
        # *   **true**: The workflow is deleted.
        # *   **false**: Failed to delete the workflow.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWorkflowResponseBody, self).to_map()
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


class DeleteWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWorkflowResponse, self).to_map()
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
            temp_model = DeleteWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The displayed name of the region, which varies based on the current language.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, regions=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The list of regions.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
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
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DesignateWorkersRequest(TeaModel):
    def __init__(self, designate_type=None, group_id=None, job_id=None, labels=None, namespace=None,
                 namespace_source=None, region_id=None, transferable=None, workers=None):
        # The type of the designated machines. Valid values: 1: worker. 2: label.
        self.designate_type = designate_type  # type: int
        # The ID of the application group.
        self.group_id = group_id  # type: str
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The designated `labels`. The value is a `JSON` string.
        self.labels = labels  # type: str
        # The ID of the namespace.
        self.namespace = namespace  # type: str
        # The source of the namespace.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to allow a failover.
        self.transferable = transferable  # type: bool
        # The designated workers. The value is a JSON string.
        self.workers = workers  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DesignateWorkersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.transferable is not None:
            result['Transferable'] = self.transferable
        if self.workers is not None:
            result['Workers'] = self.workers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')
        if m.get('Workers') is not None:
            self.workers = m.get('Workers')
        return self


class DesignateWorkersResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DesignateWorkersResponseBody, self).to_map()
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


class DesignateWorkersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DesignateWorkersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DesignateWorkersResponse, self).to_map()
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
            temp_model = DesignateWorkersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableJobRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the ID of the application on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the ID of the job on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # Required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The status code.
        self.code = code  # type: int
        # The error message. The error message is returned only when an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableJobResponseBody, self).to_map()
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


class DisableJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableJobResponse, self).to_map()
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
            temp_model = DisableJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWorkflowRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, workflow_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class DisableWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the workflow is disabled. Valid values:
        # 
        # *   **true**: The workflow is disabled.
        # *   **false**: Failed to disable the workflow.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWorkflowResponseBody, self).to_map()
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


class DisableWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableWorkflowResponse, self).to_map()
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
            temp_model = DisableWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableJobRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the application. You can obtain the ID of the application on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the ID of the job on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # Required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The status code.
        self.code = code  # type: int
        # The error message. The error message is returned only when an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableJobResponseBody, self).to_map()
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


class EnableJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableJobResponse, self).to_map()
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
            temp_model = EnableJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWorkflowRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, workflow_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class EnableWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the workflow is enabled. Valid values:
        # 
        # *   **true**: The workflow is enabled.
        # *   **false**: Failed to enable the workflow.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWorkflowResponseBody, self).to_map()
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


class EnableWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableWorkflowResponse, self).to_map()
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
            temp_model = EnableWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteJobRequest(TeaModel):
    def __init__(self, check_job_status=None, designate_type=None, group_id=None, instance_parameters=None,
                 job_id=None, label=None, namespace=None, namespace_source=None, region_id=None, worker=None):
        # Specifies whether to check the job status. Valid values: -**true**: The job can be run only if the job is enabled. -**false**: The job can be run even if the job is disabled.
        self.check_job_status = check_job_status  # type: bool
        # The type of the designated machine. Valid values: -**1**: worker. -**2**: label.
        self.designate_type = designate_type  # type: int
        # The ID of the application. You can obtain the application ID on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The parameters that are passed to trigger the job to run. The input value can be any string. The parameters that are passed are obtained by calling the `context.getInstanceParameters()` class in the `processor` code. The parameters are different from custom parameters for creating jobs.
        self.instance_parameters = instance_parameters  # type: str
        # The ID of the job. You can obtain the job ID on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The label of the worker.
        self.label = label  # type: str
        # The ID of the namespace. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The worker address of the application. To query the worker address, call the GetWokerList operation.
        self.worker = worker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_job_status is not None:
            result['CheckJobStatus'] = self.check_job_status
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.label is not None:
            result['Label'] = self.label
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.worker is not None:
            result['Worker'] = self.worker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckJobStatus') is not None:
            self.check_job_status = m.get('CheckJobStatus')
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Worker') is not None:
            self.worker = m.get('Worker')
        return self


class ExecuteJobResponseBodyData(TeaModel):
    def __init__(self, job_instance_id=None):
        # The ID of the job instance.
        self.job_instance_id = job_instance_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        return self


class ExecuteJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The ID of the job instance that is returned if the call is successful.
        self.data = data  # type: ExecuteJobResponseBodyData
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   `true`: The call is successful.
        # *   `false`: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExecuteJobResponseBody, self).to_map()
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
            temp_model = ExecuteJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteJobResponse, self).to_map()
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
            temp_model = ExecuteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteWorkflowRequest(TeaModel):
    def __init__(self, group_id=None, instance_parameters=None, namespace=None, namespace_source=None,
                 region_id=None, workflow_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The dynamic parameter of the workflow instance. The parameter must be 1 to 1,000 bytes in length.
        self.instance_parameters = instance_parameters  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_parameters is not None:
            result['InstanceParameters'] = self.instance_parameters
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceParameters') is not None:
            self.instance_parameters = m.get('InstanceParameters')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class ExecuteWorkflowResponseBodyData(TeaModel):
    def __init__(self, wf_instance_id=None):
        # The ID of the workflow instance.
        self.wf_instance_id = wf_instance_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteWorkflowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')
        return self


class ExecuteWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # If the call is successful, the ID of the workflow instance is returned.
        self.data = data  # type: ExecuteWorkflowResponseBodyData
        # The error message that is returned only if the error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the API call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExecuteWorkflowResponseBody, self).to_map()
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
            temp_model = ExecuteWorkflowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteWorkflowResponse, self).to_map()
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
            temp_model = ExecuteWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInfoRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, job_name=None, namespace=None, namespace_source=None,
                 region_id=None):
        # The ID of the application. You can obtain the ID of the application on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the ID of the job on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The name of the job.
        self.job_name = job_name  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the job resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo(TeaModel):
    def __init__(self, ding=None, user_mail=None, user_name=None, user_phone=None):
        # The webhook URL of the DingTalk chatbot.
        self.ding = ding  # type: str
        # The email address of the user.
        self.user_mail = user_mail  # type: str
        # The name of the user.
        self.user_name = user_name  # type: str
        # The mobile number of the user.
        self.user_phone = user_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig(TeaModel):
    def __init__(self, fail_enable=None, miss_worker_enable=None, send_channel=None, timeout=None,
                 timeout_enable=None, timeout_kill_enable=None):
        # Indicates whether an alert is generated upon a failure. Valid values:
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.fail_enable = fail_enable  # type: bool
        # Indicates whether an alert is generated if no worker is available.
        self.miss_worker_enable = miss_worker_enable  # type: bool
        # The notification method. Only Short Message Service (SMS) is supported.
        self.send_channel = send_channel  # type: str
        # The timeout threshold. Unit: seconds. Default value: 7200.
        self.timeout = timeout  # type: long
        # Indicates whether an alert is generated upon a timeout. Valid values:
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.timeout_enable = timeout_enable  # type: bool
        # Indicates whether the job is terminated upon a timeout. By default, this feature is disabled.
        self.timeout_kill_enable = timeout_kill_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo(TeaModel):
    def __init__(self, contact_info=None, monitor_config=None):
        # The contact Information.
        self.contact_info = contact_info  # type: list[GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo]
        # The configurations of the alerting feature and alert thresholds.
        self.monitor_config = monitor_config  # type: GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()
        if self.monitor_config:
            self.monitor_config.validate()

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('MonitorConfig') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m['MonitorConfig'])
        return self


class GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs(TeaModel):
    def __init__(self, consumer_size=None, dispatcher_size=None, page_size=None, queue_size=None,
                 task_attempt_interval=None, task_max_attempt=None):
        # The number of threads that are triggered by an instance. Default value: 5.
        self.consumer_size = consumer_size  # type: int
        # The number of task distribution threads. Default value: 5.
        self.dispatcher_size = dispatcher_size  # type: int
        # The number of tasks that are returned for a parallel job at a time. Default value: 100.
        self.page_size = page_size  # type: int
        # The maximum number of tasks that can be queued. Default value: 10000.
        self.queue_size = queue_size  # type: int
        # The retry interval of the task after a task failure.
        self.task_attempt_interval = task_attempt_interval  # type: int
        # The number of retries after a task failure.
        self.task_max_attempt = task_max_attempt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        return self


class GetJobInfoResponseBodyDataJobConfigInfoTimeConfig(TeaModel):
    def __init__(self, calendar=None, data_offset=None, time_expression=None, time_type=None):
        # If the TimeType parameter is set to **1** (cron), you can customize the calendar.
        self.calendar = calendar  # type: str
        # If the TimeType parameter is set to **1** (cron), you can configure the time offset. Unit: seconds.
        self.data_offset = data_offset  # type: int
        # The time expression. The time expression varies with the time type:
        # 
        # *   **api**: No time expression exists.
        # *   **fix_rate**: a specific fixed frequency. For example, a value of 30 indicates that the job is triggered every 30 seconds.
        # *   **cron**: a standard Cron expression.
        # *   **second_delay**: a fixed delay after which the job is triggered. Valid values: 1 to 60. Unit: seconds.
        self.time_expression = time_expression  # type: str
        # The time type. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **100**: api
        self.time_type = time_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfoTimeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        return self


class GetJobInfoResponseBodyDataJobConfigInfo(TeaModel):
    def __init__(self, attempt_interval=None, class_name=None, content=None, description=None, execute_mode=None,
                 jar_url=None, job_id=None, job_monitor_info=None, job_type=None, map_task_xattrs=None, max_attempt=None,
                 max_concurrency=None, name=None, parameters=None, status=None, time_config=None, xattrs=None):
        # The interval at which the system retries to run the job after a job failure. Unit: seconds. Default value: 30.
        self.attempt_interval = attempt_interval  # type: int
        # The full path of the job interface class. This parameter is returned only for jobs whose job type is Java.
        self.class_name = class_name  # type: str
        # The script of a script job.
        self.content = content  # type: str
        # The description of the job.
        self.description = description  # type: str
        # The execution mode of the job. Valid values:
        # 
        # *   **standalone**\
        # *   **broadcast**\
        # *   **parallel**\
        # *   **grid**\
        # *   **batch**\
        # *   **shard**\
        self.execute_mode = execute_mode  # type: str
        # The full path that is used to upload files to Object Storage Service (OSS).
        # 
        # If you use a JAR package, you can upload the JAR package to this OSS path.
        self.jar_url = jar_url  # type: str
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The monitoring information of the job.
        self.job_monitor_info = job_monitor_info  # type: GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo
        # The type of the job.
        self.job_type = job_type  # type: str
        # The advanced configurations of the job. The parameters are returned only if the execution mode of the job is parallel, grid, or batch.
        self.map_task_xattrs = map_task_xattrs  # type: GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs
        # The maximum number of retries after a job failure. This parameter is specified based on your business requirements. Default value: 0.
        self.max_attempt = max_attempt  # type: int
        # The maximum number of concurrent instances. Default value: 1. A value of 1 indicates that if the last triggered instance is running, the next instance is not triggered even if the scheduled point in time for running the next instance is reached.
        self.max_concurrency = max_concurrency  # type: str
        # The name of the job.
        self.name = name  # type: str
        # The user-defined parameters. These parameters can be obtained when the job is running.
        self.parameters = parameters  # type: str
        # The status of the job. Valid values:
        # 
        # *   **1**: The job is enabled and can be triggered.
        # *   **0**: The job is disabled and cannot be triggered.
        self.status = status  # type: int
        # The time configurations.
        self.time_config = time_config  # type: GetJobInfoResponseBodyDataJobConfigInfoTimeConfig
        # The extended fields.
        self.xattrs = xattrs  # type: str

    def validate(self):
        if self.job_monitor_info:
            self.job_monitor_info.validate()
        if self.map_task_xattrs:
            self.map_task_xattrs.validate()
        if self.time_config:
            self.time_config.validate()

    def to_map(self):
        _map = super(GetJobInfoResponseBodyDataJobConfigInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_monitor_info is not None:
            result['JobMonitorInfo'] = self.job_monitor_info.to_map()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.map_task_xattrs is not None:
            result['MapTaskXAttrs'] = self.map_task_xattrs.to_map()
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status is not None:
            result['Status'] = self.status
        if self.time_config is not None:
            result['TimeConfig'] = self.time_config.to_map()
        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobMonitorInfo') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m['JobMonitorInfo'])
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MapTaskXAttrs') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m['MapTaskXAttrs'])
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeConfig') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfoTimeConfig()
            self.time_config = temp_model.from_map(m['TimeConfig'])
        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')
        return self


class GetJobInfoResponseBodyData(TeaModel):
    def __init__(self, job_config_info=None):
        # The configurations of the job.
        self.job_config_info = job_config_info  # type: GetJobInfoResponseBodyDataJobConfigInfo

    def validate(self):
        if self.job_config_info:
            self.job_config_info.validate()

    def to_map(self):
        _map = super(GetJobInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_config_info is not None:
            result['JobConfigInfo'] = self.job_config_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobConfigInfo') is not None:
            temp_model = GetJobInfoResponseBodyDataJobConfigInfo()
            self.job_config_info = temp_model.from_map(m['JobConfigInfo'])
        return self


class GetJobInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The details of the job.
        self.data = data  # type: GetJobInfoResponseBodyData
        # The error message that is returned only when an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the job details are obtained. Valid values:
        # 
        # *   **true**: The job details are obtained.
        # *   **false**: Failed to obtain the job details.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobInfoResponseBody, self).to_map()
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
            temp_model = GetJobInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobInfoResponse, self).to_map()
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
            temp_model = GetJobInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInstanceRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, job_instance_id=None, namespace=None, namespace_source=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The ID of the job instance.
        self.job_instance_id = job_instance_id  # type: long
        # The ID of the namespace. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        return self


class GetJobInstanceResponseBodyDataJobInstanceDetail(TeaModel):
    def __init__(self, data_time=None, end_time=None, executor=None, instance_id=None, job_id=None, progress=None,
                 result=None, schedule_time=None, start_time=None, status=None, time_type=None, trigger_type=None,
                 work_addr=None):
        # The data time.
        self.data_time = data_time  # type: str
        # The end time of the job execution.
        self.end_time = end_time  # type: str
        # The user who executes the job.
        self.executor = executor  # type: str
        # The ID of the job instance.
        self.instance_id = instance_id  # type: long
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The progress of the job instance.
        self.progress = progress  # type: str
        # The execution results of the job instance.
        self.result = result  # type: str
        # The scheduled time of the job.
        self.schedule_time = schedule_time  # type: str
        # The start time of the job execution.
        self.start_time = start_time  # type: str
        # The status of the job instance. Valid values:
        # 
        # *   **1**: The job instance is waiting for execution.
        # *   **3**: The job instance is running.
        # *   **4**: The job instance is successful.
        # *   **5**: The job instance fails.
        # *   **9**: The job instance is rejected.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.InstanceStatus
        self.status = status  # type: int
        # The method that is used to specify the time when to schedule the job instance. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **100**: api
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TimeType
        self.time_type = time_type  # type: int
        # The trigger type of the job instance. Valid values:
        # 
        # *   **1**: The job instance is triggered at the scheduled time.
        # *   **2**: The job instance is triggered due to data update.
        # *   **3**: The job instance is triggered by an API call.
        # *   **4**: The job instance is triggered because it is manually rerun.
        # *   **5**: The job instance is triggered because the system automatically reruns the job instance upon a system exception, such as a database exception.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TriggerType
        self.trigger_type = trigger_type  # type: int
        # The endpoint of the triggered client. The value is in the IP address:Port number format.
        self.work_addr = work_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInstanceResponseBodyDataJobInstanceDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class GetJobInstanceResponseBodyData(TeaModel):
    def __init__(self, job_instance_detail=None):
        # The details of the job instance.
        self.job_instance_detail = job_instance_detail  # type: GetJobInstanceResponseBodyDataJobInstanceDetail

    def validate(self):
        if self.job_instance_detail:
            self.job_instance_detail.validate()

    def to_map(self):
        _map = super(GetJobInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_detail is not None:
            result['JobInstanceDetail'] = self.job_instance_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobInstanceDetail') is not None:
            temp_model = GetJobInstanceResponseBodyDataJobInstanceDetail()
            self.job_instance_detail = temp_model.from_map(m['JobInstanceDetail'])
        return self


class GetJobInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The information about the job instance.
        self.data = data  # type: GetJobInstanceResponseBodyData
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobInstanceResponseBody, self).to_map()
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
            temp_model = GetJobInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobInstanceResponse, self).to_map()
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
            temp_model = GetJobInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInstanceListRequest(TeaModel):
    def __init__(self, end_timestamp=None, group_id=None, job_id=None, namespace=None, namespace_source=None,
                 region_id=None, start_timestamp=None, status=None):
        self.end_timestamp = end_timestamp  # type: long
        # The ID of the application. You can obtain the application ID on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the job ID on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The ID of the namespace. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the application resides.
        self.region_id = region_id  # type: str
        self.start_timestamp = start_timestamp  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInstanceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetJobInstanceListResponseBodyDataJobInstanceDetails(TeaModel):
    def __init__(self, data_time=None, end_time=None, executor=None, instance_id=None, job_id=None, progress=None,
                 result=None, schedule_time=None, start_time=None, status=None, time_type=None, trigger_type=None,
                 work_addr=None):
        # The data time.
        self.data_time = data_time  # type: str
        # The end time of the job execution.
        self.end_time = end_time  # type: str
        # The user who executes the job.
        self.executor = executor  # type: str
        # The ID of the job instance.
        self.instance_id = instance_id  # type: long
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The progress of the job instance.
        self.progress = progress  # type: str
        # The execution results of the job instance.
        self.result = result  # type: str
        # The scheduled time of the job.
        self.schedule_time = schedule_time  # type: str
        # The start time of the job execution.
        self.start_time = start_time  # type: str
        # The status of the job instance. Valid values:
        # 
        # *   **1**: The job instance is waiting for execution.
        # *   **3**: The job instance is running.
        # *   **4**: The job instance is successful.
        # *   **5**: The job instance fails.
        # *   **9**: The job instance is rejected.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.InstanceStatus
        self.status = status  # type: int
        # The method that is used to specify the time when to schedule the job instance. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **100**: api
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TimeType
        self.time_type = time_type  # type: int
        # The trigger type of the job instance. Valid values:
        # 
        # *   **1**: The job instance is triggered at the scheduled time.
        # *   **2**: The job instance is triggered due to data update.
        # *   **3**: The job instance is triggered by an API call.
        # *   **4**: The job instance is triggered because it is manually rerun.
        # *   **5**: The job instance is triggered because the system automatically reruns the job instance upon a system exception, such as a database exception.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TriggerType
        self.trigger_type = trigger_type  # type: int
        # The endpoint of the triggered client. The value is in the IP address:Port number format.
        self.work_addr = work_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobInstanceListResponseBodyDataJobInstanceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result is not None:
            result['Result'] = self.result
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class GetJobInstanceListResponseBodyData(TeaModel):
    def __init__(self, job_instance_details=None):
        # The details of the job instance.
        self.job_instance_details = job_instance_details  # type: list[GetJobInstanceListResponseBodyDataJobInstanceDetails]

    def validate(self):
        if self.job_instance_details:
            for k in self.job_instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobInstanceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInstanceDetails'] = []
        if self.job_instance_details is not None:
            for k in self.job_instance_details:
                result['JobInstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_instance_details = []
        if m.get('JobInstanceDetails') is not None:
            for k in m.get('JobInstanceDetails'):
                temp_model = GetJobInstanceListResponseBodyDataJobInstanceDetails()
                self.job_instance_details.append(temp_model.from_map(k))
        return self


class GetJobInstanceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The information about the job instances.
        self.data = data  # type: GetJobInstanceListResponseBodyData
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobInstanceListResponseBody, self).to_map()
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
            temp_model = GetJobInstanceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobInstanceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobInstanceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobInstanceListResponse, self).to_map()
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
            temp_model = GetJobInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogRequest(TeaModel):
    def __init__(self, end_timestamp=None, group_id=None, job_id=None, job_instance_id=None, keyword=None, line=None,
                 namespace=None, namespace_source=None, offset=None, region_id=None, reverse=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: long
        self.group_id = group_id  # type: str
        self.job_id = job_id  # type: str
        self.job_instance_id = job_instance_id  # type: str
        self.keyword = keyword  # type: str
        self.line = line  # type: int
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.offset = offset  # type: int
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.start_timestamp = start_timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.line is not None:
            result['Line'] = self.line
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class GetLogResponseBodyData(TeaModel):
    def __init__(self, logs=None):
        self.logs = logs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        return self


class GetLogResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetLogResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetLogResponseBody, self).to_map()
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
            temp_model = GetLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogResponse, self).to_map()
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
            temp_model = GetLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkFlowRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, workflow_id=None):
        # The ID of the application group.
        self.group_id = group_id  # type: str
        # The ID of the namespace.
        self.namespace = namespace  # type: str
        # The source of the namespcae.
        self.namespace_source = namespace_source  # type: str
        # The region information.
        self.region_id = region_id  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class GetWorkFlowResponseBodyDataWorkFlowInfo(TeaModel):
    def __init__(self, description=None, name=None, status=None, time_expression=None, time_type=None,
                 workflow_id=None):
        # The description of the workflow.
        self.description = description  # type: str
        # The name of the workflow.
        self.name = name  # type: str
        # The status of the workflow.
        self.status = status  # type: str
        # The time expression of the workflow.
        self.time_expression = time_expression  # type: str
        # The time type of the workflow.
        self.time_type = time_type  # type: str
        # The ID of the workflow.
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkFlowResponseBodyDataWorkFlowInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges(TeaModel):
    def __init__(self, source=None, target=None):
        # The ID of the source job.
        self.source = source  # type: long
        # The ID of the target job.
        self.target = target  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes(TeaModel):
    def __init__(self, id=None, label=None, status=None):
        # The ID of the job.
        self.id = id  # type: long
        # The name of the job.
        self.label = label  # type: str
        # The status of the job.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWorkFlowResponseBodyDataWorkFlowNodeInfo(TeaModel):
    def __init__(self, edges=None, nodes=None):
        # The workflow edges.
        self.edges = edges  # type: list[GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges]
        # The list of workflow nodes.
        self.nodes = nodes  # type: list[GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes]

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkFlowResponseBodyDataWorkFlowNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class GetWorkFlowResponseBodyData(TeaModel):
    def __init__(self, work_flow_info=None, work_flow_node_info=None):
        # The basic information of the workflow.
        self.work_flow_info = work_flow_info  # type: GetWorkFlowResponseBodyDataWorkFlowInfo
        # The node information of the workflow.
        self.work_flow_node_info = work_flow_node_info  # type: GetWorkFlowResponseBodyDataWorkFlowNodeInfo

    def validate(self):
        if self.work_flow_info:
            self.work_flow_info.validate()
        if self.work_flow_node_info:
            self.work_flow_node_info.validate()

    def to_map(self):
        _map = super(GetWorkFlowResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.work_flow_info is not None:
            result['WorkFlowInfo'] = self.work_flow_info.to_map()
        if self.work_flow_node_info is not None:
            result['WorkFlowNodeInfo'] = self.work_flow_node_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkFlowInfo') is not None:
            temp_model = GetWorkFlowResponseBodyDataWorkFlowInfo()
            self.work_flow_info = temp_model.from_map(m['WorkFlowInfo'])
        if m.get('WorkFlowNodeInfo') is not None:
            temp_model = GetWorkFlowResponseBodyDataWorkFlowNodeInfo()
            self.work_flow_node_info = temp_model.from_map(m['WorkFlowNodeInfo'])
        return self


class GetWorkFlowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The error code that is returned.
        self.code = code  # type: int
        # The data of the workflow.
        self.data = data  # type: GetWorkFlowResponseBodyData
        # The error message that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the API call.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWorkFlowResponseBody, self).to_map()
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
            temp_model = GetWorkFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWorkFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkFlowResponse, self).to_map()
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
            temp_model = GetWorkFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkerListRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None):
        # The ID of the permission group.
        self.group_id = group_id  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkerListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetWorkerListResponseBodyDataWorkerInfos(TeaModel):
    def __init__(self, ip=None, label=None, port=None, starter=None, version=None, worker_address=None):
        # The IP address of the worker.
        self.ip = ip  # type: str
        # The label of the worker.
        self.label = label  # type: str
        # The port number of the worker.
        self.port = port  # type: int
        # The startup method of the worker.
        self.starter = starter  # type: str
        # The version of the worker.
        self.version = version  # type: str
        # The address of the worker. The address is in the format of ${worker_id}@${worker_ip}:${worker_port}.
        self.worker_address = worker_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkerListResponseBodyDataWorkerInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.label is not None:
            result['Label'] = self.label
        if self.port is not None:
            result['Port'] = self.port
        if self.starter is not None:
            result['Starter'] = self.starter
        if self.version is not None:
            result['Version'] = self.version
        if self.worker_address is not None:
            result['WorkerAddress'] = self.worker_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Starter') is not None:
            self.starter = m.get('Starter')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkerAddress') is not None:
            self.worker_address = m.get('WorkerAddress')
        return self


class GetWorkerListResponseBodyData(TeaModel):
    def __init__(self, worker_infos=None):
        # The worker information.
        self.worker_infos = worker_infos  # type: list[GetWorkerListResponseBodyDataWorkerInfos]

    def validate(self):
        if self.worker_infos:
            for k in self.worker_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkerListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WorkerInfos'] = []
        if self.worker_infos is not None:
            for k in self.worker_infos:
                result['WorkerInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.worker_infos = []
        if m.get('WorkerInfos') is not None:
            for k in m.get('WorkerInfos'):
                temp_model = GetWorkerListResponseBodyDataWorkerInfos()
                self.worker_infos.append(temp_model.from_map(k))
        return self


class GetWorkerListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The job information.
        self.data = data  # type: GetWorkerListResponseBodyData
        # The additional information that is returned.
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWorkerListResponseBody, self).to_map()
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
            temp_model = GetWorkerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkerListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWorkerListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkerListResponse, self).to_map()
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
            temp_model = GetWorkerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkflowInstanceRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, wf_instance_id=None,
                 workflow_id=None):
        self.group_id = group_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.wf_instance_id = wf_instance_id  # type: long
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges(TeaModel):
    def __init__(self, source=None, target=None):
        self.source = source  # type: long
        self.target = target  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes(TeaModel):
    def __init__(self, attempt=None, data_time=None, end_time=None, job_id=None, job_instance_id=None, result=None,
                 schedule_time=None, start_time=None, work_addr=None):
        self.attempt = attempt  # type: int
        self.data_time = data_time  # type: str
        self.end_time = end_time  # type: str
        self.job_id = job_id  # type: long
        self.job_instance_id = job_instance_id  # type: long
        self.result = result  # type: str
        self.schedule_time = schedule_time  # type: str
        self.start_time = start_time  # type: str
        self.work_addr = work_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt is not None:
            result['Attempt'] = self.attempt
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.result is not None:
            result['Result'] = self.result
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attempt') is not None:
            self.attempt = m.get('Attempt')
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')
        return self


class GetWorkflowInstanceResponseBodyDataWfInstanceDag(TeaModel):
    def __init__(self, edges=None, nodes=None):
        self.edges = edges  # type: list[GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges]
        self.nodes = nodes  # type: list[GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes]

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBodyDataWfInstanceDag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = GetWorkflowInstanceResponseBodyDataWfInstanceDagEdges()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetWorkflowInstanceResponseBodyDataWfInstanceDagNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class GetWorkflowInstanceResponseBodyDataWfInstanceInfo(TeaModel):
    def __init__(self, data_time=None, end_time=None, schedule_time=None, start_time=None, status=None):
        self.data_time = data_time  # type: str
        self.end_time = end_time  # type: str
        self.schedule_time = schedule_time  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBodyDataWfInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWorkflowInstanceResponseBodyData(TeaModel):
    def __init__(self, wf_instance_dag=None, wf_instance_info=None):
        self.wf_instance_dag = wf_instance_dag  # type: GetWorkflowInstanceResponseBodyDataWfInstanceDag
        self.wf_instance_info = wf_instance_info  # type: GetWorkflowInstanceResponseBodyDataWfInstanceInfo

    def validate(self):
        if self.wf_instance_dag:
            self.wf_instance_dag.validate()
        if self.wf_instance_info:
            self.wf_instance_info.validate()

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wf_instance_dag is not None:
            result['WfInstanceDag'] = self.wf_instance_dag.to_map()
        if self.wf_instance_info is not None:
            result['WfInstanceInfo'] = self.wf_instance_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WfInstanceDag') is not None:
            temp_model = GetWorkflowInstanceResponseBodyDataWfInstanceDag()
            self.wf_instance_dag = temp_model.from_map(m['WfInstanceDag'])
        if m.get('WfInstanceInfo') is not None:
            temp_model = GetWorkflowInstanceResponseBodyDataWfInstanceInfo()
            self.wf_instance_info = temp_model.from_map(m['WfInstanceInfo'])
        return self


class GetWorkflowInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetWorkflowInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetWorkflowInstanceResponseBody, self).to_map()
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
            temp_model = GetWorkflowInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkflowInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWorkflowInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkflowInstanceResponse, self).to_map()
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
            temp_model = GetWorkflowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPermissionRequest(TeaModel):
    def __init__(self, grant_option=None, group_id=None, namespace=None, namespace_source=None, region_id=None,
                 user_id=None, user_name=None):
        # Specifies whether to grant the permissions with the GRANT option. Valid values: -**true**: grants the permissions with the GRANT option. -**false**: does not grant the permissions with the GRANT option.
        self.grant_option = grant_option  # type: bool
        # The ID of the application group.
        self.group_id = group_id  # type: str
        # The ID of the namespace.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The user ID.
        self.user_id = user_id  # type: str
        # The username.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GrantPermissionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantPermissionResponseBody, self).to_map()
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


class GrantPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantPermissionResponse, self).to_map()
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
            temp_model = GrantPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, namespace=None, namespace_source=None, region_id=None):
        # The namespace. You can obtain the namespace on the **Namespace** page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # Required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the application is located.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListGroupsResponseBodyDataAppGroups(TeaModel):
    def __init__(self, app_group_id=None, app_key=None, app_name=None, description=None, group_id=None):
        # 应用分组ID
        self.app_group_id = app_group_id  # type: long
        # The key for the application.
        self.app_key = app_key  # type: str
        # The name of the application.
        self.app_name = app_name  # type: str
        # The application description.
        self.description = description  # type: str
        # The application ID.
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsResponseBodyDataAppGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsResponseBodyData(TeaModel):
    def __init__(self, app_groups=None):
        # The list of applications and details of applications.
        self.app_groups = app_groups  # type: list[ListGroupsResponseBodyDataAppGroups]

    def validate(self):
        if self.app_groups:
            for k in self.app_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppGroups'] = []
        if self.app_groups is not None:
            for k in self.app_groups:
                result['AppGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_groups = []
        if m.get('AppGroups') is not None:
            for k in m.get('AppGroups'):
                temp_model = ListGroupsResponseBodyDataAppGroups()
                self.app_groups.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code returned.
        self.code = code  # type: int
        # The information about the list of applications.
        self.data = data  # type: ListGroupsResponseBodyData
        # The additional information returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
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
            temp_model = ListGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsResponse, self).to_map()
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, group_id=None, job_name=None, namespace=None, namespace_source=None, region_id=None,
                 status=None):
        # The ID of the application. You can obtain the application ID on the **Application Management** page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The name of the job.
        self.job_name = job_name  # type: str
        # The ID of the namespace. You can obtain the namespace ID on the **Namespace** page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the job resides.
        self.region_id = region_id  # type: str
        # Specifies whether to enable the job. Valid values:
        # 
        # *   **0**: disables the job.
        # *   **1**: enables the job.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo(TeaModel):
    def __init__(self, ding=None, user_mail=None, user_name=None, user_phone=None):
        # The webhook URL of the DingTalk chatbot.
        self.ding = ding  # type: str
        # The email address of the user.
        self.user_mail = user_mail  # type: str
        # The name of the user.
        self.user_name = user_name  # type: str
        # The mobile number of the user.
        self.user_phone = user_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig(TeaModel):
    def __init__(self, fail_enable=None, miss_worker_enable=None, send_channel=None, timeout=None,
                 timeout_enable=None, timeout_kill_enable=None):
        # Indicates whether the feature of generating an alert upon a failure is enabled. Valid values:
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.fail_enable = fail_enable  # type: bool
        # Indicates whether the feature of generating an alert when no machine is available for running the job is enabled.
        self.miss_worker_enable = miss_worker_enable  # type: bool
        # The method that is used to send an alert notification. Only Short Message Service (SMS) is supported.
        self.send_channel = send_channel  # type: str
        # The timeout threshold. Unit: seconds. Default value: 7200.
        self.timeout = timeout  # type: long
        # Indicates whether the feature of generating an alert upon a timeout is enabled. Valid values:
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.timeout_enable = timeout_enable  # type: bool
        # Indicates whether the feature of stopping job triggering upon a timeout is enabled. By default, the feature is disabled.
        # 
        # *   **true**: The feature is enabled.
        # *   **false**: The feature is disabled.
        self.timeout_kill_enable = timeout_kill_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class ListJobsResponseBodyDataJobsJobMonitorInfo(TeaModel):
    def __init__(self, contact_info=None, monitor_config=None):
        # The contact information.
        self.contact_info = contact_info  # type: list[ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo]
        # The configurations of the alerting feature and the alert threshold.
        self.monitor_config = monitor_config  # type: ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()
        if self.monitor_config:
            self.monitor_config.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobsJobMonitorInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('MonitorConfig') is not None:
            temp_model = ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m['MonitorConfig'])
        return self


class ListJobsResponseBodyDataJobsMapTaskXAttrs(TeaModel):
    def __init__(self, consumer_size=None, dispatcher_size=None, page_size=None, queue_size=None,
                 task_attempt_interval=None, task_max_attempt=None):
        # The number of threads that are triggered by a standalone job at a time. Default value: 5.
        self.consumer_size = consumer_size  # type: int
        # The number of task distribution threads. Default value: 5.
        self.dispatcher_size = dispatcher_size  # type: int
        # The number of tasks that are pulled by a parallel job at a time. Default value: 100.
        self.page_size = page_size  # type: int
        # The maximum number of task queues that can be cached. Default value: 10000.
        self.queue_size = queue_size  # type: int
        # The interval at which the system retries to run the task after a task failure.
        self.task_attempt_interval = task_attempt_interval  # type: int
        # The number of retries after a task failure.
        self.task_max_attempt = task_max_attempt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobsMapTaskXAttrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        return self


class ListJobsResponseBodyDataJobsTimeConfig(TeaModel):
    def __init__(self, calendar=None, data_offset=None, time_expression=None, time_type=None):
        # If the TimeType parameter is set to cron, you can specify custom calendar days.
        self.calendar = calendar  # type: str
        # The time offset if the TimeType parameter is set to cron. Unit: seconds.
        self.data_offset = data_offset  # type: int
        # The time expression. Valid values:
        # 
        # *   **api**: indicates that no time expression is used to specify the time when to schedule the job.
        # *   **fix_rate**: indicates that the job is triggered at a fixed frequency. For example, a value of 30 indicates that the job is triggered every 30 seconds.
        # *   **cron**: indicates that a standard CRON expression is used to specify the time when to schedule the job.
        # *   **second_delay**: indicates that the job is triggered after a fixed delay. Valid values: 1 to 60. Unit: seconds.
        self.time_expression = time_expression  # type: str
        # The method that is used to specify the time when to schedule the job. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **100**: api
        self.time_type = time_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobsTimeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        return self


class ListJobsResponseBodyDataJobs(TeaModel):
    def __init__(self, attempt_interval=None, class_name=None, content=None, description=None, execute_mode=None,
                 jar_url=None, job_id=None, job_monitor_info=None, job_type=None, map_task_xattrs=None, max_attempt=None,
                 max_concurrency=None, name=None, parameters=None, status=None, time_config=None, xattrs=None):
        # The interval at which the system retries to run the job after a job failure. Unit: seconds. Default value: 30.
        self.attempt_interval = attempt_interval  # type: int
        # The full path of the job interface class. This parameter is returned only for a Java job.
        self.class_name = class_name  # type: str
        # The script of the job. This parameter is returned only for a Python, Shell, or Go job.
        self.content = content  # type: str
        # The description of the job.
        self.description = description  # type: str
        # The execution mode of the job. Valid values:
        # 
        # *   **standalone**: The job runs in standalone mode.
        # *   **broadcast**: The job runs in broadcast mode.
        # *   **parallel**: The job runs in parallel computing mode.
        # *   **grid**: The job runs in memory grid mode.
        # *   **batch**: The job runs in grid computing mode.
        # *   **shard**: The job runs in multipart mode.
        self.execute_mode = execute_mode  # type: str
        # The full path to which a JAR package is uploaded in Object Storage Service (OSS).
        self.jar_url = jar_url  # type: str
        # The ID of the job.
        self.job_id = job_id  # type: long
        # The monitoring information of the job.
        self.job_monitor_info = job_monitor_info  # type: ListJobsResponseBodyDataJobsJobMonitorInfo
        # The type of the job.
        self.job_type = job_type  # type: str
        # The advanced configurations of the job. The parameters are returned only if the value of the ExecuteMode parameter is parallel, grid, or batch.
        self.map_task_xattrs = map_task_xattrs  # type: ListJobsResponseBodyDataJobsMapTaskXAttrs
        # The maximum number of retries after a job failure. This parameter is specified based on your business requirements. Default value: 0.
        self.max_attempt = max_attempt  # type: int
        # The maximum number of instances that can concurrently run for the job. Default value: 1. A value of 1 indicates that if the last triggered instance is running, the next instance is not triggered even if the scheduled point in time for running the instance is reached.
        self.max_concurrency = max_concurrency  # type: str
        # The name of the job.
        self.name = name  # type: str
        # The user-defined parameters. These parameters can be obtained when the job is running.
        self.parameters = parameters  # type: str
        # The status of the job. Valid values:
        # 
        # *   **1**: The job is enabled and can be triggered.
        # *   **0**: The job is disabled and cannot be triggered.
        self.status = status  # type: int
        # The time configurations.
        self.time_config = time_config  # type: ListJobsResponseBodyDataJobsTimeConfig
        # The extended fields.
        self.xattrs = xattrs  # type: str

    def validate(self):
        if self.job_monitor_info:
            self.job_monitor_info.validate()
        if self.map_task_xattrs:
            self.map_task_xattrs.validate()
        if self.time_config:
            self.time_config.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyDataJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_monitor_info is not None:
            result['JobMonitorInfo'] = self.job_monitor_info.to_map()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.map_task_xattrs is not None:
            result['MapTaskXAttrs'] = self.map_task_xattrs.to_map()
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status is not None:
            result['Status'] = self.status
        if self.time_config is not None:
            result['TimeConfig'] = self.time_config.to_map()
        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobMonitorInfo') is not None:
            temp_model = ListJobsResponseBodyDataJobsJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m['JobMonitorInfo'])
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MapTaskXAttrs') is not None:
            temp_model = ListJobsResponseBodyDataJobsMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m['MapTaskXAttrs'])
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeConfig') is not None:
            temp_model = ListJobsResponseBodyDataJobsTimeConfig()
            self.time_config = temp_model.from_map(m['TimeConfig'])
        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')
        return self


class ListJobsResponseBodyData(TeaModel):
    def __init__(self, jobs=None):
        # The jobs and their details.
        self.jobs = jobs  # type: list[ListJobsResponseBodyDataJobs]

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The information about the jobs.
        self.data = data  # type: ListJobsResponseBodyData
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
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
            temp_model = ListJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobsResponse, self).to_map()
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacesRequest(TeaModel):
    def __init__(self, region_id=None):
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNamespacesResponseBodyDataNamespaces(TeaModel):
    def __init__(self, description=None, name=None, uid=None):
        # The description of the namespace.
        self.description = description  # type: str
        # The name of the namespace.
        self.name = name  # type: str
        # The ID of the namespace.
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacesResponseBodyDataNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.uid is not None:
            result['UId'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UId') is not None:
            self.uid = m.get('UId')
        return self


class ListNamespacesResponseBodyData(TeaModel):
    def __init__(self, namespaces=None):
        # The list and details of the namespaces.
        self.namespaces = namespaces  # type: list[ListNamespacesResponseBodyDataNamespaces]

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        return self


class ListNamespacesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The list of namespaces.
        self.data = data  # type: ListNamespacesResponseBodyData
        # The additional information that is returned.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNamespacesResponseBody, self).to_map()
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
            temp_model = ListNamespacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNamespacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespacesResponse, self).to_map()
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
            temp_model = ListNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowInstanceRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, workflow_id=None):
        self.group_id = group_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class ListWorkflowInstanceResponseBodyDataWfInstanceInfos(TeaModel):
    def __init__(self, data_time=None, end_time=None, schedule_time=None, start_time=None, status=None,
                 wf_instance_id=None, workflow_id=None):
        self.data_time = data_time  # type: str
        self.end_time = end_time  # type: str
        self.schedule_time = schedule_time  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.wf_instance_id = wf_instance_id  # type: long
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkflowInstanceResponseBodyDataWfInstanceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class ListWorkflowInstanceResponseBodyData(TeaModel):
    def __init__(self, wf_instance_infos=None):
        self.wf_instance_infos = wf_instance_infos  # type: list[ListWorkflowInstanceResponseBodyDataWfInstanceInfos]

    def validate(self):
        if self.wf_instance_infos:
            for k in self.wf_instance_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkflowInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WfInstanceInfos'] = []
        if self.wf_instance_infos is not None:
            for k in self.wf_instance_infos:
                result['WfInstanceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.wf_instance_infos = []
        if m.get('WfInstanceInfos') is not None:
            for k in m.get('WfInstanceInfos'):
                temp_model = ListWorkflowInstanceResponseBodyDataWfInstanceInfos()
                self.wf_instance_infos.append(temp_model.from_map(k))
        return self


class ListWorkflowInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListWorkflowInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListWorkflowInstanceResponseBody, self).to_map()
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
            temp_model = ListWorkflowInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWorkflowInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWorkflowInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkflowInstanceResponse, self).to_map()
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
            temp_model = ListWorkflowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunJobRequest(TeaModel):
    def __init__(self, data_time=None, end_date=None, group_id=None, job_id=None, namespace=None,
                 namespace_source=None, region_id=None, start_date=None):
        self.data_time = data_time  # type: str
        self.end_date = end_date  # type: long
        self.group_id = group_id  # type: str
        self.job_id = job_id  # type: long
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.start_date = start_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_time is not None:
            result['DataTime'] = self.data_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class RerunJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunJobResponseBody, self).to_map()
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


class RerunJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RerunJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RerunJobResponse, self).to_map()
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
            temp_model = RerunJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryJobInstanceRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, job_instance_id=None, namespace=None, namespace_source=None,
                 region_id=None):
        self.group_id = group_id  # type: str
        self.job_id = job_id  # type: long
        self.job_instance_id = job_instance_id  # type: long
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryJobInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RetryJobInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryJobInstanceResponseBody, self).to_map()
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


class RetryJobInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RetryJobInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryJobInstanceResponse, self).to_map()
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
            temp_model = RetryJobInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePermissionRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, user_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the namespace. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The unique ID (UID) of the RAM user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokePermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RevokePermissionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokePermissionResponseBody, self).to_map()
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


class RevokePermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokePermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokePermissionResponse, self).to_map()
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
            temp_model = RevokePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetJobInstanceSuccessRequest(TeaModel):
    def __init__(self, group_id=None, job_id=None, job_instance_id=None, namespace=None, namespace_source=None,
                 region_id=None):
        self.group_id = group_id  # type: str
        self.job_id = job_id  # type: long
        self.job_instance_id = job_instance_id  # type: long
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetJobInstanceSuccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetJobInstanceSuccessResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetJobInstanceSuccessResponseBody, self).to_map()
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


class SetJobInstanceSuccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetJobInstanceSuccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetJobInstanceSuccessResponse, self).to_map()
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
            temp_model = SetJobInstanceSuccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWfInstanceSuccessRequest(TeaModel):
    def __init__(self, group_id=None, namespace=None, namespace_source=None, region_id=None, wf_instance_id=None,
                 workflow_id=None):
        self.group_id = group_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.wf_instance_id = wf_instance_id  # type: long
        self.workflow_id = workflow_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWfInstanceSuccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wf_instance_id is not None:
            result['WfInstanceId'] = self.wf_instance_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WfInstanceId') is not None:
            self.wf_instance_id = m.get('WfInstanceId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class SetWfInstanceSuccessResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWfInstanceSuccessResponseBody, self).to_map()
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


class SetWfInstanceSuccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetWfInstanceSuccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetWfInstanceSuccessResponse, self).to_map()
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
            temp_model = SetWfInstanceSuccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None, job_id=None, namespace=None, namespace_source=None,
                 region_id=None):
        # The ID of the application. You can obtain the application ID on the Application Management page in the SchedulerX console.
        self.group_id = group_id  # type: str
        # The ID of the job instance in the running state.
        self.instance_id = instance_id  # type: long
        # The ID of the job. You can obtain the job ID on the Task Management page in the SchedulerX console.
        self.job_id = job_id  # type: long
        # The ID of the namespace. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        self.namespace = namespace  # type: str
        # The source of the namespace. This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The ID of the region in which the application resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The error message that is returned if an error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceResponseBody, self).to_map()
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


class StopInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopInstanceResponse, self).to_map()
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateJobRequestContactInfo(TeaModel):
    def __init__(self, ding=None, user_mail=None, user_name=None, user_phone=None):
        # The webhook URL of the DingTalk chatbot. For more information, see [DingTalk development documentation](https://open.dingtalk.com/document/org/application-types).
        self.ding = ding  # type: str
        # The email address of the contact.
        self.user_mail = user_mail  # type: str
        # The name of the contact.
        self.user_name = user_name  # type: str
        # The mobile phone number of the contact.
        self.user_phone = user_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateJobRequestContactInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding is not None:
            result['Ding'] = self.ding
        if self.user_mail is not None:
            result['UserMail'] = self.user_mail
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')
        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')
        return self


class UpdateJobRequest(TeaModel):
    def __init__(self, attempt_interval=None, calendar=None, class_name=None, consumer_size=None, contact_info=None,
                 content=None, data_offset=None, description=None, dispatcher_size=None, execute_mode=None,
                 fail_enable=None, fail_times=None, group_id=None, job_id=None, max_attempt=None, max_concurrency=None,
                 miss_worker_enable=None, name=None, namespace=None, namespace_source=None, page_size=None, parameters=None,
                 queue_size=None, region_id=None, send_channel=None, success_notice_enable=None, task_attempt_interval=None,
                 task_max_attempt=None, time_expression=None, time_type=None, timeout=None, timeout_enable=None,
                 timeout_kill_enable=None):
        # The interval at which the system attempts to rerun a job. Default value: 30. Unit: seconds.
        self.attempt_interval = attempt_interval  # type: int
        # When the Time type parameter is set to cron, you can specify a custom calendar.
        self.calendar = calendar  # type: str
        # The full path of the job interface class.
        # 
        # This field is available only when you select a java job. In this case, you must enter a full path.
        self.class_name = class_name  # type: str
        # The number of threads that are triggered by a single worker at a time. Default value: 5. This parameter is an advanced configuration item of the MapReduce job.
        self.consumer_size = consumer_size  # type: int
        # The information of the job contact.
        self.contact_info = contact_info  # type: list[UpdateJobRequestContactInfo]
        # The script code content that is required when you set the job type to **python**, **shell**, or **go**.
        self.content = content  # type: str
        # When the Time type parameter is set to cron, you can specify a time offset. Unit: seconds.
        self.data_offset = data_offset  # type: int
        # The description of the job.
        self.description = description  # type: str
        # Default value: 5. This parameter is an advanced configuration item of the MapReduce job.
        self.dispatcher_size = dispatcher_size  # type: int
        # The execution mode of the job. The following execution modes are supported:
        # 
        # *   **standalone**: The job runs in standalone mode.
        # *   **broadcast**: The job runs in broadcast mode.
        # *   **parallel**: The job runs in parallel computing mode.
        # *   **grid**: The job runs in memory grid mode.
        # *   **batch**: The job runs in grid computing mode.
        # *   **sharding**: The job runs in sharding mode.
        self.execute_mode = execute_mode  # type: str
        # Specifies whether to turn on Failure alarm. Valid values:
        # 
        # *   **true**: Turn on Failure alarm.
        # *   **false**: Turn off Failure alarm.
        self.fail_enable = fail_enable  # type: bool
        self.fail_times = fail_times  # type: int
        # The ID of the application. You can obtain the application ID on the Application Management page in Distributed Task Scheduling Platform.
        self.group_id = group_id  # type: str
        # The ID of the job. You can obtain the job ID on the Task Management page in Distributed Task Scheduling Platform.
        self.job_id = job_id  # type: long
        # The maximum number of attempts that the system can make when an error occurs on a job. You can specify this parameter based on your business requirements.
        self.max_attempt = max_attempt  # type: int
        # The maximum number of instances that the system can run at the same time. Default value: 1. When you set this parameter to 1, if the current job does not end, the system will not run the next job even if the runtime is reached.
        self.max_concurrency = max_concurrency  # type: int
        # Specifies whether to turn on No machine alarm available when no worker is available.
        # 
        # *   **true**: Turn on No machine alarm available when no worker is available.
        # *   **false**: Turn off No machine alarm available when no worker is available.
        self.miss_worker_enable = miss_worker_enable  # type: bool
        # The name of the job.
        self.name = name  # type: str
        # The ID of the namespace. You can obtain the ID of the namespace on the Namespace page in Distributed Task Scheduling Platform.
        self.namespace = namespace  # type: str
        # This parameter is required only for a special third party.
        self.namespace_source = namespace_source  # type: str
        # The number of subtasks that can be pulled at a time. Default value: 100. This parameter is an advanced configuration item of the MapReduce job.
        self.page_size = page_size  # type: int
        # The user-defined parameters that you can obtain when you run the job.
        self.parameters = parameters  # type: str
        # The maximum number of subtask queues that you can cache. Default value: 10000. This parameter is an advanced configuration item of the MapReduce job.
        self.queue_size = queue_size  # type: int
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The channel for sending alerts. Only SMS messages are supported.
        self.send_channel = send_channel  # type: str
        self.success_notice_enable = success_notice_enable  # type: bool
        # The interval at which the system can rerun the subtask when the subtask fails. This parameter is an advanced configuration item of the MapReduce job.
        self.task_attempt_interval = task_attempt_interval  # type: int
        # The number of retries that the system can perform when the subtask fails. This parameter is an advanced configuration item of the MapReduce job.
        self.task_max_attempt = task_max_attempt  # type: int
        # The time expression. You can set the time expression according to the selected time type.
        # 
        # *   **cron**: Specify a standard Cron expression. You can verify the expression online after you specify the expression.
        # *   **api**: No time expression is available.
        # *   **fixed_rate**: Specify a fixed frequency value. Unit: seconds. For example, if you set this parameter to 30, the system triggers a job every 30 seconds.
        # *   **second_delay**: Specify a delay after which you can run a job. You can specify a value from 1 to 60. Unit: seconds.
        self.time_expression = time_expression  # type: str
        # The type of time. The following time types are supported:
        # 
        # *   **cron**: 1
        # *   **fix_rate**: 3
        # *   **second_delay**: 4
        # *   **api**: 100
        self.time_type = time_type  # type: int
        # The timeout threshold. Default value: 7200. Unit: seconds.
        self.timeout = timeout  # type: long
        # Specifies whether to turn on Timeout alarm. Valid values:
        # 
        # *   **true**: Turn on Timeout alarm.
        # *   **false**: Turn off Timeout alarm.
        self.timeout_enable = timeout_enable  # type: bool
        # Specifies whether to turn on Timeout termination. Valid values:
        # 
        # *   **true**: Turn on Timeout termination.
        # *   **false**: Turn off Timeout termination.
        self.timeout_kill_enable = timeout_kill_enable  # type: bool

    def validate(self):
        if self.contact_info:
            for k in self.contact_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval
        if self.calendar is not None:
            result['Calendar'] = self.calendar
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k in self.contact_info:
                result['ContactInfo'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset
        if self.description is not None:
            result['Description'] = self.description
        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size
        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel
        if self.success_notice_enable is not None:
            result['SuccessNoticeEnable'] = self.success_notice_enable
        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval
        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable
        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k in m.get('ContactInfo'):
                temp_model = UpdateJobRequestContactInfo()
                self.contact_info.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')
        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')
        if m.get('SuccessNoticeEnable') is not None:
            self.success_notice_enable = m.get('SuccessNoticeEnable')
        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')
        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')
        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')
        return self


class UpdateJobResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The HTTP status code that is returned.
        self.code = code  # type: int
        # The additional information that is returned only if the error occurs.
        self.message = message  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateJobResponseBody, self).to_map()
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


class UpdateJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateJobResponse, self).to_map()
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
            temp_model = UpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkflowRequest(TeaModel):
    def __init__(self, description=None, group_id=None, name=None, namespace=None, namespace_source=None,
                 region_id=None, time_expression=None, time_type=None, workflow_id=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.time_expression = time_expression  # type: str
        self.time_type = time_type  # type: int
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkflowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression
        if self.time_type is not None:
            result['TimeType'] = self.time_type
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')
        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class UpdateWorkflowResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkflowResponseBody, self).to_map()
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


class UpdateWorkflowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWorkflowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkflowResponse, self).to_map()
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
            temp_model = UpdateWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkflowDagRequest(TeaModel):
    def __init__(self, dag_json=None, group_id=None, namespace=None, namespace_source=None, region_id=None,
                 workflow_id=None):
        self.dag_json = dag_json  # type: str
        self.group_id = group_id  # type: str
        self.namespace = namespace  # type: str
        self.namespace_source = namespace_source  # type: str
        self.region_id = region_id  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkflowDagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_json is not None:
            result['DagJson'] = self.dag_json
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DagJson') is not None:
            self.dag_json = m.get('DagJson')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class UpdateWorkflowDagResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkflowDagResponseBody, self).to_map()
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


class UpdateWorkflowDagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWorkflowDagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkflowDagResponse, self).to_map()
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
            temp_model = UpdateWorkflowDagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


