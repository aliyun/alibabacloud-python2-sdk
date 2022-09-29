# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateCampaignRequest(TeaModel):
    def __init__(self, name=None, remark=None):
        self.name = name  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCampaignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateCampaignResponseBodyData(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, remark=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCampaignResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateCampaignResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateCampaignResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateCampaignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateCampaignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCampaignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCampaignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCampaignResponse, self).to_map()
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
            temp_model = CreateCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, algorithm=None, column=None, filter=None, inference_job_id=None, name=None, phone_number=None,
                 project=None, remark=None, source=None, table=None, text=None, uri=None):
        self.algorithm = algorithm  # type: str
        self.column = column  # type: str
        self.filter = filter  # type: str
        self.inference_job_id = inference_job_id  # type: str
        self.name = name  # type: str
        self.phone_number = phone_number  # type: bool
        self.project = project  # type: str
        self.remark = remark  # type: str
        self.source = source  # type: int
        self.table = table  # type: str
        self.text = text  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.column is not None:
            result['Column'] = self.column
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateGroupResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, amount=None, column=None, created_time=None, filter=None, id=None,
                 inference_job_id=None, name=None, phone_number=None, project=None, remark=None, source=None, status=None, table=None,
                 text=None, updated_time=None, uri=None):
        self.algorithm = algorithm  # type: str
        self.amount = amount  # type: int
        self.column = column  # type: str
        self.created_time = created_time  # type: str
        self.filter = filter  # type: str
        self.id = id  # type: str
        self.inference_job_id = inference_job_id  # type: str
        self.name = name  # type: str
        self.phone_number = phone_number  # type: bool
        self.project = project  # type: str
        self.remark = remark  # type: str
        self.source = source  # type: int
        self.status = status  # type: int
        self.table = table  # type: str
        self.text = text  # type: str
        self.updated_time = updated_time  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateGroupResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInferenceJobRequest(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, data_path=None, name=None, remark=None, target_path=None,
                 training_job_id=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.data_path = data_path  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.target_path = target_path  # type: str
        self.training_job_id = training_job_id  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInferenceJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateInferenceJobResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, group_id=None,
                 history=None, id=None, name=None, remark=None, status=None, target_path=None, training_job_id=None,
                 updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.group_id = group_id  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.target_path = target_path  # type: str
        self.training_job_id = training_job_id  # type: str
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInferenceJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateInferenceJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateInferenceJobResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateInferenceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInferenceJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInferenceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInferenceJobResponse, self).to_map()
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
            temp_model = CreateInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleRequest(TeaModel):
    def __init__(self, end_time=None, execute_time=None, group_id=None, name=None, repeat_cycle=None,
                 repeat_cycle_unit=None, repeat_times=None, sign_name=None, signature_id=None, template_code=None, template_id=None):
        self.end_time = end_time  # type: int
        self.execute_time = execute_time  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.repeat_cycle = repeat_cycle  # type: int
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        self.repeat_times = repeat_times  # type: int
        self.sign_name = sign_name  # type: str
        self.signature_id = signature_id  # type: str
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateScheduleResponseBodyData(TeaModel):
    def __init__(self, created_time=None, end_time=None, execute_time=None, group_id=None, id=None, name=None,
                 repeat_cycle=None, repeat_cycle_unit=None, repeat_times=None, sign_name=None, signature_id=None, status=None,
                 template_code=None, template_id=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.end_time = end_time  # type: int
        self.execute_time = execute_time  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.repeat_cycle = repeat_cycle  # type: int
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        self.repeat_times = repeat_times  # type: int
        self.sign_name = sign_name  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateScheduleResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateScheduleResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateScheduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScheduleResponse, self).to_map()
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
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSignatureRequest(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSignatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSignatureResponseBodyData(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, status=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSignatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateSignatureResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSignatureResponse, self).to_map()
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
            temp_model = CreateSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, content=None, description=None, name=None, signature=None, signature_id=None, type=None):
        self.content = content  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.signature = signature  # type: str
        self.signature_id = signature_id  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBodyData(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        self.content = content  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.reason = reason  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.type = type  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateTemplateResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainingJobRequest(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, data_path=None, name=None, remark=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.data_path = data_path  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateTrainingJobResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, history=None, id=None,
                 name=None, remark=None, status=None, updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrainingJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class CreateTrainingJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: CreateTrainingJobResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTrainingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateTrainingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrainingJobResponse, self).to_map()
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
            temp_model = CreateTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCampaignResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCampaignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCampaignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCampaignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCampaignResponse, self).to_map()
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
            temp_model = DeleteCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupResponse, self).to_map()
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInferenceJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInferenceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInferenceJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInferenceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInferenceJobResponse, self).to_map()
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
            temp_model = DeleteInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScheduleResponse, self).to_map()
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
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSignatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSignatureResponse, self).to_map()
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
            temp_model = DeleteSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrainingJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrainingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrainingJobResponse, self).to_map()
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
            temp_model = DeleteTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlgorithmResponseBodyData(TeaModel):
    def __init__(self, description=None, id=None, infer_user_config_map=None, name=None, train_user_config_map=None):
        self.description = description  # type: str
        self.id = id  # type: str
        self.infer_user_config_map = infer_user_config_map  # type: str
        self.name = name  # type: str
        self.train_user_config_map = train_user_config_map  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlgorithmResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.infer_user_config_map is not None:
            result['InferUserConfigMap'] = self.infer_user_config_map
        if self.name is not None:
            result['Name'] = self.name
        if self.train_user_config_map is not None:
            result['TrainUserConfigMap'] = self.train_user_config_map
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferUserConfigMap') is not None:
            self.infer_user_config_map = m.get('InferUserConfigMap')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TrainUserConfigMap') is not None:
            self.train_user_config_map = m.get('TrainUserConfigMap')
        return self


class GetAlgorithmResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetAlgorithmResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAlgorithmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAlgorithmResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlgorithmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlgorithmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlgorithmResponse, self).to_map()
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
            temp_model = GetAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCampaignResponseBodyData(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, remark=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCampaignResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetCampaignResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetCampaignResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCampaignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCampaignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCampaignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCampaignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCampaignResponse, self).to_map()
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
            temp_model = GetCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, amount=None, campaign_id=None, column=None, created_time=None, filter=None,
                 history=None, id=None, inference_job_id=None, name=None, phone_number=None, project=None, remark=None,
                 source=None, status=None, table=None, text=None, updated_time=None, uri=None):
        self.algorithm = algorithm  # type: str
        self.amount = amount  # type: int
        self.campaign_id = campaign_id  # type: str
        self.column = column  # type: str
        self.created_time = created_time  # type: str
        self.filter = filter  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.inference_job_id = inference_job_id  # type: str
        self.name = name  # type: str
        self.phone_number = phone_number  # type: bool
        self.project = project  # type: str
        self.remark = remark  # type: str
        self.source = source  # type: int
        self.status = status  # type: int
        self.table = table  # type: str
        self.text = text  # type: str
        self.updated_time = updated_time  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetGroupResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupResponse, self).to_map()
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
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInferenceJobResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, group_id=None,
                 history=None, id=None, name=None, remark=None, status=None, target_path=None, training_job_id=None,
                 updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.group_id = group_id  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.target_path = target_path  # type: str
        self.training_job_id = training_job_id  # type: str
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInferenceJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class GetInferenceJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetInferenceJobResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInferenceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetInferenceJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInferenceJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInferenceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInferenceJobResponse, self).to_map()
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
            temp_model = GetInferenceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageConfigResponseBodyData(TeaModel):
    def __init__(self, sms_report_url=None, sms_up_url=None):
        self.sms_report_url = sms_report_url  # type: str
        self.sms_up_url = sms_up_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sms_report_url is not None:
            result['SmsReportUrl'] = self.sms_report_url
        if self.sms_up_url is not None:
            result['SmsUpUrl'] = self.sms_up_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SmsReportUrl') is not None:
            self.sms_report_url = m.get('SmsReportUrl')
        if m.get('SmsUpUrl') is not None:
            self.sms_up_url = m.get('SmsUpUrl')
        return self


class GetMessageConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetMessageConfigResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMessageConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMessageConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMessageConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMessageConfigResponse, self).to_map()
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
            temp_model = GetMessageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduleResponseBodyData(TeaModel):
    def __init__(self, created_time=None, end_time=None, execute_time=None, group_id=None, history=None, id=None,
                 name=None, repeat_cycle=None, repeat_cycle_unit=None, repeat_times=None, sign_name=None,
                 signature_id=None, status=None, template_code=None, template_id=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.end_time = end_time  # type: int
        self.execute_time = execute_time  # type: str
        self.group_id = group_id  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.repeat_cycle = repeat_cycle  # type: int
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        self.repeat_times = repeat_times  # type: int
        self.sign_name = sign_name  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScheduleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetScheduleResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetScheduleResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetScheduleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetScheduleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetScheduleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScheduleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScheduleResponse, self).to_map()
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
            temp_model = GetScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSignatureResponseBodyData(TeaModel):
    def __init__(self, created_time=None, description=None, id=None, name=None, reason=None, status=None,
                 updated_time=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSignatureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetSignatureResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetSignatureResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSignatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSignatureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSignatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSignatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSignatureResponse, self).to_map()
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
            temp_model = GetSignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        self.content = content  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.reason = reason  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.type = type  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetTemplateResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainingJobResponseBodyData(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, history=None, id=None,
                 name=None, remark=None, status=None, updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTrainingJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class GetTrainingJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetTrainingJobResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTrainingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTrainingJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTrainingJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTrainingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTrainingJobResponse, self).to_map()
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
            temp_model = GetTrainingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(self, account_status=None):
        self.account_status = account_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: GetUserResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmsRequest(TeaModel):
    def __init__(self, id=None, name=None, page_number=None, page_size=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlgorithmsResponseBodyDataAlgorithms(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlgorithmsResponseBodyDataAlgorithms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAlgorithmsResponseBodyData(TeaModel):
    def __init__(self, algorithms=None, page_number=None, page_size=None, total_count=None):
        self.algorithms = algorithms  # type: list[ListAlgorithmsResponseBodyDataAlgorithms]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.algorithms:
            for k in self.algorithms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlgorithmsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Algorithms'] = []
        if self.algorithms is not None:
            for k in self.algorithms:
                result['Algorithms'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.algorithms = []
        if m.get('Algorithms') is not None:
            for k in m.get('Algorithms'):
                temp_model = ListAlgorithmsResponseBodyDataAlgorithms()
                self.algorithms.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlgorithmsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListAlgorithmsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAlgorithmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAlgorithmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlgorithmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlgorithmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlgorithmsResponse, self).to_map()
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
            temp_model = ListAlgorithmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCampaignsRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, remark=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCampaignsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ListCampaignsResponseBodyDataCampaigns(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, remark=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCampaignsResponseBodyDataCampaigns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListCampaignsResponseBodyData(TeaModel):
    def __init__(self, campaigns=None, page_number=None, page_size=None, total_count=None):
        self.campaigns = campaigns  # type: list[ListCampaignsResponseBodyDataCampaigns]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.campaigns:
            for k in self.campaigns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCampaignsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Campaigns'] = []
        if self.campaigns is not None:
            for k in self.campaigns:
                result['Campaigns'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.campaigns = []
        if m.get('Campaigns') is not None:
            for k in m.get('Campaigns'):
                temp_model = ListCampaignsResponseBodyDataCampaigns()
                self.campaigns.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCampaignsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListCampaignsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCampaignsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListCampaignsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCampaignsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCampaignsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCampaignsResponse, self).to_map()
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
            temp_model = ListCampaignsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, phone_number=None, remark=None, source=None,
                 status=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.phone_number = phone_number  # type: bool
        self.remark = remark  # type: str
        self.source = source  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListGroupsResponseBodyDataGroups(TeaModel):
    def __init__(self, algorithm=None, amount=None, column=None, created_time=None, filter=None, id=None,
                 inference_job_id=None, name=None, phone_number=None, project=None, remark=None, source=None, status=None, table=None,
                 text=None, updated_time=None, uri=None):
        self.algorithm = algorithm  # type: str
        self.amount = amount  # type: int
        self.column = column  # type: str
        self.created_time = created_time  # type: str
        self.filter = filter  # type: str
        self.id = id  # type: str
        self.inference_job_id = inference_job_id  # type: str
        self.name = name  # type: str
        self.phone_number = phone_number  # type: bool
        self.project = project  # type: str
        self.remark = remark  # type: str
        self.source = source  # type: int
        self.status = status  # type: int
        self.table = table  # type: str
        self.text = text  # type: str
        self.updated_time = updated_time  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsResponseBodyDataGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.column is not None:
            result['Column'] = self.column
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.id is not None:
            result['Id'] = self.id
        if self.inference_job_id is not None:
            result['InferenceJobId'] = self.inference_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.project is not None:
            result['Project'] = self.project
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.table is not None:
            result['Table'] = self.table
        if self.text is not None:
            result['Text'] = self.text
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InferenceJobId') is not None:
            self.inference_job_id = m.get('InferenceJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListGroupsResponseBodyData(TeaModel):
    def __init__(self, groups=None, page_number=None, page_size=None, total_count=None):
        self.groups = groups  # type: list[ListGroupsResponseBodyDataGroups]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListGroupsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ListInferenceJobsRequest(TeaModel):
    def __init__(self, campaign_id=None, campaign_name=None, name=None, page_number=None, page_size=None,
                 remark=None, status=None, training_job_name=None):
        self.campaign_id = campaign_id  # type: str
        self.campaign_name = campaign_name  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.training_job_name = training_job_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInferenceJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.campaign_name is not None:
            result['CampaignName'] = self.campaign_name
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CampaignName') is not None:
            self.campaign_name = m.get('CampaignName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')
        return self


class ListInferenceJobsResponseBodyDataInferenceJobs(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, group_id=None,
                 history=None, id=None, name=None, remark=None, status=None, target_group_id=None, target_path=None,
                 training_job_id=None, updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.group_id = group_id  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.target_group_id = target_group_id  # type: str
        self.target_path = target_path  # type: str
        self.training_job_id = training_job_id  # type: str
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInferenceJobsResponseBodyDataInferenceJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.target_group_id is not None:
            result['TargetGroupId'] = self.target_group_id
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.training_job_id is not None:
            result['TrainingJobId'] = self.training_job_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetGroupId') is not None:
            self.target_group_id = m.get('TargetGroupId')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TrainingJobId') is not None:
            self.training_job_id = m.get('TrainingJobId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ListInferenceJobsResponseBodyData(TeaModel):
    def __init__(self, inference_jobs=None, page_number=None, page_size=None, total_count=None):
        self.inference_jobs = inference_jobs  # type: list[ListInferenceJobsResponseBodyDataInferenceJobs]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.inference_jobs:
            for k in self.inference_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInferenceJobsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InferenceJobs'] = []
        if self.inference_jobs is not None:
            for k in self.inference_jobs:
                result['InferenceJobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.inference_jobs = []
        if m.get('InferenceJobs') is not None:
            for k in m.get('InferenceJobs'):
                temp_model = ListInferenceJobsResponseBodyDataInferenceJobs()
                self.inference_jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInferenceJobsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListInferenceJobsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInferenceJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListInferenceJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInferenceJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInferenceJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInferenceJobsResponse, self).to_map()
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
            temp_model = ListInferenceJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageMetricsRequest(TeaModel):
    def __init__(self, end_date=None, group_id=None, page_number=None, page_size=None, schedule_id=None,
                 signature=None, signature_id=None, start_date=None, template_code=None, template_id=None, template_type=None):
        self.end_date = end_date  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.schedule_id = schedule_id  # type: str
        self.signature = signature  # type: str
        self.signature_id = signature_id  # type: str
        self.start_date = start_date  # type: str
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessageMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessageMetricsResponseBodyDataMetrics(TeaModel):
    def __init__(self, date=None, fail=None, pending=None, rate=None, success=None, total=None):
        self.date = date  # type: str
        self.fail = fail  # type: int
        self.pending = pending  # type: int
        self.rate = rate  # type: float
        self.success = success  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessageMetricsResponseBodyDataMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMessageMetricsResponseBodyData(TeaModel):
    def __init__(self, metrics=None, page_number=None, page_size=None, total_count=None):
        self.metrics = metrics  # type: list[ListMessageMetricsResponseBodyDataMetrics]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = ListMessageMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageMetricsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListMessageMetricsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessageMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessageMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMessageMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMessageMetricsResponse, self).to_map()
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
            temp_model = ListMessageMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessagesRequest(TeaModel):
    def __init__(self, datetime=None, error_code=None, group_id=None, message_id=None, page_number=None,
                 page_size=None, phone_number=None, request_id=None, schedule_id=None, signature=None, signature_id=None,
                 status=None, template_code=None, template_id=None, template_type=None):
        self.datetime = datetime  # type: str
        self.error_code = error_code  # type: str
        self.group_id = group_id  # type: str
        self.message_id = message_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.phone_number = phone_number  # type: str
        self.request_id = request_id  # type: str
        self.schedule_id = schedule_id  # type: str
        self.signature = signature  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datetime is not None:
            result['Datetime'] = self.datetime
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyDataMessages(TeaModel):
    def __init__(self, error_code=None, group_id=None, id=None, out_id=None, phone_number=None, schedule_id=None,
                 signature=None, status=None, template_code=None, template_params=None, template_type=None):
        self.error_code = error_code  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.out_id = out_id  # type: str
        self.phone_number = phone_number  # type: str
        self.schedule_id = schedule_id  # type: str
        self.signature = signature  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.template_params = template_params  # type: str
        self.template_type = template_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMessagesResponseBodyDataMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListMessagesResponseBodyData(TeaModel):
    def __init__(self, messages=None, page_number=None, page_size=None, total_count=None):
        self.messages = messages  # type: list[ListMessagesResponseBodyDataMessages]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMessagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ListMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessagesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListMessagesResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListMessagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMessagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMessagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMessagesResponse, self).to_map()
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
            temp_model = ListMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, status=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSchedulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSchedulesResponseBodyDataSchedules(TeaModel):
    def __init__(self, created_time=None, end_time=None, execute_time=None, group_id=None, id=None, name=None,
                 repeat_cycle=None, repeat_cycle_unit=None, repeat_times=None, sign_name=None, signature_id=None, status=None,
                 template_code=None, template_id=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.end_time = end_time  # type: int
        self.execute_time = execute_time  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.repeat_cycle = repeat_cycle  # type: int
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        self.repeat_times = repeat_times  # type: int
        self.sign_name = sign_name  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSchedulesResponseBodyDataSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.repeat_cycle is not None:
            result['RepeatCycle'] = self.repeat_cycle
        if self.repeat_cycle_unit is not None:
            result['RepeatCycleUnit'] = self.repeat_cycle_unit
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepeatCycle') is not None:
            self.repeat_cycle = m.get('RepeatCycle')
        if m.get('RepeatCycleUnit') is not None:
            self.repeat_cycle_unit = m.get('RepeatCycleUnit')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSchedulesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, schedules=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.schedules = schedules  # type: list[ListSchedulesResponseBodyDataSchedules]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSchedulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = ListSchedulesResponseBodyDataSchedules()
                self.schedules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSchedulesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListSchedulesResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListSchedulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSchedulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSchedulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSchedulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSchedulesResponse, self).to_map()
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
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSignaturesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, status=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSignaturesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSignaturesResponseBodyDataSignatures(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, status=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSignaturesResponseBodyDataSignatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListSignaturesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, signatures=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.signatures = signatures  # type: list[ListSignaturesResponseBodyDataSignatures]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSignaturesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = ListSignaturesResponseBodyDataSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSignaturesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListSignaturesResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListSignaturesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListSignaturesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSignaturesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSignaturesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSignaturesResponse, self).to_map()
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
            temp_model = ListSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, content=None, name=None, page_number=None, page_size=None, status=None, type=None):
        self.content = content  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBodyDataTemplates(TeaModel):
    def __init__(self, content=None, created_time=None, description=None, id=None, name=None, reason=None,
                 signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        self.content = content  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.reason = reason  # type: str
        self.signature_id = signature_id  # type: str
        self.status = status  # type: int
        self.template_code = template_code  # type: str
        self.type = type  # type: int
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyDataTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class ListTemplatesResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, templates=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.templates = templates  # type: list[ListTemplatesResponseBodyDataTemplates]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListTemplatesResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainingJobsRequest(TeaModel):
    def __init__(self, campaign_id=None, campaign_name=None, name=None, page_number=None, page_size=None,
                 remark=None, status=None, training_schedule_id=None):
        self.campaign_id = campaign_id  # type: str
        self.campaign_name = campaign_name  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.training_schedule_id = training_schedule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.campaign_name is not None:
            result['CampaignName'] = self.campaign_name
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_schedule_id is not None:
            result['TrainingScheduleId'] = self.training_schedule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CampaignName') is not None:
            self.campaign_name = m.get('CampaignName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingScheduleId') is not None:
            self.training_schedule_id = m.get('TrainingScheduleId')
        return self


class ListTrainingJobsResponseBodyDataTrainingJobs(TeaModel):
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, history=None, id=None,
                 name=None, remark=None, status=None, training_schedule_id=None, updated_time=None, user_config=None):
        self.algorithm = algorithm  # type: str
        self.campaign_id = campaign_id  # type: str
        self.created_time = created_time  # type: str
        self.data_path = data_path  # type: str
        self.history = history  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.status = status  # type: int
        self.training_schedule_id = training_schedule_id  # type: str
        self.updated_time = updated_time  # type: str
        self.user_config = user_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyDataTrainingJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.history is not None:
            result['History'] = self.history
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.training_schedule_id is not None:
            result['TrainingScheduleId'] = self.training_schedule_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_config is not None:
            result['UserConfig'] = self.user_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrainingScheduleId') is not None:
            self.training_schedule_id = m.get('TrainingScheduleId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserConfig') is not None:
            self.user_config = m.get('UserConfig')
        return self


class ListTrainingJobsResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, training_jobs=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.training_jobs = training_jobs  # type: list[ListTrainingJobsResponseBodyDataTrainingJobs]

    def validate(self):
        if self.training_jobs:
            for k in self.training_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrainingJobs'] = []
        if self.training_jobs is not None:
            for k in self.training_jobs:
                result['TrainingJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.training_jobs = []
        if m.get('TrainingJobs') is not None:
            for k in m.get('TrainingJobs'):
                temp_model = ListTrainingJobsResponseBodyDataTrainingJobs()
                self.training_jobs.append(temp_model.from_map(k))
        return self


class ListTrainingJobsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: ListTrainingJobsResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTrainingJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTrainingJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrainingJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrainingJobsResponse, self).to_map()
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
            temp_model = ListTrainingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, group_id=None, out_ids=None, phone_numbers=None, schedule_id=None, sign_name=None,
                 signature_id=None, sms_up_extend_codes=None, template_code=None, template_id=None, template_params=None):
        self.group_id = group_id  # type: str
        self.out_ids = out_ids  # type: list[str]
        self.phone_numbers = phone_numbers  # type: list[str]
        self.schedule_id = schedule_id  # type: str
        self.sign_name = sign_name  # type: str
        self.signature_id = signature_id  # type: str
        self.sms_up_extend_codes = sms_up_extend_codes  # type: list[str]
        self.template_code = template_code  # type: str
        self.template_id = template_id  # type: str
        self.template_params = template_params  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.out_ids is not None:
            result['OutIds'] = self.out_ids
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.sms_up_extend_codes is not None:
            result['SmsUpExtendCodes'] = self.sms_up_extend_codes
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OutIds') is not None:
            self.out_ids = m.get('OutIds')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SmsUpExtendCodes') is not None:
            self.sms_up_extend_codes = m.get('SmsUpExtendCodes')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        return self


class SendMessageResponseBodyDataMessages(TeaModel):
    def __init__(self, id=None, phone_number=None):
        self.id = id  # type: str
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBodyDataMessages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(self, messages=None, request_id=None):
        self.messages = messages  # type: list[SendMessageResponseBodyDataMessages]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendMessageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = SendMessageResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: SendMessageResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class SmsReportRequestBody(TeaModel):
    def __init__(self, biz_id=None, err_code=None, err_msg=None, message_id=None, out_id=None, phone_number=None,
                 report_time=None, request_id=None, send_time=None, sign_name=None, sms_size=None, success=None,
                 template_code=None):
        self.biz_id = biz_id  # type: str
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.message_id = message_id  # type: str
        self.out_id = out_id  # type: str
        self.phone_number = phone_number  # type: str
        self.report_time = report_time  # type: str
        self.request_id = request_id  # type: str
        self.send_time = send_time  # type: str
        self.sign_name = sign_name  # type: str
        self.sms_size = sms_size  # type: str
        self.success = success  # type: bool
        self.template_code = template_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsReportRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['biz_id'] = self.biz_id
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.err_msg is not None:
            result['err_msg'] = self.err_msg
        if self.message_id is not None:
            result['message_id'] = self.message_id
        if self.out_id is not None:
            result['out_id'] = self.out_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.report_time is not None:
            result['report_time'] = self.report_time
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        if self.sms_size is not None:
            result['sms_size'] = self.sms_size
        if self.success is not None:
            result['success'] = self.success
        if self.template_code is not None:
            result['template_code'] = self.template_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('biz_id') is not None:
            self.biz_id = m.get('biz_id')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')
        if m.get('message_id') is not None:
            self.message_id = m.get('message_id')
        if m.get('out_id') is not None:
            self.out_id = m.get('out_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('report_time') is not None:
            self.report_time = m.get('report_time')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        if m.get('sms_size') is not None:
            self.sms_size = m.get('sms_size')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('template_code') is not None:
            self.template_code = m.get('template_code')
        return self


class SmsReportRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: list[SmsReportRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SmsReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsReportRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsReportResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: int
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SmsReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsReportResponse, self).to_map()
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
            temp_model = SmsReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsUpRequestBody(TeaModel):
    def __init__(self, content=None, dest_code=None, phone_number=None, send_time=None, sequence_id=None,
                 sign_name=None):
        self.content = content  # type: str
        self.dest_code = dest_code  # type: str
        self.phone_number = phone_number  # type: str
        self.send_time = send_time  # type: str
        self.sequence_id = sequence_id  # type: int
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsUpRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.dest_code is not None:
            result['dest_code'] = self.dest_code
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.sequence_id is not None:
            result['sequence_id'] = self.sequence_id
        if self.sign_name is not None:
            result['sign_name'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dest_code') is not None:
            self.dest_code = m.get('dest_code')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('sequence_id') is not None:
            self.sequence_id = m.get('sequence_id')
        if m.get('sign_name') is not None:
            self.sign_name = m.get('sign_name')
        return self


class SmsUpRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: list[SmsUpRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SmsUpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = SmsUpRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class SmsUpResponseBody(TeaModel):
    def __init__(self, code=None, msg=None):
        self.code = code  # type: int
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsUpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SmsUpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SmsUpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsUpResponse, self).to_map()
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
            temp_model = SmsUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCampaignRequest(TeaModel):
    def __init__(self, name=None, remark=None):
        self.name = name  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCampaignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateCampaignResponseBodyData(TeaModel):
    def __init__(self, created_time=None, id=None, name=None, remark=None, updated_time=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.remark = remark  # type: str
        self.updated_time = updated_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCampaignResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class UpdateCampaignResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: UpdateCampaignResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateCampaignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateCampaignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCampaignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCampaignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCampaignResponse, self).to_map()
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
            temp_model = UpdateCampaignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReportUrlRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReportUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateReportUrlResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReportUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateReportUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateReportUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateReportUrlResponse, self).to_map()
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
            temp_model = UpdateReportUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUploadUrlRequest(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUploadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateUploadUrlResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUploadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUploadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUploadUrlResponse, self).to_map()
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
            temp_model = UpdateUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


