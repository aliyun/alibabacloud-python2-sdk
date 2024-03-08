# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataValue(TeaModel):
    def __init__(self, master_uid=None, c_instance_id=None, access_key=None, user_name=None, password=None,
                 deleted=None, create_timestamp=None):
        # The Alibaba Cloud account ID or Resource Access Management (RAM) user to which the AccessKey pair that is used to create the static username and password belongs.
        self.master_uid = master_uid  # type: long
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.c_instance_id = c_instance_id  # type: str
        # The AccessKey ID that is used to create the static username and password.
        self.access_key = access_key  # type: str
        # The static username.
        self.user_name = user_name  # type: str
        # The static password.
        self.password = password  # type: str
        # The timestamp that indicates when the static username and password were deleted. Unit: milliseconds.
        self.deleted = deleted  # type: long
        # The timestamp that indicates when the static username and password were created. Unit: milliseconds.
        self.create_timestamp = create_timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.master_uid is not None:
            result['masterUid'] = self.master_uid
        if self.c_instance_id is not None:
            result['cInstanceId'] = self.c_instance_id
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.password is not None:
            result['password'] = self.password
        if self.deleted is not None:
            result['deleted'] = self.deleted
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('masterUid') is not None:
            self.master_uid = m.get('masterUid')
        if m.get('cInstanceId') is not None:
            self.c_instance_id = m.get('cInstanceId')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_access_key=None, create_timestamp=None, instance_id=None, secret_sign=None,
                 signature=None, user_name=None):
        # The AccessKey ID of your Alibaba Cloud account or RAM user. For information about how to obtain an AccessKey pair, see [Create an AccessKey pair](~~116401~~).
        # 
        # >  If you use the pair of static username and password that is created by using the Accesskey pair of a RAM user to access ApsaraMQ for RabbitMQ to send and receive messages, make sure that the RAM user is granted the required permissions. For more information, see [RAM policies](~~146559~~).
        self.account_access_key = account_access_key  # type: str
        # The timestamp that indicates when the password is created. Unit: milliseconds.
        # 
        # >  This timestamp is specified by you and is used to generate a static password. The timestamp is not the timestamp that indicates when the system generates the password.
        self.create_timestamp = create_timestamp  # type: long
        # The ID of the instance for which you want to create a pair of static username and password.
        self.instance_id = instance_id  # type: str
        # The AccessKey secret signature. The system generates a static password based on the signature in the request, the AccessKey secret signature, and the username.
        # 
        # The system uses the HMAC-SHA1 algorithm to generate the AccessKey secret signature based on the timestamp that indicates when the username is created and the AccessKey ID. For more information, see the **"Sample code on how to generate a signature"** section of this topic.
        self.secret_sign = secret_sign  # type: str
        # The signature. The system generates a static password based on the signature in the request, the AccessKey secret signature, and the username.
        # 
        # The system uses the HMAC-SHA1 algorithm to generate the signature based on the timestamp that indicates when the username is created and the AccessKey ID. For more information, see the **"Sample code on how to generate a signature"** section of this topic.
        self.signature = signature  # type: str
        # The static username that you want to create.
        # 
        # The value of this parameter is a Base64-encoded string that is generated based on the instance ID and AccessKey ID. For more information, see the "**Sample code on how to generate a username**" section of this topic.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_access_key is not None:
            result['accountAccessKey'] = self.account_access_key
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.secret_sign is not None:
            result['secretSign'] = self.secret_sign
        if self.signature is not None:
            result['signature'] = self.signature
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountAccessKey') is not None:
            self.account_access_key = m.get('accountAccessKey')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('secretSign') is not None:
            self.secret_sign = m.get('secretSign')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class CreateAccountResponseBodyData(TeaModel):
    def __init__(self, access_key=None, create_time_stamp=None, instance_id=None, master_uid=None, password=None,
                 user_name=None):
        # The AccessKey ID that is used to create the password.
        self.access_key = access_key  # type: str
        # The timestamp that indicates when the password was created. Unit: milliseconds.
        self.create_time_stamp = create_time_stamp  # type: long
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The Alibaba Cloud account ID or RAM user to which the AccessKey pair that is used to create the static username and password belongs.
        self.master_uid = master_uid  # type: long
        # The created static password.
        self.password = password  # type: str
        # The created static username.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.master_uid is not None:
            result['MasterUId'] = self.master_uid
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MasterUId') is not None:
            self.master_uid = m.get('MasterUId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: CreateAccountResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
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
            temp_model = CreateAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccountResponse, self).to_map()
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(self, argument=None, binding_key=None, binding_type=None, destination_name=None, instance_id=None,
                 source_exchange=None, virtual_host=None):
        # The key-value pairs that are configured for the headers attributes of a message. One or more key-value pairs can be concatenated to configure the headers attributes of a message. You must specify the x-match attribute as one of the valid values. You can specify custom values for other attributes. Valid values of the x-match attribute:
        # 
        # *   \*\*all: \*\*A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   \*\*any: \*\*A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # Separate the attributes with semicolons (;). Separate the key and value of an attribute with a colon (:). Example: x-match:all;type:report;format:pdf. This parameter is available for only headers exchanges. You can set this parameter to an arbitrary value for other types of exchanges.
        self.argument = argument  # type: str
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (\_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (\_), asterisks (\*), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\*) is used in the middle of a binding key, the number sign (#) or asterisk (\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key  # type: str
        # The type of the object that you want to bind to the source exchange. Valid values:
        # 
        # *   \*\*0: \*\*Queue
        # *   \*\*1: \*\*Exchange
        self.binding_type = binding_type  # type: str
        # The name of the object that you want to bind to the source exchange. You must create the object in the ApsaraMQ for RabbitMQ console in advance. The vhost of the object is the same as the vhost to which the source exchange specified by **SourceExchange** belongs. The vhost of the source exchange is the one specified by **VirtualHost**.
        self.destination_name = destination_name  # type: str
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The name of the source exchange. You must create the source exchange in the ApsaraMQ for RabbitMQ console in advance.
        self.source_exchange = source_exchange  # type: str
        # The virtual host (vhost) name. You must create the vhost in the ApsaraMQ for RabbitMQ console in advance. The object specified by **DestinationName** and the source exchange specified by **SourceExchange** must belong to the vhost.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBindingResponseBody, self).to_map()
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


class CreateBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBindingResponse, self).to_map()
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
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExchangeRequest(TeaModel):
    def __init__(self, alternate_exchange=None, auto_delete_state=None, exchange_name=None, exchange_type=None,
                 instance_id=None, internal=None, virtual_host=None):
        # The alternate exchange. An alternate exchange is used to receive messages that fail to be routed to queues from the current exchange.
        self.alternate_exchange = alternate_exchange  # type: str
        # Specifies whether to automatically delete the exchange. Valid values:
        # 
        # *   **true**: If the last queue that is bound to the exchange is unbound, the exchange is automatically deleted.
        # *   **false**: If the last queue that is bound to the exchange is unbound, the exchange is not automatically deleted.
        self.auto_delete_state = auto_delete_state  # type: bool
        # The name of the exchange that you want to create. The exchange name must meet the following conventions:
        # 
        # *   The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # *   After the exchange is created, you cannot change its name. If you want to change its name, delete the exchange and create another exchange.
        self.exchange_name = exchange_name  # type: str
        # The exchange type. Valid values:
        # 
        # *   **DIRECT**: An exchange of this type routes a message to the queue whose binding key is exactly the same as the routing key of the message.
        # *   **TOPIC**: This type of exchange is similar to direct exchanges. An exchange of this type routes a message to one or more queues based on the results of the fuzzy match or multi-condition match between the routing key of the message and the binding keys of the current exchange.
        # *   **FANOUT**: An exchange of this type routes all received messages to all queues bound to this exchange. You can use a fanout exchange to broadcast messages.
        # *   **HEADERS**: This type of exchange is similar to direct exchanges. The only difference is that a headers exchange routes messages based on the headers attributes instead of routing keys. When you bind a headers exchange to a queue, you must configure binding attributes in the key-value format for the binding. When you send a message to a headers exchange, you must configure the headers attributes in the key-value format for the message. After a headers exchange receives a message, the exchange routes the message based on the matching results between the headers attributes of the message and the binding attributes of the bound queues.
        # *   **X-CONSISTENT-HASH**: An exchange of this type allows you to perform hash calculations on routing keys or header values and use consistent hashing to route a message to different queues.
        self.exchange_type = exchange_type  # type: str
        # The ID of the ApsaraMQ for RabbitMQ for which you want to create an exchange.
        self.instance_id = instance_id  # type: str
        # Specifies whether the exchange is an internal exchange. Valid values:
        # 
        # *   **false**\
        # *   **true**\
        self.internal = internal  # type: bool
        # The name of the vhost to which the exchange that you want to create belongs.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExchangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class CreateExchangeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExchangeResponseBody, self).to_map()
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


class CreateExchangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateExchangeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExchangeResponse, self).to_map()
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
            temp_model = CreateExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, instance_name=None,
                 instance_type=None, max_connections=None, max_eip_tps=None, max_private_tps=None, payment_type=None, period=None,
                 period_cycle=None, queue_capacity=None, renew_status=None, renewal_duration_unit=None,
                 serverless_charge_type=None, storage_size=None, support_eip=None, support_tracing=None, tracing_storage_time=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.max_connections = max_connections  # type: int
        self.max_eip_tps = max_eip_tps  # type: long
        self.max_private_tps = max_private_tps  # type: long
        self.payment_type = payment_type  # type: str
        self.period = period  # type: int
        self.period_cycle = period_cycle  # type: str
        self.queue_capacity = queue_capacity  # type: int
        # autoRenew和renewStatus都是续费方式，当两个同时填写时，以renewStatus为准
        self.renew_status = renew_status  # type: str
        self.renewal_duration_unit = renewal_duration_unit  # type: str
        self.serverless_charge_type = serverless_charge_type  # type: str
        self.storage_size = storage_size  # type: int
        self.support_eip = support_eip  # type: bool
        self.support_tracing = support_tracing  # type: bool
        self.tracing_storage_time = tracing_storage_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps
        if self.max_private_tps is not None:
            result['MaxPrivateTps'] = self.max_private_tps
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_cycle is not None:
            result['PeriodCycle'] = self.period_cycle
        if self.queue_capacity is not None:
            result['QueueCapacity'] = self.queue_capacity
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.renewal_duration_unit is not None:
            result['RenewalDurationUnit'] = self.renewal_duration_unit
        if self.serverless_charge_type is not None:
            result['ServerlessChargeType'] = self.serverless_charge_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.support_eip is not None:
            result['SupportEip'] = self.support_eip
        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing
        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')
        if m.get('MaxPrivateTps') is not None:
            self.max_private_tps = m.get('MaxPrivateTps')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodCycle') is not None:
            self.period_cycle = m.get('PeriodCycle')
        if m.get('QueueCapacity') is not None:
            self.queue_capacity = m.get('QueueCapacity')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('RenewalDurationUnit') is not None:
            self.renewal_duration_unit = m.get('RenewalDurationUnit')
        if m.get('ServerlessChargeType') is not None:
            self.serverless_charge_type = m.get('ServerlessChargeType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SupportEip') is not None:
            self.support_eip = m.get('SupportEip')
        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')
        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
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


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequest(TeaModel):
    def __init__(self, auto_delete_state=None, auto_expire_state=None, dead_letter_exchange=None,
                 dead_letter_routing_key=None, exclusive_state=None, instance_id=None, max_length=None, maximum_priority=None,
                 message_ttl=None, queue_name=None, virtual_host=None):
        # Specifies whether to automatically delete the queue. Valid values:
        # 
        # *   true: The queue is automatically deleted. After the last consumer unsubscribes from the queue, the queue is automatically deleted.
        # *   false: The queue is not automatically deleted.
        self.auto_delete_state = auto_delete_state  # type: bool
        # The validity period after which the queue is automatically deleted. If the queue is not accessed within the specified period of time, the queue is automatically deleted.
        # 
        # Unit: milliseconds.
        # 
        # >  You can use the feature that corresponds to this parameter only after you enable the feature. To enable the feature, [submit a ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex).
        self.auto_expire_state = auto_expire_state  # type: long
        # The dead-letter exchange. A dead-letter exchange is used to receive rejected messages.
        # 
        # If a consumer rejects a message that cannot be redelivered, ApsaraMQ for RabbitMQ routes the message to the specified dead-letter exchange. Then, the dead-letter exchange routes the message to the queue that is bound to the dead-letter exchange for storage.
        self.dead_letter_exchange = dead_letter_exchange  # type: str
        # The dead-letter routing key. The key must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        self.dead_letter_routing_key = dead_letter_routing_key  # type: str
        # Specifies whether the exchange is an exclusive exchange. Valid values:
        # 
        # *   true: The exchange is an exclusive exchange. Only the connection that declares the exclusive exchange can use the exclusive exchange. After the connection is closed, the exclusive exchange is automatically deleted.
        # *   false: The exchange is not an exclusive exchange.
        self.exclusive_state = exclusive_state  # type: bool
        # The ID of the ApsaraMQ for RabbitMQ instance on which you want to create a queue.
        self.instance_id = instance_id  # type: str
        # This parameter is unavailable in the current version of ApsaraMQ for RabbitMQ.
        # 
        # The maximum number of messages that can be stored in the queue. If this threshold is exceeded, the earliest stored messages in the queue are deleted.
        self.max_length = max_length  # type: long
        # Queue priorities are not supported. The value does not affect the call or return results.
        self.maximum_priority = maximum_priority  # type: int
        # The message time to live (TTL) of the queue.
        # 
        # *   If the retention period of a message in the queue exceeds the message TTL of the queue, the message expires.
        # *   The message TTL must be set to a non-negative integer. The maximum message TTL is one day. Unit: milliseconds. For example, if the message TTL is 1,000 milliseconds, the message can be retained for up to 1 second in the queue.
        self.message_ttl = message_ttl  # type: long
        # The name of the queue that you want to create.
        # 
        # *   The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # *   After the queue is created, you cannot change the name of the queue. If you want to change the name of the queue, delete the queue and create another queue.
        self.queue_name = queue_name  # type: str
        # The name of the vhost to which the queue that you want to create belongs. The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.auto_expire_state is not None:
            result['AutoExpireState'] = self.auto_expire_state
        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange
        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.maximum_priority is not None:
            result['MaximumPriority'] = self.maximum_priority
        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('AutoExpireState') is not None:
            self.auto_expire_state = m.get('AutoExpireState')
        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')
        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaximumPriority') is not None:
            self.maximum_priority = m.get('MaximumPriority')
        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueueResponseBody, self).to_map()
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


class CreateQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateQueueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQueueResponse, self).to_map()
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
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualHostRequest(TeaModel):
    def __init__(self, instance_id=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The name of the vhost that you want to create. Valid values:
        # 
        # *   The name can contain letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slash (/), and at signs (@).
        # *   The name must be 1 to 255 characters in length.
        # *   After the vhost is created, you cannot change its name. If you want to change the name of a vhost, delete the vhost and create another vhost.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class CreateVirtualHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualHostResponseBody, self).to_map()
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


class CreateVirtualHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVirtualHostResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVirtualHostResponse, self).to_map()
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
            temp_model = CreateVirtualHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, create_timestamp=None, user_name=None):
        # The timestamp that indicates when the pair of static username and password that you want to delete was created. Unit: milliseconds.
        # 
        # You can call the [ListAccounts](~~472730~~) operation to view the timestamp.
        self.create_timestamp = create_timestamp  # type: long
        # The pair of username and password that you want to delete.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: bool
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountResponseBody, self).to_map()
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


class DeleteAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccountResponse, self).to_map()
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(self, binding_key=None, binding_type=None, destination_name=None, instance_id=None,
                 source_exchange=None, virtual_host=None):
        # The binding key.
        self.binding_key = binding_key  # type: str
        # The type of the object that you want to unbind from the source exchange. Valid values:
        # 
        # *   **QUEUE**\
        # *   **EXCHANGE**\
        self.binding_type = binding_type  # type: str
        # The name of the object that you want to unbind from the source exchange.
        self.destination_name = destination_name  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The name of the source exchange.
        self.source_exchange = source_exchange  # type: str
        # The vhost name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindingResponseBody, self).to_map()
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


class DeleteBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBindingResponse, self).to_map()
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
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExchangeRequest(TeaModel):
    def __init__(self, exchange_name=None, instance_id=None, virtual_host=None):
        # The name of the exchange that you want to delete.
        self.exchange_name = exchange_name  # type: str
        # The ID of the ApsaraMQ for RabbitMQ instance whose exchange you want to delete.
        self.instance_id = instance_id  # type: str
        # The vhost to which the exchange that you want to delete belongs.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExchangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteExchangeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExchangeResponseBody, self).to_map()
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


class DeleteExchangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExchangeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExchangeResponse, self).to_map()
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
            temp_model = DeleteExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, virtual_host=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The queue name.
        self.queue_name = queue_name  # type: str
        # The vhost name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueResponseBody, self).to_map()
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


class DeleteQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQueueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQueueResponse, self).to_map()
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
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualHostRequest(TeaModel):
    def __init__(self, instance_id=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance to which the vhost you want to delete belongs.
        self.instance_id = instance_id  # type: str
        # The name of the vhost that you want to delete.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteVirtualHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualHostResponseBody, self).to_map()
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


class DeleteVirtualHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVirtualHostResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVirtualHostResponse, self).to_map()
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
            temp_model = DeleteVirtualHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetadataAmountRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMetadataAmountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetMetadataAmountResponseBodyData(TeaModel):
    def __init__(self, current_exchanges=None, current_queues=None, current_virtual_hosts=None, max_exchanges=None,
                 max_queues=None, max_virtual_hosts=None):
        # The number of created exchanges on the ApsaraMQ for RabbitMQ instance.
        self.current_exchanges = current_exchanges  # type: int
        # The number of created queues on the ApsaraMQ for RabbitMQ instance.
        self.current_queues = current_queues  # type: int
        # The number of created vhosts on the ApsaraMQ for RabbitMQ instance.
        self.current_virtual_hosts = current_virtual_hosts  # type: int
        # The maximum number of exchanges that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_exchanges = max_exchanges  # type: int
        # The maximum number of queues that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_queues = max_queues  # type: int
        # The maximum number of vhosts that can be created on the ApsaraMQ for RabbitMQ instance.
        self.max_virtual_hosts = max_virtual_hosts  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMetadataAmountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_exchanges is not None:
            result['CurrentExchanges'] = self.current_exchanges
        if self.current_queues is not None:
            result['CurrentQueues'] = self.current_queues
        if self.current_virtual_hosts is not None:
            result['CurrentVirtualHosts'] = self.current_virtual_hosts
        if self.max_exchanges is not None:
            result['MaxExchanges'] = self.max_exchanges
        if self.max_queues is not None:
            result['MaxQueues'] = self.max_queues
        if self.max_virtual_hosts is not None:
            result['MaxVirtualHosts'] = self.max_virtual_hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentExchanges') is not None:
            self.current_exchanges = m.get('CurrentExchanges')
        if m.get('CurrentQueues') is not None:
            self.current_queues = m.get('CurrentQueues')
        if m.get('CurrentVirtualHosts') is not None:
            self.current_virtual_hosts = m.get('CurrentVirtualHosts')
        if m.get('MaxExchanges') is not None:
            self.max_exchanges = m.get('MaxExchanges')
        if m.get('MaxQueues') is not None:
            self.max_queues = m.get('MaxQueues')
        if m.get('MaxVirtualHosts') is not None:
            self.max_virtual_hosts = m.get('MaxVirtualHosts')
        return self


class GetMetadataAmountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: GetMetadataAmountResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMetadataAmountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMetadataAmountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMetadataAmountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMetadataAmountResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMetadataAmountResponse, self).to_map()
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
            temp_model = GetMetadataAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the ApsaraMQ for RabbitMQ instance for which you want to query the static username and password.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: dict[str, list[DataValue]]
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['Data'][k] = l1
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
        self.data = {}
        if m.get('Data') is not None:
            for k, v in m.get('Data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountsResponse, self).to_map()
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
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return. Valid values:
        # 
        # **1 to 100**\
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The vhost name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListBindingsResponseBodyDataBindings(TeaModel):
    def __init__(self, argument=None, binding_key=None, binding_type=None, destination_name=None,
                 source_exchange=None):
        # The x-match attribute. Valid values:
        # 
        # *   **all:** A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   **any:** A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # This parameter is available only for headers exchanges.
        self.argument = argument  # type: str
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (\_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (\_), asterisks (\*), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\*) is used in the middle of a binding key, the number sign (#) or asterisk (\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key  # type: str
        # The type of the object to which the source exchange is bound. Valid values:
        # 
        # *   **QUEUE**\
        # *   **EXCHANGE**\
        self.binding_type = binding_type  # type: str
        # The name of the object to which the source exchange is bound.
        self.destination_name = destination_name  # type: str
        # The name of the source exchange.
        self.source_exchange = source_exchange  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingsResponseBodyDataBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListBindingsResponseBodyData(TeaModel):
    def __init__(self, bindings=None, max_results=None, next_token=None):
        # The bindings.
        self.bindings = bindings  # type: list[ListBindingsResponseBodyDataBindings]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListBindingsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindingsResponse, self).to_map()
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
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDownStreamBindingsRequest(TeaModel):
    def __init__(self, exchange_name=None, instance_id=None, max_results=None, next_token=None, virtual_host=None):
        # The exchange name.
        self.exchange_name = exchange_name  # type: str
        # The ID of the ApsaraMQ for RabbitMQ instance to which the exchange belongs.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return.
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The name of the vhost to which the exchange belongs.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDownStreamBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListDownStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(self, argument=None, binding_key=None, binding_type=None, destination_name=None,
                 source_exchange=None):
        # The x-match attribute. Valid values:
        # 
        # *   **all:** A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   **any:** A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # This parameter is available only for headers exchanges.
        self.argument = argument  # type: str
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (\_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\*) is used in the middle of a binding key, the number sign (#) or asterisk (\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key  # type: str
        # The type of the object to which the source exchange is bound. Valid values:
        # 
        # *   **QUEUE**\
        # *   **EXCHANGE**\
        self.binding_type = binding_type  # type: str
        # The name of the object to which the source exchange is bound.
        self.destination_name = destination_name  # type: str
        # The name of the source exchange.
        self.source_exchange = source_exchange  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDownStreamBindingsResponseBodyDataBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListDownStreamBindingsResponseBodyData(TeaModel):
    def __init__(self, bindings=None, max_results=None, next_token=None):
        # The bindings.
        self.bindings = bindings  # type: list[ListDownStreamBindingsResponseBodyDataBindings]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDownStreamBindingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListDownStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListDownStreamBindingsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: ListDownStreamBindingsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDownStreamBindingsResponseBody, self).to_map()
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
            temp_model = ListDownStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDownStreamBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDownStreamBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDownStreamBindingsResponse, self).to_map()
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
            temp_model = ListDownStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeUpStreamBindingsRequest(TeaModel):
    def __init__(self, exchange_name=None, instance_id=None, max_results=None, next_token=None, virtual_host=None):
        # The exchange name.
        self.exchange_name = exchange_name  # type: str
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return.
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The virtual host (vhost) name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExchangeUpStreamBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListExchangeUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(self, argument=None, binding_key=None, binding_type=None, destination_name=None,
                 source_exchange=None):
        # The x-match attribute. Valid values:
        # 
        # *   **all:** A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   **any:** A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # This parameter is available only for headers exchanges.
        self.argument = argument  # type: str
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (\_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\*) is used in the middle of a binding key, the number sign (#) or asterisk (\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key  # type: str
        # The type of the object to which the source exchange is bound. Valid values:
        # 
        # *   **QUEUE**\
        # *   **EXCHANGE**\
        self.binding_type = binding_type  # type: str
        # The name of the object to which the source exchange is bound.
        self.destination_name = destination_name  # type: str
        # The name of the source exchange.
        self.source_exchange = source_exchange  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExchangeUpStreamBindingsResponseBodyDataBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListExchangeUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(self, bindings=None, max_results=None, next_token=None):
        # The bindings.
        self.bindings = bindings  # type: list[ListExchangeUpStreamBindingsResponseBodyDataBindings]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExchangeUpStreamBindingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListExchangeUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExchangeUpStreamBindingsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: ListExchangeUpStreamBindingsResponseBodyData
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListExchangeUpStreamBindingsResponseBody, self).to_map()
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
            temp_model = ListExchangeUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeUpStreamBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExchangeUpStreamBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExchangeUpStreamBindingsResponse, self).to_map()
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
            temp_model = ListExchangeUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangesRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return. Valid values: **1 to 100**\
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If you call this operation for the first time or a next query is not required, leave this parameter empty.
        # *   If a next query is to be sent, set the value to the value of `NextToken` that is returned from the previous request.
        self.next_token = next_token  # type: str
        # The vhost name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExchangesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListExchangesResponseBodyDataExchanges(TeaModel):
    def __init__(self, attributes=None, auto_delete_state=None, create_time=None, exchange_type=None, name=None,
                 vhost_name=None):
        # The attributes. This parameter is unavailable in the current version.
        self.attributes = attributes  # type: dict[str, any]
        # Indicates whether the exchange was automatically deleted.
        self.auto_delete_state = auto_delete_state  # type: bool
        # The timestamp that indicates when the exchange was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The exchange type.
        self.exchange_type = exchange_type  # type: str
        # The exchange name.
        self.name = name  # type: str
        # The vhost name.
        self.vhost_name = vhost_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExchangesResponseBodyDataExchanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.name is not None:
            result['Name'] = self.name
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        return self


class ListExchangesResponseBodyData(TeaModel):
    def __init__(self, exchanges=None, max_results=None, next_token=None):
        # The exchanges.
        self.exchanges = exchanges  # type: list[ListExchangesResponseBodyDataExchanges]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page.``
        # 
        # *   If the value of this parameter is empty, the next query is not required and the token used to start the next query is unavailable.``
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.``
        self.next_token = next_token  # type: str

    def validate(self):
        if self.exchanges:
            for k in self.exchanges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExchangesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Exchanges'] = []
        if self.exchanges is not None:
            for k in self.exchanges:
                result['Exchanges'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.exchanges = []
        if m.get('Exchanges') is not None:
            for k in m.get('Exchanges'):
                temp_model = ListExchangesResponseBodyDataExchanges()
                self.exchanges.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExchangesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListExchangesResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListExchangesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListExchangesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExchangesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExchangesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExchangesResponse, self).to_map()
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
            temp_model = ListExchangesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None):
        # The maximum number of entries to return. Valid values: 1 to 100.
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListInstancesResponseBodyDataInstancesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键。
        self.key = key  # type: str
        # 标签值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyDataInstancesTags, self).to_map()
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


class ListInstancesResponseBodyDataInstances(TeaModel):
    def __init__(self, auto_renew_instance=None, classic_endpoint=None, expire_time=None, instance_id=None,
                 instance_name=None, instance_type=None, max_eip_tps=None, max_queue=None, max_tps=None, max_vhost=None,
                 order_create_time=None, order_type=None, private_endpoint=None, public_endpoint=None, status=None, storage_size=None,
                 support_eip=None, tags=None):
        # Indicates whether the instance is automatically renewed.
        self.auto_renew_instance = auto_renew_instance  # type: bool
        # The endpoint that is used to access the instance over the classic network. This parameter is no longer available.
        self.classic_endpoint = classic_endpoint  # type: str
        # The timestamp that indicates when the instance expires. Unit: milliseconds.
        self.expire_time = expire_time  # type: long
        # The instance ID
        self.instance_id = instance_id  # type: str
        # The instance name.
        self.instance_name = instance_name  # type: str
        # The instance type.
        # 
        # *   PROFESSIONAL: Professional Edition
        # *   ENTERPRISE: Enterprise Edition
        # *   VIP: Enterprise Platinum Edition
        self.instance_type = instance_type  # type: str
        # The maximum number of Internet-based transactions per second (TPS) for the instance.
        self.max_eip_tps = max_eip_tps  # type: int
        # The maximum number of queues on the instance.
        self.max_queue = max_queue  # type: int
        # The maximum number of VPC-based TPS for the instance.
        self.max_tps = max_tps  # type: int
        # The maximum number of vhosts on the instance.
        self.max_vhost = max_vhost  # type: int
        # The timestamp that indicates when the order was created. Unit: milliseconds.
        self.order_create_time = order_create_time  # type: long
        # The billing method. Valid values:
        # 
        # *   PrePaid: the subscription billing method.
        # *   POST_PAID: the pay-as-you-go billing method.
        self.order_type = order_type  # type: str
        # The virtual private cloud (VPC) endpoint of the instance.
        self.private_endpoint = private_endpoint  # type: str
        # The public endpoint of the instance.
        self.public_endpoint = public_endpoint  # type: str
        # The instance status. Valid values:
        # 
        # *   DEPLOYING: The instance is being deployed.
        # *   EXPIRED: The instance is expired.
        # *   SERVING: The instance is running.
        # *   RELEASED: The instance is released.
        self.status = status  # type: str
        # The disk size. Unit: GB.
        # 
        # >  For Professional Edition instances and Enterprise Edition instances, this parameter is unavailable and \*\*-1\*\* is returned.
        self.storage_size = storage_size  # type: int
        # Indicates whether the instance supports elastic IP addresses (EIPs).
        self.support_eip = support_eip  # type: bool
        # 标签列表。
        self.tags = tags  # type: list[ListInstancesResponseBodyDataInstancesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyDataInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_instance is not None:
            result['AutoRenewInstance'] = self.auto_renew_instance
        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps
        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost
        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint
        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewInstance') is not None:
            self.auto_renew_instance = m.get('AutoRenewInstance')
        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')
        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')
        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')
        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyDataInstancesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(self, instances=None, max_results=None, next_token=None):
        # The instances.
        self.instances = instances  # type: list[ListInstancesResponseBodyDataInstances]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListInstancesResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueConsumersRequest(TeaModel):
    def __init__(self, instance_id=None, next_token=None, query_count=None, queue=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The number of data entries to return. If you do not configure this parameter, the default value 1 is used.
        # 
        # Valid values: 1 to 100.
        self.query_count = query_count  # type: int
        # The name of the queue for which you want to query online consumers.
        self.queue = queue  # type: str
        # The virtual host (vhost) name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueConsumersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListQueueConsumersResponseBodyDataConsumers(TeaModel):
    def __init__(self, consumer_tag=None):
        # The consumer tag.
        self.consumer_tag = consumer_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueConsumersResponseBodyDataConsumers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')
        return self


class ListQueueConsumersResponseBodyData(TeaModel):
    def __init__(self, consumers=None, max_results=None, next_token=None):
        # The consumers.
        self.consumers = consumers  # type: list[ListQueueConsumersResponseBodyDataConsumers]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.consumers:
            for k in self.consumers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueueConsumersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Consumers'] = []
        if self.consumers is not None:
            for k in self.consumers:
                result['Consumers'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.consumers = []
        if m.get('Consumers') is not None:
            for k in m.get('Consumers'):
                temp_model = ListQueueConsumersResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListQueueConsumersResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListQueueConsumersResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQueueConsumersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueueConsumersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueueConsumersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueueConsumersResponse, self).to_map()
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
            temp_model = ListQueueConsumersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueUpStreamBindingsRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None, queue_name=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return.
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The queue name.
        self.queue_name = queue_name  # type: str
        # The virtual host (vhost) name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueUpStreamBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListQueueUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(self, argument=None, binding_key=None, binding_type=None, destination_name=None,
                 source_exchange=None):
        # The x-match attribute. Valid values:
        # 
        # *   **all:** A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   **any:** A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # This parameter is available for only headers exchanges.
        self.argument = argument  # type: str
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (\_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (\_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\*), the number sign (#) or asterisk (\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\*) is used in the middle of a binding key, the number sign (#) or asterisk (\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key  # type: str
        # The type of the object to which the source exchange is bound. Valid values:
        # 
        # *   **QUEUE**\
        # *   **EXCHANGE**\
        self.binding_type = binding_type  # type: str
        # The name of the object to which the source exchange is bound.
        self.destination_name = destination_name  # type: str
        # The name of the source exchange.
        self.source_exchange = source_exchange  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueueUpStreamBindingsResponseBodyDataBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListQueueUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(self, bindings=None, max_results=None, next_token=None):
        # The bindings.
        self.bindings = bindings  # type: list[ListQueueUpStreamBindingsResponseBodyDataBindings]
        # The maximum number of entries returned.
        self.max_results = max_results  # type: str
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueueUpStreamBindingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListQueueUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListQueueUpStreamBindingsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListQueueUpStreamBindingsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQueueUpStreamBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueueUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueueUpStreamBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueueUpStreamBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueueUpStreamBindingsResponse, self).to_map()
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
            temp_model = ListQueueUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None, virtual_host=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return.
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str
        # The virtual host (vhost) name.
        self.virtual_host = virtual_host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListQueuesResponseBodyDataQueues(TeaModel):
    def __init__(self, attributes=None, auto_delete_state=None, create_time=None, exclusive_state=None,
                 last_consume_time=None, name=None, owner_id=None, vhost_name=None):
        # The attributes.
        self.attributes = attributes  # type: dict[str, any]
        # Indicates whether the queue was automatically deleted.
        self.auto_delete_state = auto_delete_state  # type: bool
        # The time when the queue was created.
        self.create_time = create_time  # type: long
        # Indicates whether the queue is an exclusive queue.
        self.exclusive_state = exclusive_state  # type: bool
        # The time when messages in the queue were last consumed.
        self.last_consume_time = last_consume_time  # type: long
        # The queue name.
        self.name = name  # type: str
        # The ID of the ApsaraMQ for RabbitMQ instance to which the queue belongs.
        self.owner_id = owner_id  # type: str
        # The vhost name.
        self.vhost_name = vhost_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueuesResponseBodyDataQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.last_consume_time is not None:
            result['LastConsumeTime'] = self.last_consume_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('LastConsumeTime') is not None:
            self.last_consume_time = m.get('LastConsumeTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        return self


class ListQueuesResponseBodyData(TeaModel):
    def __init__(self, max_results=None, next_token=None, queues=None):
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str
        # The queues.
        self.queues = queues  # type: list[ListQueuesResponseBodyDataQueues]

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = ListQueuesResponseBodyDataQueues()
                self.queues.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListQueuesResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueuesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueuesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueuesResponse, self).to_map()
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
            temp_model = ListQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualHostsRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, next_token=None):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of entries to return. Valid values: **1 to 100**\
        self.max_results = max_results  # type: int
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVirtualHostsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListVirtualHostsResponseBodyDataVirtualHosts(TeaModel):
    def __init__(self, name=None):
        # The vhost name.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVirtualHostsResponseBodyDataVirtualHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListVirtualHostsResponseBodyData(TeaModel):
    def __init__(self, max_results=None, next_token=None, virtual_hosts=None):
        # The maximum number of entries returned.
        self.max_results = max_results  # type: int
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token  # type: str
        # The vhosts.
        self.virtual_hosts = virtual_hosts  # type: list[ListVirtualHostsResponseBodyDataVirtualHosts]

    def validate(self):
        if self.virtual_hosts:
            for k in self.virtual_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVirtualHostsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['VirtualHosts'] = []
        if self.virtual_hosts is not None:
            for k in self.virtual_hosts:
                result['VirtualHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.virtual_hosts = []
        if m.get('VirtualHosts') is not None:
            for k in m.get('VirtualHosts'):
                temp_model = ListVirtualHostsResponseBodyDataVirtualHosts()
                self.virtual_hosts.append(temp_model.from_map(k))
        return self


class ListVirtualHostsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned data.
        self.data = data  # type: ListVirtualHostsResponseBodyData
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListVirtualHostsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListVirtualHostsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVirtualHostsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVirtualHostsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVirtualHostsResponse, self).to_map()
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
            temp_model = ListVirtualHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, instance_type=None, max_connections=None,
                 max_eip_tps=None, max_private_tps=None, modify_type=None, queue_capacity=None, serverless_charge_type=None,
                 storage_size=None, support_eip=None, support_tracing=None, tracing_storage_time=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.max_connections = max_connections  # type: int
        self.max_eip_tps = max_eip_tps  # type: long
        self.max_private_tps = max_private_tps  # type: long
        self.modify_type = modify_type  # type: str
        self.queue_capacity = queue_capacity  # type: int
        self.serverless_charge_type = serverless_charge_type  # type: str
        self.storage_size = storage_size  # type: int
        self.support_eip = support_eip  # type: bool
        self.support_tracing = support_tracing  # type: bool
        self.tracing_storage_time = tracing_storage_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps
        if self.max_private_tps is not None:
            result['MaxPrivateTps'] = self.max_private_tps
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.queue_capacity is not None:
            result['QueueCapacity'] = self.queue_capacity
        if self.serverless_charge_type is not None:
            result['ServerlessChargeType'] = self.serverless_charge_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.support_eip is not None:
            result['SupportEip'] = self.support_eip
        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing
        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')
        if m.get('MaxPrivateTps') is not None:
            self.max_private_tps = m.get('MaxPrivateTps')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('QueueCapacity') is not None:
            self.queue_capacity = m.get('QueueCapacity')
        if m.get('ServerlessChargeType') is not None:
            self.serverless_charge_type = m.get('ServerlessChargeType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SupportEip') is not None:
            self.support_eip = m.get('SupportEip')
        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')
        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, status_code=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status_code = status_code  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
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
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
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
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(self, instance_id=None, instance_name=None):
        # The ID of the ApsaraMQ for RabbitMQ instance for which you want to update the name.
        self.instance_id = instance_id  # type: str
        # The new name of the instance. No limits are imposed on the value. We recommend that you set this parameter to a maximum of 64 characters in length.
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class UpdateInstanceNameResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code.
        self.code = code  # type: int
        # The returned data.
        self.data = data  # type: str
        # The error message that is returned when an error occurs during the update of the instance name.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned message that indicates the request is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNameResponseBody, self).to_map()
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


class UpdateInstanceNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceNameResponse, self).to_map()
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
            temp_model = UpdateInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


