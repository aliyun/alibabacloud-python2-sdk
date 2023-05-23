# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateCampaignRequest(TeaModel):
    def __init__(self, name=None, remark=None):
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 运营活动Id。
        self.id = id  # type: str
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: CreateCampaignResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 关联算法，人群来源为算法。
        self.algorithm = algorithm  # type: str
        # 手机号列名，人群来源为CSV文件，MaxCompute，并且包含手机号时需指定。
        self.column = column  # type: str
        # 过滤条件，人群来源为MaxCompute时可指定。
        self.filter = filter  # type: str
        # 预测任务Id，人群来源为算法。
        self.inference_job_id = inference_job_id  # type: str
        # 人群名称。
        self.name = name  # type: str
        # 是否包含手机号，包含手机号的人群可用于触达计划。
        self.phone_number = phone_number  # type: bool
        # MaxCompute(ODPS)项目名，人群来源为MaxCompute时需指定。
        self.project = project  # type: str
        # 人群备注。
        self.remark = remark  # type: str
        # 人群来源。
        # - 0: 文本，每行一个手机号，最多100个。
        # - 1: 文本文件，每行一个手机号，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 2: CSV文件，需指定手机号列名，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 3: MaxCompute(ODPS)表，需指定手机号列名。
        # - 4: 算法。
        self.source = source  # type: int
        # MaxCompute(ODPS)表名，人群来源为MaxCompute时需指定。
        self.table = table  # type: str
        # 文本，人群来源为文本时需指定。
        self.text = text  # type: str
        # 文件地址，人群来源为文本文件，CSV文件，MaxCompute时需指定。
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
        # 关联算法，人群来源为算法。
        self.algorithm = algorithm  # type: str
        # 人群数量。
        self.amount = amount  # type: int
        # 手机号列名，人群来源为CSV文件，MaxCompute，并且包含手机号时需指定。
        self.column = column  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 过滤条件，人群来源为MaxCompute时可指定。
        self.filter = filter  # type: str
        # 人群Id。
        self.id = id  # type: str
        # 预测任务Id，人群来源为算法。
        self.inference_job_id = inference_job_id  # type: str
        # 人群名称。
        self.name = name  # type: str
        # 是否包含手机号，包含手机号的人群可用于触达计划。
        self.phone_number = phone_number  # type: bool
        # MaxCompute(ODPS)项目名，人群来源为MaxCompute时需指定。
        self.project = project  # type: str
        # 人群备注。
        self.remark = remark  # type: str
        # 人群来源。
        # - 0: 文本，每行一个手机号，最多100个。
        # - 1: 文本文件，每行一个手机号，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 2: CSV文件，需指定手机号列名，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 3: MaxCompute(ODPS)表，需指定手机号列名。
        # - 4: 算法。
        self.source = source  # type: int
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status  # type: int
        # MaxCompute(ODPS)表名，人群来源为MaxCompute时需指定。
        self.table = table  # type: str
        # 文本，人群来源为文本时需指定。
        self.text = text  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 文件地址，人群来源为文本文件，CSV文件，MaxCompute时需指定。
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
        # 返回数据。
        self.data = data  # type: CreateGroupResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 关联算法。
        self.algorithm = algorithm  # type: str
        # 关联运营活动Id。
        self.campaign_id = campaign_id  # type: str
        # 预测数据路径。
        self.data_path = data_path  # type: str
        # 预测任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 输出数据路径，需要为空目录。
        self.target_path = target_path  # type: str
        # 关联训练任务。
        self.training_job_id = training_job_id  # type: str
        # 用户配置。
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
        # 关联算法。
        self.algorithm = algorithm  # type: str
        # 关联运营活动Id。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 预测数据路径。
        self.data_path = data_path  # type: str
        # 关联人群Id，如果任务失败则人群无效。
        self.group_id = group_id  # type: str
        # 预测任务日志。
        self.history = history  # type: str
        # 预测任务Id。
        self.id = id  # type: str
        # 预测任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 预测任务状态。
        self.status = status  # type: int
        # 输出数据路径，需要为空目录。
        self.target_path = target_path  # type: str
        # 关联训练任务。
        self.training_job_id = training_job_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        # 返回数据。
        self.data = data  # type: CreateInferenceJobResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
    def __init__(self, aisend_end_date=None, aisend_start_date=None, end_time=None, execute_time=None,
                 group_id=None, name=None, payment_type=None, repeat_cycle=None, repeat_cycle_unit=None, repeat_times=None,
                 sign_name=None, signature_id=None, template_code=None, template_id=None):
        self.aisend_end_date = aisend_end_date  # type: str
        self.aisend_start_date = aisend_start_date  # type: str
        # 终止时间（UTC+8）。
        self.end_time = end_time  # type: int
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time  # type: str
        # 人群ID。
        self.group_id = group_id  # type: str
        # 触达计划名称。
        self.name = name  # type: str
        self.payment_type = payment_type  # type: str
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle  # type: int
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        # 重复次数。
        # - 0: 不设终止时间（默认）。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times  # type: int
        # 签名。
        self.sign_name = sign_name  # type: str
        # 签名ID，或指定签名。
        self.signature_id = signature_id  # type: str
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板ID，或指定模板Code。
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aisend_end_date is not None:
            result['AISendEndDate'] = self.aisend_end_date
        if self.aisend_start_date is not None:
            result['AISendStartDate'] = self.aisend_start_date
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
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
        if m.get('AISendEndDate') is not None:
            self.aisend_end_date = m.get('AISendEndDate')
        if m.get('AISendStartDate') is not None:
            self.aisend_start_date = m.get('AISendStartDate')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 终止时间（UTC+8）。
        self.end_time = end_time  # type: int
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time  # type: str
        # 人群ID。
        self.group_id = group_id  # type: str
        # 触达计划ID。
        self.id = id  # type: str
        # 触达计划名称。
        self.name = name  # type: str
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle  # type: int
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        # 重复次数。
        # - 0: 不设终止时间（默认）。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times  # type: int
        # 签名。
        self.sign_name = sign_name  # type: str
        # 签名ID，或指定签名。
        self.signature_id = signature_id  # type: str
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板ID，或指定模板Code。
        self.template_id = template_id  # type: str
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: CreateScheduleResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 申请说明。
        self.description = description  # type: str
        # 签名名称。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 签名ID。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: CreateSignatureResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 模板内容，请注意控制总字数在70个字以内，超出部分按长短信收费，按67个字为单位记一条短信，营销短信必须在结尾添加“回T退订”。
        self.content = content  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板名称。
        self.name = name  # type: str
        # 签名名称，同时只能指定签名名称或签名ID其中之一。
        self.signature = signature  # type: str
        # 签名ID，可通过ListSignatures获取审核状态为已通过的签名列表，获取签名ID。
        self.signature_id = signature_id  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
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
                 signature=None, signature_id=None, status=None, template_code=None, type=None, updated_time=None):
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板ID。
        self.id = id  # type: str
        # 模板名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名。
        self.signature = signature  # type: str
        # 签名ID。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
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
        if self.signature is not None:
            result['Signature'] = self.signature
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
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
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
        # 返回数据。
        self.data = data  # type: CreateTemplateResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 关联算法ID。
        self.algorithm = algorithm  # type: str
        # 关联运营活动ID。
        self.campaign_id = campaign_id  # type: str
        # 训练数据路径，指定路径前需确保已在控制台完成一键授权。
        self.data_path = data_path  # type: str
        # 训练任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 用户配置。
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
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, has_model_info=None,
                 history=None, id=None, name=None, remark=None, status=None, training_schedule_id=None, updated_time=None,
                 user_config=None):
        # 关联算法ID。
        self.algorithm = algorithm  # type: str
        # 关联运营活动ID。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 训练数据路径，指定路径前需确保已在控制台完成一键授权。
        self.data_path = data_path  # type: str
        self.has_model_info = has_model_info  # type: bool
        # 训练任务日志。
        self.history = history  # type: str
        # 训练任务ID。
        self.id = id  # type: str
        # 训练任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 训练任务状态。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status  # type: int
        # 关联训练计划ID。
        self.training_schedule_id = training_schedule_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        if self.has_model_info is not None:
            result['HasModelInfo'] = self.has_model_info
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
        if m.get('HasModelInfo') is not None:
            self.has_model_info = m.get('HasModelInfo')
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


class CreateTrainingJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: CreateTrainingJobResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 算法说明。
        self.description = description  # type: str
        # 算法Id。
        self.id = id  # type: str
        # 预测所需参数名与对应的参数说明。
        self.infer_user_config_map = infer_user_config_map  # type: str
        # 算法名称。
        self.name = name  # type: str
        # 训练所需参数名与对应的参数说明。
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
        # 返回数据。
        self.data = data  # type: GetAlgorithmResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 运营活动Id。
        self.id = id  # type: str
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: GetCampaignResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 关联算法，人群来源为算法。
        self.algorithm = algorithm  # type: str
        # 人群数量。
        self.amount = amount  # type: int
        # 关联运营活动Id。
        self.campaign_id = campaign_id  # type: str
        # 手机号列名，人群来源为CSV文件，MaxCompute，并且包含手机号时需指定。
        self.column = column  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 过滤条件，人群来源为MaxCompute时可指定。
        self.filter = filter  # type: str
        # 历史记录。
        self.history = history  # type: str
        # 人群Id。
        self.id = id  # type: str
        # 预测任务Id，人群来源为算法。
        self.inference_job_id = inference_job_id  # type: str
        # 人群名称。
        self.name = name  # type: str
        # 是否包含手机号，包含手机号的人群可用于触达计划。
        self.phone_number = phone_number  # type: bool
        # MaxCompute(ODPS)项目名，人群来源为MaxCompute时需指定。
        self.project = project  # type: str
        # 人群备注。
        self.remark = remark  # type: str
        # 人群来源。
        # - 0: 文本，每行一个手机号，最多100个。
        # - 1: 文本文件，每行一个手机号，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 2: 多列CSV文件，需指定手机号列名，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 3: MaxCompute表，需指定手机号列名。
        # - 4: 算法。
        self.source = source  # type: int
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status  # type: int
        # MaxCompute(ODPS)表名，人群来源为MaxCompute时需指定。
        self.table = table  # type: str
        # 文本，人群来源为文本时需指定。
        self.text = text  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 文件地址，人群来源为文本文件，CSV文件时需指定。
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
        # 返回数据。
        self.data = data  # type: GetGroupResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 关联算法。
        self.algorithm = algorithm  # type: str
        # 关联运营活动Id。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 预测数据路径。
        self.data_path = data_path  # type: str
        # 关联人群Id，如果任务失败则人群无效。
        self.group_id = group_id  # type: str
        # 预测任务日志。
        self.history = history  # type: str
        # 预测任务Id。
        self.id = id  # type: str
        # 预测任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 预测任务状态。
        self.status = status  # type: int
        # 输出数据路径，需要为空目录。
        self.target_path = target_path  # type: str
        # 关联训练任务。
        self.training_job_id = training_job_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        # 返回数据。
        self.data = data  # type: GetInferenceJobResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 短信发送状态回执接收服务地址。
        self.sms_report_url = sms_report_url  # type: str
        # 上行短信消息接收服务地址。
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
        # 返回数据。
        self.data = data  # type: GetMessageConfigResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
                 name=None, payment_type=None, repeat_cycle=None, repeat_cycle_unit=None, repeat_times=None,
                 sign_name=None, signature_id=None, status=None, template_code=None, template_id=None, updated_time=None):
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 终止时间（UTC+8）。
        self.end_time = end_time  # type: int
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time  # type: str
        # 人群ID。
        self.group_id = group_id  # type: str
        # 历史记录。
        self.history = history  # type: str
        # 触达计划ID。
        self.id = id  # type: str
        # 触达计划名称。
        self.name = name  # type: str
        self.payment_type = payment_type  # type: str
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle  # type: int
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        # 重复次数。
        # - 0: 不设终止时间（默认）。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times  # type: int
        # 签名。
        self.sign_name = sign_name  # type: str
        # 签名ID，或指定签名。
        self.signature_id = signature_id  # type: str
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板ID，或指定模板Code。
        self.template_id = template_id  # type: str
        # 更新时间 (UTC+8)。
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
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
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
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
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
        # 返回数据。
        self.data = data  # type: GetScheduleResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 签名Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核建议。
        self.reason = reason  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: GetSignatureResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名Id。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: GetTemplateResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, has_model_info=None,
                 history=None, id=None, name=None, remark=None, status=None, training_schedule_id=None, updated_time=None,
                 user_config=None):
        # 关联算法ID。
        self.algorithm = algorithm  # type: str
        # 关联运营活动ID。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 训练数据路径，指定路径前需确保已在控制台完成一键授权。
        self.data_path = data_path  # type: str
        self.has_model_info = has_model_info  # type: bool
        # 训练任务日志。
        self.history = history  # type: str
        # 训练任务ID。
        self.id = id  # type: str
        # 训练任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 训练任务状态。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status  # type: int
        # 关联训练计划ID。
        self.training_schedule_id = training_schedule_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        if self.has_model_info is not None:
            result['HasModelInfo'] = self.has_model_info
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
        if m.get('HasModelInfo') is not None:
            self.has_model_info = m.get('HasModelInfo')
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


class GetTrainingJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None):
        # 返回数据。
        self.data = data  # type: GetTrainingJobResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 账号状态。
        # - 0 : 正常使用。
        # - 1 : 因欠费等原因暂时停用。
        # - 2 : 已释放产品。
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
        # 返回数据。
        self.data = data  # type: GetUserResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 算法Id过滤。
        self.id = id  # type: str
        # 算法名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
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
        # 算法Id。
        self.id = id  # type: str
        # 算法名称。
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
        # 算法列表。
        self.algorithms = algorithms  # type: list[ListAlgorithmsResponseBodyDataAlgorithms]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总算法数量。
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
        # 返回数据。
        self.data = data  # type: ListAlgorithmsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 运营活动名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 运营活动备注过滤。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 运营活动Id。
        self.id = id  # type: str
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 更新时间 (UTC+8)。
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
        # 运营活动列表。
        self.campaigns = campaigns  # type: list[ListCampaignsResponseBodyDataCampaigns]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总运营活动数量。
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
        # 返回数据。
        self.data = data  # type: ListCampaignsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 人群名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 是否包含手机号过滤。
        self.phone_number = phone_number  # type: bool
        # 人群备注过滤。
        self.remark = remark  # type: str
        # 来源过滤。
        self.source = source  # type: int
        # 审核状态过滤。
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
        # 关联算法，人群来源为算法。
        self.algorithm = algorithm  # type: str
        # 人群数量。
        self.amount = amount  # type: int
        # 手机号列名，人群来源为CSV文件，MaxCompute，并且包含手机号时需指定。
        self.column = column  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 过滤条件，人群来源为MaxCompute时可指定。
        self.filter = filter  # type: str
        # 人群Id。
        self.id = id  # type: str
        # 预测任务Id，人群来源为算法。
        self.inference_job_id = inference_job_id  # type: str
        # 人群名称。
        self.name = name  # type: str
        # 是否包含手机号，包含手机号的人群可用于触达计划。
        self.phone_number = phone_number  # type: bool
        # MaxCompute(ODPS)项目名，人群来源为MaxCompute时需指定。
        self.project = project  # type: str
        # 人群备注。
        self.remark = remark  # type: str
        # 人群来源。
        # - 0: 文本，每行一个手机号，最多100个。
        # - 1: 文本文件，每行一个手机号，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 2: CSV文件，需指定手机号列名，可通过控制台上传或指定自定义OSS地址，指定自定义OSS地址前需确保已在控制台完成一键授权。
        # - 3: MaxCompute(ODPS)表，需指定手机号列名。
        # - 4: 算法。
        self.source = source  # type: int
        # 人群状态。
        # - 0: 检查中。
        # - 1: 已通过。
        # - 2: 未通过。
        self.status = status  # type: int
        # MaxCompute(ODPS)表名，人群来源为MaxCompute时需指定。
        self.table = table  # type: str
        # 文本，人群来源为文本时需指定。
        self.text = text  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 文件地址，人群来源为文本文件，CSV文件，MaxCompute时需指定。
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
        # 人群列表。
        self.groups = groups  # type: list[ListGroupsResponseBodyDataGroups]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总人群数量。
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
        # 返回数据。
        self.data = data  # type: ListGroupsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 归属运营活动过滤。
        self.campaign_id = campaign_id  # type: str
        self.campaign_name = campaign_name  # type: str
        # 预测任务名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 预测任务备注过滤。
        self.remark = remark  # type: str
        # 预测任务状态过滤。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
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
        # 关联算法。
        self.algorithm = algorithm  # type: str
        # 关联运营活动ID。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 预测数据路径，当预测人群数据分布在多个csv文件时可指定目录，指定路径前需确保已在控制台完成一键授权。
        self.data_path = data_path  # type: str
        # 预测人群，人群来源必须为多列csv，当同时指定DataPath与GroupId时，以GroupId为准。
        self.group_id = group_id  # type: str
        # 预测任务日志。
        self.history = history  # type: str
        # 预测任务ID。
        self.id = id  # type: str
        # 预测任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 预测任务状态。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status  # type: int
        # 关联目标人群ID，如果任务失败则人群无效。
        self.target_group_id = target_group_id  # type: str
        # 输出数据路径，需要为空目录，指定路径前需确保已在控制台完成一键授权。
        self.target_path = target_path  # type: str
        # 关联训练任务。
        self.training_job_id = training_job_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        # 预测任务列表。
        self.inference_jobs = inference_jobs  # type: list[ListInferenceJobsResponseBodyDataInferenceJobs]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总预测任务数量。
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
        # 返回数据。
        self.data = data  # type: ListInferenceJobsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 结束日期，格式20220102。
        self.end_date = end_date  # type: str
        # 关联人群Id。
        self.group_id = group_id  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 关联触达计划Id。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.signature = signature  # type: str
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 开始日期，格式20220102。
        self.start_date = start_date  # type: str
        # 模板号。
        self.template_code = template_code  # type: str
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
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
        # 发送日期。
        self.date = date  # type: str
        # 发送失败。
        self.fail = fail  # type: int
        # 发送中。
        self.pending = pending  # type: int
        # 发送成功率。
        self.rate = rate  # type: float
        # 发送成功。
        self.success = success  # type: int
        # 总计短信数量。
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
        # 分页返回的统计数据条目列表。
        self.metrics = metrics  # type: list[ListMessageMetricsResponseBodyDataMetrics]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总统计数据条目数量。
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
        # 返回数据。
        self.data = data  # type: ListMessageMetricsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 发送日期，格式为20220101。
        self.datetime = datetime  # type: str
        # 短信错误码过滤。
        self.error_code = error_code  # type: str
        # 关联人群Id过滤。
        self.group_id = group_id  # type: str
        # 短信Id过滤，短信Id为SendMessage成功返回的Id。
        self.message_id = message_id  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 手机号码过滤。
        self.phone_number = phone_number  # type: str
        # 短信批处理Id过滤，短信批处理Id为SendMessage成功返回的RequestId。
        self.request_id = request_id  # type: str
        # 关联触达计划Id过滤。
        self.schedule_id = schedule_id  # type: str
        # 签名名称过滤。
        self.signature = signature  # type: str
        # 签名Id过滤，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 短信发送状态过滤。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status  # type: int
        # 模板号过滤。
        self.template_code = template_code  # type: str
        # 模板Id过滤，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 模板类型过滤。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
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
        # 短信错误码。
        self.error_code = error_code  # type: str
        # 关联人群Id，未关联则为空。
        self.group_id = group_id  # type: str
        # 短信序列号。
        self.id = id  # type: str
        # 外部拓展字段。
        self.out_id = out_id  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 关联触达计划Id，未关联则为空。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.signature = signature  # type: str
        # 短信发送状态。
        # - 0 : 发送中。
        # - 1 : 发送成功。
        # - 2 : 发送失败。
        self.status = status  # type: int
        # 模板号。
        self.template_code = template_code  # type: str
        # 模板参数。
        self.template_params = template_params  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
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
        # 短信列表。
        self.messages = messages  # type: list[ListMessagesResponseBodyDataMessages]
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 短信数量。
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
        # 返回数据。
        self.data = data  # type: ListMessagesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 触达计划名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 发送状态过滤。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 终止时间（UTC+8）。
        self.end_time = end_time  # type: int
        # 执行时间 (UTC+8)，为空立即执行。
        self.execute_time = execute_time  # type: str
        # 人群ID。
        self.group_id = group_id  # type: str
        # 触达计划ID。
        self.id = id  # type: str
        # 触达计划名称。
        self.name = name  # type: str
        # 重复周期，按重复周期与重复周期单位执行。
        self.repeat_cycle = repeat_cycle  # type: int
        # 重复周期单位，若指定执行时间，则重复周期生效。
        # - 0: 从不（默认）。
        # - 1: 小时。
        # - 2: 天。
        # - 3: 周。
        # - 4: 月。
        self.repeat_cycle_unit = repeat_cycle_unit  # type: int
        # 重复次数。
        # - 0: 不设终止时间（默认）。
        # - N: 重复N次后终止。
        self.repeat_times = repeat_times  # type: int
        # 签名。
        self.sign_name = sign_name  # type: str
        # 签名ID，或指定签名。
        self.signature_id = signature_id  # type: str
        # 状态。
        # - 0: 检查中。
        # - 1: 检查成功。
        # - 2: 检查失败。
        # - 3: 发送中。
        # - 4: 发送成功。
        # - 5: 发送失败。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板ID，或指定模板Code。
        self.template_id = template_id  # type: str
        # 更新时间 (UTC+8)。
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
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 触达计划列表。
        self.schedules = schedules  # type: list[ListSchedulesResponseBodyDataSchedules]
        # 触达计划数量。
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
        # 返回数据。
        self.data = data  # type: ListSchedulesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 签名名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 签名审核状态过滤。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 签名Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 签名审核状态。
        # - 0：审核中。
        # - 1：审核通过。
        # - 2：审核不通过。
        self.status = status  # type: int
        # 更新时间 (UTC+8)。
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
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 分页返回的签名列表。
        self.signatures = signatures  # type: list[ListSignaturesResponseBodyDataSignatures]
        # 账号下全部签名注册记录数量。
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
        # 返回数据。
        self.data = data  # type: ListSignaturesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 模板内容过滤。
        self.content = content  # type: str
        # 模板名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 审核状态过滤。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板类型过滤。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
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
        # 模板内容。
        self.content = content  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 申请说明。
        self.description = description  # type: str
        # 模板Id。
        self.id = id  # type: str
        # 签名名称。
        self.name = name  # type: str
        # 审核意见。
        self.reason = reason  # type: str
        # 签名Id。
        self.signature_id = signature_id  # type: str
        # 审核状态。
        # - 0 : 审核中。
        # - 1 : 审核通过。
        # - 2 : 审核不通过。
        self.status = status  # type: int
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板类型。
        # - 0 : 验证码。
        # - 1 : 短信通知。
        # - 2 : 推广短信。
        self.type = type  # type: int
        # 更新时间 (UTC+8)。
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
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 分页返回的模板列表。
        self.templates = templates  # type: list[ListTemplatesResponseBodyDataTemplates]
        # 全部模板注册记录数量。
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
        # 返回数据。
        self.data = data  # type: ListTemplatesResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 归属运营活动过滤。
        self.campaign_id = campaign_id  # type: str
        self.campaign_name = campaign_name  # type: str
        # 训练任务名称过滤。
        self.name = name  # type: str
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 训练任务备注过滤。
        self.remark = remark  # type: str
        # 训练任务状态过滤。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status  # type: int
        # 归属训练计划过滤。
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
    def __init__(self, algorithm=None, campaign_id=None, created_time=None, data_path=None, has_model_info=None,
                 history=None, id=None, name=None, remark=None, status=None, training_schedule_id=None, updated_time=None,
                 user_config=None):
        # 关联算法ID。
        self.algorithm = algorithm  # type: str
        # 关联运营活动ID。
        self.campaign_id = campaign_id  # type: str
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 训练数据路径，指定路径前需确保已在控制台完成一键授权。
        self.data_path = data_path  # type: str
        self.has_model_info = has_model_info  # type: bool
        # 训练任务日志。
        self.history = history  # type: str
        # 训练任务ID。
        self.id = id  # type: str
        # 训练任务名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 训练任务状态。
        # - 0: 队列中。
        # - 1: 已提交。
        # - 2: 运行中。
        # - 3: 成功。
        # - 4: 失败。
        self.status = status  # type: int
        # 关联训练计划ID。
        self.training_schedule_id = training_schedule_id  # type: str
        # 更新时间 (UTC+8)。
        self.updated_time = updated_time  # type: str
        # 用户配置。
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
        if self.has_model_info is not None:
            result['HasModelInfo'] = self.has_model_info
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
        if m.get('HasModelInfo') is not None:
            self.has_model_info = m.get('HasModelInfo')
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
        # 分页数，从1开始，默认为1。
        self.page_number = page_number  # type: int
        # 分页大小，默认为10。
        self.page_size = page_size  # type: int
        # 总训练任务数量。
        self.total_count = total_count  # type: int
        # 训练任务列表。
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
        # 返回数据。
        self.data = data  # type: ListTrainingJobsResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
    def __init__(self, group_id=None, out_ids=None, payment_type=None, phone_numbers=None, schedule_id=None,
                 sign_name=None, signature_id=None, sms_up_extend_codes=None, template_code=None, template_id=None,
                 template_params=None):
        # 人群Id，用于关联人群。
        self.group_id = group_id  # type: str
        # 外部拓展字段，示例：["1234567890"]。
        self.out_ids = out_ids  # type: list[str]
        self.payment_type = payment_type  # type: str
        # 手机号，每个手机号对应一个模板变量、上行拓展码和外部拓展字段，示例：["1234567890"]。
        self.phone_numbers = phone_numbers  # type: list[str]
        # 触达计划Id，用于关联触达计划。
        self.schedule_id = schedule_id  # type: str
        # 签名名称。
        self.sign_name = sign_name  # type: str
        # 签名Id，同时只能指定签名名称或签名Id其中之一。
        self.signature_id = signature_id  # type: str
        # 短信上行拓展码，示例：["1234567890"]。
        self.sms_up_extend_codes = sms_up_extend_codes  # type: list[str]
        # 模板Code。
        self.template_code = template_code  # type: str
        # 模板Id，同时只能指定模板Code或模板Id其中之一。
        self.template_id = template_id  # type: str
        # 短信模板变量对应的实际值，JSON格式。支持传入多个参数，示例：[{"name":"张三","number":"15038****76"}]。
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
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
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
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
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
        # 短信Id，可使用ListMessages查询短信状态。
        self.id = id  # type: str
        # 手机号码。
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
        # 短信结果列表，列表中手机号的顺序与输入请求手机号顺序一一对应。
        self.messages = messages  # type: list[SendMessageResponseBodyDataMessages]
        # 短信批处理Id，可使用ListMessages查询短信状态。
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
        # 返回数据。
        self.data = data  # type: SendMessageResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 发送回执ID，即发送流水号。
        self.biz_id = biz_id  # type: str
        # 状态报告编码。
        self.err_code = err_code  # type: str
        # 状态报告说明。
        self.err_msg = err_msg  # type: str
        # 短信Id。调用发送接口SendMessage发送短信时，返回值中的Id字段。可使用短信Id在接口ListMessages查询具体的发送状态。
        self.message_id = message_id  # type: str
        # 外部拓展字段。
        self.out_id = out_id  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 状态报告时间。
        self.report_time = report_time  # type: str
        # 短信批处理Id。调用发送接口SendMessage发送短信时，返回值中的RequestId字段。可使用短信批处理Id在接口ListMessages查询具体的发送状态。
        self.request_id = request_id  # type: str
        # 发送时间。
        self.send_time = send_time  # type: str
        # 签名。
        self.sign_name = sign_name  # type: str
        # 短信长度。短信长度不超过70个字，按照一条短信计费；超过70个字，即为长短信，按照67字/条拆分成多条计费。
        self.sms_size = sms_size  # type: str
        # 是否接收成功。
        # - true : 接收成功。
        # - false : 接收失败。
        self.success = success  # type: bool
        # 模板号。
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
        # 请求参数的主体信息。
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
        # 应答编码。
        self.code = code  # type: int
        # 描述信息。
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
        # 发送内容。
        self.content = content  # type: str
        # 上行短信扩展号码，系统后台自动生成，不支持自定义传入。
        self.dest_code = dest_code  # type: str
        # 手机号码。
        self.phone_number = phone_number  # type: str
        # 发送时间。
        self.send_time = send_time  # type: str
        # 序列号。
        self.sequence_id = sequence_id  # type: int
        # 签名信息。
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
        # 请求参数的主体信息。
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
        # 应答编码。
        self.code = code  # type: int
        # 描述信息。
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
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
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
        # 创建时间 (UTC+8)。
        self.created_time = created_time  # type: str
        # 运营活动Id。
        self.id = id  # type: str
        # 运营活动名称。
        self.name = name  # type: str
        # 备注。
        self.remark = remark  # type: str
        # 更新时间 (UTC+8)。
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
        # 返回数据。
        self.data = data  # type: UpdateCampaignResponseBodyData
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 可公开访问的地址。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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
        # 可公开访问的地址。
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
        # 返回数据。
        self.data = data  # type: str
        # 错误码。
        self.error_code = error_code  # type: int
        # 错误信息。
        self.error_message = error_message  # type: str
        # 请求ID。
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


