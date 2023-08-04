# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchExecuteStatementResult(TeaModel):
    def __init__(self, generated_fields_list=None):
        self.generated_fields_list = generated_fields_list  # type: list[list[Field]]

    def validate(self):
        if self.generated_fields_list:
            for k in self.generated_fields_list:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(BatchExecuteStatementResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GeneratedFieldsList'] = []
        if self.generated_fields_list is not None:
            for k in self.generated_fields_list:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['generatedFieldsList'].append(l1)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.generated_fields_list = []
        if m.get('GeneratedFieldsList') is not None:
            for k in m.get('GeneratedFieldsList'):
                l1 = []
                for k1 in k:
                    temp_model = Field()
                    l1.append(temp_model.from_map(k1))
                self.generated_fields_list.append(l1)
        return self


class BeginTransactionResult(TeaModel):
    def __init__(self, transaction_id=None):
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeginTransactionResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class ColumnMetadata(TeaModel):
    def __init__(self, array_base_column_type=None, is_auto_increment=None, is_case_sensitive=None,
                 is_currency=None, is_signed=None, label=None, name=None, nullable=None, precision=None, scale=None,
                 schema_name=None, table_name=None, type=None, type_name=None):
        self.array_base_column_type = array_base_column_type  # type: int
        self.is_auto_increment = is_auto_increment  # type: bool
        self.is_case_sensitive = is_case_sensitive  # type: bool
        self.is_currency = is_currency  # type: bool
        self.is_signed = is_signed  # type: bool
        self.label = label  # type: str
        self.name = name  # type: str
        self.nullable = nullable  # type: int
        self.precision = precision  # type: int
        self.scale = scale  # type: int
        self.schema_name = schema_name  # type: str
        self.table_name = table_name  # type: str
        self.type = type  # type: int
        self.type_name = type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ColumnMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_base_column_type is not None:
            result['ArrayBaseColumnType'] = self.array_base_column_type
        if self.is_auto_increment is not None:
            result['IsAutoIncrement'] = self.is_auto_increment
        if self.is_case_sensitive is not None:
            result['IsCaseSensitive'] = self.is_case_sensitive
        if self.is_currency is not None:
            result['IsCurrency'] = self.is_currency
        if self.is_signed is not None:
            result['IsSigned'] = self.is_signed
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.scale is not None:
            result['Scale'] = self.scale
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayBaseColumnType') is not None:
            self.array_base_column_type = m.get('ArrayBaseColumnType')
        if m.get('IsAutoIncrement') is not None:
            self.is_auto_increment = m.get('IsAutoIncrement')
        if m.get('IsCaseSensitive') is not None:
            self.is_case_sensitive = m.get('IsCaseSensitive')
        if m.get('IsCurrency') is not None:
            self.is_currency = m.get('IsCurrency')
        if m.get('IsSigned') is not None:
            self.is_signed = m.get('IsSigned')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class CommitTransactionResult(TeaModel):
    def __init__(self, transaction_status=None):
        self.transaction_status = transaction_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitTransactionResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transaction_status is not None:
            result['TransactionStatus'] = self.transaction_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransactionStatus') is not None:
            self.transaction_status = m.get('TransactionStatus')
        return self


class DeleteResult(TeaModel):
    def __init__(self, number_of_records_updated=None):
        self.number_of_records_updated = number_of_records_updated  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number_of_records_updated is not None:
            result['NumberOfRecordsUpdated'] = self.number_of_records_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NumberOfRecordsUpdated') is not None:
            self.number_of_records_updated = m.get('NumberOfRecordsUpdated')
        return self


class ExecuteStatementResult(TeaModel):
    def __init__(self, column_metadata=None, formatted_records=None, generated_fields=None,
                 number_of_records_updated=None, records=None):
        self.column_metadata = column_metadata  # type: list[ColumnMetadata]
        self.formatted_records = formatted_records  # type: str
        self.generated_fields = generated_fields  # type: list[Field]
        self.number_of_records_updated = number_of_records_updated  # type: long
        self.records = records  # type: list[list[Field]]

    def validate(self):
        if self.column_metadata:
            for k in self.column_metadata:
                if k:
                    k.validate()
        if self.generated_fields:
            for k in self.generated_fields:
                if k:
                    k.validate()
        if self.records:
            for k in self.records:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ExecuteStatementResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ColumnMetadata'] = []
        if self.column_metadata is not None:
            for k in self.column_metadata:
                result['ColumnMetadata'].append(k.to_map() if k else None)
        if self.formatted_records is not None:
            result['FormattedRecords'] = self.formatted_records
        result['GeneratedFields'] = []
        if self.generated_fields is not None:
            for k in self.generated_fields:
                result['GeneratedFields'].append(k.to_map() if k else None)
        if self.number_of_records_updated is not None:
            result['NumberOfRecordsUpdated'] = self.number_of_records_updated
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['records'].append(l1)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column_metadata = []
        if m.get('ColumnMetadata') is not None:
            for k in m.get('ColumnMetadata'):
                temp_model = ColumnMetadata()
                self.column_metadata.append(temp_model.from_map(k))
        if m.get('FormattedRecords') is not None:
            self.formatted_records = m.get('FormattedRecords')
        self.generated_fields = []
        if m.get('GeneratedFields') is not None:
            for k in m.get('GeneratedFields'):
                temp_model = Field()
                self.generated_fields.append(temp_model.from_map(k))
        if m.get('NumberOfRecordsUpdated') is not None:
            self.number_of_records_updated = m.get('NumberOfRecordsUpdated')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                l1 = []
                for k1 in k:
                    temp_model = Field()
                    l1.append(temp_model.from_map(k1))
                self.records.append(l1)
        return self


class Field(TeaModel):
    def __init__(self, array_value=None, blob_value=None, boolean_value=None, is_null=None, long_value=None,
                 string_value=None):
        self.array_value = array_value  # type: str
        self.blob_value = blob_value  # type: str
        self.boolean_value = boolean_value  # type: bool
        self.is_null = is_null  # type: bool
        self.long_value = long_value  # type: long
        self.string_value = string_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Field, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_value is not None:
            result['ArrayValue'] = self.array_value
        if self.blob_value is not None:
            result['BlobValue'] = self.blob_value
        if self.boolean_value is not None:
            result['BooleanValue'] = self.boolean_value
        if self.is_null is not None:
            result['IsNull'] = self.is_null
        if self.long_value is not None:
            result['LongValue'] = self.long_value
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayValue') is not None:
            self.array_value = m.get('ArrayValue')
        if m.get('BlobValue') is not None:
            self.blob_value = m.get('BlobValue')
        if m.get('BooleanValue') is not None:
            self.boolean_value = m.get('BooleanValue')
        if m.get('IsNull') is not None:
            self.is_null = m.get('IsNull')
        if m.get('LongValue') is not None:
            self.long_value = m.get('LongValue')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class InsertListResult(TeaModel):
    def __init__(self, auto_increment_keys=None, number_of_records_updated=None):
        self.auto_increment_keys = auto_increment_keys  # type: list[long]
        self.number_of_records_updated = number_of_records_updated  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertListResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_keys is not None:
            result['AutoIncrementKeys'] = self.auto_increment_keys
        if self.number_of_records_updated is not None:
            result['NumberOfRecordsUpdated'] = self.number_of_records_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoIncrementKeys') is not None:
            self.auto_increment_keys = m.get('AutoIncrementKeys')
        if m.get('NumberOfRecordsUpdated') is not None:
            self.number_of_records_updated = m.get('NumberOfRecordsUpdated')
        return self


class InsertResult(TeaModel):
    def __init__(self, auto_increment_key=None, number_of_records_updated=None):
        self.auto_increment_key = auto_increment_key  # type: long
        self.number_of_records_updated = number_of_records_updated  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment_key is not None:
            result['AutoIncrementKey'] = self.auto_increment_key
        if self.number_of_records_updated is not None:
            result['NumberOfRecordsUpdated'] = self.number_of_records_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoIncrementKey') is not None:
            self.auto_increment_key = m.get('AutoIncrementKey')
        if m.get('NumberOfRecordsUpdated') is not None:
            self.number_of_records_updated = m.get('NumberOfRecordsUpdated')
        return self


class ResultSetOptions(TeaModel):
    def __init__(self, decimal_return_type=None, long_return_type=None):
        self.decimal_return_type = decimal_return_type  # type: str
        self.long_return_type = long_return_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResultSetOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decimal_return_type is not None:
            result['DecimalReturnType'] = self.decimal_return_type
        if self.long_return_type is not None:
            result['LongReturnType'] = self.long_return_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DecimalReturnType') is not None:
            self.decimal_return_type = m.get('DecimalReturnType')
        if m.get('LongReturnType') is not None:
            self.long_return_type = m.get('LongReturnType')
        return self


class RollbackTransactionResult(TeaModel):
    def __init__(self, transaction_status=None):
        self.transaction_status = transaction_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackTransactionResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transaction_status is not None:
            result['TransactionStatus'] = self.transaction_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransactionStatus') is not None:
            self.transaction_status = m.get('TransactionStatus')
        return self


class SelectResult(TeaModel):
    def __init__(self, records=None):
        self.records = records  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.records is not None:
            result['Records'] = self.records
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Records') is not None:
            self.records = m.get('Records')
        return self


class Selector(TeaModel):
    def __init__(self, eq=None, ge=None, gt=None, le=None, like=None, lt=None, ne=None):
        self.eq = eq  # type: str
        self.ge = ge  # type: str
        self.gt = gt  # type: str
        self.le = le  # type: str
        self.like = like  # type: str
        self.lt = lt  # type: str
        self.ne = ne  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Selector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eq is not None:
            result['Eq'] = self.eq
        if self.ge is not None:
            result['Ge'] = self.ge
        if self.gt is not None:
            result['Gt'] = self.gt
        if self.le is not None:
            result['Le'] = self.le
        if self.like is not None:
            result['Like'] = self.like
        if self.lt is not None:
            result['Lt'] = self.lt
        if self.ne is not None:
            result['Ne'] = self.ne
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Eq') is not None:
            self.eq = m.get('Eq')
        if m.get('Ge') is not None:
            self.ge = m.get('Ge')
        if m.get('Gt') is not None:
            self.gt = m.get('Gt')
        if m.get('Le') is not None:
            self.le = m.get('Le')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('Lt') is not None:
            self.lt = m.get('Lt')
        if m.get('Ne') is not None:
            self.ne = m.get('Ne')
        return self


class SqlParameter(TeaModel):
    def __init__(self, name=None, type_hint=None, value=None):
        self.name = name  # type: str
        self.type_hint = type_hint  # type: str
        self.value = value  # type: Field

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(SqlParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type_hint is not None:
            result['TypeHint'] = self.type_hint
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TypeHint') is not None:
            self.type_hint = m.get('TypeHint')
        if m.get('Value') is not None:
            temp_model = Field()
            self.value = temp_model.from_map(m['Value'])
        return self


class UpdateResult(TeaModel):
    def __init__(self, number_of_records_updated=None):
        self.number_of_records_updated = number_of_records_updated  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number_of_records_updated is not None:
            result['NumberOfRecordsUpdated'] = self.number_of_records_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NumberOfRecordsUpdated') is not None:
            self.number_of_records_updated = m.get('NumberOfRecordsUpdated')
        return self


class BatchExecuteStatementRequest(TeaModel):
    def __init__(self, database=None, parameter_sets=None, resource_arn=None, secret_arn=None, sql=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.parameter_sets = parameter_sets  # type: list[list[SqlParameter]]
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.sql = sql  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.parameter_sets:
            for k in self.parameter_sets:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(BatchExecuteStatementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['ParameterSets'] = []
        if self.parameter_sets is not None:
            for k in self.parameter_sets:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['parameterSets'].append(l1)
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.parameter_sets = []
        if m.get('ParameterSets') is not None:
            for k in m.get('ParameterSets'):
                l1 = []
                for k1 in k:
                    temp_model = SqlParameter()
                    l1.append(temp_model.from_map(k1))
                self.parameter_sets.append(l1)
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class BatchExecuteStatementShrinkRequest(TeaModel):
    def __init__(self, database=None, parameter_sets_shrink=None, resource_arn=None, secret_arn=None, sql=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.parameter_sets_shrink = parameter_sets_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.sql = sql  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchExecuteStatementShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.parameter_sets_shrink is not None:
            result['ParameterSets'] = self.parameter_sets_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ParameterSets') is not None:
            self.parameter_sets_shrink = m.get('ParameterSets')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class BatchExecuteStatementResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: BatchExecuteStatementResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchExecuteStatementResponseBody, self).to_map()
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
            temp_model = BatchExecuteStatementResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchExecuteStatementResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchExecuteStatementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchExecuteStatementResponse, self).to_map()
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
            temp_model = BatchExecuteStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BeginTransactionRequest(TeaModel):
    def __init__(self, database=None, resource_arn=None, secret_arn=None):
        self.database = database  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BeginTransactionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        return self


class BeginTransactionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: BeginTransactionResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BeginTransactionResponseBody, self).to_map()
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
            temp_model = BeginTransactionResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BeginTransactionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BeginTransactionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BeginTransactionResponse, self).to_map()
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
            temp_model = BeginTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitTransactionRequest(TeaModel):
    def __init__(self, resource_arn=None, secret_arn=None, transaction_id=None):
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitTransactionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CommitTransactionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CommitTransactionResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CommitTransactionResponseBody, self).to_map()
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
            temp_model = CommitTransactionResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CommitTransactionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CommitTransactionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CommitTransactionResponse, self).to_map()
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
            temp_model = CommitTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRequest(TeaModel):
    def __init__(self, database=None, filter=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.filter = filter  # type: dict[str, Selector]
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.filter:
            for v in self.filter.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(DeleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['Filter'] = {}
        if self.filter is not None:
            for k, v in self.filter.items():
                result['Filter'][k] = v.to_map()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.filter = {}
        if m.get('Filter') is not None:
            for k, v in m.get('Filter').items():
                temp_model = Selector()
                self.filter[k] = temp_model.from_map(v)
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteShrinkRequest(TeaModel):
    def __init__(self, database=None, filter_shrink=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.filter_shrink = filter_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteResponseBody, self).to_map()
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
            temp_model = DeleteResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResponse, self).to_map()
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
            temp_model = DeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteStatementRequestResultSetOptions(TeaModel):
    def __init__(self, decimal_return_type=None, long_return_type=None):
        self.decimal_return_type = decimal_return_type  # type: str
        self.long_return_type = long_return_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteStatementRequestResultSetOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decimal_return_type is not None:
            result['DecimalReturnType'] = self.decimal_return_type
        if self.long_return_type is not None:
            result['LongReturnType'] = self.long_return_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DecimalReturnType') is not None:
            self.decimal_return_type = m.get('DecimalReturnType')
        if m.get('LongReturnType') is not None:
            self.long_return_type = m.get('LongReturnType')
        return self


class ExecuteStatementRequest(TeaModel):
    def __init__(self, continue_after_timeout=None, database=None, format_records_as=None,
                 include_result_metadata=None, parameters=None, resource_arn=None, result_set_options=None, secret_arn=None, sql=None,
                 transaction_id=None):
        self.continue_after_timeout = continue_after_timeout  # type: bool
        self.database = database  # type: str
        self.format_records_as = format_records_as  # type: str
        self.include_result_metadata = include_result_metadata  # type: bool
        self.parameters = parameters  # type: list[SqlParameter]
        self.resource_arn = resource_arn  # type: str
        self.result_set_options = result_set_options  # type: ExecuteStatementRequestResultSetOptions
        self.secret_arn = secret_arn  # type: str
        self.sql = sql  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.result_set_options:
            self.result_set_options.validate()

    def to_map(self):
        _map = super(ExecuteStatementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continue_after_timeout is not None:
            result['ContinueAfterTimeout'] = self.continue_after_timeout
        if self.database is not None:
            result['Database'] = self.database
        if self.format_records_as is not None:
            result['FormatRecordsAs'] = self.format_records_as
        if self.include_result_metadata is not None:
            result['IncludeResultMetadata'] = self.include_result_metadata
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.result_set_options is not None:
            result['ResultSetOptions'] = self.result_set_options.to_map()
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContinueAfterTimeout') is not None:
            self.continue_after_timeout = m.get('ContinueAfterTimeout')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('FormatRecordsAs') is not None:
            self.format_records_as = m.get('FormatRecordsAs')
        if m.get('IncludeResultMetadata') is not None:
            self.include_result_metadata = m.get('IncludeResultMetadata')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = SqlParameter()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResultSetOptions') is not None:
            temp_model = ExecuteStatementRequestResultSetOptions()
            self.result_set_options = temp_model.from_map(m['ResultSetOptions'])
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class ExecuteStatementShrinkRequest(TeaModel):
    def __init__(self, continue_after_timeout=None, database=None, format_records_as=None,
                 include_result_metadata=None, parameters_shrink=None, resource_arn=None, result_set_options_shrink=None, secret_arn=None,
                 sql=None, transaction_id=None):
        self.continue_after_timeout = continue_after_timeout  # type: bool
        self.database = database  # type: str
        self.format_records_as = format_records_as  # type: str
        self.include_result_metadata = include_result_metadata  # type: bool
        self.parameters_shrink = parameters_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.result_set_options_shrink = result_set_options_shrink  # type: str
        self.secret_arn = secret_arn  # type: str
        self.sql = sql  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteStatementShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.continue_after_timeout is not None:
            result['ContinueAfterTimeout'] = self.continue_after_timeout
        if self.database is not None:
            result['Database'] = self.database
        if self.format_records_as is not None:
            result['FormatRecordsAs'] = self.format_records_as
        if self.include_result_metadata is not None:
            result['IncludeResultMetadata'] = self.include_result_metadata
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.result_set_options_shrink is not None:
            result['ResultSetOptions'] = self.result_set_options_shrink
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContinueAfterTimeout') is not None:
            self.continue_after_timeout = m.get('ContinueAfterTimeout')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('FormatRecordsAs') is not None:
            self.format_records_as = m.get('FormatRecordsAs')
        if m.get('IncludeResultMetadata') is not None:
            self.include_result_metadata = m.get('IncludeResultMetadata')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResultSetOptions') is not None:
            self.result_set_options_shrink = m.get('ResultSetOptions')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class ExecuteStatementResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ExecuteStatementResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExecuteStatementResponseBody, self).to_map()
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
            temp_model = ExecuteStatementResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteStatementResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteStatementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteStatementResponse, self).to_map()
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
            temp_model = ExecuteStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRequest(TeaModel):
    def __init__(self, database=None, record=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.record = record  # type: dict[str, any]
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.record is not None:
            result['Record'] = self.record
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class InsertShrinkRequest(TeaModel):
    def __init__(self, database=None, record_shrink=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.record_shrink = record_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.record_shrink is not None:
            result['Record'] = self.record_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Record') is not None:
            self.record_shrink = m.get('Record')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class InsertResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertResponseBody, self).to_map()
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
            temp_model = InsertResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertResponse, self).to_map()
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
            temp_model = InsertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertListRequest(TeaModel):
    def __init__(self, database=None, records=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.records = records  # type: list[dict[str, any]]
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.records is not None:
            result['Records'] = self.records
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Records') is not None:
            self.records = m.get('Records')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class InsertListShrinkRequest(TeaModel):
    def __init__(self, database=None, records_shrink=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.records_shrink = records_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.records_shrink is not None:
            result['Records'] = self.records_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Records') is not None:
            self.records_shrink = m.get('Records')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class InsertListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertListResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertListResponseBody, self).to_map()
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
            temp_model = InsertListResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertListResponse, self).to_map()
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
            temp_model = InsertListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackTransactionRequest(TeaModel):
    def __init__(self, resource_arn=None, secret_arn=None, transaction_id=None):
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackTransactionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class RollbackTransactionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RollbackTransactionResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RollbackTransactionResponseBody, self).to_map()
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
            temp_model = RollbackTransactionResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackTransactionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RollbackTransactionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackTransactionResponse, self).to_map()
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
            temp_model = RollbackTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectRequest(TeaModel):
    def __init__(self, database=None, filter=None, page_number=None, page_size=None, resource_arn=None,
                 secret_arn=None, table=None, transaction_id=None):
        self.database = database  # type: str
        self.filter = filter  # type: dict[str, Selector]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.filter:
            for v in self.filter.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(SelectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['Filter'] = {}
        if self.filter is not None:
            for k, v in self.filter.items():
                result['Filter'][k] = v.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.filter = {}
        if m.get('Filter') is not None:
            for k, v in m.get('Filter').items():
                temp_model = Selector()
                self.filter[k] = temp_model.from_map(v)
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class SelectShrinkRequest(TeaModel):
    def __init__(self, database=None, filter_shrink=None, page_number=None, page_size=None, resource_arn=None,
                 secret_arn=None, table=None, transaction_id=None):
        self.database = database  # type: str
        self.filter_shrink = filter_shrink  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class SelectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SelectResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SelectResponseBody, self).to_map()
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
            temp_model = SelectResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SelectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SelectResponse, self).to_map()
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
            temp_model = SelectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRequest(TeaModel):
    def __init__(self, database=None, filter=None, record=None, resource_arn=None, secret_arn=None, table=None,
                 transaction_id=None):
        self.database = database  # type: str
        self.filter = filter  # type: dict[str, Selector]
        self.record = record  # type: dict[str, any]
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.filter:
            for v in self.filter.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(UpdateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        result['Filter'] = {}
        if self.filter is not None:
            for k, v in self.filter.items():
                result['Filter'][k] = v.to_map()
        if self.record is not None:
            result['Record'] = self.record
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        self.filter = {}
        if m.get('Filter') is not None:
            for k, v in m.get('Filter').items():
                temp_model = Selector()
                self.filter[k] = temp_model.from_map(v)
        if m.get('Record') is not None:
            self.record = m.get('Record')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class UpdateShrinkRequest(TeaModel):
    def __init__(self, database=None, filter_shrink=None, record_shrink=None, resource_arn=None, secret_arn=None,
                 table=None, transaction_id=None):
        self.database = database  # type: str
        self.filter_shrink = filter_shrink  # type: str
        self.record_shrink = record_shrink  # type: str
        self.resource_arn = resource_arn  # type: str
        self.secret_arn = secret_arn  # type: str
        self.table = table  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.record_shrink is not None:
            result['Record'] = self.record_shrink
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn
        if self.table is not None:
            result['Table'] = self.table
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('Record') is not None:
            self.record_shrink = m.get('Record')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class UpdateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateResult
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateResponseBody, self).to_map()
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
            temp_model = UpdateResult()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResponse, self).to_map()
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
            temp_model = UpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


