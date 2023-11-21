# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataProductListLogMapValueExtraParameters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataProductListLogMapValueExtraParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DataProductListLogMapValue(TeaModel):
    def __init__(self, log_code=None, log_name=None, log_name_en=None, log_name_key=None, status=None,
                 can_operate_or_not=None, topic=None, extra_parameters=None):
        self.log_code = log_code  # type: str
        self.log_name = log_name  # type: str
        self.log_name_en = log_name_en  # type: str
        self.log_name_key = log_name_key  # type: str
        self.status = status  # type: bool
        self.can_operate_or_not = can_operate_or_not  # type: bool
        self.topic = topic  # type: str
        self.extra_parameters = extra_parameters  # type: list[DataProductListLogMapValueExtraParameters]

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataProductListLogMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        if self.topic is not None:
            result['Topic'] = self.topic
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = DataProductListLogMapValueExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        return self


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


class CloseDeliveryRequest(TeaModel):
    def __init__(self, log_code=None, product_code=None, region_id=None):
        self.log_code = log_code  # type: str
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloseDeliveryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseDeliveryResponse, self).to_map()
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
            temp_model = CloseDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutomateResponseConfigRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAutomateResponseConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAutomateResponseConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutomateResponseConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutomateResponseConfigResponse, self).to_map()
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
            temp_model = DeleteAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizeRuleRequest(TeaModel):
    def __init__(self, region_id=None, rule_id=None):
        self.region_id = region_id  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomizeRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomizeRuleResponse, self).to_map()
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
            temp_model = DeleteCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuickQueryRequest(TeaModel):
    def __init__(self, region_id=None, search_name=None):
        self.region_id = region_id  # type: str
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class DeleteQuickQueryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQuickQueryResponse, self).to_map()
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
            temp_model = DeleteQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhiteRuleListRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhiteRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWhiteRuleListResponse, self).to_map()
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
            temp_model = DeleteWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAggregateFunctionRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAggregateFunctionRequest, self).to_map()
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


class DescribeAggregateFunctionResponseBodyData(TeaModel):
    def __init__(self, function=None, function_name=None):
        self.function = function  # type: str
        self.function_name = function_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['Function'] = self.function
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeAggregateFunctionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAggregateFunctionResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAggregateFunctionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAggregateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAggregateFunctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAggregateFunctionResponse, self).to_map()
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
            temp_model = DescribeAggregateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneRequest, self).to_map()
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


class DescribeAlertSceneResponseBodyDataTargets(TeaModel):
    def __init__(self, name=None, type=None, value=None, values=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneResponseBodyData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_tile=None, alert_tile_id=None, alert_type=None,
                 alert_type_id=None, targets=None):
        self.alert_name = alert_name  # type: str
        self.alert_name_id = alert_name_id  # type: str
        self.alert_tile = alert_tile  # type: str
        self.alert_tile_id = alert_tile_id  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_id = alert_type_id  # type: str
        self.targets = targets  # type: list[DescribeAlertSceneResponseBodyDataTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAlertSceneResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSceneResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneResponse, self).to_map()
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
            temp_model = DescribeAlertSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSceneByEventRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneByEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSceneByEventResponseBodyDataTargets(TeaModel):
    def __init__(self, name=None, type=None, value=None, values=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.value = value  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertSceneByEventResponseBodyData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_tile=None, alert_tile_id=None, alert_type=None,
                 alert_type_id=None, targets=None):
        self.alert_name = alert_name  # type: str
        self.alert_name_id = alert_name_id  # type: str
        self.alert_tile = alert_tile  # type: str
        self.alert_tile_id = alert_tile_id  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_id = alert_type_id  # type: str
        self.targets = targets  # type: list[DescribeAlertSceneByEventResponseBodyDataTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_tile is not None:
            result['AlertTile'] = self.alert_tile
        if self.alert_tile_id is not None:
            result['AlertTileId'] = self.alert_tile_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertTile') is not None:
            self.alert_tile = m.get('AlertTile')
        if m.get('AlertTileId') is not None:
            self.alert_tile_id = m.get('AlertTileId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = DescribeAlertSceneByEventResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class DescribeAlertSceneByEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAlertSceneByEventResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSceneByEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSceneByEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSceneByEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSceneByEventResponse, self).to_map()
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
            temp_model = DescribeAlertSceneByEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceRequest(TeaModel):
    def __init__(self, end_time=None, level=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.level = level  # type: list[str]
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.level is not None:
            result['Level'] = self.level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertSourceResponseBodyData(TeaModel):
    def __init__(self, source=None, source_name=None):
        self.source = source  # type: str
        self.source_name = source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAlertSourceResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceResponse, self).to_map()
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
            temp_model = DescribeAlertSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertSourceWithEventRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAlertSourceWithEventResponseBodyData(TeaModel):
    def __init__(self, source=None, source_name=None):
        self.source = source  # type: str
        self.source_name = source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        return self


class DescribeAlertSourceWithEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAlertSourceWithEventResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertSourceWithEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertSourceWithEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertSourceWithEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertSourceWithEventResponse, self).to_map()
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
            temp_model = DescribeAlertSourceWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertTypeRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertTypeRequest, self).to_map()
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


class DescribeAlertTypeResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None):
        self.alert_type = alert_type  # type: str
        self.alert_type_mds = alert_type_mds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        return self


class DescribeAlertTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAlertTypeResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertTypeResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAlertTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertTypeResponse, self).to_map()
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
            temp_model = DescribeAlertTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsRequest(TeaModel):
    def __init__(self, alert_title=None, alert_uuid=None, current_page=None, end_time=None, is_defend=None,
                 level=None, page_size=None, region_id=None, source=None, start_time=None, sub_user_id=None):
        self.alert_title = alert_title  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.is_defend = is_defend  # type: str
        self.level = level  # type: list[str]
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.start_time = start_time  # type: long
        self.sub_user_id = sub_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        self.key = key  # type: str
        self.key_name = key_name  # type: str
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        self.alert_desc = alert_desc  # type: str
        self.alert_desc_code = alert_desc_code  # type: str
        self.alert_desc_en = alert_desc_en  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsResponseBodyDataResponseDataAlertInfoList]
        self.alert_level = alert_level  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_name_code = alert_name_code  # type: str
        self.alert_name_en = alert_name_en  # type: str
        self.alert_src_prod = alert_src_prod  # type: str
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        self.alert_title = alert_title  # type: str
        self.alert_title_en = alert_title_en  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_code = alert_type_code  # type: str
        self.alert_type_en = alert_type_en  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.asset_list = asset_list  # type: str
        self.att_ck = att_ck  # type: str
        self.cloud_code = cloud_code  # type: str
        self.end_time = end_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.is_defend = is_defend  # type: str
        self.log_time = log_time  # type: str
        self.log_uuid = log_uuid  # type: str
        self.main_user_id = main_user_id  # type: long
        self.occur_time = occur_time  # type: str
        self.start_time = start_time  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeAlertsResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeAlertsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeAlertsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponseBody, self).to_map()
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
            temp_model = DescribeAlertsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsResponse, self).to_map()
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
            temp_model = DescribeAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsCountRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAlertsCountResponseBodyData(TeaModel):
    def __init__(self, all=None, high=None, low=None, medium=None, product_num=None):
        self.all = all  # type: long
        self.high = high  # type: long
        self.low = low  # type: long
        self.medium = medium  # type: long
        self.product_num = product_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.high is not None:
            result['High'] = self.high
        if self.low is not None:
            result['Low'] = self.low
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.product_num is not None:
            result['ProductNum'] = self.product_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('ProductNum') is not None:
            self.product_num = m.get('ProductNum')
        return self


class DescribeAlertsCountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeAlertsCountResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsCountResponseBody, self).to_map()
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
            temp_model = DescribeAlertsCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsCountResponse, self).to_map()
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
            temp_model = DescribeAlertsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEntityRequest(TeaModel):
    def __init__(self, current_page=None, entity_id=None, incident_uuid=None, page_size=None, region_id=None,
                 sophon_task_id=None):
        self.current_page = current_page  # type: int
        self.entity_id = entity_id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.sophon_task_id = sophon_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeAlertsWithEntityResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        self.key = key  # type: str
        self.key_name = key_name  # type: str
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEntityResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        self.alert_desc = alert_desc  # type: str
        self.alert_desc_code = alert_desc_code  # type: str
        self.alert_desc_en = alert_desc_en  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList]
        self.alert_level = alert_level  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_name_code = alert_name_code  # type: str
        self.alert_name_en = alert_name_en  # type: str
        self.alert_src_prod = alert_src_prod  # type: str
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        self.alert_title = alert_title  # type: str
        self.alert_title_en = alert_title_en  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_code = alert_type_code  # type: str
        self.alert_type_en = alert_type_en  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.asset_list = asset_list  # type: str
        self.att_ck = att_ck  # type: str
        self.cloud_code = cloud_code  # type: str
        self.end_time = end_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.is_defend = is_defend  # type: str
        self.log_time = log_time  # type: str
        self.log_uuid = log_uuid  # type: str
        self.main_user_id = main_user_id  # type: long
        self.occur_time = occur_time  # type: str
        self.start_time = start_time  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEntityResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeAlertsWithEntityResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeAlertsWithEntityResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEntityResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEntityResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEntityResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeAlertsWithEntityResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponseBody, self).to_map()
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
            temp_model = DescribeAlertsWithEntityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsWithEntityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEntityResponse, self).to_map()
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
            temp_model = DescribeAlertsWithEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlertsWithEventRequest(TeaModel):
    def __init__(self, alert_title=None, current_page=None, incident_uuid=None, is_defend=None, level=None,
                 page_size=None, region_id=None, source=None, sub_user_id=None):
        self.alert_title = alert_title  # type: str
        self.current_page = current_page  # type: int
        self.incident_uuid = incident_uuid  # type: str
        self.is_defend = is_defend  # type: str
        self.level = level  # type: list[str]
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        self.key = key  # type: str
        self.key_name = key_name  # type: str
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeAlertsWithEventResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_desc_code=None, alert_desc_en=None, alert_detail=None,
                 alert_info_list=None, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_title=None, alert_title_en=None, alert_type=None,
                 alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_list=None, att_ck=None, cloud_code=None,
                 end_time=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, is_defend=None,
                 log_time=None, log_uuid=None, main_user_id=None, occur_time=None, start_time=None, sub_user_id=None):
        self.alert_desc = alert_desc  # type: str
        self.alert_desc_code = alert_desc_code  # type: str
        self.alert_desc_en = alert_desc_en  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_info_list = alert_info_list  # type: list[DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList]
        self.alert_level = alert_level  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_name_code = alert_name_code  # type: str
        self.alert_name_en = alert_name_en  # type: str
        self.alert_src_prod = alert_src_prod  # type: str
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        self.alert_title = alert_title  # type: str
        self.alert_title_en = alert_title_en  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_code = alert_type_code  # type: str
        self.alert_type_en = alert_type_en  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.asset_list = asset_list  # type: str
        self.att_ck = att_ck  # type: str
        self.cloud_code = cloud_code  # type: str
        self.end_time = end_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.is_defend = is_defend  # type: str
        self.log_time = log_time  # type: str
        self.log_uuid = log_uuid  # type: str
        self.main_user_id = main_user_id  # type: long
        self.occur_time = occur_time  # type: str
        self.start_time = start_time  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.alert_info_list:
            for k in self.alert_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code
        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k in self.alert_info_list:
                result['AlertInfoList'].append(k.to_map() if k else None)
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')
        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k in m.get('AlertInfoList'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k))
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeAlertsWithEventResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeAlertsWithEventResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeAlertsWithEventResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeAlertsWithEventResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeAlertsWithEventResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeAlertsWithEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeAlertsWithEventResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponseBody, self).to_map()
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
            temp_model = DescribeAlertsWithEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlertsWithEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAlertsWithEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlertsWithEventResponse, self).to_map()
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
            temp_model = DescribeAlertsWithEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackTimeLineRequest(TeaModel):
    def __init__(self, asset_name=None, end_time=None, incident_uuid=None, region_id=None, start_time=None):
        self.asset_name = asset_name  # type: str
        self.end_time = end_time  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackTimeLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAttackTimeLineResponseBodyData(TeaModel):
    def __init__(self, alert_level=None, alert_name=None, alert_name_code=None, alert_name_en=None,
                 alert_src_prod=None, alert_src_prod_module=None, alert_time=None, alert_title=None, alert_title_en=None,
                 alert_type=None, alert_type_code=None, alert_type_en=None, alert_uuid=None, asset_id=None, asset_list=None,
                 asset_name=None, att_ck=None, cloud_code=None, incident_uuid=None, log_time=None):
        self.alert_level = alert_level  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_name_code = alert_name_code  # type: str
        self.alert_name_en = alert_name_en  # type: str
        self.alert_src_prod = alert_src_prod  # type: str
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        self.alert_time = alert_time  # type: long
        self.alert_title = alert_title  # type: str
        self.alert_title_en = alert_title_en  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_code = alert_type_code  # type: str
        self.alert_type_en = alert_type_en  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.asset_id = asset_id  # type: str
        self.asset_list = asset_list  # type: str
        self.asset_name = asset_name  # type: str
        self.att_ck = att_ck  # type: str
        self.cloud_code = cloud_code  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.log_time = log_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code
        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code
        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_list is not None:
            result['AssetList'] = self.asset_list
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')
        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')
        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        return self


class DescribeAttackTimeLineResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAttackTimeLineResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAttackTimeLineResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAttackTimeLineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAttackTimeLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAttackTimeLineResponse, self).to_map()
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
            temp_model = DescribeAttackTimeLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigCounterRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterRequest, self).to_map()
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


class DescribeAutomateResponseConfigCounterResponseBodyData(TeaModel):
    def __init__(self, all=None, online=None):
        self.all = all  # type: long
        self.online = online  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class DescribeAutomateResponseConfigCounterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeAutomateResponseConfigCounterResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponseBody, self).to_map()
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
            temp_model = DescribeAutomateResponseConfigCounterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigCounterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigCounterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigCounterResponse, self).to_map()
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
            temp_model = DescribeAutomateResponseConfigCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigFeatureRequest(TeaModel):
    def __init__(self, auto_response_type=None, region_id=None):
        self.auto_response_type = auto_response_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums(TeaModel):
    def __init__(self, value=None, value_mds=None):
        self.value = value  # type: str
        self.value_mds = value_mds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_mds is not None:
            result['ValueMds'] = self.value_mds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueMds') is not None:
            self.value_mds = m.get('ValueMds')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators(TeaModel):
    def __init__(self, has_right_value=None, index=None, operator=None, operator_desc_cn=None,
                 operator_desc_en=None, operator_name=None, support_data_type=None, support_tag=None):
        self.has_right_value = has_right_value  # type: bool
        self.index = index  # type: int
        self.operator = operator  # type: str
        self.operator_desc_cn = operator_desc_cn  # type: str
        self.operator_desc_en = operator_desc_en  # type: str
        self.operator_name = operator_name  # type: str
        self.support_data_type = support_data_type  # type: str
        self.support_tag = support_tag  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_right_value is not None:
            result['HasRightValue'] = self.has_right_value
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasRightValue') is not None:
            self.has_right_value = m.get('HasRightValue')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeAutomateResponseConfigFeatureResponseBodyData(TeaModel):
    def __init__(self, data_type=None, feature=None, right_value_enums=None, support_operators=None):
        self.data_type = data_type  # type: str
        self.feature = feature  # type: str
        self.right_value_enums = right_value_enums  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums]
        self.support_operators = support_operators  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators]

    def validate(self):
        if self.right_value_enums:
            for k in self.right_value_enums:
                if k:
                    k.validate()
        if self.support_operators:
            for k in self.support_operators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.feature is not None:
            result['Feature'] = self.feature
        result['RightValueEnums'] = []
        if self.right_value_enums is not None:
            for k in self.right_value_enums:
                result['RightValueEnums'].append(k.to_map() if k else None)
        result['SupportOperators'] = []
        if self.support_operators is not None:
            for k in self.support_operators:
                result['SupportOperators'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        self.right_value_enums = []
        if m.get('RightValueEnums') is not None:
            for k in m.get('RightValueEnums'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataRightValueEnums()
                self.right_value_enums.append(temp_model.from_map(k))
        self.support_operators = []
        if m.get('SupportOperators') is not None:
            for k in m.get('SupportOperators'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyDataSupportOperators()
                self.support_operators.append(temp_model.from_map(k))
        return self


class DescribeAutomateResponseConfigFeatureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAutomateResponseConfigFeatureResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAutomateResponseConfigFeatureResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigFeatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigFeatureResponse, self).to_map()
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
            temp_model = DescribeAutomateResponseConfigFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutomateResponseConfigPlayBooksRequest(TeaModel):
    def __init__(self, auto_response_type=None, entity_type=None, region_id=None):
        self.auto_response_type = auto_response_type  # type: str
        self.entity_type = entity_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBodyData(TeaModel):
    def __init__(self, description=None, display_name=None, name=None, param_type=None, uuid=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.name = name  # type: str
        self.param_type = param_type  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeAutomateResponseConfigPlayBooksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeAutomateResponseConfigPlayBooksResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAutomateResponseConfigPlayBooksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutomateResponseConfigPlayBooksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutomateResponseConfigPlayBooksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutomateResponseConfigPlayBooksResponse, self).to_map()
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
            temp_model = DescribeAutomateResponseConfigPlayBooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsRequest(TeaModel):
    def __init__(self, asset_type=None, current_page=None, incident_uuid=None, page_size=None, region_id=None):
        self.asset_type = asset_type  # type: str
        self.current_page = current_page  # type: int
        self.incident_uuid = incident_uuid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo(TeaModel):
    def __init__(self, key=None, key_name=None, values=None):
        self.key = key  # type: str
        self.key_name = key_name  # type: str
        self.values = values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeCloudSiemAssetsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_uuid=None, aliuid=None, asset_id=None, asset_info=None, asset_name=None,
                 asset_type=None, cloud_code=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None,
                 sub_user_id=None):
        self.alert_uuid = alert_uuid  # type: str
        self.aliuid = aliuid  # type: long
        self.asset_id = asset_id  # type: str
        self.asset_info = asset_info  # type: list[DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo]
        self.asset_name = asset_name  # type: str
        self.asset_type = asset_type  # type: str
        self.cloud_code = cloud_code  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        if self.asset_info:
            for k in self.asset_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        result['AssetInfo'] = []
        if self.asset_info is not None:
            for k in self.asset_info:
                result['AssetInfo'].append(k.to_map() if k else None)
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        self.asset_info = []
        if m.get('AssetInfo') is not None:
            for k in m.get('AssetInfo'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo()
                self.asset_info.append(temp_model.from_map(k))
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeCloudSiemAssetsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeCloudSiemAssetsResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeCloudSiemAssetsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemAssetsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemAssetsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemAssetsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCloudSiemAssetsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponseBody, self).to_map()
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
            temp_model = DescribeCloudSiemAssetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemAssetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsResponse, self).to_map()
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
            temp_model = DescribeCloudSiemAssetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemAssetsCounterRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemAssetsCounterResponseBodyData(TeaModel):
    def __init__(self, asset_num=None, asset_type=None):
        self.asset_num = asset_num  # type: int
        self.asset_type = asset_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        return self


class DescribeCloudSiemAssetsCounterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeCloudSiemAssetsCounterResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCloudSiemAssetsCounterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemAssetsCounterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemAssetsCounterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemAssetsCounterResponse, self).to_map()
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
            temp_model = DescribeCloudSiemAssetsCounterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventDetailRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None):
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudSiemEventDetailResponseBodyData(TeaModel):
    def __init__(self, alert_num=None, aliuid=None, asset_num=None, att_ck_labels=None, data_sources=None,
                 description=None, description_en=None, ext_content=None, gmt_create=None, gmt_modified=None,
                 incident_name=None, incident_name_en=None, incident_uuid=None, remark=None, status=None, threat_level=None,
                 threat_score=None):
        self.alert_num = alert_num  # type: int
        self.aliuid = aliuid  # type: long
        self.asset_num = asset_num  # type: int
        self.att_ck_labels = att_ck_labels  # type: list[str]
        self.data_sources = data_sources  # type: list[str]
        self.description = description  # type: str
        self.description_en = description_en  # type: str
        self.ext_content = ext_content  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.incident_name = incident_name  # type: str
        self.incident_name_en = incident_name_en  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str
        self.threat_score = threat_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCloudSiemEventDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponseBody, self).to_map()
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
            temp_model = DescribeCloudSiemEventDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemEventDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventDetailResponse, self).to_map()
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
            temp_model = DescribeCloudSiemEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudSiemEventsRequest(TeaModel):
    def __init__(self, asset_id=None, current_page=None, end_time=None, event_name=None, incident_uuid=None,
                 order=None, order_field=None, page_size=None, region_id=None, start_time=None, status=None,
                 thread_level=None):
        self.asset_id = asset_id  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.event_name = event_name  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.order = order  # type: str
        self.order_field = order_field  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: int
        self.thread_level = thread_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.thread_level is not None:
            result['ThreadLevel'] = self.thread_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreadLevel') is not None:
            self.thread_level = m.get('ThreadLevel')
        return self


class DescribeCloudSiemEventsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudSiemEventsResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_num=None, aliuid=None, asset_num=None, att_ck_labels=None, data_sources=None,
                 description=None, description_en=None, ext_content=None, gmt_create=None, gmt_modified=None,
                 incident_name=None, incident_name_en=None, incident_uuid=None, remark=None, status=None, threat_level=None,
                 threat_score=None):
        self.alert_num = alert_num  # type: int
        self.aliuid = aliuid  # type: long
        self.asset_num = asset_num  # type: int
        self.att_ck_labels = att_ck_labels  # type: list[str]
        self.data_sources = data_sources  # type: list[str]
        self.description = description  # type: str
        self.description_en = description_en  # type: str
        self.ext_content = ext_content  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.incident_name = incident_name  # type: str
        self.incident_name_en = incident_name_en  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str
        self.threat_score = threat_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.asset_num is not None:
            result['AssetNum'] = self.asset_num
        if self.att_ck_labels is not None:
            result['AttCkLabels'] = self.att_ck_labels
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.ext_content is not None:
            result['ExtContent'] = self.ext_content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_name_en is not None:
            result['IncidentNameEn'] = self.incident_name_en
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_score is not None:
            result['ThreatScore'] = self.threat_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AssetNum') is not None:
            self.asset_num = m.get('AssetNum')
        if m.get('AttCkLabels') is not None:
            self.att_ck_labels = m.get('AttCkLabels')
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('ExtContent') is not None:
            self.ext_content = m.get('ExtContent')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentNameEn') is not None:
            self.incident_name_en = m.get('IncidentNameEn')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatScore') is not None:
            self.threat_score = m.get('ThreatScore')
        return self


class DescribeCloudSiemEventsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeCloudSiemEventsResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeCloudSiemEventsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeCloudSiemEventsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeCloudSiemEventsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeCloudSiemEventsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCloudSiemEventsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponseBody, self).to_map()
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
            temp_model = DescribeCloudSiemEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudSiemEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudSiemEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudSiemEventsResponse, self).to_map()
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
            temp_model = DescribeCloudSiemEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleRequest(TeaModel):
    def __init__(self, region_id=None, rule_id=None):
        self.region_id = region_id  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeCustomizeRuleResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.alert_type_mds = alert_type_mds  # type: str
        self.aliuid = aliuid  # type: long
        self.event_transfer_ext = event_transfer_ext  # type: str
        self.event_transfer_switch = event_transfer_switch  # type: int
        self.event_transfer_type = event_transfer_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.log_source = log_source  # type: str
        self.log_source_mds = log_source_mds  # type: str
        self.log_type = log_type  # type: str
        self.log_type_mds = log_type_mds  # type: str
        self.query_cycle = query_cycle  # type: str
        self.rule_condition = rule_condition  # type: str
        self.rule_desc = rule_desc  # type: str
        self.rule_group = rule_group  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_threshold = rule_threshold  # type: str
        self.rule_type = rule_type  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class DescribeCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCustomizeRuleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponseBody, self).to_map()
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
            temp_model = DescribeCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleResponse, self).to_map()
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
            temp_model = DescribeCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleCountRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountRequest, self).to_map()
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


class DescribeCustomizeRuleCountResponseBodyData(TeaModel):
    def __init__(self, high_rule_num=None, in_use_rule_num=None, low_rule_num=None, medium_rule_num=None):
        self.high_rule_num = high_rule_num  # type: int
        self.in_use_rule_num = in_use_rule_num  # type: int
        self.low_rule_num = low_rule_num  # type: int
        self.medium_rule_num = medium_rule_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.high_rule_num is not None:
            result['HighRuleNum'] = self.high_rule_num
        if self.in_use_rule_num is not None:
            result['InUseRuleNum'] = self.in_use_rule_num
        if self.low_rule_num is not None:
            result['LowRuleNum'] = self.low_rule_num
        if self.medium_rule_num is not None:
            result['MediumRuleNum'] = self.medium_rule_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HighRuleNum') is not None:
            self.high_rule_num = m.get('HighRuleNum')
        if m.get('InUseRuleNum') is not None:
            self.in_use_rule_num = m.get('InUseRuleNum')
        if m.get('LowRuleNum') is not None:
            self.low_rule_num = m.get('LowRuleNum')
        if m.get('MediumRuleNum') is not None:
            self.medium_rule_num = m.get('MediumRuleNum')
        return self


class DescribeCustomizeRuleCountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCustomizeRuleCountResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponseBody, self).to_map()
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
            temp_model = DescribeCustomizeRuleCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleCountResponse, self).to_map()
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
            temp_model = DescribeCustomizeRuleCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestResponseBodyData(TeaModel):
    def __init__(self, id=None, simulate_data=None, status=None):
        self.id = id  # type: long
        self.simulate_data = simulate_data  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.simulate_data is not None:
            result['SimulateData'] = self.simulate_data
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SimulateData') is not None:
            self.simulate_data = m.get('SimulateData')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeCustomizeRuleTestResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponseBody, self).to_map()
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
            temp_model = DescribeCustomizeRuleTestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestResponse, self).to_map()
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
            temp_model = DescribeCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomizeRuleTestHistogramRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomizeRuleTestHistogramResponseBodyData(TeaModel):
    def __init__(self, count=None, from_=None, to=None):
        self.count = count  # type: long
        self.from_ = from_  # type: long
        self.to = to  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeCustomizeRuleTestHistogramResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeCustomizeRuleTestHistogramResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCustomizeRuleTestHistogramResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCustomizeRuleTestHistogramResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomizeRuleTestHistogramResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomizeRuleTestHistogramResponse, self).to_map()
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
            temp_model = DescribeCustomizeRuleTestHistogramResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeAndPlaybookRequest(TeaModel):
    def __init__(self, current_page=None, entity_type=None, incident_uuid=None, page_size=None, region_id=None):
        self.current_page = current_page  # type: int
        self.entity_type = entity_type  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList(TeaModel):
    def __init__(self, description=None, display_name=None, name=None, op_code=None, op_level=None, task_config=None,
                 waf_playbook=None):
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.name = name  # type: str
        self.op_code = op_code  # type: str
        self.op_level = op_level  # type: str
        self.task_config = task_config  # type: str
        self.waf_playbook = waf_playbook  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.op_code is not None:
            result['OpCode'] = self.op_code
        if self.op_level is not None:
            result['OpLevel'] = self.op_level
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config
        if self.waf_playbook is not None:
            result['WafPlaybook'] = self.waf_playbook
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OpCode') is not None:
            self.op_code = m.get('OpCode')
        if m.get('OpLevel') is not None:
            self.op_level = m.get('OpLevel')
        if m.get('TaskConfig') is not None:
            self.task_config = m.get('TaskConfig')
        if m.get('WafPlaybook') is not None:
            self.waf_playbook = m.get('WafPlaybook')
        return self


class DescribeDisposeAndPlaybookResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_num=None, dispose=None, entity_id=None, entity_info=None, opcode_map=None,
                 opcode_set=None, playbook_list=None, scope=None):
        self.alert_num = alert_num  # type: int
        self.dispose = dispose  # type: str
        self.entity_id = entity_id  # type: long
        self.entity_info = entity_info  # type: dict[str, any]
        self.opcode_map = opcode_map  # type: dict[str, str]
        self.opcode_set = opcode_set  # type: list[str]
        self.playbook_list = playbook_list  # type: list[DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList]
        self.scope = scope  # type: list[any]

    def validate(self):
        if self.playbook_list:
            for k in self.playbook_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_num is not None:
            result['AlertNum'] = self.alert_num
        if self.dispose is not None:
            result['Dispose'] = self.dispose
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.opcode_map is not None:
            result['OpcodeMap'] = self.opcode_map
        if self.opcode_set is not None:
            result['OpcodeSet'] = self.opcode_set
        result['PlaybookList'] = []
        if self.playbook_list is not None:
            for k in self.playbook_list:
                result['PlaybookList'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertNum') is not None:
            self.alert_num = m.get('AlertNum')
        if m.get('Dispose') is not None:
            self.dispose = m.get('Dispose')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('OpcodeMap') is not None:
            self.opcode_map = m.get('OpcodeMap')
        if m.get('OpcodeSet') is not None:
            self.opcode_set = m.get('OpcodeSet')
        self.playbook_list = []
        if m.get('PlaybookList') is not None:
            for k in m.get('PlaybookList'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseDataPlaybookList()
                self.playbook_list.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DescribeDisposeAndPlaybookResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeDisposeAndPlaybookResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeDisposeAndPlaybookResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeDisposeAndPlaybookResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeDisposeAndPlaybookResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeDisposeAndPlaybookResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeDisposeAndPlaybookResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponseBody, self).to_map()
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
            temp_model = DescribeDisposeAndPlaybookResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeAndPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDisposeAndPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDisposeAndPlaybookResponse, self).to_map()
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
            temp_model = DescribeDisposeAndPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisposeStrategyPlaybookRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDisposeStrategyPlaybookResponseBodyData(TeaModel):
    def __init__(self, playbook_name=None, playbook_uuid=None):
        self.playbook_name = playbook_name  # type: str
        self.playbook_uuid = playbook_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        return self


class DescribeDisposeStrategyPlaybookResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeDisposeStrategyPlaybookResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeDisposeStrategyPlaybookResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDisposeStrategyPlaybookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDisposeStrategyPlaybookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDisposeStrategyPlaybookResponse, self).to_map()
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
            temp_model = DescribeDisposeStrategyPlaybookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntityInfoRequest(TeaModel):
    def __init__(self, entity_id=None, entity_identity=None, incident_uuid=None, region_id=None,
                 sophon_task_id=None):
        self.entity_id = entity_id  # type: long
        self.entity_identity = entity_identity  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str
        self.sophon_task_id = sophon_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntityInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        return self


class DescribeEntityInfoResponseBodyData(TeaModel):
    def __init__(self, entity_id=None, entity_info=None, entity_type=None, tip_info=None):
        self.entity_id = entity_id  # type: long
        self.entity_info = entity_info  # type: dict[str, any]
        self.entity_type = entity_type  # type: str
        self.tip_info = tip_info  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEntityInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.tip_info is not None:
            result['TipInfo'] = self.tip_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityInfo') is not None:
            self.entity_info = m.get('EntityInfo')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('TipInfo') is not None:
            self.tip_info = m.get('TipInfo')
        return self


class DescribeEntityInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeEntityInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEntityInfoResponseBody, self).to_map()
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
            temp_model = DescribeEntityInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEntityInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEntityInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEntityInfoResponse, self).to_map()
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
            temp_model = DescribeEntityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventCountByThreatLevelRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelRequest, self).to_map()
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


class DescribeEventCountByThreatLevelResponseBodyData(TeaModel):
    def __init__(self, event_num=None, high_level_event_num=None, low_level_event_num=None,
                 medium_level_event_num=None, undeal_event_num=None):
        self.event_num = event_num  # type: long
        self.high_level_event_num = high_level_event_num  # type: long
        self.low_level_event_num = low_level_event_num  # type: long
        self.medium_level_event_num = medium_level_event_num  # type: long
        self.undeal_event_num = undeal_event_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_num is not None:
            result['EventNum'] = self.event_num
        if self.high_level_event_num is not None:
            result['HighLevelEventNum'] = self.high_level_event_num
        if self.low_level_event_num is not None:
            result['LowLevelEventNum'] = self.low_level_event_num
        if self.medium_level_event_num is not None:
            result['MediumLevelEventNum'] = self.medium_level_event_num
        if self.undeal_event_num is not None:
            result['UndealEventNum'] = self.undeal_event_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')
        if m.get('HighLevelEventNum') is not None:
            self.high_level_event_num = m.get('HighLevelEventNum')
        if m.get('LowLevelEventNum') is not None:
            self.low_level_event_num = m.get('LowLevelEventNum')
        if m.get('MediumLevelEventNum') is not None:
            self.medium_level_event_num = m.get('MediumLevelEventNum')
        if m.get('UndealEventNum') is not None:
            self.undeal_event_num = m.get('UndealEventNum')
        return self


class DescribeEventCountByThreatLevelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeEventCountByThreatLevelResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponseBody, self).to_map()
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
            temp_model = DescribeEventCountByThreatLevelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventCountByThreatLevelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventCountByThreatLevelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventCountByThreatLevelResponse, self).to_map()
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
            temp_model = DescribeEventCountByThreatLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventDisposeRequest(TeaModel):
    def __init__(self, current_page=None, incident_uuid=None, page_size=None, region_id=None):
        self.current_page = current_page  # type: int
        self.incident_uuid = incident_uuid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDisposeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEventDisposeResponseBodyDataReceiverInfo(TeaModel):
    def __init__(self, channel=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None,
                 message_title=None, receiver=None, status=None):
        self.channel = channel  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.message_title = message_title  # type: str
        self.receiver = receiver  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBodyDataReceiverInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.message_title is not None:
            result['MessageTitle'] = self.message_title
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('MessageTitle') is not None:
            self.message_title = m.get('MessageTitle')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBodyData(TeaModel):
    def __init__(self, event_dispose=None, receiver_info=None, remark=None, status=None):
        self.event_dispose = event_dispose  # type: list[any]
        self.receiver_info = receiver_info  # type: DescribeEventDisposeResponseBodyDataReceiverInfo
        self.remark = remark  # type: str
        self.status = status  # type: int

    def validate(self):
        if self.receiver_info:
            self.receiver_info.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info.to_map()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('ReceiverInfo') is not None:
            temp_model = DescribeEventDisposeResponseBodyDataReceiverInfo()
            self.receiver_info = temp_model.from_map(m['ReceiverInfo'])
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEventDisposeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeEventDisposeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponseBody, self).to_map()
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
            temp_model = DescribeEventDisposeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEventDisposeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventDisposeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventDisposeResponse, self).to_map()
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
            temp_model = DescribeEventDisposeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobStatusRequest(TeaModel):
    def __init__(self, region_id=None, submit_id=None):
        self.region_id = region_id  # type: str
        self.submit_id = submit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobStatusRequest, self).to_map()
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


class DescribeJobStatusResponseBodyDataErrTaskListProductListLogList(TeaModel):
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
        _map = super(DescribeJobStatusResponseBodyDataErrTaskListProductListLogList, self).to_map()
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


class DescribeJobStatusResponseBodyDataErrTaskListProductList(TeaModel):
    def __init__(self, log_list=None, product_code=None):
        self.log_list = log_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskListProductListLogList]
        self.product_code = product_code  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyDataErrTaskListProductList, self).to_map()
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeJobStatusResponseBodyDataErrTaskList(TeaModel):
    def __init__(self, product_list=None, user_id=None):
        self.product_list = product_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskListProductList]
        self.user_id = user_id  # type: long

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyDataErrTaskList, self).to_map()
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskListProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeJobStatusResponseBodyData(TeaModel):
    def __init__(self, config_id=None, err_task_list=None, failed_count=None, finish_count=None, folder_id=None,
                 task_count=None, task_status=None):
        self.config_id = config_id  # type: str
        self.err_task_list = err_task_list  # type: list[DescribeJobStatusResponseBodyDataErrTaskList]
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
        _map = super(DescribeJobStatusResponseBodyData, self).to_map()
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
                temp_model = DescribeJobStatusResponseBodyDataErrTaskList()
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


class DescribeJobStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeJobStatusResponseBodyData
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBody, self).to_map()
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
            temp_model = DescribeJobStatusResponseBodyData()
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


class DescribeJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponse, self).to_map()
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
            temp_model = DescribeJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogFieldsRequest(TeaModel):
    def __init__(self, log_source=None, log_type=None, region_id=None):
        self.log_source = log_source  # type: str
        self.log_type = log_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogFieldsResponseBodyData(TeaModel):
    def __init__(self, activity_name=None, field_desc=None, field_name=None, field_type=None, log_code=None):
        self.activity_name = activity_name  # type: str
        self.field_desc = field_desc  # type: str
        self.field_name = field_name  # type: str
        self.field_type = field_type  # type: str
        self.log_code = log_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogFieldsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.field_desc is not None:
            result['FieldDesc'] = self.field_desc
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('FieldDesc') is not None:
            self.field_desc = m.get('FieldDesc')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        return self


class DescribeLogFieldsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeLogFieldsResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogFieldsResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogFieldsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogFieldsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogFieldsResponse, self).to_map()
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
            temp_model = DescribeLogFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogSourceRequest(TeaModel):
    def __init__(self, log_type=None, region_id=None):
        self.log_type = log_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLogSourceResponseBodyData(TeaModel):
    def __init__(self, log_source=None, log_source_name=None):
        self.log_source = log_source  # type: str
        self.log_source_name = log_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_name is not None:
            result['LogSourceName'] = self.log_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceName') is not None:
            self.log_source_name = m.get('LogSourceName')
        return self


class DescribeLogSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeLogSourceResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogSourceResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogSourceResponse, self).to_map()
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
            temp_model = DescribeLogSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreRequest, self).to_map()
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


class DescribeLogStoreResponseBodyData(TeaModel):
    def __init__(self, append_meta=None, auto_split=None, enable_tracking=None, log_store_name=None,
                 max_split_shard=None, shard_count=None, ttl=None):
        self.append_meta = append_meta  # type: bool
        self.auto_split = auto_split  # type: bool
        self.enable_tracking = enable_tracking  # type: bool
        self.log_store_name = log_store_name  # type: str
        self.max_split_shard = max_split_shard  # type: int
        self.shard_count = shard_count  # type: int
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['AppendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['AutoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['EnableTracking'] = self.enable_tracking
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.max_split_shard is not None:
            result['MaxSplitShard'] = self.max_split_shard
        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppendMeta') is not None:
            self.append_meta = m.get('AppendMeta')
        if m.get('AutoSplit') is not None:
            self.auto_split = m.get('AutoSplit')
        if m.get('EnableTracking') is not None:
            self.enable_tracking = m.get('EnableTracking')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('MaxSplitShard') is not None:
            self.max_split_shard = m.get('MaxSplitShard')
        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeLogStoreResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeLogStoreResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeLogStoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = DescribeLogStoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogStoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogStoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogStoreResponse, self).to_map()
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
            temp_model = DescribeLogStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogTypeRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogTypeRequest, self).to_map()
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


class DescribeLogTypeResponseBodyData(TeaModel):
    def __init__(self, log_type=None, log_type_name=None):
        self.log_type = log_type  # type: str
        self.log_type_name = log_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_name is not None:
            result['LogTypeName'] = self.log_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeName') is not None:
            self.log_type_name = m.get('LogTypeName')
        return self


class DescribeLogTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeLogTypeResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogTypeResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeLogTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogTypeResponse, self).to_map()
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
            temp_model = DescribeLogTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOperatorsRequest(TeaModel):
    def __init__(self, region_id=None, scene_type=None):
        self.region_id = region_id  # type: str
        self.scene_type = scene_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOperatorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class DescribeOperatorsResponseBodyData(TeaModel):
    def __init__(self, index=None, operator=None, operator_desc_cn=None, operator_desc_en=None, operator_name=None,
                 support_data_type=None, support_tag=None):
        self.index = index  # type: int
        self.operator = operator  # type: str
        self.operator_desc_cn = operator_desc_cn  # type: str
        self.operator_desc_en = operator_desc_en  # type: str
        self.operator_name = operator_name  # type: str
        self.support_data_type = support_data_type  # type: str
        self.support_tag = support_tag  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOperatorsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_desc_cn is not None:
            result['OperatorDescCn'] = self.operator_desc_cn
        if self.operator_desc_en is not None:
            result['OperatorDescEn'] = self.operator_desc_en
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.support_data_type is not None:
            result['SupportDataType'] = self.support_data_type
        if self.support_tag is not None:
            result['SupportTag'] = self.support_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorDescCn') is not None:
            self.operator_desc_cn = m.get('OperatorDescCn')
        if m.get('OperatorDescEn') is not None:
            self.operator_desc_en = m.get('OperatorDescEn')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('SupportDataType') is not None:
            self.support_data_type = m.get('SupportDataType')
        if m.get('SupportTag') is not None:
            self.support_tag = m.get('SupportTag')
        return self


class DescribeOperatorsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeOperatorsResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOperatorsResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeOperatorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeOperatorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOperatorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOperatorsResponse, self).to_map()
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
            temp_model = DescribeOperatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScopeUsersRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScopeUsersRequest, self).to_map()
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


class DescribeScopeUsersResponseBodyData(TeaModel):
    def __init__(self, ali_uid=None, domains=None, instance_id=None, user_name=None):
        self.ali_uid = ali_uid  # type: long
        self.domains = domains  # type: list[str]
        self.instance_id = instance_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScopeUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeScopeUsersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeScopeUsersResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeScopeUsersResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeScopeUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeScopeUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeScopeUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScopeUsersResponse, self).to_map()
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
            temp_model = DescribeScopeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStorageRequest, self).to_map()
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


class DescribeStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStorageResponse, self).to_map()
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
            temp_model = DescribeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafScopeRequest(TeaModel):
    def __init__(self, entity_id=None, region_id=None):
        self.entity_id = entity_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWafScopeResponseBodyData(TeaModel):
    def __init__(self, aliuid=None, domains=None, instance_id=None):
        self.aliuid = aliuid  # type: long
        self.domains = domains  # type: list[str]
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafScopeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeWafScopeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeWafScopeResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWafScopeResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeWafScopeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWafScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWafScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWafScopeResponse, self).to_map()
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
            temp_model = DescribeWafScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhiteRuleListRequest(TeaModel):
    def __init__(self, alert_name=None, alert_type=None, current_page=None, incident_uuid=None, page_size=None,
                 region_id=None):
        self.alert_name = alert_name  # type: str
        self.alert_type = alert_type  # type: str
        self.current_page = current_page  # type: int
        self.incident_uuid = incident_uuid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeWhiteRuleListResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft(TeaModel):
    def __init__(self, is_var=None, modifier=None, modifier_param=None, type=None, value=None):
        self.is_var = is_var  # type: bool
        self.modifier = modifier  # type: str
        self.modifier_param = modifier_param  # type: dict[str, any]
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight(TeaModel):
    def __init__(self, is_var=None, modifier=None, modifier_param=None, type=None, value=None):
        self.is_var = is_var  # type: bool
        self.modifier = modifier  # type: str
        self.modifier_param = modifier_param  # type: dict[str, any]
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_var is not None:
            result['IsVar'] = self.is_var
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.modifier_param is not None:
            result['ModifierParam'] = self.modifier_param
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsVar') is not None:
            self.is_var = m.get('IsVar')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ModifierParam') is not None:
            self.modifier_param = m.get('ModifierParam')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions(TeaModel):
    def __init__(self, is_not=None, item_id=None, left=None, operator=None, right=None):
        self.is_not = is_not  # type: bool
        self.item_id = item_id  # type: int
        self.left = left  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft
        self.operator = operator  # type: str
        self.right = right  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight

    def validate(self):
        if self.left:
            self.left.validate()
        if self.right:
            self.right.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_not is not None:
            result['IsNot'] = self.is_not
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.left is not None:
            result['Left'] = self.left.to_map()
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.right is not None:
            result['Right'] = self.right.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsNot') is not None:
            self.is_not = m.get('IsNot')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Left') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsLeft()
            self.left = temp_model.from_map(m['Left'])
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Right') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditionsRight()
            self.right = temp_model.from_map(m['Right'])
        return self


class DescribeWhiteRuleListResponseBodyDataResponseDataExpression(TeaModel):
    def __init__(self, conditions=None, logic=None):
        self.conditions = conditions  # type: list[DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions]
        self.logic = logic  # type: str

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseDataExpression, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpressionConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class DescribeWhiteRuleListResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_name=None, alert_name_id=None, alert_type=None, alert_type_id=None, alert_uuid=None,
                 aliuid=None, expression=None, gmt_create=None, gmt_modified=None, id=None, incident_uuid=None, status=None,
                 sub_aliuid=None):
        self.alert_name = alert_name  # type: str
        self.alert_name_id = alert_name_id  # type: str
        self.alert_type = alert_type  # type: str
        self.alert_type_id = alert_type_id  # type: str
        self.alert_uuid = alert_uuid  # type: str
        self.aliuid = aliuid  # type: long
        self.expression = expression  # type: DescribeWhiteRuleListResponseBodyDataResponseDataExpression
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_uuid = incident_uuid  # type: str
        self.status = status  # type: int
        self.sub_aliuid = sub_aliuid  # type: long

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_name_id is not None:
            result['AlertNameId'] = self.alert_name_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_id is not None:
            result['AlertTypeId'] = self.alert_type_id
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.expression is not None:
            result['Expression'] = self.expression.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertNameId') is not None:
            self.alert_name_id = m.get('AlertNameId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeId') is not None:
            self.alert_type_id = m.get('AlertTypeId')
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Expression') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataResponseDataExpression()
            self.expression = temp_model.from_map(m['Expression'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        return self


class DescribeWhiteRuleListResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: DescribeWhiteRuleListResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[DescribeWhiteRuleListResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = DescribeWhiteRuleListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = DescribeWhiteRuleListResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class DescribeWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DescribeWhiteRuleListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponseBody, self).to_map()
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
            temp_model = DescribeWhiteRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWhiteRuleListResponse, self).to_map()
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
            temp_model = DescribeWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoQuickFieldRequest(TeaModel):
    def __init__(self, from_=None, index=None, page=None, region_id=None, reverse=None, size=None, to=None):
        self.from_ = from_  # type: int
        self.index = index  # type: str
        self.page = page  # type: int
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.size = size  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoQuickFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.index is not None:
            result['Index'] = self.index
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.size is not None:
            result['Size'] = self.size
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DoQuickFieldResponseBodyData(TeaModel):
    def __init__(self, agg_queryd=None, complete_or_not=None, count=None, has_sql=None, keys=None, limited=None,
                 logs=None, pquery=None, processed_rows=None, query_mode=None, where_query=None):
        self.agg_queryd = agg_queryd  # type: str
        self.complete_or_not = complete_or_not  # type: bool
        self.count = count  # type: int
        self.has_sql = has_sql  # type: bool
        self.keys = keys  # type: list[str]
        self.limited = limited  # type: long
        self.logs = logs  # type: list[any]
        self.pquery = pquery  # type: str
        self.processed_rows = processed_rows  # type: long
        self.query_mode = query_mode  # type: int
        self.where_query = where_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoQuickFieldResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_queryd is not None:
            result['AggQueryd'] = self.agg_queryd
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSQL'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.limited is not None:
            result['Limited'] = self.limited
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.pquery is not None:
            result['PQuery'] = self.pquery
        if self.processed_rows is not None:
            result['ProcessedRows'] = self.processed_rows
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.where_query is not None:
            result['WhereQuery'] = self.where_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AggQueryd') is not None:
            self.agg_queryd = m.get('AggQueryd')
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSQL') is not None:
            self.has_sql = m.get('HasSQL')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Limited') is not None:
            self.limited = m.get('Limited')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PQuery') is not None:
            self.pquery = m.get('PQuery')
        if m.get('ProcessedRows') is not None:
            self.processed_rows = m.get('ProcessedRows')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('WhereQuery') is not None:
            self.where_query = m.get('WhereQuery')
        return self


class DoQuickFieldResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DoQuickFieldResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DoQuickFieldResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = DoQuickFieldResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DoQuickFieldResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DoQuickFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoQuickFieldResponse, self).to_map()
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
            temp_model = DoQuickFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoSelfDelegateRequest(TeaModel):
    def __init__(self, ali_uid=None, delegate_or_not=None, region_id=None):
        self.ali_uid = ali_uid  # type: long
        self.delegate_or_not = delegate_or_not  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoSelfDelegateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.delegate_or_not is not None:
            result['DelegateOrNot'] = self.delegate_or_not
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DelegateOrNot') is not None:
            self.delegate_or_not = m.get('DelegateOrNot')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoSelfDelegateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoSelfDelegateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DoSelfDelegateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DoSelfDelegateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoSelfDelegateResponse, self).to_map()
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
            temp_model = DoSelfDelegateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCapacityRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityRequest, self).to_map()
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


class GetCapacityResponseBodyData(TeaModel):
    def __init__(self, exist_log_store=None, preserved_capacity=None, used_capacity=None):
        self.exist_log_store = exist_log_store  # type: bool
        self.preserved_capacity = preserved_capacity  # type: long
        self.used_capacity = used_capacity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_log_store is not None:
            result['ExistLogStore'] = self.exist_log_store
        if self.preserved_capacity is not None:
            result['PreservedCapacity'] = self.preserved_capacity
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExistLogStore') is not None:
            self.exist_log_store = m.get('ExistLogStore')
        if m.get('PreservedCapacity') is not None:
            self.preserved_capacity = m.get('PreservedCapacity')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class GetCapacityResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetCapacityResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetCapacityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCapacityResponse, self).to_map()
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
            temp_model = GetCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistogramsRequest(TeaModel):
    def __init__(self, from_=None, query=None, region_id=None, to=None):
        self.from_ = from_  # type: int
        self.query = query  # type: str
        self.region_id = region_id  # type: str
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyDataHistograms(TeaModel):
    def __init__(self, completed_or_not=None, count=None, from_=None, to=None):
        self.completed_or_not = completed_or_not  # type: bool
        self.count = count  # type: long
        self.from_ = from_  # type: int
        self.to = to  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHistogramsResponseBodyDataHistograms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed_or_not is not None:
            result['CompletedOrNot'] = self.completed_or_not
        if self.count is not None:
            result['Count'] = self.count
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletedOrNot') is not None:
            self.completed_or_not = m.get('CompletedOrNot')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetHistogramsResponseBodyData(TeaModel):
    def __init__(self, histograms=None, server=None, total_count=None):
        self.histograms = histograms  # type: list[GetHistogramsResponseBodyDataHistograms]
        self.server = server  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.histograms:
            for k in self.histograms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHistogramsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Histograms'] = []
        if self.histograms is not None:
            for k in self.histograms:
                result['Histograms'].append(k.to_map() if k else None)
        if self.server is not None:
            result['Server'] = self.server
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.histograms = []
        if m.get('Histograms') is not None:
            for k in m.get('Histograms'):
                temp_model = GetHistogramsResponseBodyDataHistograms()
                self.histograms.append(temp_model.from_map(k))
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetHistogramsResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHistogramsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetHistogramsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHistogramsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHistogramsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHistogramsResponse, self).to_map()
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
            temp_model = GetHistogramsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsRequest(TeaModel):
    def __init__(self, from_=None, page_index=None, page_size=None, query=None, region_id=None, reverse_or_not=None,
                 to=None, total=None):
        self.from_ = from_  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.region_id = region_id  # type: str
        self.reverse_or_not = reverse_or_not  # type: bool
        self.to = to  # type: int
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse_or_not is not None:
            result['ReverseOrNot'] = self.reverse_or_not
        if self.to is not None:
            result['To'] = self.to
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReverseOrNot') is not None:
            self.reverse_or_not = m.get('ReverseOrNot')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLogsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetLogsResponseBodyDataResponseData(TeaModel):
    def __init__(self, complete_or_not=None, cost=None, count=None, has_sql=None, keys=None, lines=None):
        self.complete_or_not = complete_or_not  # type: bool
        self.cost = cost  # type: long
        self.count = count  # type: int
        self.has_sql = has_sql  # type: bool
        self.keys = keys  # type: list[str]
        self.lines = lines  # type: list[any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_or_not is not None:
            result['CompleteOrNot'] = self.complete_or_not
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.count is not None:
            result['Count'] = self.count
        if self.has_sql is not None:
            result['HasSql'] = self.has_sql
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteOrNot') is not None:
            self.complete_or_not = m.get('CompleteOrNot')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HasSql') is not None:
            self.has_sql = m.get('HasSql')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class GetLogsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: GetLogsResponseBodyDataPageInfo
        self.response_data = response_data  # type: GetLogsResponseBodyDataResponseData

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            self.response_data.validate()

    def to_map(self):
        _map = super(GetLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.response_data is not None:
            result['ResponseData'] = self.response_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = GetLogsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('ResponseData') is not None:
            temp_model = GetLogsResponseBodyDataResponseData()
            self.response_data = temp_model.from_map(m['ResponseData'])
        return self


class GetLogsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetLogsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetLogsResponseBody, self).to_map()
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
            temp_model = GetLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogsResponse, self).to_map()
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
            temp_model = GetLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuickQueryRequest(TeaModel):
    def __init__(self, region_id=None, search_name=None):
        self.region_id = region_id  # type: str
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetQuickQueryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQuickQueryResponse, self).to_map()
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
            temp_model = GetQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStorageRequest, self).to_map()
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


class GetStorageResponseBodyData(TeaModel):
    def __init__(self, can_operate=None, display_region=None, region=None, ttl=None):
        self.can_operate = can_operate  # type: bool
        self.display_region = display_region  # type: bool
        self.region = region  # type: str
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStorageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate is not None:
            result['CanOperate'] = self.can_operate
        if self.display_region is not None:
            result['DisplayRegion'] = self.display_region
        if self.region is not None:
            result['Region'] = self.region
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanOperate') is not None:
            self.can_operate = m.get('CanOperate')
        if m.get('DisplayRegion') is not None:
            self.display_region = m.get('DisplayRegion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class GetStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetStorageResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = GetStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStorageResponse, self).to_map()
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
            temp_model = GetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutomateResponseConfigsRequest(TeaModel):
    def __init__(self, action_type=None, auto_response_type=None, current_page=None, id=None, page_size=None,
                 playbook_uuid=None, region_id=None, rule_name=None, status=None, sub_user_id=None):
        self.action_type = action_type  # type: str
        self.auto_response_type = auto_response_type  # type: str
        self.current_page = current_page  # type: int
        self.id = id  # type: long
        self.page_size = page_size  # type: int
        self.playbook_uuid = playbook_uuid  # type: str
        self.region_id = region_id  # type: str
        self.rule_name = rule_name  # type: str
        self.status = status  # type: int
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutomateResponseConfigsResponseBodyDataResponseData(TeaModel):
    def __init__(self, action_config=None, action_type=None, aliuid=None, auto_response_type=None,
                 execution_condition=None, gmt_create=None, gmt_modified=None, id=None, rule_name=None, status=None, sub_user_id=None):
        self.action_config = action_config  # type: str
        self.action_type = action_type  # type: str
        self.aliuid = aliuid  # type: long
        self.auto_response_type = auto_response_type  # type: str
        self.execution_condition = execution_condition  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.rule_name = rule_name  # type: str
        self.status = status  # type: int
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListAutomateResponseConfigsResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: ListAutomateResponseConfigsResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[ListAutomateResponseConfigsResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListAutomateResponseConfigsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListAutomateResponseConfigsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListAutomateResponseConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListAutomateResponseConfigsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponseBody, self).to_map()
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
            temp_model = ListAutomateResponseConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAutomateResponseConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAutomateResponseConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAutomateResponseConfigsResponse, self).to_map()
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
            temp_model = ListAutomateResponseConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemCustomizeRulesRequest(TeaModel):
    def __init__(self, alert_type=None, current_page=None, end_time=None, id=None, page_size=None, region_id=None,
                 rule_name=None, rule_type=None, start_time=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.id = id  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: int
        self.threat_level = threat_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemCustomizeRulesResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.alert_type_mds = alert_type_mds  # type: str
        self.aliuid = aliuid  # type: long
        self.event_transfer_ext = event_transfer_ext  # type: str
        self.event_transfer_switch = event_transfer_switch  # type: int
        self.event_transfer_type = event_transfer_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.log_source = log_source  # type: str
        self.log_source_mds = log_source_mds  # type: str
        self.log_type = log_type  # type: str
        self.log_type_mds = log_type_mds  # type: str
        self.query_cycle = query_cycle  # type: str
        self.rule_condition = rule_condition  # type: str
        self.rule_desc = rule_desc  # type: str
        self.rule_group = rule_group  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_threshold = rule_threshold  # type: str
        self.rule_type = rule_type  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemCustomizeRulesResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: ListCloudSiemCustomizeRulesResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[ListCloudSiemCustomizeRulesResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemCustomizeRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemCustomizeRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemCustomizeRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListCloudSiemCustomizeRulesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponseBody, self).to_map()
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
            temp_model = ListCloudSiemCustomizeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemCustomizeRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCloudSiemCustomizeRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudSiemCustomizeRulesResponse, self).to_map()
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
            temp_model = ListCloudSiemCustomizeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudSiemPredefinedRulesRequest(TeaModel):
    def __init__(self, alert_type=None, current_page=None, end_time=None, id=None, page_size=None, region_id=None,
                 rule_name=None, rule_type=None, start_time=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.id = id  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: int
        self.threat_level = threat_level  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCloudSiemPredefinedRulesResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_type=None, gmt_create=None, gmt_modified=None, id=None, rule_desc_mds=None,
                 rule_name=None, rule_name_mds=None, source=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.rule_desc_mds = rule_desc_mds  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_name_mds = rule_name_mds  # type: str
        self.source = source  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_desc_mds is not None:
            result['RuleDescMds'] = self.rule_desc_mds
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_name_mds is not None:
            result['RuleNameMds'] = self.rule_name_mds
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleDescMds') is not None:
            self.rule_desc_mds = m.get('RuleDescMds')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleNameMds') is not None:
            self.rule_name_mds = m.get('RuleNameMds')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class ListCloudSiemPredefinedRulesResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: ListCloudSiemPredefinedRulesResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[ListCloudSiemPredefinedRulesResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCloudSiemPredefinedRulesResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCloudSiemPredefinedRulesResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCloudSiemPredefinedRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListCloudSiemPredefinedRulesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponseBody, self).to_map()
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
            temp_model = ListCloudSiemPredefinedRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudSiemPredefinedRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCloudSiemPredefinedRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudSiemPredefinedRulesResponse, self).to_map()
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
            temp_model = ListCloudSiemPredefinedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomizeRuleTestResultRequest(TeaModel):
    def __init__(self, current_page=None, id=None, page_size=None, region_id=None):
        self.current_page = current_page  # type: int
        self.id = id  # type: long
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomizeRuleTestResultResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomizeRuleTestResultResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_desc=None, alert_detail=None, alert_src_prod=None, alert_src_prod_module=None,
                 att_ck=None, event_name=None, event_type=None, level=None, log_source=None, log_time=None, log_type=None,
                 main_user_id=None, online_status=None, sub_user_id=None, uuid=None):
        self.alert_desc = alert_desc  # type: str
        self.alert_detail = alert_detail  # type: str
        self.alert_src_prod = alert_src_prod  # type: str
        self.alert_src_prod_module = alert_src_prod_module  # type: str
        self.att_ck = att_ck  # type: str
        self.event_name = event_name  # type: str
        self.event_type = event_type  # type: str
        self.level = level  # type: str
        self.log_source = log_source  # type: str
        self.log_time = log_time  # type: str
        self.log_type = log_type  # type: str
        self.main_user_id = main_user_id  # type: str
        self.online_status = online_status  # type: str
        self.sub_user_id = sub_user_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc
        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail
        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod
        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module
        if self.att_ck is not None:
            result['AttCk'] = self.att_ck
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.level is not None:
            result['Level'] = self.level
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')
        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')
        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')
        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')
        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListCustomizeRuleTestResultResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: ListCustomizeRuleTestResultResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[ListCustomizeRuleTestResultResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListCustomizeRuleTestResultResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListCustomizeRuleTestResultResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListCustomizeRuleTestResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListCustomizeRuleTestResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponseBody, self).to_map()
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
            temp_model = ListCustomizeRuleTestResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCustomizeRuleTestResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomizeRuleTestResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomizeRuleTestResultResponse, self).to_map()
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
            temp_model = ListCustomizeRuleTestResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeliveryRequest, self).to_map()
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


class ListDeliveryResponseBodyDataProductListLogListExtraParameters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductListLogListExtraParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDeliveryResponseBodyDataProductListLogList(TeaModel):
    def __init__(self, can_operate_or_not=None, extra_parameters=None, log_code=None, log_name=None,
                 log_name_en=None, log_name_key=None, status=None, topic=None):
        self.can_operate_or_not = can_operate_or_not  # type: bool
        self.extra_parameters = extra_parameters  # type: list[ListDeliveryResponseBodyDataProductListLogListExtraParameters]
        self.log_code = log_code  # type: str
        self.log_name = log_name  # type: str
        self.log_name_en = log_name_en  # type: str
        self.log_name_key = log_name_key  # type: str
        self.status = status  # type: bool
        self.topic = topic  # type: str

    def validate(self):
        if self.extra_parameters:
            for k in self.extra_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductListLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_operate_or_not is not None:
            result['CanOperateOrNot'] = self.can_operate_or_not
        result['ExtraParameters'] = []
        if self.extra_parameters is not None:
            for k in self.extra_parameters:
                result['ExtraParameters'].append(k.to_map() if k else None)
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_name_en is not None:
            result['LogNameEn'] = self.log_name_en
        if self.log_name_key is not None:
            result['LogNameKey'] = self.log_name_key
        if self.status is not None:
            result['Status'] = self.status
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanOperateOrNot') is not None:
            self.can_operate_or_not = m.get('CanOperateOrNot')
        self.extra_parameters = []
        if m.get('ExtraParameters') is not None:
            for k in m.get('ExtraParameters'):
                temp_model = ListDeliveryResponseBodyDataProductListLogListExtraParameters()
                self.extra_parameters.append(temp_model.from_map(k))
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogNameEn') is not None:
            self.log_name_en = m.get('LogNameEn')
        if m.get('LogNameKey') is not None:
            self.log_name_key = m.get('LogNameKey')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListDeliveryResponseBodyDataProductList(TeaModel):
    def __init__(self, log_list=None, log_map=None, product_code=None, product_name=None):
        self.log_list = log_list  # type: list[ListDeliveryResponseBodyDataProductListLogList]
        self.log_map = log_map  # type: dict[str, list[DataProductListLogMapValue]]
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()
        if self.log_map:
            for v in self.log_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyDataProductList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        result['LogMap'] = {}
        if self.log_map is not None:
            for k, v in self.log_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['logMap'][k] = l1
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = ListDeliveryResponseBodyDataProductListLogList()
                self.log_list.append(temp_model.from_map(k))
        self.log_map = {}
        if m.get('LogMap') is not None:
            for k, v in m.get('LogMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataProductListLogMapValue()
                    l1.append(temp_model.from_map(k1))
                self.log_map['k'] = l1
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListDeliveryResponseBodyData(TeaModel):
    def __init__(self, dashboard_url=None, display_switch_or_not=None, log_store_name=None, product_list=None,
                 project_name=None, search_url=None):
        self.dashboard_url = dashboard_url  # type: str
        self.display_switch_or_not = display_switch_or_not  # type: bool
        self.log_store_name = log_store_name  # type: str
        self.product_list = product_list  # type: list[ListDeliveryResponseBodyDataProductList]
        self.project_name = project_name  # type: str
        self.search_url = search_url  # type: str

    def validate(self):
        if self.product_list:
            for k in self.product_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_url is not None:
            result['DashboardUrl'] = self.dashboard_url
        if self.display_switch_or_not is not None:
            result['DisplaySwitchOrNot'] = self.display_switch_or_not
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        result['ProductList'] = []
        if self.product_list is not None:
            for k in self.product_list:
                result['ProductList'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.search_url is not None:
            result['SearchUrl'] = self.search_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardUrl') is not None:
            self.dashboard_url = m.get('DashboardUrl')
        if m.get('DisplaySwitchOrNot') is not None:
            self.display_switch_or_not = m.get('DisplaySwitchOrNot')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        self.product_list = []
        if m.get('ProductList') is not None:
            for k in m.get('ProductList'):
                temp_model = ListDeliveryResponseBodyDataProductList()
                self.product_list.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SearchUrl') is not None:
            self.search_url = m.get('SearchUrl')
        return self


class ListDeliveryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListDeliveryResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListDeliveryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeliveryResponse, self).to_map()
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
            temp_model = ListDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisposeStrategyRequest(TeaModel):
    def __init__(self, current_page=None, effective_status=None, end_time=None, entity_identity=None,
                 entity_type=None, order=None, order_field=None, page_size=None, playbook_name=None, playbook_types=None,
                 playbook_uuid=None, region_id=None, sophon_task_id=None, start_time=None):
        self.current_page = current_page  # type: int
        self.effective_status = effective_status  # type: int
        self.end_time = end_time  # type: long
        self.entity_identity = entity_identity  # type: str
        self.entity_type = entity_type  # type: str
        self.order = order  # type: str
        self.order_field = order_field  # type: str
        self.page_size = page_size  # type: int
        self.playbook_name = playbook_name  # type: str
        self.playbook_types = playbook_types  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.region_id = region_id  # type: str
        self.sophon_task_id = sophon_task_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.order is not None:
            result['Order'] = self.order
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_types is not None:
            result['PlaybookTypes'] = self.playbook_types
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookTypes') is not None:
            self.playbook_types = m.get('PlaybookTypes')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDisposeStrategyResponseBodyDataPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyDataPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDisposeStrategyResponseBodyDataResponseData(TeaModel):
    def __init__(self, alert_uuid=None, aliuid=None, effective_status=None, entity=None, entity_id=None,
                 entity_type=None, error_message=None, finish_time=None, gmt_create=None, gmt_modified=None, id=None,
                 incident_name=None, incident_uuid=None, playbook_name=None, playbook_type=None, playbook_uuid=None, scope=None,
                 sophon_task_id=None, status=None, sub_aliuid=None, task_param=None):
        self.alert_uuid = alert_uuid  # type: str
        self.aliuid = aliuid  # type: long
        self.effective_status = effective_status  # type: int
        self.entity = entity  # type: list[any]
        self.entity_id = entity_id  # type: long
        self.entity_type = entity_type  # type: str
        self.error_message = error_message  # type: str
        self.finish_time = finish_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.incident_name = incident_name  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.playbook_name = playbook_name  # type: str
        self.playbook_type = playbook_type  # type: str
        self.playbook_uuid = playbook_uuid  # type: str
        self.scope = scope  # type: list[any]
        self.sophon_task_id = sophon_task_id  # type: str
        self.status = status  # type: int
        self.sub_aliuid = sub_aliuid  # type: long
        self.task_param = task_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyDataResponseData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status
        if self.entity is not None:
            result['Entity'] = self.entity
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name
        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type
        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')
        if m.get('Entity') is not None:
            self.entity = m.get('Entity')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')
        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')
        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        return self


class ListDisposeStrategyResponseBodyData(TeaModel):
    def __init__(self, page_info=None, response_data=None):
        self.page_info = page_info  # type: ListDisposeStrategyResponseBodyDataPageInfo
        self.response_data = response_data  # type: list[ListDisposeStrategyResponseBodyDataResponseData]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for k in self.response_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        result['ResponseData'] = []
        if self.response_data is not None:
            for k in self.response_data:
                result['ResponseData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListDisposeStrategyResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        self.response_data = []
        if m.get('ResponseData') is not None:
            for k in m.get('ResponseData'):
                temp_model = ListDisposeStrategyResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k))
        return self


class ListDisposeStrategyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListDisposeStrategyResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponseBody, self).to_map()
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
            temp_model = ListDisposeStrategyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDisposeStrategyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDisposeStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDisposeStrategyResponse, self).to_map()
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
            temp_model = ListDisposeStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationRequest, self).to_map()
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


class ListOperationResponseBodyData(TeaModel):
    def __init__(self, admin_or_not=None, operation_list=None):
        self.admin_or_not = admin_or_not  # type: bool
        self.operation_list = operation_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_or_not is not None:
            result['AdminOrNot'] = self.admin_or_not
        if self.operation_list is not None:
            result['OperationList'] = self.operation_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdminOrNot') is not None:
            self.admin_or_not = m.get('AdminOrNot')
        if m.get('OperationList') is not None:
            self.operation_list = m.get('OperationList')
        return self


class ListOperationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListOperationResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListOperationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListOperationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOperationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOperationResponse, self).to_map()
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
            temp_model = ListOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuickQueryRequest(TeaModel):
    def __init__(self, offset=None, page_size=None, region_id=None):
        self.offset = offset  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListQuickQueryResponseBodyDataQuickQueryList(TeaModel):
    def __init__(self, display_name=None, query=None, search_name=None):
        self.display_name = display_name  # type: str
        self.query = query  # type: str
        self.search_name = search_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuickQueryResponseBodyDataQuickQueryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListQuickQueryResponseBodyData(TeaModel):
    def __init__(self, count=None, quick_query_list=None, total=None):
        self.count = count  # type: int
        self.quick_query_list = quick_query_list  # type: list[ListQuickQueryResponseBodyDataQuickQueryList]
        self.total = total  # type: int

    def validate(self):
        if self.quick_query_list:
            for k in self.quick_query_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['QuickQueryList'] = []
        if self.quick_query_list is not None:
            for k in self.quick_query_list:
                result['QuickQueryList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.quick_query_list = []
        if m.get('QuickQueryList') is not None:
            for k in m.get('QuickQueryList'):
                temp_model = ListQuickQueryResponseBodyDataQuickQueryList()
                self.quick_query_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQuickQueryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListQuickQueryResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ListQuickQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuickQueryResponse, self).to_map()
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
            temp_model = ListQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDeliveryRequest(TeaModel):
    def __init__(self, log_code=None, product_code=None, region_id=None):
        self.log_code = log_code  # type: str
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_code is not None:
            result['LogCode'] = self.log_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenDeliveryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OpenDeliveryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenDeliveryResponse, self).to_map()
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
            temp_model = OpenDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostAutomateResponseConfigRequest(TeaModel):
    def __init__(self, action_config=None, action_type=None, auto_response_type=None, execution_condition=None,
                 id=None, region_id=None, rule_name=None, sub_user_id=None):
        self.action_config = action_config  # type: str
        self.action_type = action_type  # type: str
        self.auto_response_type = auto_response_type  # type: str
        self.execution_condition = execution_condition  # type: str
        self.id = id  # type: long
        self.region_id = region_id  # type: str
        self.rule_name = rule_name  # type: str
        self.sub_user_id = sub_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostAutomateResponseConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type
        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')
        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class PostAutomateResponseConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostAutomateResponseConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostAutomateResponseConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostAutomateResponseConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostAutomateResponseConfigResponse, self).to_map()
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
            temp_model = PostAutomateResponseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleRequest(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, event_transfer_ext=None, event_transfer_switch=None,
                 event_transfer_type=None, id=None, log_source=None, log_source_mds=None, log_type=None, log_type_mds=None,
                 query_cycle=None, region_id=None, rule_condition=None, rule_desc=None, rule_group=None, rule_name=None,
                 rule_threshold=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.alert_type_mds = alert_type_mds  # type: str
        self.event_transfer_ext = event_transfer_ext  # type: str
        self.event_transfer_switch = event_transfer_switch  # type: int
        self.event_transfer_type = event_transfer_type  # type: str
        self.id = id  # type: long
        self.log_source = log_source  # type: str
        self.log_source_mds = log_source_mds  # type: str
        self.log_type = log_type  # type: str
        self.log_type_mds = log_type_mds  # type: str
        self.query_cycle = query_cycle  # type: str
        self.region_id = region_id  # type: str
        self.rule_condition = rule_condition  # type: str
        self.rule_desc = rule_desc  # type: str
        self.rule_group = rule_group  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_threshold = rule_threshold  # type: str
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBodyData(TeaModel):
    def __init__(self, alert_type=None, alert_type_mds=None, aliuid=None, event_transfer_ext=None,
                 event_transfer_switch=None, event_transfer_type=None, gmt_create=None, gmt_modified=None, id=None, log_source=None,
                 log_source_mds=None, log_type=None, log_type_mds=None, query_cycle=None, rule_condition=None, rule_desc=None,
                 rule_group=None, rule_name=None, rule_threshold=None, rule_type=None, status=None, threat_level=None):
        self.alert_type = alert_type  # type: str
        self.alert_type_mds = alert_type_mds  # type: str
        self.aliuid = aliuid  # type: long
        self.event_transfer_ext = event_transfer_ext  # type: str
        self.event_transfer_switch = event_transfer_switch  # type: int
        self.event_transfer_type = event_transfer_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.log_source = log_source  # type: str
        self.log_source_mds = log_source_mds  # type: str
        self.log_type = log_type  # type: str
        self.log_type_mds = log_type_mds  # type: str
        self.query_cycle = query_cycle  # type: str
        self.rule_condition = rule_condition  # type: str
        self.rule_desc = rule_desc  # type: str
        self.rule_group = rule_group  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_threshold = rule_threshold  # type: str
        self.rule_type = rule_type  # type: str
        self.status = status  # type: int
        self.threat_level = threat_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_type_mds is not None:
            result['AlertTypeMds'] = self.alert_type_mds
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.event_transfer_ext is not None:
            result['EventTransferExt'] = self.event_transfer_ext
        if self.event_transfer_switch is not None:
            result['EventTransferSwitch'] = self.event_transfer_switch
        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.log_source_mds is not None:
            result['LogSourceMds'] = self.log_source_mds
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.log_type_mds is not None:
            result['LogTypeMds'] = self.log_type_mds
        if self.query_cycle is not None:
            result['QueryCycle'] = self.query_cycle
        if self.rule_condition is not None:
            result['RuleCondition'] = self.rule_condition
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_threshold is not None:
            result['RuleThreshold'] = self.rule_threshold
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertTypeMds') is not None:
            self.alert_type_mds = m.get('AlertTypeMds')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('EventTransferExt') is not None:
            self.event_transfer_ext = m.get('EventTransferExt')
        if m.get('EventTransferSwitch') is not None:
            self.event_transfer_switch = m.get('EventTransferSwitch')
        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('LogSourceMds') is not None:
            self.log_source_mds = m.get('LogSourceMds')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('LogTypeMds') is not None:
            self.log_type_mds = m.get('LogTypeMds')
        if m.get('QueryCycle') is not None:
            self.query_cycle = m.get('QueryCycle')
        if m.get('RuleCondition') is not None:
            self.rule_condition = m.get('RuleCondition')
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleThreshold') is not None:
            self.rule_threshold = m.get('RuleThreshold')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        return self


class PostCustomizeRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: PostCustomizeRuleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleResponseBody, self).to_map()
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
            temp_model = PostCustomizeRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostCustomizeRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostCustomizeRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleResponse, self).to_map()
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
            temp_model = PostCustomizeRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None, simulated_data=None, test_type=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str
        self.simulated_data = simulated_data  # type: str
        self.test_type = test_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.simulated_data is not None:
            result['SimulatedData'] = self.simulated_data
        if self.test_type is not None:
            result['TestType'] = self.test_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SimulatedData') is not None:
            self.simulated_data = m.get('SimulatedData')
        if m.get('TestType') is not None:
            self.test_type = m.get('TestType')
        return self


class PostCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostCustomizeRuleTestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostCustomizeRuleTestResponse, self).to_map()
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
            temp_model = PostCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventDisposeAndWhiteruleListRequest(TeaModel):
    def __init__(self, event_dispose=None, incident_uuid=None, receiver_info=None, region_id=None, remark=None,
                 status=None):
        self.event_dispose = event_dispose  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.receiver_info = receiver_info  # type: str
        self.region_id = region_id  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('ReceiverInfo') is not None:
            self.receiver_info = m.get('ReceiverInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostEventDisposeAndWhiteruleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEventDisposeAndWhiteruleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostEventDisposeAndWhiteruleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostEventDisposeAndWhiteruleListResponse, self).to_map()
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
            temp_model = PostEventDisposeAndWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEventWhiteruleListRequest(TeaModel):
    def __init__(self, incident_uuid=None, region_id=None, whiterule_list=None):
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str
        self.whiterule_list = whiterule_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventWhiteruleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.whiterule_list is not None:
            result['WhiteruleList'] = self.whiterule_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteruleList') is not None:
            self.whiterule_list = m.get('WhiteruleList')
        return self


class PostEventWhiteruleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEventWhiteruleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEventWhiteruleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostEventWhiteruleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostEventWhiteruleListResponse, self).to_map()
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
            temp_model = PostEventWhiteruleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostFinishCustomizeRuleTestRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PostFinishCustomizeRuleTestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostFinishCustomizeRuleTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostFinishCustomizeRuleTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostFinishCustomizeRuleTestResponse, self).to_map()
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
            temp_model = PostFinishCustomizeRuleTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostRuleStatusChangeRequest(TeaModel):
    def __init__(self, ids=None, in_use=None, region_id=None, rule_type=None):
        self.ids = ids  # type: str
        self.in_use = in_use  # type: bool
        self.region_id = region_id  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostRuleStatusChangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class PostRuleStatusChangeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostRuleStatusChangeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostRuleStatusChangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostRuleStatusChangeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostRuleStatusChangeResponse, self).to_map()
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
            temp_model = PostRuleStatusChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreCapacityRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreCapacityRequest, self).to_map()
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


class RestoreCapacityResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestoreCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreCapacityResponse, self).to_map()
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
            temp_model = RestoreCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveQuickQueryRequest(TeaModel):
    def __init__(self, display_name=None, query=None, region_id=None):
        self.display_name = display_name  # type: str
        self.query = query  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveQuickQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SaveQuickQueryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveQuickQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveQuickQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveQuickQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveQuickQueryResponse, self).to_map()
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
            temp_model = SaveQuickQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetStorageRequest(TeaModel):
    def __init__(self, region=None, region_id=None, ttl=None):
        self.region = region  # type: str
        self.region_id = region_id  # type: str
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SetStorageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetStorageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetStorageResponse, self).to_map()
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
            temp_model = SetStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShowQuickAnalysisRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShowQuickAnalysisRequest, self).to_map()
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


class ShowQuickAnalysisResponseBodyData(TeaModel):
    def __init__(self, index_list=None):
        self.index_list = index_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShowQuickAnalysisResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_list is not None:
            result['IndexList'] = self.index_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IndexList') is not None:
            self.index_list = m.get('IndexList')
        return self


class ShowQuickAnalysisResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dy_code=None, dy_message=None, err_code=None, message=None,
                 request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ShowQuickAnalysisResponseBodyData
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str
        self.err_code = err_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ShowQuickAnalysisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dy_code is not None:
            result['DyCode'] = self.dy_code
        if self.dy_message is not None:
            result['DyMessage'] = self.dy_message
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
            temp_model = ShowQuickAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DyCode') is not None:
            self.dy_code = m.get('DyCode')
        if m.get('DyMessage') is not None:
            self.dy_message = m.get('DyMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ShowQuickAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShowQuickAnalysisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ShowQuickAnalysisResponse, self).to_map()
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
            temp_model = ShowQuickAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutomateResponseConfigStatusRequest(TeaModel):
    def __init__(self, ids=None, in_use=None, region_id=None):
        self.ids = ids  # type: str
        self.in_use = in_use  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.in_use is not None:
            result['InUse'] = self.in_use
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAutomateResponseConfigStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutomateResponseConfigStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAutomateResponseConfigStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAutomateResponseConfigStatusResponse, self).to_map()
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
            temp_model = UpdateAutomateResponseConfigStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWhiteRuleListRequest(TeaModel):
    def __init__(self, expression=None, incident_uuid=None, region_id=None, white_rule_id=None):
        self.expression = expression  # type: str
        self.incident_uuid = incident_uuid  # type: str
        self.region_id = region_id  # type: str
        self.white_rule_id = white_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_rule_id is not None:
            result['WhiteRuleId'] = self.white_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteRuleId') is not None:
            self.white_rule_id = m.get('WhiteRuleId')
        return self


class UpdateWhiteRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWhiteRuleListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWhiteRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWhiteRuleListResponse, self).to_map()
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
            temp_model = UpdateWhiteRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


