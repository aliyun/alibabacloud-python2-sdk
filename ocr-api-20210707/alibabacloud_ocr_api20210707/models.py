# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataSubImagesFigureInfoValueFigureDetailsFigurePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSubImagesFigureInfoValueFigureDetailsFigurePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DataSubImagesFigureInfoValueFigureDetailsFigureRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, width=None, height=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSubImagesFigureInfoValueFigureDetailsFigureRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DataSubImagesFigureInfoValueFigureDetails(TeaModel):
    def __init__(self, type=None, data=None, figure_points=None, figure_rect=None, figure_angle=None):
        self.type = type  # type: str
        self.data = data  # type: any
        self.figure_points = figure_points  # type: list[DataSubImagesFigureInfoValueFigureDetailsFigurePoints]
        self.figure_rect = figure_rect  # type: DataSubImagesFigureInfoValueFigureDetailsFigureRect
        self.figure_angle = figure_angle  # type: int

    def validate(self):
        if self.figure_points:
            for k in self.figure_points:
                if k:
                    k.validate()
        if self.figure_rect:
            self.figure_rect.validate()

    def to_map(self):
        _map = super(DataSubImagesFigureInfoValueFigureDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.data is not None:
            result['Data'] = self.data
        result['FigurePoints'] = []
        if self.figure_points is not None:
            for k in self.figure_points:
                result['FigurePoints'].append(k.to_map() if k else None)
        if self.figure_rect is not None:
            result['FigureRect'] = self.figure_rect.to_map()
        if self.figure_angle is not None:
            result['FigureAngle'] = self.figure_angle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        self.figure_points = []
        if m.get('FigurePoints') is not None:
            for k in m.get('FigurePoints'):
                temp_model = DataSubImagesFigureInfoValueFigureDetailsFigurePoints()
                self.figure_points.append(temp_model.from_map(k))
        if m.get('FigureRect') is not None:
            temp_model = DataSubImagesFigureInfoValueFigureDetailsFigureRect()
            self.figure_rect = temp_model.from_map(m['FigureRect'])
        if m.get('FigureAngle') is not None:
            self.figure_angle = m.get('FigureAngle')
        return self


class DataSubImagesFigureInfoValue(TeaModel):
    def __init__(self, figure_count=None, figure_details=None):
        self.figure_count = figure_count  # type: int
        self.figure_details = figure_details  # type: list[DataSubImagesFigureInfoValueFigureDetails]

    def validate(self):
        if self.figure_details:
            for k in self.figure_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DataSubImagesFigureInfoValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_count is not None:
            result['FigureCount'] = self.figure_count
        result['FigureDetails'] = []
        if self.figure_details is not None:
            for k in self.figure_details:
                result['FigureDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureCount') is not None:
            self.figure_count = m.get('FigureCount')
        self.figure_details = []
        if m.get('FigureDetails') is not None:
            for k in m.get('FigureDetails'):
                temp_model = DataSubImagesFigureInfoValueFigureDetails()
                self.figure_details.append(temp_model.from_map(k))
        return self


class DataSubImagesKvInfoKvDetailsValueValuePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSubImagesKvInfoKvDetailsValueValuePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DataSubImagesKvInfoKvDetailsValueValueRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, width=None, height=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataSubImagesKvInfoKvDetailsValueValueRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DataSubImagesKvInfoKvDetailsValue(TeaModel):
    def __init__(self, key_name=None, key_confidence=None, value=None, value_confidence=None, value_points=None,
                 value_rect=None, value_angle=None):
        self.key_name = key_name  # type: str
        self.key_confidence = key_confidence  # type: int
        self.value = value  # type: str
        self.value_confidence = value_confidence  # type: int
        self.value_points = value_points  # type: list[DataSubImagesKvInfoKvDetailsValueValuePoints]
        self.value_rect = value_rect  # type: DataSubImagesKvInfoKvDetailsValueValueRect
        self.value_angle = value_angle  # type: int

    def validate(self):
        if self.value_points:
            for k in self.value_points:
                if k:
                    k.validate()
        if self.value_rect:
            self.value_rect.validate()

    def to_map(self):
        _map = super(DataSubImagesKvInfoKvDetailsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_name is not None:
            result['KeyName'] = self.key_name
        if self.key_confidence is not None:
            result['KeyConfidence'] = self.key_confidence
        if self.value is not None:
            result['Value'] = self.value
        if self.value_confidence is not None:
            result['ValueConfidence'] = self.value_confidence
        result['ValuePoints'] = []
        if self.value_points is not None:
            for k in self.value_points:
                result['ValuePoints'].append(k.to_map() if k else None)
        if self.value_rect is not None:
            result['ValueRect'] = self.value_rect.to_map()
        if self.value_angle is not None:
            result['ValueAngle'] = self.value_angle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')
        if m.get('KeyConfidence') is not None:
            self.key_confidence = m.get('KeyConfidence')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueConfidence') is not None:
            self.value_confidence = m.get('ValueConfidence')
        self.value_points = []
        if m.get('ValuePoints') is not None:
            for k in m.get('ValuePoints'):
                temp_model = DataSubImagesKvInfoKvDetailsValueValuePoints()
                self.value_points.append(temp_model.from_map(k))
        if m.get('ValueRect') is not None:
            temp_model = DataSubImagesKvInfoKvDetailsValueValueRect()
            self.value_rect = temp_model.from_map(m['ValueRect'])
        if m.get('ValueAngle') is not None:
            self.value_angle = m.get('ValueAngle')
        return self


class RecognizeAdvancedRequest(TeaModel):
    def __init__(self, need_rotate=None, need_sort_page=None, no_stamp=None, output_char_info=None,
                 output_figure=None, output_table=None, paragraph=None, row=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.need_sort_page = need_sort_page  # type: bool
        self.no_stamp = no_stamp  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_figure = output_figure  # type: bool
        self.output_table = output_table  # type: bool
        self.paragraph = paragraph  # type: bool
        self.row = row  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAdvancedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        if self.no_stamp is not None:
            result['NoStamp'] = self.no_stamp
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.paragraph is not None:
            result['Paragraph'] = self.paragraph
        if self.row is not None:
            result['Row'] = self.row
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        if m.get('NoStamp') is not None:
            self.no_stamp = m.get('NoStamp')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Paragraph') is not None:
            self.paragraph = m.get('Paragraph')
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeAdvancedResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAdvancedResponseBody, self).to_map()
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
        return self


class RecognizeAdvancedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeAdvancedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAdvancedResponse, self).to_map()
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
            temp_model = RecognizeAdvancedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAirItineraryRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAirItineraryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeAirItineraryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAirItineraryResponseBody, self).to_map()
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
        return self


class RecognizeAirItineraryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeAirItineraryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAirItineraryResponse, self).to_map()
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
            temp_model = RecognizeAirItineraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeAllTextRequestAdvancedConfig(TeaModel):
    def __init__(self, is_hand_writing_table=None, is_line_less_table=None, output_char_info=None,
                 output_paragraph=None, output_row=None, output_table=None, output_table_excel=None, output_table_html=None):
        self.is_hand_writing_table = is_hand_writing_table  # type: bool
        self.is_line_less_table = is_line_less_table  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_paragraph = output_paragraph  # type: bool
        self.output_row = output_row  # type: bool
        self.output_table = output_table  # type: bool
        self.output_table_excel = output_table_excel  # type: bool
        self.output_table_html = output_table_html  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextRequestAdvancedConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_hand_writing_table is not None:
            result['IsHandWritingTable'] = self.is_hand_writing_table
        if self.is_line_less_table is not None:
            result['IsLineLessTable'] = self.is_line_less_table
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_paragraph is not None:
            result['OutputParagraph'] = self.output_paragraph
        if self.output_row is not None:
            result['OutputRow'] = self.output_row
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.output_table_excel is not None:
            result['OutputTableExcel'] = self.output_table_excel
        if self.output_table_html is not None:
            result['OutputTableHtml'] = self.output_table_html
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsHandWritingTable') is not None:
            self.is_hand_writing_table = m.get('IsHandWritingTable')
        if m.get('IsLineLessTable') is not None:
            self.is_line_less_table = m.get('IsLineLessTable')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputParagraph') is not None:
            self.output_paragraph = m.get('OutputParagraph')
        if m.get('OutputRow') is not None:
            self.output_row = m.get('OutputRow')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('OutputTableExcel') is not None:
            self.output_table_excel = m.get('OutputTableExcel')
        if m.get('OutputTableHtml') is not None:
            self.output_table_html = m.get('OutputTableHtml')
        return self


class RecognizeAllTextRequestIdCardConfig(TeaModel):
    def __init__(self, output_id_card_quality=None):
        self.output_id_card_quality = output_id_card_quality  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextRequestIdCardConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_id_card_quality is not None:
            result['OutputIdCardQuality'] = self.output_id_card_quality
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputIdCardQuality') is not None:
            self.output_id_card_quality = m.get('OutputIdCardQuality')
        return self


class RecognizeAllTextRequestInternationalIdCardConfig(TeaModel):
    def __init__(self, country=None):
        self.country = country  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextRequestInternationalIdCardConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class RecognizeAllTextRequestMultiLanConfig(TeaModel):
    def __init__(self, languages=None):
        self.languages = languages  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextRequestMultiLanConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.languages is not None:
            result['Languages'] = self.languages
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Languages') is not None:
            self.languages = m.get('Languages')
        return self


class RecognizeAllTextRequest(TeaModel):
    def __init__(self, advanced_config=None, id_card_config=None, international_id_card_config=None,
                 multi_lan_config=None, output_bar_code=None, output_coordinate=None, output_figure=None, output_kvexcel=None,
                 output_oricoord=None, output_qrcode=None, output_stamp=None, page_no=None, type=None, url=None, body=None):
        self.advanced_config = advanced_config  # type: RecognizeAllTextRequestAdvancedConfig
        self.id_card_config = id_card_config  # type: RecognizeAllTextRequestIdCardConfig
        self.international_id_card_config = international_id_card_config  # type: RecognizeAllTextRequestInternationalIdCardConfig
        self.multi_lan_config = multi_lan_config  # type: RecognizeAllTextRequestMultiLanConfig
        self.output_bar_code = output_bar_code  # type: bool
        self.output_coordinate = output_coordinate  # type: bytes
        self.output_figure = output_figure  # type: bool
        self.output_kvexcel = output_kvexcel  # type: bool
        self.output_oricoord = output_oricoord  # type: bool
        self.output_qrcode = output_qrcode  # type: bool
        self.output_stamp = output_stamp  # type: bool
        self.page_no = page_no  # type: int
        self.type = type  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        if self.advanced_config:
            self.advanced_config.validate()
        if self.id_card_config:
            self.id_card_config.validate()
        if self.international_id_card_config:
            self.international_id_card_config.validate()
        if self.multi_lan_config:
            self.multi_lan_config.validate()

    def to_map(self):
        _map = super(RecognizeAllTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_config is not None:
            result['AdvancedConfig'] = self.advanced_config.to_map()
        if self.id_card_config is not None:
            result['IdCardConfig'] = self.id_card_config.to_map()
        if self.international_id_card_config is not None:
            result['InternationalIdCardConfig'] = self.international_id_card_config.to_map()
        if self.multi_lan_config is not None:
            result['MultiLanConfig'] = self.multi_lan_config.to_map()
        if self.output_bar_code is not None:
            result['OutputBarCode'] = self.output_bar_code
        if self.output_coordinate is not None:
            result['OutputCoordinate'] = self.output_coordinate
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.output_kvexcel is not None:
            result['OutputKVExcel'] = self.output_kvexcel
        if self.output_oricoord is not None:
            result['OutputOricoord'] = self.output_oricoord
        if self.output_qrcode is not None:
            result['OutputQrcode'] = self.output_qrcode
        if self.output_stamp is not None:
            result['OutputStamp'] = self.output_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedConfig') is not None:
            temp_model = RecognizeAllTextRequestAdvancedConfig()
            self.advanced_config = temp_model.from_map(m['AdvancedConfig'])
        if m.get('IdCardConfig') is not None:
            temp_model = RecognizeAllTextRequestIdCardConfig()
            self.id_card_config = temp_model.from_map(m['IdCardConfig'])
        if m.get('InternationalIdCardConfig') is not None:
            temp_model = RecognizeAllTextRequestInternationalIdCardConfig()
            self.international_id_card_config = temp_model.from_map(m['InternationalIdCardConfig'])
        if m.get('MultiLanConfig') is not None:
            temp_model = RecognizeAllTextRequestMultiLanConfig()
            self.multi_lan_config = temp_model.from_map(m['MultiLanConfig'])
        if m.get('OutputBarCode') is not None:
            self.output_bar_code = m.get('OutputBarCode')
        if m.get('OutputCoordinate') is not None:
            self.output_coordinate = m.get('OutputCoordinate')
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('OutputKVExcel') is not None:
            self.output_kvexcel = m.get('OutputKVExcel')
        if m.get('OutputOricoord') is not None:
            self.output_oricoord = m.get('OutputOricoord')
        if m.get('OutputQrcode') is not None:
            self.output_qrcode = m.get('OutputQrcode')
        if m.get('OutputStamp') is not None:
            self.output_stamp = m.get('OutputStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeAllTextShrinkRequest(TeaModel):
    def __init__(self, advanced_config_shrink=None, id_card_config_shrink=None,
                 international_id_card_config_shrink=None, multi_lan_config_shrink=None, output_bar_code=None, output_coordinate=None,
                 output_figure=None, output_kvexcel=None, output_oricoord=None, output_qrcode=None, output_stamp=None,
                 page_no=None, type=None, url=None, body=None):
        self.advanced_config_shrink = advanced_config_shrink  # type: str
        self.id_card_config_shrink = id_card_config_shrink  # type: str
        self.international_id_card_config_shrink = international_id_card_config_shrink  # type: str
        self.multi_lan_config_shrink = multi_lan_config_shrink  # type: str
        self.output_bar_code = output_bar_code  # type: bool
        self.output_coordinate = output_coordinate  # type: bytes
        self.output_figure = output_figure  # type: bool
        self.output_kvexcel = output_kvexcel  # type: bool
        self.output_oricoord = output_oricoord  # type: bool
        self.output_qrcode = output_qrcode  # type: bool
        self.output_stamp = output_stamp  # type: bool
        self.page_no = page_no  # type: int
        self.type = type  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_config_shrink is not None:
            result['AdvancedConfig'] = self.advanced_config_shrink
        if self.id_card_config_shrink is not None:
            result['IdCardConfig'] = self.id_card_config_shrink
        if self.international_id_card_config_shrink is not None:
            result['InternationalIdCardConfig'] = self.international_id_card_config_shrink
        if self.multi_lan_config_shrink is not None:
            result['MultiLanConfig'] = self.multi_lan_config_shrink
        if self.output_bar_code is not None:
            result['OutputBarCode'] = self.output_bar_code
        if self.output_coordinate is not None:
            result['OutputCoordinate'] = self.output_coordinate
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.output_kvexcel is not None:
            result['OutputKVExcel'] = self.output_kvexcel
        if self.output_oricoord is not None:
            result['OutputOricoord'] = self.output_oricoord
        if self.output_qrcode is not None:
            result['OutputQrcode'] = self.output_qrcode
        if self.output_stamp is not None:
            result['OutputStamp'] = self.output_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedConfig') is not None:
            self.advanced_config_shrink = m.get('AdvancedConfig')
        if m.get('IdCardConfig') is not None:
            self.id_card_config_shrink = m.get('IdCardConfig')
        if m.get('InternationalIdCardConfig') is not None:
            self.international_id_card_config_shrink = m.get('InternationalIdCardConfig')
        if m.get('MultiLanConfig') is not None:
            self.multi_lan_config_shrink = m.get('MultiLanConfig')
        if m.get('OutputBarCode') is not None:
            self.output_bar_code = m.get('OutputBarCode')
        if m.get('OutputCoordinate') is not None:
            self.output_coordinate = m.get('OutputCoordinate')
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('OutputKVExcel') is not None:
            self.output_kvexcel = m.get('OutputKVExcel')
        if m.get('OutputOricoord') is not None:
            self.output_oricoord = m.get('OutputOricoord')
        if m.get('OutputQrcode') is not None:
            self.output_qrcode = m.get('OutputQrcode')
        if m.get('OutputStamp') is not None:
            self.output_stamp = m.get('OutputStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodeRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodeRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetails(TeaModel):
    def __init__(self, bar_code_angle=None, bar_code_points=None, bar_code_rect=None, data=None, type=None):
        self.bar_code_angle = bar_code_angle  # type: int
        self.bar_code_points = bar_code_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodePoints]
        self.bar_code_rect = bar_code_rect  # type: RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodeRect
        self.data = data  # type: any
        self.type = type  # type: str

    def validate(self):
        if self.bar_code_points:
            for k in self.bar_code_points:
                if k:
                    k.validate()
        if self.bar_code_rect:
            self.bar_code_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bar_code_angle is not None:
            result['BarCodeAngle'] = self.bar_code_angle
        result['BarCodePoints'] = []
        if self.bar_code_points is not None:
            for k in self.bar_code_points:
                result['BarCodePoints'].append(k.to_map() if k else None)
        if self.bar_code_rect is not None:
            result['BarCodeRect'] = self.bar_code_rect.to_map()
        if self.data is not None:
            result['Data'] = self.data
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BarCodeAngle') is not None:
            self.bar_code_angle = m.get('BarCodeAngle')
        self.bar_code_points = []
        if m.get('BarCodePoints') is not None:
            for k in m.get('BarCodePoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodePoints()
                self.bar_code_points.append(temp_model.from_map(k))
        if m.get('BarCodeRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetailsBarCodeRect()
            self.bar_code_rect = temp_model.from_map(m['BarCodeRect'])
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBarCodeInfo(TeaModel):
    def __init__(self, bar_code_count=None, bar_code_details=None):
        self.bar_code_count = bar_code_count  # type: int
        self.bar_code_details = bar_code_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetails]

    def validate(self):
        if self.bar_code_details:
            for k in self.bar_code_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBarCodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bar_code_count is not None:
            result['BarCodeCount'] = self.bar_code_count
        result['BarCodeDetails'] = []
        if self.bar_code_details is not None:
            for k in self.bar_code_details:
                result['BarCodeDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BarCodeCount') is not None:
            self.bar_code_count = m.get('BarCodeCount')
        self.bar_code_details = []
        if m.get('BarCodeDetails') is not None:
            for k in m.get('BarCodeDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBarCodeInfoBarCodeDetails()
                self.bar_code_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockPoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharPoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfos(TeaModel):
    def __init__(self, char_confidence=None, char_content=None, char_id=None, char_points=None, char_rect=None):
        self.char_confidence = char_confidence  # type: int
        self.char_content = char_content  # type: str
        self.char_id = char_id  # type: int
        self.char_points = char_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharPoints]
        self.char_rect = char_rect  # type: RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharRect

    def validate(self):
        if self.char_points:
            for k in self.char_points:
                if k:
                    k.validate()
        if self.char_rect:
            self.char_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.char_confidence is not None:
            result['CharConfidence'] = self.char_confidence
        if self.char_content is not None:
            result['CharContent'] = self.char_content
        if self.char_id is not None:
            result['CharId'] = self.char_id
        result['CharPoints'] = []
        if self.char_points is not None:
            for k in self.char_points:
                result['CharPoints'].append(k.to_map() if k else None)
        if self.char_rect is not None:
            result['CharRect'] = self.char_rect.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharConfidence') is not None:
            self.char_confidence = m.get('CharConfidence')
        if m.get('CharContent') is not None:
            self.char_content = m.get('CharContent')
        if m.get('CharId') is not None:
            self.char_id = m.get('CharId')
        self.char_points = []
        if m.get('CharPoints') is not None:
            for k in m.get('CharPoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharPoints()
                self.char_points.append(temp_model.from_map(k))
        if m.get('CharRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfosCharRect()
            self.char_rect = temp_model.from_map(m['CharRect'])
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetails(TeaModel):
    def __init__(self, block_angle=None, block_confidence=None, block_content=None, block_id=None,
                 block_points=None, block_rect=None, char_infos=None):
        self.block_angle = block_angle  # type: int
        self.block_confidence = block_confidence  # type: int
        self.block_content = block_content  # type: str
        self.block_id = block_id  # type: int
        self.block_points = block_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockPoints]
        self.block_rect = block_rect  # type: RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockRect
        self.char_infos = char_infos  # type: list[RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfos]

    def validate(self):
        if self.block_points:
            for k in self.block_points:
                if k:
                    k.validate()
        if self.block_rect:
            self.block_rect.validate()
        if self.char_infos:
            for k in self.char_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_angle is not None:
            result['BlockAngle'] = self.block_angle
        if self.block_confidence is not None:
            result['BlockConfidence'] = self.block_confidence
        if self.block_content is not None:
            result['BlockContent'] = self.block_content
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        result['BlockPoints'] = []
        if self.block_points is not None:
            for k in self.block_points:
                result['BlockPoints'].append(k.to_map() if k else None)
        if self.block_rect is not None:
            result['BlockRect'] = self.block_rect.to_map()
        result['CharInfos'] = []
        if self.char_infos is not None:
            for k in self.char_infos:
                result['CharInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockAngle') is not None:
            self.block_angle = m.get('BlockAngle')
        if m.get('BlockConfidence') is not None:
            self.block_confidence = m.get('BlockConfidence')
        if m.get('BlockContent') is not None:
            self.block_content = m.get('BlockContent')
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        self.block_points = []
        if m.get('BlockPoints') is not None:
            for k in m.get('BlockPoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockPoints()
                self.block_points.append(temp_model.from_map(k))
        if m.get('BlockRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsBlockRect()
            self.block_rect = temp_model.from_map(m['BlockRect'])
        self.char_infos = []
        if m.get('CharInfos') is not None:
            for k in m.get('CharInfos'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetailsCharInfos()
                self.char_infos.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesBlockInfo(TeaModel):
    def __init__(self, block_count=None, block_details=None):
        self.block_count = block_count  # type: int
        self.block_details = block_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetails]

    def validate(self):
        if self.block_details:
            for k in self.block_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesBlockInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        result['BlockDetails'] = []
        if self.block_details is not None:
            for k in self.block_details:
                result['BlockDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        self.block_details = []
        if m.get('BlockDetails') is not None:
            for k in m.get('BlockDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfoBlockDetails()
                self.block_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesKvInfo(TeaModel):
    def __init__(self, data=None, kv_count=None, kv_details=None):
        self.data = data  # type: any
        self.kv_count = kv_count  # type: int
        self.kv_details = kv_details  # type: dict[str, DataSubImagesKvInfoKvDetailsValue]

    def validate(self):
        if self.kv_details:
            for v in self.kv_details.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesKvInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.kv_count is not None:
            result['KvCount'] = self.kv_count
        result['KvDetails'] = {}
        if self.kv_details is not None:
            for k, v in self.kv_details.items():
                result['KvDetails'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('KvCount') is not None:
            self.kv_count = m.get('KvCount')
        self.kv_details = {}
        if m.get('KvDetails') is not None:
            for k, v in m.get('KvDetails').items():
                temp_model = DataSubImagesKvInfoKvDetailsValue()
                self.kv_details[k] = temp_model.from_map(v)
        return self


class RecognizeAllTextResponseBodyDataSubImagesParagraphInfoParagraphDetails(TeaModel):
    def __init__(self, block_list=None, paragraph_content=None, paragraph_id=None):
        self.block_list = block_list  # type: list[int]
        self.paragraph_content = paragraph_content  # type: str
        self.paragraph_id = paragraph_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesParagraphInfoParagraphDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_list is not None:
            result['BlockList'] = self.block_list
        if self.paragraph_content is not None:
            result['ParagraphContent'] = self.paragraph_content
        if self.paragraph_id is not None:
            result['ParagraphId'] = self.paragraph_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockList') is not None:
            self.block_list = m.get('BlockList')
        if m.get('ParagraphContent') is not None:
            self.paragraph_content = m.get('ParagraphContent')
        if m.get('ParagraphId') is not None:
            self.paragraph_id = m.get('ParagraphId')
        return self


class RecognizeAllTextResponseBodyDataSubImagesParagraphInfo(TeaModel):
    def __init__(self, paragraph_count=None, paragraph_details=None):
        self.paragraph_count = paragraph_count  # type: int
        self.paragraph_details = paragraph_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesParagraphInfoParagraphDetails]

    def validate(self):
        if self.paragraph_details:
            for k in self.paragraph_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesParagraphInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paragraph_count is not None:
            result['ParagraphCount'] = self.paragraph_count
        result['ParagraphDetails'] = []
        if self.paragraph_details is not None:
            for k in self.paragraph_details:
                result['ParagraphDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParagraphCount') is not None:
            self.paragraph_count = m.get('ParagraphCount')
        self.paragraph_details = []
        if m.get('ParagraphDetails') is not None:
            for k in m.get('ParagraphDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesParagraphInfoParagraphDetails()
                self.paragraph_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodeRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodeRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetails(TeaModel):
    def __init__(self, data=None, qr_code_angle=None, qr_code_points=None, qr_code_rect=None):
        self.data = data  # type: any
        self.qr_code_angle = qr_code_angle  # type: int
        self.qr_code_points = qr_code_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodePoints]
        self.qr_code_rect = qr_code_rect  # type: RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodeRect

    def validate(self):
        if self.qr_code_points:
            for k in self.qr_code_points:
                if k:
                    k.validate()
        if self.qr_code_rect:
            self.qr_code_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.qr_code_angle is not None:
            result['QrCodeAngle'] = self.qr_code_angle
        result['QrCodePoints'] = []
        if self.qr_code_points is not None:
            for k in self.qr_code_points:
                result['QrCodePoints'].append(k.to_map() if k else None)
        if self.qr_code_rect is not None:
            result['QrCodeRect'] = self.qr_code_rect.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('QrCodeAngle') is not None:
            self.qr_code_angle = m.get('QrCodeAngle')
        self.qr_code_points = []
        if m.get('QrCodePoints') is not None:
            for k in m.get('QrCodePoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodePoints()
                self.qr_code_points.append(temp_model.from_map(k))
        if m.get('QrCodeRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetailsQrCodeRect()
            self.qr_code_rect = temp_model.from_map(m['QrCodeRect'])
        return self


class RecognizeAllTextResponseBodyDataSubImagesQrCodeInfo(TeaModel):
    def __init__(self, qr_code_count=None, qr_code_details=None):
        self.qr_code_count = qr_code_count  # type: int
        self.qr_code_details = qr_code_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetails]

    def validate(self):
        if self.qr_code_details:
            for k in self.qr_code_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesQrCodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qr_code_count is not None:
            result['QrCodeCount'] = self.qr_code_count
        result['QrCodeDetails'] = []
        if self.qr_code_details is not None:
            for k in self.qr_code_details:
                result['QrCodeDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QrCodeCount') is not None:
            self.qr_code_count = m.get('QrCodeCount')
        self.qr_code_details = []
        if m.get('QrCodeDetails') is not None:
            for k in m.get('QrCodeDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesQrCodeInfoQrCodeDetails()
                self.qr_code_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesQualityInfo(TeaModel):
    def __init__(self, completeness_score=None, is_copy=None, is_reshoot=None, quality_score=None,
                 tamper_score=None):
        self.completeness_score = completeness_score  # type: float
        self.is_copy = is_copy  # type: bool
        self.is_reshoot = is_reshoot  # type: bool
        self.quality_score = quality_score  # type: float
        self.tamper_score = tamper_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesQualityInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completeness_score is not None:
            result['CompletenessScore'] = self.completeness_score
        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy
        if self.is_reshoot is not None:
            result['IsReshoot'] = self.is_reshoot
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        if self.tamper_score is not None:
            result['TamperScore'] = self.tamper_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletenessScore') is not None:
            self.completeness_score = m.get('CompletenessScore')
        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')
        if m.get('IsReshoot') is not None:
            self.is_reshoot = m.get('IsReshoot')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        if m.get('TamperScore') is not None:
            self.tamper_score = m.get('TamperScore')
        return self


class RecognizeAllTextResponseBodyDataSubImagesRowInfoRowDetails(TeaModel):
    def __init__(self, block_list=None, row_content=None, row_id=None):
        self.block_list = block_list  # type: list[int]
        self.row_content = row_content  # type: str
        self.row_id = row_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesRowInfoRowDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_list is not None:
            result['BlockList'] = self.block_list
        if self.row_content is not None:
            result['RowContent'] = self.row_content
        if self.row_id is not None:
            result['RowId'] = self.row_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockList') is not None:
            self.block_list = m.get('BlockList')
        if m.get('RowContent') is not None:
            self.row_content = m.get('RowContent')
        if m.get('RowId') is not None:
            self.row_id = m.get('RowId')
        return self


class RecognizeAllTextResponseBodyDataSubImagesRowInfo(TeaModel):
    def __init__(self, row_count=None, row_details=None):
        self.row_count = row_count  # type: int
        self.row_details = row_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesRowInfoRowDetails]

    def validate(self):
        if self.row_details:
            for k in self.row_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesRowInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        result['RowDetails'] = []
        if self.row_details is not None:
            for k in self.row_details:
                result['RowDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        self.row_details = []
        if m.get('RowDetails') is not None:
            for k in m.get('RowDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesRowInfoRowDetails()
                self.row_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsData(TeaModel):
    def __init__(self, anti_fake_code=None, company_id=None, organization_name=None, organization_name_eng=None,
                 other_text=None, taxpayer_id=None, top_text=None):
        self.anti_fake_code = anti_fake_code  # type: str
        self.company_id = company_id  # type: str
        self.organization_name = organization_name  # type: str
        self.organization_name_eng = organization_name_eng  # type: str
        self.other_text = other_text  # type: str
        self.taxpayer_id = taxpayer_id  # type: str
        self.top_text = top_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_fake_code is not None:
            result['AntiFakeCode'] = self.anti_fake_code
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_name_eng is not None:
            result['OrganizationNameEng'] = self.organization_name_eng
        if self.other_text is not None:
            result['OtherText'] = self.other_text
        if self.taxpayer_id is not None:
            result['TaxpayerId'] = self.taxpayer_id
        if self.top_text is not None:
            result['TopText'] = self.top_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AntiFakeCode') is not None:
            self.anti_fake_code = m.get('AntiFakeCode')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationNameEng') is not None:
            self.organization_name_eng = m.get('OrganizationNameEng')
        if m.get('OtherText') is not None:
            self.other_text = m.get('OtherText')
        if m.get('TaxpayerId') is not None:
            self.taxpayer_id = m.get('TaxpayerId')
        if m.get('TopText') is not None:
            self.top_text = m.get('TopText')
        return self


class RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampPoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetails(TeaModel):
    def __init__(self, data=None, stamp_angle=None, stamp_points=None, stamp_rect=None):
        self.data = data  # type: RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsData
        self.stamp_angle = stamp_angle  # type: int
        self.stamp_points = stamp_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampPoints]
        self.stamp_rect = stamp_rect  # type: RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampRect

    def validate(self):
        if self.data:
            self.data.validate()
        if self.stamp_points:
            for k in self.stamp_points:
                if k:
                    k.validate()
        if self.stamp_rect:
            self.stamp_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.stamp_angle is not None:
            result['StampAngle'] = self.stamp_angle
        result['StampPoints'] = []
        if self.stamp_points is not None:
            for k in self.stamp_points:
                result['StampPoints'].append(k.to_map() if k else None)
        if self.stamp_rect is not None:
            result['StampRect'] = self.stamp_rect.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('StampAngle') is not None:
            self.stamp_angle = m.get('StampAngle')
        self.stamp_points = []
        if m.get('StampPoints') is not None:
            for k in m.get('StampPoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampPoints()
                self.stamp_points.append(temp_model.from_map(k))
        if m.get('StampRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetailsStampRect()
            self.stamp_rect = temp_model.from_map(m['StampRect'])
        return self


class RecognizeAllTextResponseBodyDataSubImagesStampInfo(TeaModel):
    def __init__(self, stamp_count=None, stamp_details=None):
        self.stamp_count = stamp_count  # type: int
        self.stamp_details = stamp_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetails]

    def validate(self):
        if self.stamp_details:
            for k in self.stamp_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesStampInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stamp_count is not None:
            result['StampCount'] = self.stamp_count
        result['StampDetails'] = []
        if self.stamp_details is not None:
            for k in self.stamp_details:
                result['StampDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StampCount') is not None:
            self.stamp_count = m.get('StampCount')
        self.stamp_details = []
        if m.get('StampDetails') is not None:
            for k in m.get('StampDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesStampInfoStampDetails()
                self.stamp_details.append(temp_model.from_map(k))
        return self


class RecognizeAllTextResponseBodyDataSubImagesSubImagePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesSubImagePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesSubImageRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesSubImageRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellPoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetails(TeaModel):
    def __init__(self, block_list=None, cell_angle=None, cell_content=None, cell_id=None, cell_points=None,
                 cell_rect=None, column_end=None, column_start=None, row_end=None, row_start=None):
        self.block_list = block_list  # type: list[int]
        self.cell_angle = cell_angle  # type: int
        self.cell_content = cell_content  # type: str
        self.cell_id = cell_id  # type: int
        self.cell_points = cell_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellPoints]
        self.cell_rect = cell_rect  # type: RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellRect
        self.column_end = column_end  # type: int
        self.column_start = column_start  # type: int
        self.row_end = row_end  # type: int
        self.row_start = row_start  # type: int

    def validate(self):
        if self.cell_points:
            for k in self.cell_points:
                if k:
                    k.validate()
        if self.cell_rect:
            self.cell_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_list is not None:
            result['BlockList'] = self.block_list
        if self.cell_angle is not None:
            result['CellAngle'] = self.cell_angle
        if self.cell_content is not None:
            result['CellContent'] = self.cell_content
        if self.cell_id is not None:
            result['CellId'] = self.cell_id
        result['CellPoints'] = []
        if self.cell_points is not None:
            for k in self.cell_points:
                result['CellPoints'].append(k.to_map() if k else None)
        if self.cell_rect is not None:
            result['CellRect'] = self.cell_rect.to_map()
        if self.column_end is not None:
            result['ColumnEnd'] = self.column_end
        if self.column_start is not None:
            result['ColumnStart'] = self.column_start
        if self.row_end is not None:
            result['RowEnd'] = self.row_end
        if self.row_start is not None:
            result['RowStart'] = self.row_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockList') is not None:
            self.block_list = m.get('BlockList')
        if m.get('CellAngle') is not None:
            self.cell_angle = m.get('CellAngle')
        if m.get('CellContent') is not None:
            self.cell_content = m.get('CellContent')
        if m.get('CellId') is not None:
            self.cell_id = m.get('CellId')
        self.cell_points = []
        if m.get('CellPoints') is not None:
            for k in m.get('CellPoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellPoints()
                self.cell_points.append(temp_model.from_map(k))
        if m.get('CellRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetailsCellRect()
            self.cell_rect = temp_model.from_map(m['CellRect'])
        if m.get('ColumnEnd') is not None:
            self.column_end = m.get('ColumnEnd')
        if m.get('ColumnStart') is not None:
            self.column_start = m.get('ColumnStart')
        if m.get('RowEnd') is not None:
            self.row_end = m.get('RowEnd')
        if m.get('RowStart') is not None:
            self.row_start = m.get('RowStart')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsFooter(TeaModel):
    def __init__(self, block_id=None, contents=None):
        self.block_id = block_id  # type: int
        self.contents = contents  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsFooter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsHeader(TeaModel):
    def __init__(self, block_id=None, contents=None):
        self.block_id = block_id  # type: int
        self.contents = contents  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsHeader, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_id is not None:
            result['BlockId'] = self.block_id
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTablePoints(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTablePoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTableRect(TeaModel):
    def __init__(self, center_x=None, center_y=None, height=None, width=None):
        self.center_x = center_x  # type: int
        self.center_y = center_y  # type: int
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTableRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.center_x is not None:
            result['CenterX'] = self.center_x
        if self.center_y is not None:
            result['CenterY'] = self.center_y
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenterX') is not None:
            self.center_x = m.get('CenterX')
        if m.get('CenterY') is not None:
            self.center_y = m.get('CenterY')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetails(TeaModel):
    def __init__(self, cell_count=None, cell_details=None, column_count=None, footer=None, header=None,
                 row_count=None, table_id=None, table_points=None, table_rect=None):
        self.cell_count = cell_count  # type: int
        self.cell_details = cell_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetails]
        self.column_count = column_count  # type: int
        self.footer = footer  # type: RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsFooter
        self.header = header  # type: RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsHeader
        self.row_count = row_count  # type: int
        self.table_id = table_id  # type: int
        self.table_points = table_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTablePoints]
        self.table_rect = table_rect  # type: RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTableRect

    def validate(self):
        if self.cell_details:
            for k in self.cell_details:
                if k:
                    k.validate()
        if self.footer:
            self.footer.validate()
        if self.header:
            self.header.validate()
        if self.table_points:
            for k in self.table_points:
                if k:
                    k.validate()
        if self.table_rect:
            self.table_rect.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cell_count is not None:
            result['CellCount'] = self.cell_count
        result['CellDetails'] = []
        if self.cell_details is not None:
            for k in self.cell_details:
                result['CellDetails'].append(k.to_map() if k else None)
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count
        if self.footer is not None:
            result['Footer'] = self.footer.to_map()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.table_id is not None:
            result['TableId'] = self.table_id
        result['TablePoints'] = []
        if self.table_points is not None:
            for k in self.table_points:
                result['TablePoints'].append(k.to_map() if k else None)
        if self.table_rect is not None:
            result['TableRect'] = self.table_rect.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CellCount') is not None:
            self.cell_count = m.get('CellCount')
        self.cell_details = []
        if m.get('CellDetails') is not None:
            for k in m.get('CellDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsCellDetails()
                self.cell_details.append(temp_model.from_map(k))
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')
        if m.get('Footer') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsFooter()
            self.footer = temp_model.from_map(m['Footer'])
        if m.get('Header') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        self.table_points = []
        if m.get('TablePoints') is not None:
            for k in m.get('TablePoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTablePoints()
                self.table_points.append(temp_model.from_map(k))
        if m.get('TableRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetailsTableRect()
            self.table_rect = temp_model.from_map(m['TableRect'])
        return self


class RecognizeAllTextResponseBodyDataSubImagesTableInfo(TeaModel):
    def __init__(self, table_count=None, table_details=None, table_excel=None, table_html=None):
        self.table_count = table_count  # type: int
        self.table_details = table_details  # type: list[RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetails]
        self.table_excel = table_excel  # type: str
        self.table_html = table_html  # type: str

    def validate(self):
        if self.table_details:
            for k in self.table_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImagesTableInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        result['TableDetails'] = []
        if self.table_details is not None:
            for k in self.table_details:
                result['TableDetails'].append(k.to_map() if k else None)
        if self.table_excel is not None:
            result['TableExcel'] = self.table_excel
        if self.table_html is not None:
            result['TableHtml'] = self.table_html
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        self.table_details = []
        if m.get('TableDetails') is not None:
            for k in m.get('TableDetails'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfoTableDetails()
                self.table_details.append(temp_model.from_map(k))
        if m.get('TableExcel') is not None:
            self.table_excel = m.get('TableExcel')
        if m.get('TableHtml') is not None:
            self.table_html = m.get('TableHtml')
        return self


class RecognizeAllTextResponseBodyDataSubImages(TeaModel):
    def __init__(self, angle=None, bar_code_info=None, block_info=None, figure_info=None, kv_info=None,
                 paragraph_info=None, qr_code_info=None, quality_info=None, row_info=None, stamp_info=None, sub_image_id=None,
                 sub_image_points=None, sub_image_rect=None, table_info=None, type=None):
        self.angle = angle  # type: int
        self.bar_code_info = bar_code_info  # type: RecognizeAllTextResponseBodyDataSubImagesBarCodeInfo
        self.block_info = block_info  # type: RecognizeAllTextResponseBodyDataSubImagesBlockInfo
        self.figure_info = figure_info  # type: dict[str, DataSubImagesFigureInfoValue]
        self.kv_info = kv_info  # type: RecognizeAllTextResponseBodyDataSubImagesKvInfo
        self.paragraph_info = paragraph_info  # type: RecognizeAllTextResponseBodyDataSubImagesParagraphInfo
        self.qr_code_info = qr_code_info  # type: RecognizeAllTextResponseBodyDataSubImagesQrCodeInfo
        self.quality_info = quality_info  # type: RecognizeAllTextResponseBodyDataSubImagesQualityInfo
        self.row_info = row_info  # type: RecognizeAllTextResponseBodyDataSubImagesRowInfo
        self.stamp_info = stamp_info  # type: RecognizeAllTextResponseBodyDataSubImagesStampInfo
        self.sub_image_id = sub_image_id  # type: int
        self.sub_image_points = sub_image_points  # type: list[RecognizeAllTextResponseBodyDataSubImagesSubImagePoints]
        self.sub_image_rect = sub_image_rect  # type: RecognizeAllTextResponseBodyDataSubImagesSubImageRect
        self.table_info = table_info  # type: RecognizeAllTextResponseBodyDataSubImagesTableInfo
        self.type = type  # type: str

    def validate(self):
        if self.bar_code_info:
            self.bar_code_info.validate()
        if self.block_info:
            self.block_info.validate()
        if self.figure_info:
            for v in self.figure_info.values():
                if v:
                    v.validate()
        if self.kv_info:
            self.kv_info.validate()
        if self.paragraph_info:
            self.paragraph_info.validate()
        if self.qr_code_info:
            self.qr_code_info.validate()
        if self.quality_info:
            self.quality_info.validate()
        if self.row_info:
            self.row_info.validate()
        if self.stamp_info:
            self.stamp_info.validate()
        if self.sub_image_points:
            for k in self.sub_image_points:
                if k:
                    k.validate()
        if self.sub_image_rect:
            self.sub_image_rect.validate()
        if self.table_info:
            self.table_info.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyDataSubImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.bar_code_info is not None:
            result['BarCodeInfo'] = self.bar_code_info.to_map()
        if self.block_info is not None:
            result['BlockInfo'] = self.block_info.to_map()
        result['FigureInfo'] = {}
        if self.figure_info is not None:
            for k, v in self.figure_info.items():
                result['FigureInfo'][k] = v.to_map()
        if self.kv_info is not None:
            result['KvInfo'] = self.kv_info.to_map()
        if self.paragraph_info is not None:
            result['ParagraphInfo'] = self.paragraph_info.to_map()
        if self.qr_code_info is not None:
            result['QrCodeInfo'] = self.qr_code_info.to_map()
        if self.quality_info is not None:
            result['QualityInfo'] = self.quality_info.to_map()
        if self.row_info is not None:
            result['RowInfo'] = self.row_info.to_map()
        if self.stamp_info is not None:
            result['StampInfo'] = self.stamp_info.to_map()
        if self.sub_image_id is not None:
            result['SubImageId'] = self.sub_image_id
        result['SubImagePoints'] = []
        if self.sub_image_points is not None:
            for k in self.sub_image_points:
                result['SubImagePoints'].append(k.to_map() if k else None)
        if self.sub_image_rect is not None:
            result['SubImageRect'] = self.sub_image_rect.to_map()
        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('BarCodeInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesBarCodeInfo()
            self.bar_code_info = temp_model.from_map(m['BarCodeInfo'])
        if m.get('BlockInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesBlockInfo()
            self.block_info = temp_model.from_map(m['BlockInfo'])
        self.figure_info = {}
        if m.get('FigureInfo') is not None:
            for k, v in m.get('FigureInfo').items():
                temp_model = DataSubImagesFigureInfoValue()
                self.figure_info[k] = temp_model.from_map(v)
        if m.get('KvInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesKvInfo()
            self.kv_info = temp_model.from_map(m['KvInfo'])
        if m.get('ParagraphInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesParagraphInfo()
            self.paragraph_info = temp_model.from_map(m['ParagraphInfo'])
        if m.get('QrCodeInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesQrCodeInfo()
            self.qr_code_info = temp_model.from_map(m['QrCodeInfo'])
        if m.get('QualityInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesQualityInfo()
            self.quality_info = temp_model.from_map(m['QualityInfo'])
        if m.get('RowInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesRowInfo()
            self.row_info = temp_model.from_map(m['RowInfo'])
        if m.get('StampInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesStampInfo()
            self.stamp_info = temp_model.from_map(m['StampInfo'])
        if m.get('SubImageId') is not None:
            self.sub_image_id = m.get('SubImageId')
        self.sub_image_points = []
        if m.get('SubImagePoints') is not None:
            for k in m.get('SubImagePoints'):
                temp_model = RecognizeAllTextResponseBodyDataSubImagesSubImagePoints()
                self.sub_image_points.append(temp_model.from_map(k))
        if m.get('SubImageRect') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesSubImageRect()
            self.sub_image_rect = temp_model.from_map(m['SubImageRect'])
        if m.get('TableInfo') is not None:
            temp_model = RecognizeAllTextResponseBodyDataSubImagesTableInfo()
            self.table_info = temp_model.from_map(m['TableInfo'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecognizeAllTextResponseBodyData(TeaModel):
    def __init__(self, algo_server=None, algo_version=None, content=None, debug_info=None, height=None,
                 is_mixed_mode=None, kv_excel_url=None, page_no=None, sub_image_count=None, sub_images=None, width=None,
                 xml_result=None):
        self.algo_server = algo_server  # type: list[str]
        self.algo_version = algo_version  # type: str
        self.content = content  # type: str
        self.debug_info = debug_info  # type: any
        self.height = height  # type: int
        self.is_mixed_mode = is_mixed_mode  # type: bool
        self.kv_excel_url = kv_excel_url  # type: str
        self.page_no = page_no  # type: int
        self.sub_image_count = sub_image_count  # type: int
        self.sub_images = sub_images  # type: list[RecognizeAllTextResponseBodyDataSubImages]
        self.width = width  # type: int
        self.xml_result = xml_result  # type: str

    def validate(self):
        if self.sub_images:
            for k in self.sub_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_server is not None:
            result['AlgoServer'] = self.algo_server
        if self.algo_version is not None:
            result['AlgoVersion'] = self.algo_version
        if self.content is not None:
            result['Content'] = self.content
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.height is not None:
            result['Height'] = self.height
        if self.is_mixed_mode is not None:
            result['IsMixedMode'] = self.is_mixed_mode
        if self.kv_excel_url is not None:
            result['KvExcelUrl'] = self.kv_excel_url
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.sub_image_count is not None:
            result['SubImageCount'] = self.sub_image_count
        result['SubImages'] = []
        if self.sub_images is not None:
            for k in self.sub_images:
                result['SubImages'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        if self.xml_result is not None:
            result['XmlResult'] = self.xml_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgoServer') is not None:
            self.algo_server = m.get('AlgoServer')
        if m.get('AlgoVersion') is not None:
            self.algo_version = m.get('AlgoVersion')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('IsMixedMode') is not None:
            self.is_mixed_mode = m.get('IsMixedMode')
        if m.get('KvExcelUrl') is not None:
            self.kv_excel_url = m.get('KvExcelUrl')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('SubImageCount') is not None:
            self.sub_image_count = m.get('SubImageCount')
        self.sub_images = []
        if m.get('SubImages') is not None:
            for k in m.get('SubImages'):
                temp_model = RecognizeAllTextResponseBodyDataSubImages()
                self.sub_images.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('XmlResult') is not None:
            self.xml_result = m.get('XmlResult')
        return self


class RecognizeAllTextResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: RecognizeAllTextResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponseBody, self).to_map()
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
            temp_model = RecognizeAllTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecognizeAllTextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeAllTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeAllTextResponse, self).to_map()
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
            temp_model = RecognizeAllTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankAcceptanceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAcceptanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBankAcceptanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAcceptanceResponseBody, self).to_map()
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
        return self


class RecognizeBankAcceptanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBankAcceptanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankAcceptanceResponse, self).to_map()
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
            temp_model = RecognizeBankAcceptanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankAccountLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBankAccountLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseResponseBody, self).to_map()
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
        return self


class RecognizeBankAccountLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBankAccountLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankAccountLicenseResponse, self).to_map()
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
            temp_model = RecognizeBankAccountLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBankCardRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBankCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBankCardResponseBody, self).to_map()
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
        return self


class RecognizeBankCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBankCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBankCardResponse, self).to_map()
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
            temp_model = RecognizeBankCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBasicRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBasicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBasicResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBasicResponseBody, self).to_map()
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
        return self


class RecognizeBasicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBasicResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBasicResponse, self).to_map()
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
            temp_model = RecognizeBasicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBirthCertificationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBirthCertificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBirthCertificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBirthCertificationResponseBody, self).to_map()
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
        return self


class RecognizeBirthCertificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBirthCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBirthCertificationResponse, self).to_map()
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
            temp_model = RecognizeBirthCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusShipTicketRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusShipTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBusShipTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusShipTicketResponseBody, self).to_map()
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
        return self


class RecognizeBusShipTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBusShipTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBusShipTicketResponse, self).to_map()
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
            temp_model = RecognizeBusShipTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeBusinessLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeBusinessLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponseBody, self).to_map()
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
        return self


class RecognizeBusinessLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeBusinessLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeBusinessLicenseResponse, self).to_map()
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
            temp_model = RecognizeBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCarInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeCarInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCarInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarInvoiceResponse, self).to_map()
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
            temp_model = RecognizeCarInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarNumberRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCarNumberResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarNumberResponseBody, self).to_map()
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
        return self


class RecognizeCarNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCarNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarNumberResponse, self).to_map()
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
            temp_model = RecognizeCarNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCarVinCodeRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarVinCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCarVinCodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCarVinCodeResponseBody, self).to_map()
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
        return self


class RecognizeCarVinCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCarVinCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCarVinCodeResponse, self).to_map()
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
            temp_model = RecognizeCarVinCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeChinesePassportRequest(TeaModel):
    def __init__(self, output_figure=None, url=None, body=None):
        self.output_figure = output_figure  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeChinesePassportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeChinesePassportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeChinesePassportResponseBody, self).to_map()
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
        return self


class RecognizeChinesePassportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeChinesePassportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeChinesePassportResponse, self).to_map()
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
            temp_model = RecognizeChinesePassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCommonPrintedInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCommonPrintedInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCommonPrintedInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCommonPrintedInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeCommonPrintedInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCommonPrintedInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCommonPrintedInvoiceResponse, self).to_map()
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
            temp_model = RecognizeCommonPrintedInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCosmeticProduceLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCosmeticProduceLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCosmeticProduceLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCosmeticProduceLicenseResponseBody, self).to_map()
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
        return self


class RecognizeCosmeticProduceLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCosmeticProduceLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCosmeticProduceLicenseResponse, self).to_map()
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
            temp_model = RecognizeCosmeticProduceLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCovidTestReportRequest(TeaModel):
    def __init__(self, multiple_result=None, url=None, body=None):
        self.multiple_result = multiple_result  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCovidTestReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multiple_result is not None:
            result['MultipleResult'] = self.multiple_result
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MultipleResult') is not None:
            self.multiple_result = m.get('MultipleResult')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCovidTestReportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCovidTestReportResponseBody, self).to_map()
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
        return self


class RecognizeCovidTestReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCovidTestReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCovidTestReportResponse, self).to_map()
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
            temp_model = RecognizeCovidTestReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeCtwoMedicalDeviceManageLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeCtwoMedicalDeviceManageLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseResponseBody, self).to_map()
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
        return self


class RecognizeCtwoMedicalDeviceManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeCtwoMedicalDeviceManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeCtwoMedicalDeviceManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeCtwoMedicalDeviceManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDocumentStructureRequest(TeaModel):
    def __init__(self, need_rotate=None, need_sort_page=None, no_stamp=None, output_char_info=None,
                 output_table=None, page=None, paragraph=None, row=None, url=None, use_new_style_output=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.need_sort_page = need_sort_page  # type: bool
        self.no_stamp = no_stamp  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.page = page  # type: bool
        self.paragraph = paragraph  # type: bool
        self.row = row  # type: bool
        self.url = url  # type: str
        self.use_new_style_output = use_new_style_output  # type: bool
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDocumentStructureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        if self.no_stamp is not None:
            result['NoStamp'] = self.no_stamp
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.page is not None:
            result['Page'] = self.page
        if self.paragraph is not None:
            result['Paragraph'] = self.paragraph
        if self.row is not None:
            result['Row'] = self.row
        if self.url is not None:
            result['Url'] = self.url
        if self.use_new_style_output is not None:
            result['UseNewStyleOutput'] = self.use_new_style_output
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        if m.get('NoStamp') is not None:
            self.no_stamp = m.get('NoStamp')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Paragraph') is not None:
            self.paragraph = m.get('Paragraph')
        if m.get('Row') is not None:
            self.row = m.get('Row')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UseNewStyleOutput') is not None:
            self.use_new_style_output = m.get('UseNewStyleOutput')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeDocumentStructureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDocumentStructureResponseBody, self).to_map()
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
        return self


class RecognizeDocumentStructureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeDocumentStructureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDocumentStructureResponse, self).to_map()
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
            temp_model = RecognizeDocumentStructureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeDrivingLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeDrivingLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponseBody, self).to_map()
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
        return self


class RecognizeDrivingLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeDrivingLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeDrivingLicenseResponse, self).to_map()
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
            temp_model = RecognizeDrivingLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduFormulaRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduFormulaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduFormulaResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduFormulaResponseBody, self).to_map()
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
        return self


class RecognizeEduFormulaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduFormulaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduFormulaResponse, self).to_map()
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
            temp_model = RecognizeEduFormulaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduOralCalculationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduOralCalculationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduOralCalculationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduOralCalculationResponseBody, self).to_map()
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
        return self


class RecognizeEduOralCalculationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduOralCalculationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduOralCalculationResponse, self).to_map()
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
            temp_model = RecognizeEduOralCalculationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperCutRequest(TeaModel):
    def __init__(self, cut_type=None, image_type=None, subject=None, url=None, body=None):
        self.cut_type = cut_type  # type: str
        self.image_type = image_type  # type: str
        self.subject = subject  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperCutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cut_type is not None:
            result['CutType'] = self.cut_type
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CutType') is not None:
            self.cut_type = m.get('CutType')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduPaperCutResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperCutResponseBody, self).to_map()
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
        return self


class RecognizeEduPaperCutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduPaperCutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperCutResponse, self).to_map()
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
            temp_model = RecognizeEduPaperCutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperOcrRequest(TeaModel):
    def __init__(self, image_type=None, output_oricoord=None, subject=None, url=None, body=None):
        self.image_type = image_type  # type: str
        self.output_oricoord = output_oricoord  # type: bool
        self.subject = subject  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.output_oricoord is not None:
            result['OutputOricoord'] = self.output_oricoord
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('OutputOricoord') is not None:
            self.output_oricoord = m.get('OutputOricoord')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduPaperOcrResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperOcrResponseBody, self).to_map()
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
        return self


class RecognizeEduPaperOcrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduPaperOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperOcrResponse, self).to_map()
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
            temp_model = RecognizeEduPaperOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduPaperStructedRequest(TeaModel):
    def __init__(self, need_rotate=None, subject=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.subject = subject  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperStructedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduPaperStructedResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduPaperStructedResponseBody, self).to_map()
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
        return self


class RecognizeEduPaperStructedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduPaperStructedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduPaperStructedResponse, self).to_map()
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
            temp_model = RecognizeEduPaperStructedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEduQuestionOcrRequest(TeaModel):
    def __init__(self, need_rotate=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEduQuestionOcrResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrResponseBody, self).to_map()
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
        return self


class RecognizeEduQuestionOcrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEduQuestionOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEduQuestionOcrResponse, self).to_map()
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
            temp_model = RecognizeEduQuestionOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEnglishRequest(TeaModel):
    def __init__(self, need_rotate=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEnglishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEnglishResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEnglishResponseBody, self).to_map()
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
        return self


class RecognizeEnglishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEnglishResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEnglishResponse, self).to_map()
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
            temp_model = RecognizeEnglishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeEstateCertificationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEstateCertificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeEstateCertificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeEstateCertificationResponseBody, self).to_map()
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
        return self


class RecognizeEstateCertificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeEstateCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeEstateCertificationResponse, self).to_map()
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
            temp_model = RecognizeEstateCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeExitEntryPermitToHKRequest(TeaModel):
    def __init__(self, output_figure=None, url=None, body=None):
        self.output_figure = output_figure  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToHKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeExitEntryPermitToHKResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToHKResponseBody, self).to_map()
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
        return self


class RecognizeExitEntryPermitToHKResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeExitEntryPermitToHKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToHKResponse, self).to_map()
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
            temp_model = RecognizeExitEntryPermitToHKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeExitEntryPermitToMainlandRequest(TeaModel):
    def __init__(self, output_figure=None, url=None, body=None):
        self.output_figure = output_figure  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToMainlandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeExitEntryPermitToMainlandResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToMainlandResponseBody, self).to_map()
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
        return self


class RecognizeExitEntryPermitToMainlandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeExitEntryPermitToMainlandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeExitEntryPermitToMainlandResponse, self).to_map()
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
            temp_model = RecognizeExitEntryPermitToMainlandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodManageLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeFoodManageLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseResponseBody, self).to_map()
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
        return self


class RecognizeFoodManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeFoodManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeFoodManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeFoodManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFoodProduceLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeFoodProduceLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseResponseBody, self).to_map()
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
        return self


class RecognizeFoodProduceLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeFoodProduceLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeFoodProduceLicenseResponse, self).to_map()
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
            temp_model = RecognizeFoodProduceLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeGeneralRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeGeneralResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeGeneralResponseBody, self).to_map()
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
        return self


class RecognizeGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeGeneralResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeGeneralResponse, self).to_map()
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
            temp_model = RecognizeGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHKIdcardRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHKIdcardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeHKIdcardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHKIdcardResponseBody, self).to_map()
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
        return self


class RecognizeHKIdcardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeHKIdcardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHKIdcardResponse, self).to_map()
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
            temp_model = RecognizeHKIdcardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHandwritingRequest(TeaModel):
    def __init__(self, need_rotate=None, need_sort_page=None, output_char_info=None, output_table=None, url=None,
                 body=None):
        self.need_rotate = need_rotate  # type: bool
        self.need_sort_page = need_sort_page  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHandwritingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeHandwritingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHandwritingResponseBody, self).to_map()
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
        return self


class RecognizeHandwritingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeHandwritingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHandwritingResponse, self).to_map()
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
            temp_model = RecognizeHandwritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHealthCodeRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHealthCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeHealthCodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHealthCodeResponseBody, self).to_map()
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
        return self


class RecognizeHealthCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeHealthCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHealthCodeResponse, self).to_map()
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
            temp_model = RecognizeHealthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHotelConsumeRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHotelConsumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeHotelConsumeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHotelConsumeResponseBody, self).to_map()
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
        return self


class RecognizeHotelConsumeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeHotelConsumeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHotelConsumeResponse, self).to_map()
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
            temp_model = RecognizeHotelConsumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeHouseholdRequest(TeaModel):
    def __init__(self, is_resident_page=None, url=None, body=None):
        self.is_resident_page = is_resident_page  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseholdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_resident_page is not None:
            result['IsResidentPage'] = self.is_resident_page
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsResidentPage') is not None:
            self.is_resident_page = m.get('IsResidentPage')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeHouseholdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeHouseholdResponseBody, self).to_map()
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
        return self


class RecognizeHouseholdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeHouseholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeHouseholdResponse, self).to_map()
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
            temp_model = RecognizeHouseholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeIdcardRequest(TeaModel):
    def __init__(self, output_figure=None, output_quality_info=None, url=None, body=None):
        self.output_figure = output_figure  # type: bool
        self.output_quality_info = output_quality_info  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdcardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_figure is not None:
            result['OutputFigure'] = self.output_figure
        if self.output_quality_info is not None:
            result['OutputQualityInfo'] = self.output_quality_info
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputFigure') is not None:
            self.output_figure = m.get('OutputFigure')
        if m.get('OutputQualityInfo') is not None:
            self.output_quality_info = m.get('OutputQualityInfo')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeIdcardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeIdcardResponseBody, self).to_map()
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
        return self


class RecognizeIdcardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeIdcardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeIdcardResponse, self).to_map()
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
            temp_model = RecognizeIdcardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeInternationalBusinessLicenseRequest(TeaModel):
    def __init__(self, country=None, url=None, body=None):
        self.country = country  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInternationalBusinessLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeInternationalBusinessLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInternationalBusinessLicenseResponseBody, self).to_map()
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
        return self


class RecognizeInternationalBusinessLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeInternationalBusinessLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeInternationalBusinessLicenseResponse, self).to_map()
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
            temp_model = RecognizeInternationalBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeInternationalIdcardRequest(TeaModel):
    def __init__(self, country=None, url=None, body=None):
        self.country = country  # type: str
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInternationalIdcardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeInternationalIdcardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInternationalIdcardResponseBody, self).to_map()
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
        return self


class RecognizeInternationalIdcardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeInternationalIdcardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeInternationalIdcardResponse, self).to_map()
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
            temp_model = RecognizeInternationalIdcardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeInvoiceRequest(TeaModel):
    def __init__(self, page_no=None, url=None, body=None):
        self.page_no = page_no  # type: int
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeInvoiceResponse, self).to_map()
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
            temp_model = RecognizeInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeJanpaneseRequest(TeaModel):
    def __init__(self, need_rotate=None, output_char_info=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeJanpaneseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeJanpaneseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeJanpaneseResponseBody, self).to_map()
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
        return self


class RecognizeJanpaneseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeJanpaneseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeJanpaneseResponse, self).to_map()
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
            temp_model = RecognizeJanpaneseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeKoreanRequest(TeaModel):
    def __init__(self, need_rotate=None, output_char_info=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeKoreanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeKoreanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeKoreanResponseBody, self).to_map()
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
        return self


class RecognizeKoreanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeKoreanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeKoreanResponse, self).to_map()
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
            temp_model = RecognizeKoreanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeLatinRequest(TeaModel):
    def __init__(self, need_rotate=None, output_char_info=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLatinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeLatinResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeLatinResponseBody, self).to_map()
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
        return self


class RecognizeLatinResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeLatinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeLatinResponse, self).to_map()
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
            temp_model = RecognizeLatinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMedicalDeviceManageLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeMedicalDeviceManageLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseResponseBody, self).to_map()
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
        return self


class RecognizeMedicalDeviceManageLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeMedicalDeviceManageLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMedicalDeviceManageLicenseResponse, self).to_map()
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
            temp_model = RecognizeMedicalDeviceManageLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMedicalDeviceProduceLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeMedicalDeviceProduceLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseResponseBody, self).to_map()
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
        return self


class RecognizeMedicalDeviceProduceLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeMedicalDeviceProduceLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMedicalDeviceProduceLicenseResponse, self).to_map()
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
            temp_model = RecognizeMedicalDeviceProduceLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMixedInvoicesRequest(TeaModel):
    def __init__(self, page_no=None, url=None, body=None):
        self.page_no = page_no  # type: int
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedInvoicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeMixedInvoicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMixedInvoicesResponseBody, self).to_map()
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
        return self


class RecognizeMixedInvoicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeMixedInvoicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMixedInvoicesResponse, self).to_map()
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
            temp_model = RecognizeMixedInvoicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeMultiLanguageRequest(TeaModel):
    def __init__(self, languages=None, need_rotate=None, need_sort_page=None, output_char_info=None,
                 output_table=None, url=None, body=None):
        self.languages = languages  # type: list[str]
        self.need_rotate = need_rotate  # type: bool
        self.need_sort_page = need_sort_page  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.languages is not None:
            result['Languages'] = self.languages
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Languages') is not None:
            self.languages = m.get('Languages')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeMultiLanguageShrinkRequest(TeaModel):
    def __init__(self, languages_shrink=None, need_rotate=None, need_sort_page=None, output_char_info=None,
                 output_table=None, url=None, body=None):
        self.languages_shrink = languages_shrink  # type: str
        self.need_rotate = need_rotate  # type: bool
        self.need_sort_page = need_sort_page  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.languages_shrink is not None:
            result['Languages'] = self.languages_shrink
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.need_sort_page is not None:
            result['NeedSortPage'] = self.need_sort_page
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Languages') is not None:
            self.languages_shrink = m.get('Languages')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('NeedSortPage') is not None:
            self.need_sort_page = m.get('NeedSortPage')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeMultiLanguageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeMultiLanguageResponseBody, self).to_map()
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
        return self


class RecognizeMultiLanguageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeMultiLanguageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeMultiLanguageResponse, self).to_map()
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
            temp_model = RecognizeMultiLanguageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeNonTaxInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeNonTaxInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeNonTaxInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeNonTaxInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeNonTaxInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeNonTaxInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeNonTaxInvoiceResponse, self).to_map()
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
            temp_model = RecognizeNonTaxInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePassportRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizePassportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePassportResponseBody, self).to_map()
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
        return self


class RecognizePassportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizePassportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePassportResponse, self).to_map()
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
            temp_model = RecognizePassportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePaymentRecordRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePaymentRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizePaymentRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePaymentRecordResponseBody, self).to_map()
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
        return self


class RecognizePaymentRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizePaymentRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePaymentRecordResponse, self).to_map()
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
            temp_model = RecognizePaymentRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizePurchaseRecordRequest(TeaModel):
    def __init__(self, output_multi_orders=None, url=None, body=None):
        self.output_multi_orders = output_multi_orders  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePurchaseRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_multi_orders is not None:
            result['OutputMultiOrders'] = self.output_multi_orders
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutputMultiOrders') is not None:
            self.output_multi_orders = m.get('OutputMultiOrders')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizePurchaseRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizePurchaseRecordResponseBody, self).to_map()
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
        return self


class RecognizePurchaseRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizePurchaseRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizePurchaseRecordResponse, self).to_map()
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
            temp_model = RecognizePurchaseRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeQuotaInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeQuotaInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeQuotaInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeQuotaInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeQuotaInvoiceResponse, self).to_map()
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
            temp_model = RecognizeQuotaInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeRideHailingItineraryRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRideHailingItineraryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeRideHailingItineraryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRideHailingItineraryResponseBody, self).to_map()
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
        return self


class RecognizeRideHailingItineraryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeRideHailingItineraryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeRideHailingItineraryResponse, self).to_map()
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
            temp_model = RecognizeRideHailingItineraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeRollTicketRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRollTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeRollTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRollTicketResponseBody, self).to_map()
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
        return self


class RecognizeRollTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeRollTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeRollTicketResponse, self).to_map()
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
            temp_model = RecognizeRollTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeRussianRequest(TeaModel):
    def __init__(self, need_rotate=None, output_char_info=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRussianRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeRussianResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeRussianResponseBody, self).to_map()
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
        return self


class RecognizeRussianResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeRussianResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeRussianResponse, self).to_map()
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
            temp_model = RecognizeRussianResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeShoppingReceiptRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeShoppingReceiptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeShoppingReceiptResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeShoppingReceiptResponseBody, self).to_map()
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
        return self


class RecognizeShoppingReceiptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeShoppingReceiptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeShoppingReceiptResponse, self).to_map()
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
            temp_model = RecognizeShoppingReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeSocialSecurityCardRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeSocialSecurityCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardResponseBody, self).to_map()
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
        return self


class RecognizeSocialSecurityCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeSocialSecurityCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardResponse, self).to_map()
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
            temp_model = RecognizeSocialSecurityCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeSocialSecurityCardVersionIIRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardVersionIIRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeSocialSecurityCardVersionIIResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardVersionIIResponseBody, self).to_map()
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
        return self


class RecognizeSocialSecurityCardVersionIIResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeSocialSecurityCardVersionIIResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeSocialSecurityCardVersionIIResponse, self).to_map()
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
            temp_model = RecognizeSocialSecurityCardVersionIIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTableOcrRequest(TeaModel):
    def __init__(self, is_hand_writing=None, line_less=None, need_rotate=None, skip_detection=None, url=None,
                 body=None):
        self.is_hand_writing = is_hand_writing  # type: str
        self.line_less = line_less  # type: bool
        self.need_rotate = need_rotate  # type: bool
        self.skip_detection = skip_detection  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_hand_writing is not None:
            result['IsHandWriting'] = self.is_hand_writing
        if self.line_less is not None:
            result['LineLess'] = self.line_less
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.skip_detection is not None:
            result['SkipDetection'] = self.skip_detection
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsHandWriting') is not None:
            self.is_hand_writing = m.get('IsHandWriting')
        if m.get('LineLess') is not None:
            self.line_less = m.get('LineLess')
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('SkipDetection') is not None:
            self.skip_detection = m.get('SkipDetection')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTableOcrResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTableOcrResponseBody, self).to_map()
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
        return self


class RecognizeTableOcrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTableOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTableOcrResponse, self).to_map()
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
            temp_model = RecognizeTableOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxClearanceCertificateRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxClearanceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTaxClearanceCertificateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxClearanceCertificateResponseBody, self).to_map()
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
        return self


class RecognizeTaxClearanceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTaxClearanceCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTaxClearanceCertificateResponse, self).to_map()
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
            temp_model = RecognizeTaxClearanceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTaxiInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTaxiInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeTaxiInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTaxiInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTaxiInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTaxiInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeThaiRequest(TeaModel):
    def __init__(self, need_rotate=None, output_char_info=None, output_table=None, url=None, body=None):
        self.need_rotate = need_rotate  # type: bool
        self.output_char_info = output_char_info  # type: bool
        self.output_table = output_table  # type: bool
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeThaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_rotate is not None:
            result['NeedRotate'] = self.need_rotate
        if self.output_char_info is not None:
            result['OutputCharInfo'] = self.output_char_info
        if self.output_table is not None:
            result['OutputTable'] = self.output_table
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NeedRotate') is not None:
            self.need_rotate = m.get('NeedRotate')
        if m.get('OutputCharInfo') is not None:
            self.output_char_info = m.get('OutputCharInfo')
        if m.get('OutputTable') is not None:
            self.output_table = m.get('OutputTable')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeThaiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeThaiResponseBody, self).to_map()
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
        return self


class RecognizeThaiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeThaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeThaiResponse, self).to_map()
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
            temp_model = RecognizeThaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTollInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTollInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTollInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTollInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeTollInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTollInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTollInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTollInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTradeMarkCertificationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTradeMarkCertificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationResponseBody, self).to_map()
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
        return self


class RecognizeTradeMarkCertificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTradeMarkCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTradeMarkCertificationResponse, self).to_map()
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
            temp_model = RecognizeTradeMarkCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeTrainInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeTrainInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeTrainInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeTrainInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeTrainInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeTrainInvoiceResponse, self).to_map()
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
            temp_model = RecognizeTrainInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeUsedCarInvoiceRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeUsedCarInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeUsedCarInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeUsedCarInvoiceResponseBody, self).to_map()
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
        return self


class RecognizeUsedCarInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeUsedCarInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeUsedCarInvoiceResponse, self).to_map()
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
            temp_model = RecognizeUsedCarInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleCertificationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleCertificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeVehicleCertificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleCertificationResponseBody, self).to_map()
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
        return self


class RecognizeVehicleCertificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeVehicleCertificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVehicleCertificationResponse, self).to_map()
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
            temp_model = RecognizeVehicleCertificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleLicenseRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeVehicleLicenseResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleLicenseResponseBody, self).to_map()
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
        return self


class RecognizeVehicleLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeVehicleLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVehicleLicenseResponse, self).to_map()
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
            temp_model = RecognizeVehicleLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeVehicleRegistrationRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleRegistrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeVehicleRegistrationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeVehicleRegistrationResponseBody, self).to_map()
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
        return self


class RecognizeVehicleRegistrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeVehicleRegistrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeVehicleRegistrationResponse, self).to_map()
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
            temp_model = RecognizeVehicleRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeWaybillRequest(TeaModel):
    def __init__(self, url=None, body=None):
        self.url = url  # type: str
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeWaybillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RecognizeWaybillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecognizeWaybillResponseBody, self).to_map()
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
        return self


class RecognizeWaybillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecognizeWaybillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecognizeWaybillResponse, self).to_map()
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
            temp_model = RecognizeWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyBusinessLicenseRequest(TeaModel):
    def __init__(self, company_name=None, credit_code=None, legal_person=None):
        self.company_name = company_name  # type: str
        self.credit_code = credit_code  # type: str
        self.legal_person = legal_person  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyBusinessLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.credit_code is not None:
            result['CreditCode'] = self.credit_code
        if self.legal_person is not None:
            result['LegalPerson'] = self.legal_person
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CreditCode') is not None:
            self.credit_code = m.get('CreditCode')
        if m.get('LegalPerson') is not None:
            self.legal_person = m.get('LegalPerson')
        return self


class VerifyBusinessLicenseResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyBusinessLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyBusinessLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyBusinessLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyBusinessLicenseResponse, self).to_map()
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
            temp_model = VerifyBusinessLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyVATInvoiceRequest(TeaModel):
    def __init__(self, invoice_code=None, invoice_date=None, invoice_no=None, invoice_sum=None, verify_code=None):
        self.invoice_code = invoice_code  # type: str
        self.invoice_date = invoice_date  # type: str
        self.invoice_no = invoice_no  # type: str
        self.invoice_sum = invoice_sum  # type: str
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVATInvoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_sum is not None:
            result['InvoiceSum'] = self.invoice_sum
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceSum') is not None:
            self.invoice_sum = m.get('InvoiceSum')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyVATInvoiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVATInvoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyVATInvoiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyVATInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyVATInvoiceResponse, self).to_map()
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
            temp_model = VerifyVATInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


