# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelComputeTaskByBcIdRequest(TeaModel):
    def __init__(self, bc_id=None):
        self.bc_id = bc_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelComputeTaskByBcIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class CancelComputeTaskByBcIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelComputeTaskByBcIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelComputeTaskByBcIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelComputeTaskByBcIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelComputeTaskByBcIdResponse, self).to_map()
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
            temp_model = CancelComputeTaskByBcIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions(TeaModel):
    def __init__(self, cu_id=None, cu_version=None):
        self.cu_id = cu_id  # type: str
        self.cu_version = cu_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_id is not None:
            result['CuId'] = self.cu_id
        if self.cu_version is not None:
            result['CuVersion'] = self.cu_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CuId') is not None:
            self.cu_id = m.get('CuId')
        if m.get('CuVersion') is not None:
            self.cu_version = m.get('CuVersion')
        return self


class CreateComputeTaskByDataSetIdRequestBatchInfoForm(TeaModel):
    def __init__(self, app_id=None, cu_versions=None):
        self.app_id = app_id  # type: long
        self.cu_versions = cu_versions  # type: list[CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions]

    def validate(self):
        if self.cu_versions:
            for k in self.cu_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateComputeTaskByDataSetIdRequestBatchInfoForm, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['CuVersions'] = []
        if self.cu_versions is not None:
            for k in self.cu_versions:
                result['CuVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.cu_versions = []
        if m.get('CuVersions') is not None:
            for k in m.get('CuVersions'):
                temp_model = CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions()
                self.cu_versions.append(temp_model.from_map(k))
        return self


class CreateComputeTaskByDataSetIdRequest(TeaModel):
    def __init__(self, batch_info_form=None, dataset_id=None, name=None, remarks=None):
        self.batch_info_form = batch_info_form  # type: list[CreateComputeTaskByDataSetIdRequestBatchInfoForm]
        self.dataset_id = dataset_id  # type: long
        self.name = name  # type: str
        self.remarks = remarks  # type: str

    def validate(self):
        if self.batch_info_form:
            for k in self.batch_info_form:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateComputeTaskByDataSetIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchInfoForm'] = []
        if self.batch_info_form is not None:
            for k in self.batch_info_form:
                result['BatchInfoForm'].append(k.to_map() if k else None)
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.batch_info_form = []
        if m.get('BatchInfoForm') is not None:
            for k in m.get('BatchInfoForm'):
                temp_model = CreateComputeTaskByDataSetIdRequestBatchInfoForm()
                self.batch_info_form.append(temp_model.from_map(k))
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        return self


class CreateComputeTaskByDataSetIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[long]
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskByDataSetIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateComputeTaskByDataSetIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateComputeTaskByDataSetIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateComputeTaskByDataSetIdResponse, self).to_map()
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
            temp_model = CreateComputeTaskByDataSetIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTaskByMultiDataSetIdRequest(TeaModel):
    def __init__(self, app_id=None, data_set_ids=None, name=None, remarks=None):
        self.app_id = app_id  # type: long
        self.data_set_ids = data_set_ids  # type: str
        self.name = name  # type: str
        self.remarks = remarks  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskByMultiDataSetIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.data_set_ids is not None:
            result['dataSetIds'] = self.data_set_ids
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('dataSetIds') is not None:
            self.data_set_ids = m.get('dataSetIds')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        return self


class CreateComputeTaskByMultiDataSetIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateComputeTaskByMultiDataSetIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateComputeTaskByMultiDataSetIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateComputeTaskByMultiDataSetIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateComputeTaskByMultiDataSetIdResponse, self).to_map()
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
            temp_model = CreateComputeTaskByMultiDataSetIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAvailableDataSetListResponseBodyData(TeaModel):
    def __init__(self, create_time=None, data_set_type=None, dataset_id=None, id_type_desc=None, name=None,
                 status_desc=None):
        self.create_time = create_time  # type: str
        self.data_set_type = data_set_type  # type: int
        self.dataset_id = dataset_id  # type: long
        self.id_type_desc = id_type_desc  # type: str
        self.name = name  # type: str
        self.status_desc = status_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAvailableDataSetListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class GetAvailableDataSetListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetAvailableDataSetListResponseBodyData]
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAvailableDataSetListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = GetAvailableDataSetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAvailableDataSetListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAvailableDataSetListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAvailableDataSetListResponse, self).to_map()
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
            temp_model = GetAvailableDataSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeResultRequest(TeaModel):
    def __init__(self, bc_id=None):
        self.bc_id = bc_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComputeResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class GetComputeResultResponseBodyData(TeaModel):
    def __init__(self, bc_id=None, billed_num=None, code_10000num=None, code_108num=None, code_109num=None,
                 export_file_name=None, file_line_number=None, name=None, password=None, state=None):
        self.bc_id = bc_id  # type: long
        self.billed_num = billed_num  # type: long
        self.code_10000num = code_10000num  # type: long
        self.code_108num = code_108num  # type: long
        self.code_109num = code_109num  # type: long
        self.export_file_name = export_file_name  # type: str
        self.file_line_number = file_line_number  # type: long
        self.name = name  # type: str
        self.password = password  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComputeResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.billed_num is not None:
            result['billedNum'] = self.billed_num
        if self.code_10000num is not None:
            result['code10000Num'] = self.code_10000num
        if self.code_108num is not None:
            result['code108Num'] = self.code_108num
        if self.code_109num is not None:
            result['code109Num'] = self.code_109num
        if self.export_file_name is not None:
            result['exportFileName'] = self.export_file_name
        if self.file_line_number is not None:
            result['fileLineNumber'] = self.file_line_number
        if self.name is not None:
            result['name'] = self.name
        if self.password is not None:
            result['password'] = self.password
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('billedNum') is not None:
            self.billed_num = m.get('billedNum')
        if m.get('code10000Num') is not None:
            self.code_10000num = m.get('code10000Num')
        if m.get('code108Num') is not None:
            self.code_108num = m.get('code108Num')
        if m.get('code109Num') is not None:
            self.code_109num = m.get('code109Num')
        if m.get('exportFileName') is not None:
            self.export_file_name = m.get('exportFileName')
        if m.get('fileLineNumber') is not None:
            self.file_line_number = m.get('fileLineNumber')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class GetComputeResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetComputeResultResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetComputeResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = GetComputeResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetComputeResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetComputeResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetComputeResultResponse, self).to_map()
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
            temp_model = GetComputeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSetStatusRequest(TeaModel):
    def __init__(self, data_set_id=None):
        self.data_set_id = data_set_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSetStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class GetDataSetStatusResponseBodyData(TeaModel):
    def __init__(self, create_time=None, data_set_type=None, dataset_id=None, id_type_desc=None, message=None,
                 name=None, status_desc=None):
        self.create_time = create_time  # type: str
        self.data_set_type = data_set_type  # type: int
        self.dataset_id = dataset_id  # type: long
        self.id_type_desc = id_type_desc  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.status_desc = status_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSetStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.message is not None:
            result['message'] = self.message
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class GetDataSetStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetDataSetStatusResponseBodyData
        self.msg = msg  # type: str
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDataSetStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDataSetStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataSetStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataSetStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSetStatusResponse, self).to_map()
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
            temp_model = GetDataSetStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSetStsAKResponseBodyData(TeaModel):
    def __init__(self, bucket=None, endpoint=None, id=None, path=None, secret=None, token=None):
        self.bucket = bucket  # type: str
        self.endpoint = endpoint  # type: str
        self.id = id  # type: str
        self.path = path  # type: str
        self.secret = secret  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSetStsAKResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetDataSetStsAKResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDataSetStsAKResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDataSetStsAKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = GetDataSetStsAKResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataSetStsAKResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataSetStsAKResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSetStsAKResponse, self).to_map()
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
            temp_model = GetDataSetStsAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDataSetTaskRequest(TeaModel):
    def __init__(self, data_set_type=None, id_type=None, name=None, oss_file_name=None):
        self.data_set_type = data_set_type  # type: int
        self.id_type = id_type  # type: int
        self.name = name  # type: str
        self.oss_file_name = oss_file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDataSetTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.id_type is not None:
            result['idType'] = self.id_type
        if self.name is not None:
            result['name'] = self.name
        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('idType') is not None:
            self.id_type = m.get('idType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')
        return self


class SubmitDataSetTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDataSetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitDataSetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDataSetTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDataSetTaskResponse, self).to_map()
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
            temp_model = SubmitDataSetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelYydTaskByBcIdRequest(TeaModel):
    def __init__(self, bc_id=None):
        self.bc_id = bc_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelYydTaskByBcIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class CancelYydTaskByBcIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelYydTaskByBcIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelYydTaskByBcIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelYydTaskByBcIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelYydTaskByBcIdResponse, self).to_map()
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
            temp_model = CancelYydTaskByBcIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateYydComputeTaskRequest(TeaModel):
    def __init__(self, dataset_id=None, name=None, remarks=None, app_id=None):
        self.dataset_id = dataset_id  # type: long
        self.name = name  # type: str
        self.remarks = remarks  # type: str
        self.app_id = app_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateYydComputeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self


class CreateYydComputeTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateYydComputeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateYydComputeTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateYydComputeTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateYydComputeTaskResponse, self).to_map()
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
            temp_model = CreateYydComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateYydDataSetRequest(TeaModel):
    def __init__(self, name=None, oss_file_name=None):
        self.name = name  # type: str
        self.oss_file_name = oss_file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateYydDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')
        return self


class CreateYydDataSetResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateYydDataSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateYydDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateYydDataSetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateYydDataSetResponse, self).to_map()
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
            temp_model = CreateYydDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYydComputeTaskListResponseBodyData(TeaModel):
    def __init__(self, app_id=None, bc_id=None, gmt_create=None, gmt_modified=None, name=None, remarks=None,
                 state=None):
        self.app_id = app_id  # type: long
        self.bc_id = bc_id  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.name = name  # type: str
        self.remarks = remarks  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListYydComputeTaskListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListYydComputeTaskListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListYydComputeTaskListResponseBodyData]
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListYydComputeTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = ListYydComputeTaskListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListYydComputeTaskListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListYydComputeTaskListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListYydComputeTaskListResponse, self).to_map()
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
            temp_model = ListYydComputeTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYydDataSetResponseBodyData(TeaModel):
    def __init__(self, create_time=None, data_set_type=None, dataset_id=None, id_type_desc=None, message=None,
                 name=None, status_desc=None):
        self.create_time = create_time  # type: str
        self.data_set_type = data_set_type  # type: int
        self.dataset_id = dataset_id  # type: long
        self.id_type_desc = id_type_desc  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.status_desc = status_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListYydDataSetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.message is not None:
            result['message'] = self.message
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class ListYydDataSetResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListYydDataSetResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListYydDataSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListYydDataSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYydDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListYydDataSetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListYydDataSetResponse, self).to_map()
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
            temp_model = ListYydDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


