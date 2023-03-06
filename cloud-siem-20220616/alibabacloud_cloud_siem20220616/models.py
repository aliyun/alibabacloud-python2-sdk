# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchJobCheckRequest(TeaModel):
    def __init__(self, region_id=None, submit_id=None):
        self.region_id = region_id  # type: str
        self.submit_id = submit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductListLogList(TeaModel):
    def __init__(self, error_code=None, log_code=None, log_store_name_pattern=None, product_code=None,
                 project_name_pattern=None, region_code=None):
        self.error_code = error_code  # type: str
        self.log_code = log_code  # type: str
        self.log_store_name_pattern = log_store_name_pattern  # type: str
        self.product_code = product_code  # type: str
        self.project_name_pattern = project_name_pattern  # type: str
        self.region_code = region_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskListProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        self.log_list = log_list  # type: list[BatchJobCheckResponseBodyDataErrTaskListProductListLogList]
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskListProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobCheckResponseBodyDataErrTaskList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        self.product_list = product_list  # type: list[BatchJobCheckResponseBodyDataErrTaskListProductList]
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyDataErrTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobCheckResponseBodyData(TeaModel):
    def __init__(self, config_id=None, err_task_list=None, failed_count=None, finish_count=None, folder_id=None,
                 task_count=None, task_status=None):
        self.config_id = config_id  # type: str
        self.err_task_list = err_task_list  # type: list[BatchJobCheckResponseBodyDataErrTaskList]
        self.failed_count = failed_count  # type: int
        self.finish_count = finish_count  # type: int
        self.folder_id = folder_id  # type: str
        self.task_count = task_count  # type: int
        self.task_status = task_status  # type: str

    def validate(self):
        if self.err_task_list:
            for k in self.err_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ErrTaskList'] = []
        if self.err_task_list is not None:
            for k in self.err_task_list:
                result['ErrTaskList'].append(k.to_map() if k else None)
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.err_task_list = []
        if m.get('ErrTaskList') is not None:
            for k in m.get('ErrTaskList'):
                temp_model = BatchJobCheckResponseBodyDataErrTaskList()
                self.err_task_list.append(temp_model.from_map(k))
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class BatchJobCheckResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: BatchJobCheckResponseBodyData
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchJobCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchJobCheckResponse, self).to_map()
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
            temp_model = BatchJobCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchJobSubmitRequest(TeaModel):
    def __init__(self, json_config=None, region_id=None):
        self.json_config = json_config  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobSubmitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_config is not None:
            result['JsonConfig'] = self.json_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonConfig') is not None:
            self.json_config = m.get('JsonConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductListLogList(TeaModel):
    def __init__(self, error_code=None, log_code=None, log_store_name_pattern=None, product_code=None,
                 project_name_pattern=None, region_code=None):
        self.error_code = error_code  # type: str
        self.log_code = log_code  # type: str
        self.log_store_name_pattern = log_store_name_pattern  # type: str
        self.product_code = product_code  # type: str
        self.project_name_pattern = project_name_pattern  # type: str
        self.region_code = region_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigListProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_store_name_pattern is not None:
            result['LogStoreNamePattern'] = self.log_store_name_pattern
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.project_name_pattern is not None:
            result['ProjectNamePattern'] = self.project_name_pattern
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogStoreNamePattern') is not None:
            self.log_store_name_pattern = m.get('LogStoreNamePattern')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProjectNamePattern') is not None:
            self.project_name_pattern = m.get('ProjectNamePattern')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class BatchJobSubmitResponseBodyDataConfigListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        self.log_list = log_list  # type: list[BatchJobSubmitResponseBodyDataConfigListProductListLogList]
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigListProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class BatchJobSubmitResponseBodyDataConfigList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        self.product_list = product_list  # type: list[BatchJobSubmitResponseBodyDataConfigListProductList]
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyDataConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BatchJobSubmitResponseBodyData(TeaModel):
    def __init__(self, config_id=None, config_list=None, submit_id=None, task_count=None):
        self.config_id = config_id  # type: str
        self.config_list = config_list  # type: list[BatchJobSubmitResponseBodyDataConfigList]
        self.submit_id = submit_id  # type: str
        self.task_count = task_count  # type: int

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = BatchJobSubmitResponseBodyDataConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class BatchJobSubmitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: BatchJobSubmitResponseBodyData
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            temp_model = BatchJobSubmitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchJobSubmitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchJobSubmitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchJobSubmitResponse, self).to_map()
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
            temp_model = BatchJobSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, channel_type=None, receive_uid=None, region_id=None):
        self.channel_type = channel_type  # type: int
        self.receive_uid = receive_uid  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.receive_uid is not None:
            result['ReceiveUid'] = self.receive_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ReceiveUid') is not None:
            self.receive_uid = m.get('ReceiveUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


