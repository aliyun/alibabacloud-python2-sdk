# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CompareImageFacesRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri_a=None, image_uri_b=None, face_id_a=None, face_id_b=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri_a = image_uri_a  # type: str
        self.image_uri_b = image_uri_b  # type: str
        self.face_id_a = face_id_a  # type: str
        self.face_id_b = face_id_b  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri_a is not None:
            result['ImageUriA'] = self.image_uri_a
        if self.image_uri_b is not None:
            result['ImageUriB'] = self.image_uri_b
        if self.face_id_a is not None:
            result['FaceIdA'] = self.face_id_a
        if self.face_id_b is not None:
            result['FaceIdB'] = self.face_id_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUriA') is not None:
            self.image_uri_a = m.get('ImageUriA')
        if m.get('ImageUriB') is not None:
            self.image_uri_b = m.get('ImageUriB')
        if m.get('FaceIdA') is not None:
            self.face_id_a = m.get('FaceIdA')
        if m.get('FaceIdB') is not None:
            self.face_id_b = m.get('FaceIdB')
        return self


class CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class CompareImageFacesResponseBodyFaceAFaceAttributes(TeaModel):
    def __init__(self, face_boundary=None):
        self.face_boundary = face_boundary  # type: CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceAFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class CompareImageFacesResponseBodyFaceA(TeaModel):
    def __init__(self, face_id=None, face_attributes=None):
        self.face_id = face_id  # type: str
        self.face_attributes = face_attributes  # type: CompareImageFacesResponseBodyFaceAFaceAttributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceA, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = CompareImageFacesResponseBodyFaceAFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class CompareImageFacesResponseBodyFaceBFaceAttributes(TeaModel):
    def __init__(self, face_boundary=None):
        self.face_boundary = face_boundary  # type: CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceBFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class CompareImageFacesResponseBodyFaceB(TeaModel):
    def __init__(self, face_id=None, face_attributes=None):
        self.face_id = face_id  # type: str
        self.face_attributes = face_attributes  # type: CompareImageFacesResponseBodyFaceBFaceAttributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponseBodyFaceB, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = CompareImageFacesResponseBodyFaceBFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class CompareImageFacesResponseBody(TeaModel):
    def __init__(self, request_id=None, similarity=None, set_id=None, face_a=None, face_b=None):
        self.request_id = request_id  # type: str
        self.similarity = similarity  # type: float
        self.set_id = set_id  # type: str
        self.face_a = face_a  # type: CompareImageFacesResponseBodyFaceA
        self.face_b = face_b  # type: CompareImageFacesResponseBodyFaceB

    def validate(self):
        if self.face_a:
            self.face_a.validate()
        if self.face_b:
            self.face_b.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.face_a is not None:
            result['FaceA'] = self.face_a.to_map()
        if self.face_b is not None:
            result['FaceB'] = self.face_b.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('FaceA') is not None:
            temp_model = CompareImageFacesResponseBodyFaceA()
            self.face_a = temp_model.from_map(m['FaceA'])
        if m.get('FaceB') is not None:
            temp_model = CompareImageFacesResponseBodyFaceB()
            self.face_b = temp_model.from_map(m['FaceB'])
        return self


class CompareImageFacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CompareImageFacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponse, self).to_map()
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
            temp_model = CompareImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertOfficeFormatRequest(TeaModel):
    def __init__(self, project=None, src_uri=None, tgt_type=None, tgt_uri=None, src_type=None, start_page=None,
                 end_page=None, max_sheet_row=None, max_sheet_col=None, max_sheet_count=None, sheet_one_page=None,
                 model_id=None, password=None, tgt_file_prefix=None, tgt_file_suffix=None, tgt_file_pages=None,
                 fit_to_pages_tall=None, fit_to_pages_wide=None, pdf_vector=None, hidecomments=None):
        self.project = project  # type: str
        self.src_uri = src_uri  # type: str
        self.tgt_type = tgt_type  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.src_type = src_type  # type: str
        self.start_page = start_page  # type: long
        self.end_page = end_page  # type: long
        self.max_sheet_row = max_sheet_row  # type: long
        self.max_sheet_col = max_sheet_col  # type: long
        self.max_sheet_count = max_sheet_count  # type: long
        self.sheet_one_page = sheet_one_page  # type: bool
        self.model_id = model_id  # type: str
        self.password = password  # type: str
        self.tgt_file_prefix = tgt_file_prefix  # type: str
        self.tgt_file_suffix = tgt_file_suffix  # type: str
        self.tgt_file_pages = tgt_file_pages  # type: str
        self.fit_to_pages_tall = fit_to_pages_tall  # type: bool
        self.fit_to_pages_wide = fit_to_pages_wide  # type: bool
        self.pdf_vector = pdf_vector  # type: bool
        self.hidecomments = hidecomments  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertOfficeFormatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.max_sheet_col is not None:
            result['MaxSheetCol'] = self.max_sheet_col
        if self.max_sheet_count is not None:
            result['MaxSheetCount'] = self.max_sheet_count
        if self.sheet_one_page is not None:
            result['SheetOnePage'] = self.sheet_one_page
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.password is not None:
            result['Password'] = self.password
        if self.tgt_file_prefix is not None:
            result['TgtFilePrefix'] = self.tgt_file_prefix
        if self.tgt_file_suffix is not None:
            result['TgtFileSuffix'] = self.tgt_file_suffix
        if self.tgt_file_pages is not None:
            result['TgtFilePages'] = self.tgt_file_pages
        if self.fit_to_pages_tall is not None:
            result['FitToPagesTall'] = self.fit_to_pages_tall
        if self.fit_to_pages_wide is not None:
            result['FitToPagesWide'] = self.fit_to_pages_wide
        if self.pdf_vector is not None:
            result['PdfVector'] = self.pdf_vector
        if self.hidecomments is not None:
            result['Hidecomments'] = self.hidecomments
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('MaxSheetCol') is not None:
            self.max_sheet_col = m.get('MaxSheetCol')
        if m.get('MaxSheetCount') is not None:
            self.max_sheet_count = m.get('MaxSheetCount')
        if m.get('SheetOnePage') is not None:
            self.sheet_one_page = m.get('SheetOnePage')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TgtFilePrefix') is not None:
            self.tgt_file_prefix = m.get('TgtFilePrefix')
        if m.get('TgtFileSuffix') is not None:
            self.tgt_file_suffix = m.get('TgtFileSuffix')
        if m.get('TgtFilePages') is not None:
            self.tgt_file_pages = m.get('TgtFilePages')
        if m.get('FitToPagesTall') is not None:
            self.fit_to_pages_tall = m.get('FitToPagesTall')
        if m.get('FitToPagesWide') is not None:
            self.fit_to_pages_wide = m.get('FitToPagesWide')
        if m.get('PdfVector') is not None:
            self.pdf_vector = m.get('PdfVector')
        if m.get('Hidecomments') is not None:
            self.hidecomments = m.get('Hidecomments')
        return self


class ConvertOfficeFormatResponseBody(TeaModel):
    def __init__(self, page_count=None, request_id=None):
        self.page_count = page_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertOfficeFormatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertOfficeFormatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConvertOfficeFormatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertOfficeFormatResponse, self).to_map()
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
            temp_model = ConvertOfficeFormatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGrabFrameTaskRequest(TeaModel):
    def __init__(self, project=None, video_uri=None, notify_topic_name=None, notify_endpoint=None, target_list=None,
                 custom_message=None):
        self.project = project  # type: str
        self.video_uri = video_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.target_list = target_list  # type: str
        self.custom_message = custom_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGrabFrameTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        return self


class CreateGrabFrameTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGrabFrameTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGrabFrameTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGrabFrameTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGrabFrameTaskResponse, self).to_map()
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
            temp_model = CreateGrabFrameTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupFacesJobRequest(TeaModel):
    def __init__(self, project=None, set_id=None, notify_topic_name=None, notify_endpoint=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupFacesJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateGroupFacesJobResponseBody(TeaModel):
    def __init__(self, job_type=None, request_id=None, set_id=None, job_id=None):
        self.job_type = job_type  # type: str
        self.request_id = request_id  # type: str
        self.set_id = set_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupFacesJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateGroupFacesJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupFacesJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupFacesJobResponse, self).to_map()
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
            temp_model = CreateGroupFacesJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageProcessTaskRequest(TeaModel):
    def __init__(self, project=None, image_uri=None, notify_topic_name=None, notify_endpoint=None, target_list=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.target_list = target_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageProcessTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        return self


class CreateImageProcessTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageProcessTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageProcessTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateImageProcessTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageProcessTaskResponse, self).to_map()
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
            temp_model = CreateImageProcessTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMediaComplexTaskRequest(TeaModel):
    def __init__(self, project=None, parameters=None, notify_topic_name=None, notify_endpoint=None):
        self.project = project  # type: str
        self.parameters = parameters  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaComplexTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateMediaComplexTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaComplexTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateMediaComplexTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateMediaComplexTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMediaComplexTaskResponse, self).to_map()
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
            temp_model = CreateMediaComplexTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeFaceGroupsJobRequest(TeaModel):
    def __init__(self, project=None, set_id=None, notify_topic_name=None, notify_endpoint=None, group_id_from=None,
                 group_id_to=None, custom_message=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.group_id_from = group_id_from  # type: str
        self.group_id_to = group_id_to  # type: str
        self.custom_message = custom_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeFaceGroupsJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.group_id_from is not None:
            result['GroupIdFrom'] = self.group_id_from
        if self.group_id_to is not None:
            result['GroupIdTo'] = self.group_id_to
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('GroupIdFrom') is not None:
            self.group_id_from = m.get('GroupIdFrom')
        if m.get('GroupIdTo') is not None:
            self.group_id_to = m.get('GroupIdTo')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        return self


class CreateMergeFaceGroupsJobResponseBody(TeaModel):
    def __init__(self, group_id_from=None, job_type=None, request_id=None, set_id=None, group_id_to=None,
                 job_id=None):
        self.group_id_from = group_id_from  # type: str
        self.job_type = job_type  # type: str
        self.request_id = request_id  # type: str
        self.set_id = set_id  # type: str
        self.group_id_to = group_id_to  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMergeFaceGroupsJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id_from is not None:
            result['GroupIdFrom'] = self.group_id_from
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.group_id_to is not None:
            result['GroupIdTo'] = self.group_id_to
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupIdFrom') is not None:
            self.group_id_from = m.get('GroupIdFrom')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('GroupIdTo') is not None:
            self.group_id_to = m.get('GroupIdTo')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateMergeFaceGroupsJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateMergeFaceGroupsJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMergeFaceGroupsJobResponse, self).to_map()
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
            temp_model = CreateMergeFaceGroupsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(self, project=None, src_uri=None, tgt_type=None, tgt_uri=None, notify_topic_name=None,
                 notify_endpoint=None, src_type=None, start_page=None, end_page=None, max_sheet_row=None, max_sheet_col=None,
                 max_sheet_count=None, sheet_one_page=None, model_id=None, password=None, tgt_file_prefix=None,
                 tgt_file_suffix=None, tgt_file_pages=None, fit_to_pages_tall=None, fit_to_pages_wide=None, idempotent_token=None,
                 pdf_vector=None, hidecomments=None, display_dpi=None, user_data=None):
        self.project = project  # type: str
        self.src_uri = src_uri  # type: str
        self.tgt_type = tgt_type  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.src_type = src_type  # type: str
        self.start_page = start_page  # type: long
        self.end_page = end_page  # type: long
        self.max_sheet_row = max_sheet_row  # type: long
        self.max_sheet_col = max_sheet_col  # type: long
        self.max_sheet_count = max_sheet_count  # type: long
        self.sheet_one_page = sheet_one_page  # type: bool
        self.model_id = model_id  # type: str
        self.password = password  # type: str
        self.tgt_file_prefix = tgt_file_prefix  # type: str
        self.tgt_file_suffix = tgt_file_suffix  # type: str
        self.tgt_file_pages = tgt_file_pages  # type: str
        self.fit_to_pages_tall = fit_to_pages_tall  # type: bool
        self.fit_to_pages_wide = fit_to_pages_wide  # type: bool
        self.idempotent_token = idempotent_token  # type: str
        self.pdf_vector = pdf_vector  # type: bool
        self.hidecomments = hidecomments  # type: bool
        self.display_dpi = display_dpi  # type: int
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOfficeConversionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.max_sheet_col is not None:
            result['MaxSheetCol'] = self.max_sheet_col
        if self.max_sheet_count is not None:
            result['MaxSheetCount'] = self.max_sheet_count
        if self.sheet_one_page is not None:
            result['SheetOnePage'] = self.sheet_one_page
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.password is not None:
            result['Password'] = self.password
        if self.tgt_file_prefix is not None:
            result['TgtFilePrefix'] = self.tgt_file_prefix
        if self.tgt_file_suffix is not None:
            result['TgtFileSuffix'] = self.tgt_file_suffix
        if self.tgt_file_pages is not None:
            result['TgtFilePages'] = self.tgt_file_pages
        if self.fit_to_pages_tall is not None:
            result['FitToPagesTall'] = self.fit_to_pages_tall
        if self.fit_to_pages_wide is not None:
            result['FitToPagesWide'] = self.fit_to_pages_wide
        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token
        if self.pdf_vector is not None:
            result['PdfVector'] = self.pdf_vector
        if self.hidecomments is not None:
            result['Hidecomments'] = self.hidecomments
        if self.display_dpi is not None:
            result['DisplayDpi'] = self.display_dpi
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('MaxSheetCol') is not None:
            self.max_sheet_col = m.get('MaxSheetCol')
        if m.get('MaxSheetCount') is not None:
            self.max_sheet_count = m.get('MaxSheetCount')
        if m.get('SheetOnePage') is not None:
            self.sheet_one_page = m.get('SheetOnePage')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TgtFilePrefix') is not None:
            self.tgt_file_prefix = m.get('TgtFilePrefix')
        if m.get('TgtFileSuffix') is not None:
            self.tgt_file_suffix = m.get('TgtFileSuffix')
        if m.get('TgtFilePages') is not None:
            self.tgt_file_pages = m.get('TgtFilePages')
        if m.get('FitToPagesTall') is not None:
            self.fit_to_pages_tall = m.get('FitToPagesTall')
        if m.get('FitToPagesWide') is not None:
            self.fit_to_pages_wide = m.get('FitToPagesWide')
        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')
        if m.get('PdfVector') is not None:
            self.pdf_vector = m.get('PdfVector')
        if m.get('Hidecomments') is not None:
            self.hidecomments = m.get('Hidecomments')
        if m.get('DisplayDpi') is not None:
            self.display_dpi = m.get('DisplayDpi')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(self, status=None, task_id=None, request_id=None, percent=None, create_time=None, tgt_loc=None):
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str
        self.percent = percent  # type: int
        self.create_time = create_time  # type: str
        self.tgt_loc = tgt_loc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOfficeConversionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.tgt_loc is not None:
            result['TgtLoc'] = self.tgt_loc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TgtLoc') is not None:
            self.tgt_loc = m.get('TgtLoc')
        return self


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOfficeConversionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOfficeConversionTaskResponse, self).to_map()
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
            temp_model = CreateOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSetRequest(TeaModel):
    def __init__(self, project=None, set_id=None, set_name=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.set_name = set_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.set_name is not None:
            result['SetName'] = self.set_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        return self


class CreateSetResponseBody(TeaModel):
    def __init__(self, video_count=None, request_id=None, create_time=None, video_length=None, set_id=None,
                 image_count=None, face_count=None, set_name=None, modify_time=None):
        self.video_count = video_count  # type: int
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.video_length = video_length  # type: int
        self.set_id = set_id  # type: str
        self.image_count = image_count  # type: int
        self.face_count = face_count  # type: int
        self.set_name = set_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class CreateSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSetResponse, self).to_map()
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
            temp_model = CreateSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoAbstractTaskRequest(TeaModel):
    def __init__(self, project=None, video_uri=None, notify_topic_name=None, notify_endpoint=None,
                 target_video_uri=None, target_clips_uri=None, abstract_length=None):
        self.project = project  # type: str
        self.video_uri = video_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.target_video_uri = target_video_uri  # type: str
        self.target_clips_uri = target_clips_uri  # type: str
        self.abstract_length = abstract_length  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoAbstractTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_video_uri is not None:
            result['TargetVideoUri'] = self.target_video_uri
        if self.target_clips_uri is not None:
            result['TargetClipsUri'] = self.target_clips_uri
        if self.abstract_length is not None:
            result['AbstractLength'] = self.abstract_length
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetVideoUri') is not None:
            self.target_video_uri = m.get('TargetVideoUri')
        if m.get('TargetClipsUri') is not None:
            self.target_clips_uri = m.get('TargetClipsUri')
        if m.get('AbstractLength') is not None:
            self.abstract_length = m.get('AbstractLength')
        return self


class CreateVideoAbstractTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoAbstractTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoAbstractTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVideoAbstractTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoAbstractTaskResponse, self).to_map()
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
            temp_model = CreateVideoAbstractTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoAnalyseTaskRequest(TeaModel):
    def __init__(self, project=None, video_uri=None, tgt_uri=None, notify_topic_name=None, notify_endpoint=None):
        self.project = project  # type: str
        self.video_uri = video_uri  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoAnalyseTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateVideoAnalyseTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoAnalyseTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoAnalyseTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVideoAnalyseTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoAnalyseTaskResponse, self).to_map()
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
            temp_model = CreateVideoAnalyseTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoCompressTaskRequest(TeaModel):
    def __init__(self, project=None, video_uri=None, notify_topic_name=None, notify_endpoint=None, target_list=None,
                 custom_message=None, target_container=None, target_segment=None):
        self.project = project  # type: str
        self.video_uri = video_uri  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.target_list = target_list  # type: str
        self.custom_message = custom_message  # type: str
        self.target_container = target_container  # type: str
        self.target_segment = target_segment  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoCompressTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_segment is not None:
            result['TargetSegment'] = self.target_segment
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetSegment') is not None:
            self.target_segment = m.get('TargetSegment')
        return self


class CreateVideoCompressTaskResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, task_type=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoCompressTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreateVideoCompressTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVideoCompressTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoCompressTaskResponse, self).to_map()
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
            temp_model = CreateVideoCompressTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoProduceTaskRequest(TeaModel):
    def __init__(self, project=None, images=None, notify_topic_name=None, notify_endpoint=None, target_uri=None,
                 custom_message=None, music=None, width=None, height=None, template_name=None):
        self.project = project  # type: str
        self.images = images  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.target_uri = target_uri  # type: str
        self.custom_message = custom_message  # type: str
        self.music = music  # type: str
        self.width = width  # type: int
        self.height = height  # type: int
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoProduceTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.images is not None:
            result['Images'] = self.images
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        if self.music is not None:
            result['Music'] = self.music
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        if m.get('Music') is not None:
            self.music = m.get('Music')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateVideoProduceTaskResponseBody(TeaModel):
    def __init__(self, task_type=None, request_id=None, task_id=None):
        self.task_type = task_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoProduceTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoProduceTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVideoProduceTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoProduceTaskResponse, self).to_map()
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
            temp_model = CreateVideoProduceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecodeBlindWatermarkRequest(TeaModel):
    def __init__(self, project=None, image_uri=None, original_image_uri=None, target_uri=None, image_quality=None,
                 model=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str
        self.original_image_uri = original_image_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.image_quality = image_quality  # type: int
        self.model = model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecodeBlindWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.original_image_uri is not None:
            result['OriginalImageUri'] = self.original_image_uri
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OriginalImageUri') is not None:
            self.original_image_uri = m.get('OriginalImageUri')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class DecodeBlindWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, target_uri=None, content=None):
        self.request_id = request_id  # type: str
        self.target_uri = target_uri  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecodeBlindWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DecodeBlindWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DecodeBlindWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DecodeBlindWatermarkResponse, self).to_map()
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
            temp_model = DecodeBlindWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, request_id=None, set_id=None, image_uri=None):
        self.request_id = request_id  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageJobRequest(TeaModel):
    def __init__(self, project=None, job_type=None, job_id=None):
        self.project = project  # type: str
        self.job_type = job_type  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteImageJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageJobResponseBody, self).to_map()
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


class DeleteImageJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteImageJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageJobResponse, self).to_map()
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
            temp_model = DeleteImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOfficeConversionTaskRequest(TeaModel):
    def __init__(self, project=None, task_id=None):
        self.project = project  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOfficeConversionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteOfficeConversionTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOfficeConversionTaskResponseBody, self).to_map()
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


class DeleteOfficeConversionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteOfficeConversionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOfficeConversionTaskResponse, self).to_map()
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
            temp_model = DeleteOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, project=None):
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSetRequest(TeaModel):
    def __init__(self, project=None, set_id=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class DeleteSetResponseBody(TeaModel):
    def __init__(self, set_id=None, request_id=None):
        self.set_id = set_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSetResponse, self).to_map()
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
            temp_model = DeleteSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoRequest(TeaModel):
    def __init__(self, project=None, set_id=None, video_uri=None, resources=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.video_uri = video_uri  # type: str
        self.resources = resources  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DeleteVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, video_uri=None, set_id=None):
        self.request_id = request_id  # type: str
        self.video_uri = video_uri  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class DeleteVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVideoResponse, self).to_map()
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
            temp_model = DeleteVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoTaskRequest(TeaModel):
    def __init__(self, project=None, task_type=None, task_id=None):
        self.project = project  # type: str
        self.task_type = task_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteVideoTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoTaskResponseBody, self).to_map()
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


class DeleteVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVideoTaskResponse, self).to_map()
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
            temp_model = DeleteVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, region_id=None, project_types=None):
        self.region_id = region_id  # type: str
        self.project_types = project_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.project_types is not None:
            result['ProjectTypes'] = self.project_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProjectTypes') is not None:
            self.project_types = m.get('ProjectTypes')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageBodiesRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageBodiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageBodiesResponseBodyBodiesBodyBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageBodiesResponseBodyBodiesBodyBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageBodiesResponseBodyBodies(TeaModel):
    def __init__(self, body_confidence=None, body_boundary=None):
        self.body_confidence = body_confidence  # type: float
        self.body_boundary = body_boundary  # type: DetectImageBodiesResponseBodyBodiesBodyBoundary

    def validate(self):
        if self.body_boundary:
            self.body_boundary.validate()

    def to_map(self):
        _map = super(DetectImageBodiesResponseBodyBodies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_confidence is not None:
            result['BodyConfidence'] = self.body_confidence
        if self.body_boundary is not None:
            result['BodyBoundary'] = self.body_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BodyConfidence') is not None:
            self.body_confidence = m.get('BodyConfidence')
        if m.get('BodyBoundary') is not None:
            temp_model = DetectImageBodiesResponseBodyBodiesBodyBoundary()
            self.body_boundary = temp_model.from_map(m['BodyBoundary'])
        return self


class DetectImageBodiesResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, bodies=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.bodies = bodies  # type: list[DetectImageBodiesResponseBodyBodies]

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageBodiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = DetectImageBodiesResponseBodyBodies()
                self.bodies.append(temp_model.from_map(k))
        return self


class DetectImageBodiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageBodiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageBodiesResponse, self).to_map()
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
            temp_model = DetectImageBodiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageFacesRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributesHeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageFacesResponseBodyFacesFaceAttributesHeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(self, glasses_confidence=None, glasses=None, mask=None, beard_confidence=None,
                 mask_confidence=None, beard=None, face_boundary=None, head_pose=None):
        self.glasses_confidence = glasses_confidence  # type: float
        self.glasses = glasses  # type: str
        self.mask = mask  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.mask_confidence = mask_confidence  # type: float
        self.beard = beard  # type: str
        self.face_boundary = face_boundary  # type: DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary
        self.head_pose = head_pose  # type: DetectImageFacesResponseBodyFacesFaceAttributesHeadPose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponseBodyFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class DetectImageFacesResponseBodyFacesEmotionDetails(TeaModel):
    def __init__(self, happy=None, calm=None, surprised=None, disgusted=None, angry=None, sad=None, scared=None):
        self.happy = happy  # type: float
        self.calm = calm  # type: float
        self.surprised = surprised  # type: float
        self.disgusted = disgusted  # type: float
        self.angry = angry  # type: float
        self.sad = sad  # type: float
        self.scared = scared  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageFacesResponseBodyFacesEmotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class DetectImageFacesResponseBodyFaces(TeaModel):
    def __init__(self, emotion_confidence=None, attractive=None, attractive_confidence=None, gender=None,
                 age_confidence=None, gender_confidence=None, face_id=None, face_quality=None, emotion=None, age=None,
                 face_confidence=None, face_attributes=None, emotion_details=None):
        self.emotion_confidence = emotion_confidence  # type: float
        self.attractive = attractive  # type: float
        self.attractive_confidence = attractive_confidence  # type: float
        self.gender = gender  # type: str
        self.age_confidence = age_confidence  # type: float
        self.gender_confidence = gender_confidence  # type: float
        self.face_id = face_id  # type: str
        self.face_quality = face_quality  # type: float
        self.emotion = emotion  # type: str
        self.age = age  # type: int
        self.face_confidence = face_confidence  # type: float
        self.face_attributes = face_attributes  # type: DetectImageFacesResponseBodyFacesFaceAttributes
        self.emotion_details = emotion_details  # type: DetectImageFacesResponseBodyFacesEmotionDetails

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.emotion_details:
            self.emotion_details.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponseBodyFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.attractive_confidence is not None:
            result['AttractiveConfidence'] = self.attractive_confidence
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.age_confidence is not None:
            result['AgeConfidence'] = self.age_confidence
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('AttractiveConfidence') is not None:
            self.attractive_confidence = m.get('AttractiveConfidence')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('AgeConfidence') is not None:
            self.age_confidence = m.get('AgeConfidence')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('FaceAttributes') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('EmotionDetails') is not None:
            temp_model = DetectImageFacesResponseBodyFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        return self


class DetectImageFacesResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, faces=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.faces = faces  # type: list[DetectImageFacesResponseBodyFaces]

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = DetectImageFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class DetectImageFacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageFacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponse, self).to_map()
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
            temp_model = DetectImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLogosRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageLogosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageLogosResponseBodyLogosLogoBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageLogosResponseBodyLogosLogoBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageLogosResponseBodyLogos(TeaModel):
    def __init__(self, logo_confidence=None, logo_name=None, logo_boundary=None):
        self.logo_confidence = logo_confidence  # type: float
        self.logo_name = logo_name  # type: str
        self.logo_boundary = logo_boundary  # type: DetectImageLogosResponseBodyLogosLogoBoundary

    def validate(self):
        if self.logo_boundary:
            self.logo_boundary.validate()

    def to_map(self):
        _map = super(DetectImageLogosResponseBodyLogos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_confidence is not None:
            result['LogoConfidence'] = self.logo_confidence
        if self.logo_name is not None:
            result['LogoName'] = self.logo_name
        if self.logo_boundary is not None:
            result['LogoBoundary'] = self.logo_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogoConfidence') is not None:
            self.logo_confidence = m.get('LogoConfidence')
        if m.get('LogoName') is not None:
            self.logo_name = m.get('LogoName')
        if m.get('LogoBoundary') is not None:
            temp_model = DetectImageLogosResponseBodyLogosLogoBoundary()
            self.logo_boundary = temp_model.from_map(m['LogoBoundary'])
        return self


class DetectImageLogosResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, logos=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.logos = logos  # type: list[DetectImageLogosResponseBodyLogos]

    def validate(self):
        if self.logos:
            for k in self.logos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageLogosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Logos'] = []
        if self.logos is not None:
            for k in self.logos:
                result['Logos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.logos = []
        if m.get('Logos') is not None:
            for k in m.get('Logos'):
                temp_model = DetectImageLogosResponseBodyLogos()
                self.logos.append(temp_model.from_map(k))
        return self


class DetectImageLogosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageLogosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageLogosResponse, self).to_map()
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
            temp_model = DetectImageLogosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageQRCodesRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageQRCodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageQRCodesResponseBodyQRCodes(TeaModel):
    def __init__(self, content=None, qrcode_boundary=None):
        self.content = content  # type: str
        self.qrcode_boundary = qrcode_boundary  # type: DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary

    def validate(self):
        if self.qrcode_boundary:
            self.qrcode_boundary.validate()

    def to_map(self):
        _map = super(DetectImageQRCodesResponseBodyQRCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.qrcode_boundary is not None:
            result['QRCodeBoundary'] = self.qrcode_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('QRCodeBoundary') is not None:
            temp_model = DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary()
            self.qrcode_boundary = temp_model.from_map(m['QRCodeBoundary'])
        return self


class DetectImageQRCodesResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, qrcodes=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.qrcodes = qrcodes  # type: list[DetectImageQRCodesResponseBodyQRCodes]

    def validate(self):
        if self.qrcodes:
            for k in self.qrcodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageQRCodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['QRCodes'] = []
        if self.qrcodes is not None:
            for k in self.qrcodes:
                result['QRCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.qrcodes = []
        if m.get('QRCodes') is not None:
            for k in m.get('QRCodes'):
                temp_model = DetectImageQRCodesResponseBodyQRCodes()
                self.qrcodes.append(temp_model.from_map(k))
        return self


class DetectImageQRCodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageQRCodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageQRCodesResponse, self).to_map()
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
            temp_model = DetectImageQRCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageTagsRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageTagsResponseBodyTags(TeaModel):
    def __init__(self, parent_tag_en_name=None, tag_name=None, tag_confidence=None, tag_en_name=None,
                 tag_level=None, parent_tag_name=None):
        self.parent_tag_en_name = parent_tag_en_name  # type: str
        self.tag_name = tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_en_name = tag_en_name  # type: str
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_tag_en_name is not None:
            result['ParentTagEnName'] = self.parent_tag_en_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_en_name is not None:
            result['TagEnName'] = self.tag_en_name
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentTagEnName') is not None:
            self.parent_tag_en_name = m.get('ParentTagEnName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagEnName') is not None:
            self.tag_en_name = m.get('TagEnName')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class DetectImageTagsResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, tags=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[DetectImageTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DetectImageTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DetectImageTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectImageTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageTagsResponse, self).to_map()
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
            temp_model = DetectImageTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectQRCodesRequest(TeaModel):
    def __init__(self, project=None, src_uris=None):
        self.project = project  # type: str
        self.src_uris = src_uris  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectQRCodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uris is not None:
            result['SrcUris'] = self.src_uris
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUris') is not None:
            self.src_uris = m.get('SrcUris')
        return self


class DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: str
        self.top = top  # type: str
        self.width = width  # type: str
        self.height = height  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectQRCodesResponseBodySuccessDetailsQRCodes(TeaModel):
    def __init__(self, content=None, qrcodes_rectangle=None):
        self.content = content  # type: str
        self.qrcodes_rectangle = qrcodes_rectangle  # type: DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle

    def validate(self):
        if self.qrcodes_rectangle:
            self.qrcodes_rectangle.validate()

    def to_map(self):
        _map = super(DetectQRCodesResponseBodySuccessDetailsQRCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.qrcodes_rectangle is not None:
            result['QRCodesRectangle'] = self.qrcodes_rectangle.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('QRCodesRectangle') is not None:
            temp_model = DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle()
            self.qrcodes_rectangle = temp_model.from_map(m['QRCodesRectangle'])
        return self


class DetectQRCodesResponseBodySuccessDetails(TeaModel):
    def __init__(self, src_uri=None, qrcodes=None):
        self.src_uri = src_uri  # type: str
        self.qrcodes = qrcodes  # type: list[DetectQRCodesResponseBodySuccessDetailsQRCodes]

    def validate(self):
        if self.qrcodes:
            for k in self.qrcodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectQRCodesResponseBodySuccessDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        result['QRCodes'] = []
        if self.qrcodes is not None:
            for k in self.qrcodes:
                result['QRCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        self.qrcodes = []
        if m.get('QRCodes') is not None:
            for k in m.get('QRCodes'):
                temp_model = DetectQRCodesResponseBodySuccessDetailsQRCodes()
                self.qrcodes.append(temp_model.from_map(k))
        return self


class DetectQRCodesResponseBodyFailDetails(TeaModel):
    def __init__(self, error_message=None, src_uri=None, error_code=None):
        self.error_message = error_message  # type: str
        self.src_uri = src_uri  # type: str
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectQRCodesResponseBodyFailDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DetectQRCodesResponseBody(TeaModel):
    def __init__(self, request_id=None, success_details=None, fail_details=None):
        self.request_id = request_id  # type: str
        self.success_details = success_details  # type: list[DetectQRCodesResponseBodySuccessDetails]
        self.fail_details = fail_details  # type: list[DetectQRCodesResponseBodyFailDetails]

    def validate(self):
        if self.success_details:
            for k in self.success_details:
                if k:
                    k.validate()
        if self.fail_details:
            for k in self.fail_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectQRCodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessDetails'] = []
        if self.success_details is not None:
            for k in self.success_details:
                result['SuccessDetails'].append(k.to_map() if k else None)
        result['FailDetails'] = []
        if self.fail_details is not None:
            for k in self.fail_details:
                result['FailDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_details = []
        if m.get('SuccessDetails') is not None:
            for k in m.get('SuccessDetails'):
                temp_model = DetectQRCodesResponseBodySuccessDetails()
                self.success_details.append(temp_model.from_map(k))
        self.fail_details = []
        if m.get('FailDetails') is not None:
            for k in m.get('FailDetails'):
                temp_model = DetectQRCodesResponseBodyFailDetails()
                self.fail_details.append(temp_model.from_map(k))
        return self


class DetectQRCodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectQRCodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectQRCodesResponse, self).to_map()
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
            temp_model = DetectQRCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncodeBlindWatermarkRequest(TeaModel):
    def __init__(self, project=None, image_uri=None, watermark_uri=None, target_uri=None, image_quality=None,
                 content=None, target_image_type=None, model=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str
        self.watermark_uri = watermark_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.image_quality = image_quality  # type: str
        self.content = content  # type: str
        self.target_image_type = target_image_type  # type: str
        self.model = model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncodeBlindWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.watermark_uri is not None:
            result['WatermarkUri'] = self.watermark_uri
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.content is not None:
            result['Content'] = self.content
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('WatermarkUri') is not None:
            self.watermark_uri = m.get('WatermarkUri')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class EncodeBlindWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, target_uri=None, content=None):
        self.request_id = request_id  # type: str
        self.target_uri = target_uri  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncodeBlindWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class EncodeBlindWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EncodeBlindWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EncodeBlindWatermarkResponse, self).to_map()
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
            temp_model = EncodeBlindWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindImagesRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_size_range=None, image_time_range=None,
                 create_time_range=None, modify_time_range=None, source_type=None, source_uri_prefix=None, remarks_aprefix=None,
                 remarks_bprefix=None, tag_names=None, ocrcontents_match=None, age_range=None, gender=None, emotion=None,
                 order_by=None, order=None, marker=None, location_boundary=None, remarks_cprefix=None, remarks_dprefix=None,
                 external_id=None, group_id=None, limit=None, faces_modify_time_range=None, tags_modify_time_range=None,
                 address_line_contents_match=None, remarks_array_ain=None, remarks_array_bin=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_size_range = image_size_range  # type: str
        self.image_time_range = image_time_range  # type: str
        self.create_time_range = create_time_range  # type: str
        self.modify_time_range = modify_time_range  # type: str
        self.source_type = source_type  # type: str
        self.source_uri_prefix = source_uri_prefix  # type: str
        self.remarks_aprefix = remarks_aprefix  # type: str
        self.remarks_bprefix = remarks_bprefix  # type: str
        self.tag_names = tag_names  # type: str
        self.ocrcontents_match = ocrcontents_match  # type: str
        self.age_range = age_range  # type: str
        self.gender = gender  # type: str
        self.emotion = emotion  # type: str
        self.order_by = order_by  # type: str
        self.order = order  # type: str
        self.marker = marker  # type: str
        self.location_boundary = location_boundary  # type: str
        self.remarks_cprefix = remarks_cprefix  # type: str
        self.remarks_dprefix = remarks_dprefix  # type: str
        self.external_id = external_id  # type: str
        self.group_id = group_id  # type: str
        self.limit = limit  # type: int
        self.faces_modify_time_range = faces_modify_time_range  # type: str
        self.tags_modify_time_range = tags_modify_time_range  # type: str
        self.address_line_contents_match = address_line_contents_match  # type: str
        self.remarks_array_ain = remarks_array_ain  # type: str
        self.remarks_array_bin = remarks_array_bin  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_size_range is not None:
            result['ImageSizeRange'] = self.image_size_range
        if self.image_time_range is not None:
            result['ImageTimeRange'] = self.image_time_range
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range
        if self.modify_time_range is not None:
            result['ModifyTimeRange'] = self.modify_time_range
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri_prefix is not None:
            result['SourceUriPrefix'] = self.source_uri_prefix
        if self.remarks_aprefix is not None:
            result['RemarksAPrefix'] = self.remarks_aprefix
        if self.remarks_bprefix is not None:
            result['RemarksBPrefix'] = self.remarks_bprefix
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.ocrcontents_match is not None:
            result['OCRContentsMatch'] = self.ocrcontents_match
        if self.age_range is not None:
            result['AgeRange'] = self.age_range
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order is not None:
            result['Order'] = self.order
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.location_boundary is not None:
            result['LocationBoundary'] = self.location_boundary
        if self.remarks_cprefix is not None:
            result['RemarksCPrefix'] = self.remarks_cprefix
        if self.remarks_dprefix is not None:
            result['RemarksDPrefix'] = self.remarks_dprefix
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.faces_modify_time_range is not None:
            result['FacesModifyTimeRange'] = self.faces_modify_time_range
        if self.tags_modify_time_range is not None:
            result['TagsModifyTimeRange'] = self.tags_modify_time_range
        if self.address_line_contents_match is not None:
            result['AddressLineContentsMatch'] = self.address_line_contents_match
        if self.remarks_array_ain is not None:
            result['RemarksArrayAIn'] = self.remarks_array_ain
        if self.remarks_array_bin is not None:
            result['RemarksArrayBIn'] = self.remarks_array_bin
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageSizeRange') is not None:
            self.image_size_range = m.get('ImageSizeRange')
        if m.get('ImageTimeRange') is not None:
            self.image_time_range = m.get('ImageTimeRange')
        if m.get('CreateTimeRange') is not None:
            self.create_time_range = m.get('CreateTimeRange')
        if m.get('ModifyTimeRange') is not None:
            self.modify_time_range = m.get('ModifyTimeRange')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUriPrefix') is not None:
            self.source_uri_prefix = m.get('SourceUriPrefix')
        if m.get('RemarksAPrefix') is not None:
            self.remarks_aprefix = m.get('RemarksAPrefix')
        if m.get('RemarksBPrefix') is not None:
            self.remarks_bprefix = m.get('RemarksBPrefix')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('OCRContentsMatch') is not None:
            self.ocrcontents_match = m.get('OCRContentsMatch')
        if m.get('AgeRange') is not None:
            self.age_range = m.get('AgeRange')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('LocationBoundary') is not None:
            self.location_boundary = m.get('LocationBoundary')
        if m.get('RemarksCPrefix') is not None:
            self.remarks_cprefix = m.get('RemarksCPrefix')
        if m.get('RemarksDPrefix') is not None:
            self.remarks_dprefix = m.get('RemarksDPrefix')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('FacesModifyTimeRange') is not None:
            self.faces_modify_time_range = m.get('FacesModifyTimeRange')
        if m.get('TagsModifyTimeRange') is not None:
            self.tags_modify_time_range = m.get('TagsModifyTimeRange')
        if m.get('AddressLineContentsMatch') is not None:
            self.address_line_contents_match = m.get('AddressLineContentsMatch')
        if m.get('RemarksArrayAIn') is not None:
            self.remarks_array_ain = m.get('RemarksArrayAIn')
        if m.get('RemarksArrayBIn') is not None:
            self.remarks_array_bin = m.get('RemarksArrayBIn')
        return self


class FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesCroppingSuggestion(TeaModel):
    def __init__(self, score=None, aspect_ratio=None, cropping_boundary=None):
        self.score = score  # type: float
        self.aspect_ratio = aspect_ratio  # type: str
        self.cropping_boundary = cropping_boundary  # type: FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesCroppingSuggestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class FindImagesResponseBodyImagesFacesEmotionDetails(TeaModel):
    def __init__(self, happy=None, surprised=None, calm=None, disgusted=None, angry=None, sad=None, scared=None):
        self.happy = happy  # type: float
        self.surprised = surprised  # type: float
        self.calm = calm  # type: float
        self.disgusted = disgusted  # type: float
        self.angry = angry  # type: float
        self.sad = sad  # type: float
        self.scared = scared  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesFacesEmotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesFacesFaceAttributesHeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributes(TeaModel):
    def __init__(self, glasses_confidence=None, glasses=None, mask=None, beard_confidence=None,
                 mask_confidence=None, beard=None, face_boundary=None, head_pose=None):
        self.glasses_confidence = glasses_confidence  # type: float
        self.glasses = glasses  # type: str
        self.mask = mask  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.mask_confidence = mask_confidence  # type: float
        self.beard = beard  # type: str
        self.face_boundary = face_boundary  # type: FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary
        self.head_pose = head_pose  # type: FindImagesResponseBodyImagesFacesFaceAttributesHeadPose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class FindImagesResponseBodyImagesFaces(TeaModel):
    def __init__(self, emotion_confidence=None, attractive=None, group_id=None, gender=None, face_id=None,
                 gender_confidence=None, face_quality=None, emotion=None, age=None, face_confidence=None, emotion_details=None,
                 face_attributes=None):
        self.emotion_confidence = emotion_confidence  # type: float
        self.attractive = attractive  # type: float
        self.group_id = group_id  # type: str
        self.gender = gender  # type: str
        self.face_id = face_id  # type: str
        self.gender_confidence = gender_confidence  # type: float
        self.face_quality = face_quality  # type: float
        self.emotion = emotion  # type: str
        self.age = age  # type: int
        self.face_confidence = face_confidence  # type: float
        self.emotion_details = emotion_details  # type: FindImagesResponseBodyImagesFacesEmotionDetails
        self.face_attributes = face_attributes  # type: FindImagesResponseBodyImagesFacesFaceAttributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = FindImagesResponseBodyImagesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindImagesResponseBodyImagesTags(TeaModel):
    def __init__(self, tag_level=None, parent_tag_name=None, tag_confidence=None, tag_name=None):
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class FindImagesResponseBodyImagesOCROCRBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesOCROCRBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesOCR(TeaModel):
    def __init__(self, ocrconfidence=None, ocrcontents=None, ocrboundary=None):
        self.ocrconfidence = ocrconfidence  # type: float
        self.ocrcontents = ocrcontents  # type: str
        self.ocrboundary = ocrboundary  # type: FindImagesResponseBodyImagesOCROCRBoundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesOCR, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class FindImagesResponseBodyImagesImageQuality(TeaModel):
    def __init__(self, overall_score=None, color=None, color_score=None, contrast_score=None, contrast=None,
                 exposure_score=None, clarity_score=None, clarity=None, exposure=None, composition_score=None):
        self.overall_score = overall_score  # type: float
        self.color = color  # type: float
        self.color_score = color_score  # type: float
        self.contrast_score = contrast_score  # type: float
        self.contrast = contrast  # type: float
        self.exposure_score = exposure_score  # type: float
        self.clarity_score = clarity_score  # type: float
        self.clarity = clarity  # type: float
        self.exposure = exposure  # type: float
        self.composition_score = composition_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesImageQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class FindImagesResponseBodyImagesAddress(TeaModel):
    def __init__(self, township=None, district=None, address_line=None, country=None, city=None, province=None):
        self.township = township  # type: str
        self.district = district  # type: str
        self.address_line = address_line  # type: str
        self.country = country  # type: str
        self.city = city  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindImagesResponseBodyImagesAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class FindImagesResponseBodyImages(TeaModel):
    def __init__(self, cropping_suggestion_status=None, image_quality_modify_time=None, tags_fail_reason=None,
                 remarks_c=None, create_time=None, source_type=None, faces_fail_reason=None, faces_modify_time=None,
                 image_time=None, ocrmodify_time=None, address_modify_time=None, image_quality_fail_reason=None,
                 faces_status=None, remarks_array_a=None, image_height=None, external_id=None, source_uri=None, file_size=None,
                 modify_time=None, source_position=None, image_quality_status=None, ocrfail_reason=None,
                 address_fail_reason=None, cropping_suggestion_modify_time=None, image_format=None, image_width=None,
                 remarks_array_b=None, orientation=None, remarks_d=None, tags_status=None, cropping_suggestion_fail_reason=None,
                 remarks_a=None, image_uri=None, tags_modify_time=None, ocrstatus=None, address_status=None, exif=None,
                 location=None, remarks_b=None, cropping_suggestion=None, faces=None, tags=None, ocr=None, image_quality=None,
                 address=None):
        self.cropping_suggestion_status = cropping_suggestion_status  # type: str
        self.image_quality_modify_time = image_quality_modify_time  # type: str
        self.tags_fail_reason = tags_fail_reason  # type: str
        self.remarks_c = remarks_c  # type: str
        self.create_time = create_time  # type: str
        self.source_type = source_type  # type: str
        self.faces_fail_reason = faces_fail_reason  # type: str
        self.faces_modify_time = faces_modify_time  # type: str
        self.image_time = image_time  # type: str
        self.ocrmodify_time = ocrmodify_time  # type: str
        self.address_modify_time = address_modify_time  # type: str
        self.image_quality_fail_reason = image_quality_fail_reason  # type: str
        self.faces_status = faces_status  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.image_height = image_height  # type: int
        self.external_id = external_id  # type: str
        self.source_uri = source_uri  # type: str
        self.file_size = file_size  # type: int
        self.modify_time = modify_time  # type: str
        self.source_position = source_position  # type: str
        self.image_quality_status = image_quality_status  # type: str
        self.ocrfail_reason = ocrfail_reason  # type: str
        self.address_fail_reason = address_fail_reason  # type: str
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time  # type: str
        self.image_format = image_format  # type: str
        self.image_width = image_width  # type: int
        self.remarks_array_b = remarks_array_b  # type: str
        self.orientation = orientation  # type: str
        self.remarks_d = remarks_d  # type: str
        self.tags_status = tags_status  # type: str
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason  # type: str
        self.remarks_a = remarks_a  # type: str
        self.image_uri = image_uri  # type: str
        self.tags_modify_time = tags_modify_time  # type: str
        self.ocrstatus = ocrstatus  # type: str
        self.address_status = address_status  # type: str
        self.exif = exif  # type: str
        self.location = location  # type: str
        self.remarks_b = remarks_b  # type: str
        self.cropping_suggestion = cropping_suggestion  # type: list[FindImagesResponseBodyImagesCroppingSuggestion]
        self.faces = faces  # type: list[FindImagesResponseBodyImagesFaces]
        self.tags = tags  # type: list[FindImagesResponseBodyImagesTags]
        self.ocr = ocr  # type: list[FindImagesResponseBodyImagesOCR]
        self.image_quality = image_quality  # type: FindImagesResponseBodyImagesImageQuality
        self.address = address  # type: FindImagesResponseBodyImagesAddress

    def validate(self):
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super(FindImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = FindImagesResponseBodyImagesCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = FindImagesResponseBodyImagesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = FindImagesResponseBodyImagesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = FindImagesResponseBodyImagesOCR()
                self.ocr.append(temp_model.from_map(k))
        if m.get('ImageQuality') is not None:
            temp_model = FindImagesResponseBodyImagesImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('Address') is not None:
            temp_model = FindImagesResponseBodyImagesAddress()
            self.address = temp_model.from_map(m['Address'])
        return self


class FindImagesResponseBody(TeaModel):
    def __init__(self, request_id=None, next_marker=None, set_id=None, images=None):
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.set_id = set_id  # type: str
        self.images = images  # type: list[FindImagesResponseBodyImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FindImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = FindImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class FindImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FindImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FindImagesResponse, self).to_map()
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
            temp_model = FindImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindSimilarFacesRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None, face_id=None, limit=None, min_similarity=None,
                 response_format=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str
        self.face_id = face_id  # type: str
        self.limit = limit  # type: int
        self.min_similarity = min_similarity  # type: float
        self.response_format = response_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindSimilarFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.min_similarity is not None:
            result['MinSimilarity'] = self.min_similarity
        if self.response_format is not None:
            result['ResponseFormat'] = self.response_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MinSimilarity') is not None:
            self.min_similarity = m.get('MinSimilarity')
        if m.get('ResponseFormat') is not None:
            self.response_format = m.get('ResponseFormat')
        return self


class FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes(TeaModel):
    def __init__(self, face_boundary=None):
        self.face_boundary = face_boundary  # type: FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class FindSimilarFacesResponseBodyFacesSimilarFaces(TeaModel):
    def __init__(self, external_id=None, similarity=None, face_id=None, image_uri=None, face_attributes=None):
        self.external_id = external_id  # type: str
        self.similarity = similarity  # type: float
        self.face_id = face_id  # type: str
        self.image_uri = image_uri  # type: str
        self.face_attributes = face_attributes  # type: FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFacesSimilarFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceAttributes') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindSimilarFacesResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(self, face_boundary=None):
        self.face_boundary = face_boundary  # type: FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class FindSimilarFacesResponseBodyFaces(TeaModel):
    def __init__(self, external_id=None, similarity=None, face_id=None, image_uri=None, similar_faces=None,
                 face_attributes=None):
        self.external_id = external_id  # type: str
        self.similarity = similarity  # type: float
        self.face_id = face_id  # type: str
        self.image_uri = image_uri  # type: str
        self.similar_faces = similar_faces  # type: list[FindSimilarFacesResponseBodyFacesSimilarFaces]
        self.face_attributes = face_attributes  # type: FindSimilarFacesResponseBodyFacesFaceAttributes

    def validate(self):
        if self.similar_faces:
            for k in self.similar_faces:
                if k:
                    k.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponseBodyFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['SimilarFaces'] = []
        if self.similar_faces is not None:
            for k in self.similar_faces:
                result['SimilarFaces'].append(k.to_map() if k else None)
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.similar_faces = []
        if m.get('SimilarFaces') is not None:
            for k in m.get('SimilarFaces'):
                temp_model = FindSimilarFacesResponseBodyFacesSimilarFaces()
                self.similar_faces.append(temp_model.from_map(k))
        if m.get('FaceAttributes') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindSimilarFacesResponseBody(TeaModel):
    def __init__(self, request_id=None, faces=None):
        self.request_id = request_id  # type: str
        self.faces = faces  # type: list[FindSimilarFacesResponseBodyFaces]

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = FindSimilarFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class FindSimilarFacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FindSimilarFacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FindSimilarFacesResponse, self).to_map()
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
            temp_model = FindSimilarFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContentKeyRequest(TeaModel):
    def __init__(self, project=None, version_id=None, drmserver_id=None, key_ids=None):
        self.project = project  # type: str
        self.version_id = version_id  # type: str
        self.drmserver_id = drmserver_id  # type: str
        self.key_ids = key_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.drmserver_id is not None:
            result['DRMServerId'] = self.drmserver_id
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DRMServerId') is not None:
            self.drmserver_id = m.get('DRMServerId')
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')
        return self


class GetContentKeyResponseBody(TeaModel):
    def __init__(self, version_id=None, request_id=None, key_infos=None):
        self.version_id = version_id  # type: str
        self.request_id = request_id  # type: str
        self.key_infos = key_infos  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetContentKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_infos is not None:
            result['KeyInfos'] = self.key_infos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyInfos') is not None:
            self.key_infos = m.get('KeyInfos')
        return self


class GetContentKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetContentKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetContentKeyResponse, self).to_map()
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
            temp_model = GetContentKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDRMLicenseRequest(TeaModel):
    def __init__(self, project=None, drmtype=None, drmlicense=None):
        self.project = project  # type: str
        self.drmtype = drmtype  # type: str
        self.drmlicense = drmlicense  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDRMLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.drmtype is not None:
            result['DRMType'] = self.drmtype
        if self.drmlicense is not None:
            result['DRMLicense'] = self.drmlicense
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('DRMType') is not None:
            self.drmtype = m.get('DRMType')
        if m.get('DRMLicense') is not None:
            self.drmlicense = m.get('DRMLicense')
        return self


class GetDRMLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, device_info=None, drmdata=None):
        self.request_id = request_id  # type: str
        self.device_info = device_info  # type: str
        self.drmdata = drmdata  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDRMLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.drmdata is not None:
            result['DRMData'] = self.drmdata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('DRMData') is not None:
            self.drmdata = m.get('DRMData')
        return self


class GetDRMLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDRMLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDRMLicenseResponse, self).to_map()
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
            temp_model = GetDRMLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class GetImageResponseBodyImageQuality(TeaModel):
    def __init__(self, overall_score=None, color=None, color_score=None, contrast_score=None, contrast=None,
                 exposure_score=None, clarity_score=None, clarity=None, exposure=None, composition_score=None):
        self.overall_score = overall_score  # type: float
        self.color = color  # type: float
        self.color_score = color_score  # type: float
        self.contrast_score = contrast_score  # type: float
        self.contrast = contrast  # type: float
        self.exposure_score = exposure_score  # type: float
        self.clarity_score = clarity_score  # type: float
        self.clarity = clarity  # type: float
        self.exposure = exposure  # type: float
        self.composition_score = composition_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyImageQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class GetImageResponseBodyAddress(TeaModel):
    def __init__(self, township=None, district=None, address_line=None, country=None, city=None, province=None):
        self.township = township  # type: str
        self.district = district  # type: str
        self.address_line = address_line  # type: str
        self.country = country  # type: str
        self.city = city  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetImageResponseBodyTags(TeaModel):
    def __init__(self, tag_name=None, tag_confidence=None, tag_level=None, parent_tag_name=None):
        self.tag_name = tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class GetImageResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, top=None, width=None, height=None, left=None):
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int
        self.left = left  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyFacesFaceAttributesHeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyFacesFaceAttributesHeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class GetImageResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(self, glasses_confidence=None, glasses=None, mask=None, beard_confidence=None,
                 mask_confidence=None, face_boundary=None, head_pose=None, beard=None):
        self.glasses_confidence = glasses_confidence  # type: float
        self.glasses = glasses  # type: str
        self.mask = mask  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.mask_confidence = mask_confidence  # type: float
        self.face_boundary = face_boundary  # type: GetImageResponseBodyFacesFaceAttributesFaceBoundary
        self.head_pose = head_pose  # type: GetImageResponseBodyFacesFaceAttributesHeadPose
        self.beard = beard  # type: str

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.beard is not None:
            result['Beard'] = self.beard
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('FaceBoundary') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        return self


class GetImageResponseBodyFacesEmotionDetails(TeaModel):
    def __init__(self, happy=None, calm=None, surprised=None, disgusted=None, angry=None, sad=None, scared=None):
        self.happy = happy  # type: float
        self.calm = calm  # type: float
        self.surprised = surprised  # type: float
        self.disgusted = disgusted  # type: float
        self.angry = angry  # type: float
        self.sad = sad  # type: float
        self.scared = scared  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyFacesEmotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class GetImageResponseBodyFaces(TeaModel):
    def __init__(self, gender=None, gender_confidence=None, face_id=None, face_attributes=None, face_quality=None,
                 emotion=None, age=None, face_confidence=None, emotion_confidence=None, attractive=None, group_id=None,
                 emotion_details=None):
        self.gender = gender  # type: str
        self.gender_confidence = gender_confidence  # type: float
        self.face_id = face_id  # type: str
        self.face_attributes = face_attributes  # type: GetImageResponseBodyFacesFaceAttributes
        self.face_quality = face_quality  # type: float
        self.emotion = emotion  # type: str
        self.age = age  # type: str
        self.face_confidence = face_confidence  # type: float
        self.emotion_confidence = emotion_confidence  # type: float
        self.attractive = attractive  # type: float
        self.group_id = group_id  # type: str
        self.emotion_details = emotion_details  # type: GetImageResponseBodyFacesEmotionDetails

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.emotion_details:
            self.emotion_details.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('EmotionDetails') is not None:
            temp_model = GetImageResponseBodyFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        return self


class GetImageResponseBodyCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(self, top=None, width=None, height=None, left=None):
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int
        self.left = left  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyCroppingSuggestionCroppingBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyCroppingSuggestion(TeaModel):
    def __init__(self, score=None, cropping_boundary=None, aspect_ratio=None):
        self.score = score  # type: float
        self.cropping_boundary = cropping_boundary  # type: GetImageResponseBodyCroppingSuggestionCroppingBoundary
        self.aspect_ratio = aspect_ratio  # type: str

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyCroppingSuggestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('CroppingBoundary') is not None:
            temp_model = GetImageResponseBodyCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        return self


class GetImageResponseBodyOCROCRBoundary(TeaModel):
    def __init__(self, top=None, width=None, height=None, left=None):
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int
        self.left = left  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyOCROCRBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyOCR(TeaModel):
    def __init__(self, ocrconfidence=None, ocrcontents=None, ocrboundary=None):
        self.ocrconfidence = ocrconfidence  # type: float
        self.ocrcontents = ocrcontents  # type: str
        self.ocrboundary = ocrboundary  # type: GetImageResponseBodyOCROCRBoundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super(GetImageResponseBodyOCR, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = GetImageResponseBodyOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class GetImageResponseBody(TeaModel):
    def __init__(self, image_quality=None, modify_time=None, address=None, source_type=None, source_uri=None,
                 faces_fail_reason=None, cropping_suggestion_status=None, cropping_suggestion_fail_reason=None,
                 address_fail_reason=None, remarks_a=None, address_modify_time=None, remarks_b=None, image_format=None,
                 tags_fail_reason=None, remarks_array_b=None, faces_modify_time=None, exif=None, remarks_c=None, remarks_d=None,
                 image_width=None, remarks_array_a=None, source_position=None, tags=None, faces=None, address_status=None,
                 faces_status=None, image_quality_modify_time=None, cropping_suggestion=None, request_id=None, create_time=None,
                 external_id=None, tags_modify_time=None, image_quality_fail_reason=None, orientation=None, image_uri=None,
                 ocrstatus=None, ocrmodify_time=None, image_time=None, cropping_suggestion_modify_time=None,
                 image_height=None, image_quality_status=None, tags_status=None, ocrfail_reason=None, set_id=None,
                 file_size=None, location=None, ocr=None):
        self.image_quality = image_quality  # type: GetImageResponseBodyImageQuality
        self.modify_time = modify_time  # type: str
        self.address = address  # type: GetImageResponseBodyAddress
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.faces_fail_reason = faces_fail_reason  # type: str
        self.cropping_suggestion_status = cropping_suggestion_status  # type: str
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason  # type: str
        self.address_fail_reason = address_fail_reason  # type: str
        self.remarks_a = remarks_a  # type: str
        self.address_modify_time = address_modify_time  # type: str
        self.remarks_b = remarks_b  # type: str
        self.image_format = image_format  # type: str
        self.tags_fail_reason = tags_fail_reason  # type: str
        self.remarks_array_b = remarks_array_b  # type: str
        self.faces_modify_time = faces_modify_time  # type: str
        self.exif = exif  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.image_width = image_width  # type: int
        self.remarks_array_a = remarks_array_a  # type: str
        self.source_position = source_position  # type: str
        self.tags = tags  # type: list[GetImageResponseBodyTags]
        self.faces = faces  # type: list[GetImageResponseBodyFaces]
        self.address_status = address_status  # type: str
        self.faces_status = faces_status  # type: str
        self.image_quality_modify_time = image_quality_modify_time  # type: str
        self.cropping_suggestion = cropping_suggestion  # type: list[GetImageResponseBodyCroppingSuggestion]
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.external_id = external_id  # type: str
        self.tags_modify_time = tags_modify_time  # type: str
        self.image_quality_fail_reason = image_quality_fail_reason  # type: str
        self.orientation = orientation  # type: str
        self.image_uri = image_uri  # type: str
        self.ocrstatus = ocrstatus  # type: str
        self.ocrmodify_time = ocrmodify_time  # type: str
        self.image_time = image_time  # type: str
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time  # type: str
        self.image_height = image_height  # type: int
        self.image_quality_status = image_quality_status  # type: str
        self.tags_status = tags_status  # type: str
        self.ocrfail_reason = ocrfail_reason  # type: str
        self.set_id = set_id  # type: str
        self.file_size = file_size  # type: int
        self.location = location  # type: str
        self.ocr = ocr  # type: list[GetImageResponseBodyOCR]

    def validate(self):
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.location is not None:
            result['Location'] = self.location
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageQuality') is not None:
            temp_model = GetImageResponseBodyImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Address') is not None:
            temp_model = GetImageResponseBodyAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetImageResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = GetImageResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = GetImageResponseBodyCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = GetImageResponseBodyOCR()
                self.ocr.append(temp_model.from_map(k))
        return self


class GetImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageResponse, self).to_map()
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageCroppingSuggestionsRequest(TeaModel):
    def __init__(self, project=None, image_uri=None, aspect_ratios=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str
        self.aspect_ratios = aspect_ratios  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageCroppingSuggestionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        return self


class GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetImageCroppingSuggestionsResponseBodyCroppingSuggestions(TeaModel):
    def __init__(self, score=None, aspect_ratio=None, cropping_boundary=None):
        self.score = score  # type: float
        self.aspect_ratio = aspect_ratio  # type: str
        self.cropping_boundary = cropping_boundary  # type: GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super(GetImageCroppingSuggestionsResponseBodyCroppingSuggestions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class GetImageCroppingSuggestionsResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, cropping_suggestions=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.cropping_suggestions = cropping_suggestions  # type: list[GetImageCroppingSuggestionsResponseBodyCroppingSuggestions]

    def validate(self):
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageCroppingSuggestionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = GetImageCroppingSuggestionsResponseBodyCroppingSuggestions()
                self.cropping_suggestions.append(temp_model.from_map(k))
        return self


class GetImageCroppingSuggestionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageCroppingSuggestionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageCroppingSuggestionsResponse, self).to_map()
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
            temp_model = GetImageCroppingSuggestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageQualityRequest(TeaModel):
    def __init__(self, project=None, image_uri=None):
        self.project = project  # type: str
        self.image_uri = image_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageQualityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class GetImageQualityResponseBodyImageQuality(TeaModel):
    def __init__(self, overall_score=None, color=None, color_score=None, contrast_score=None, contrast=None,
                 exposure_score=None, clarity_score=None, clarity=None, exposure=None, composition_score=None):
        self.overall_score = overall_score  # type: float
        self.color = color  # type: float
        self.color_score = color_score  # type: float
        self.contrast_score = contrast_score  # type: float
        self.contrast = contrast  # type: float
        self.exposure_score = exposure_score  # type: float
        self.clarity_score = clarity_score  # type: float
        self.clarity = clarity  # type: float
        self.exposure = exposure  # type: float
        self.composition_score = composition_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageQualityResponseBodyImageQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class GetImageQualityResponseBody(TeaModel):
    def __init__(self, image_uri=None, request_id=None, image_quality=None):
        self.image_uri = image_uri  # type: str
        self.request_id = request_id  # type: str
        self.image_quality = image_quality  # type: GetImageQualityResponseBodyImageQuality

    def validate(self):
        if self.image_quality:
            self.image_quality.validate()

    def to_map(self):
        _map = super(GetImageQualityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageQuality') is not None:
            temp_model = GetImageQualityResponseBodyImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        return self


class GetImageQualityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageQualityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageQualityResponse, self).to_map()
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
            temp_model = GetImageQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaMetaRequest(TeaModel):
    def __init__(self, project=None, media_uri=None):
        self.project = project  # type: str
        self.media_uri = media_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.media_uri is not None:
            result['MediaUri'] = self.media_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('MediaUri') is not None:
            self.media_uri = m.get('MediaUri')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormatTag(TeaModel):
    def __init__(self, creation_time=None, album=None, album_artist=None, performer=None, composer=None, artist=None,
                 title=None, language=None):
        self.creation_time = creation_time  # type: str
        self.album = album  # type: str
        self.album_artist = album_artist  # type: str
        self.performer = performer  # type: str
        self.composer = composer  # type: str
        self.artist = artist  # type: str
        self.title = title  # type: str
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaFormatTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.artist is not None:
            result['Artist'] = self.artist
        if self.title is not None:
            result['Title'] = self.title
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormatAddress(TeaModel):
    def __init__(self, township=None, district=None, address_line=None, country=None, city=None, province=None):
        self.township = township  # type: str
        self.district = district  # type: str
        self.address_line = address_line  # type: str
        self.country = country  # type: str
        self.city = city  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaFormatAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormat(TeaModel):
    def __init__(self, creation_time=None, number_programs=None, number_streams=None, tag=None, bitrate=None,
                 start_time=None, size=None, address=None, format_long_name=None, duration=None, format_name=None,
                 location=None):
        self.creation_time = creation_time  # type: str
        self.number_programs = number_programs  # type: int
        self.number_streams = number_streams  # type: int
        self.tag = tag  # type: GetMediaMetaResponseBodyMediaMetaMediaFormatTag
        self.bitrate = bitrate  # type: str
        self.start_time = start_time  # type: str
        self.size = size  # type: str
        self.address = address  # type: GetMediaMetaResponseBodyMediaMetaMediaFormatAddress
        self.format_long_name = format_long_name  # type: str
        self.duration = duration  # type: str
        self.format_name = format_name  # type: str
        self.location = location  # type: str

    def validate(self):
        if self.tag:
            self.tag.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaFormat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.number_programs is not None:
            result['NumberPrograms'] = self.number_programs
        if self.number_streams is not None:
            result['NumberStreams'] = self.number_streams
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.size is not None:
            result['Size'] = self.size
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('NumberPrograms') is not None:
            self.number_programs = m.get('NumberPrograms')
        if m.get('NumberStreams') is not None:
            self.number_streams = m.get('NumberStreams')
        if m.get('Tag') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormatTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Address') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormatAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams(TeaModel):
    def __init__(self, index=None, codec_long_name=None, height=None, sample_aspect_ratio=None,
                 average_frame_rate=None, bitrate=None, rotate=None, codec_tag_string=None, language=None, has_bframes=None,
                 frame_rrate=None, profile=None, start_time=None, frames=None, codec_name=None, width=None, duration=None,
                 display_aspect_ratio=None, codec_tag=None, codec_time_base=None, time_base=None, level=None, pixel_format=None):
        self.index = index  # type: int
        self.codec_long_name = codec_long_name  # type: str
        self.height = height  # type: int
        self.sample_aspect_ratio = sample_aspect_ratio  # type: str
        self.average_frame_rate = average_frame_rate  # type: str
        self.bitrate = bitrate  # type: str
        self.rotate = rotate  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.language = language  # type: str
        self.has_bframes = has_bframes  # type: int
        self.frame_rrate = frame_rrate  # type: str
        self.profile = profile  # type: str
        self.start_time = start_time  # type: str
        self.frames = frames  # type: str
        self.codec_name = codec_name  # type: str
        self.width = width  # type: int
        self.duration = duration  # type: str
        self.display_aspect_ratio = display_aspect_ratio  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.time_base = time_base  # type: str
        self.level = level  # type: int
        self.pixel_format = pixel_format  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.height is not None:
            result['Height'] = self.height
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.language is not None:
            result['Language'] = self.language
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.frame_rrate is not None:
            result['FrameRrate'] = self.frame_rrate
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.frames is not None:
            result['Frames'] = self.frames
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.width is not None:
            result['Width'] = self.width
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.level is not None:
            result['Level'] = self.level
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('FrameRrate') is not None:
            self.frame_rrate = m.get('FrameRrate')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Frames') is not None:
            self.frames = m.get('Frames')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams(TeaModel):
    def __init__(self, index=None, sample_rate=None, channel_layout=None, codec_long_name=None, channels=None,
                 bitrate=None, codec_tag_string=None, language=None, start_time=None, sample_format=None, frames=None,
                 codec_name=None, duration=None, codec_tag=None, codec_time_base=None, time_base=None):
        self.index = index  # type: int
        self.sample_rate = sample_rate  # type: str
        self.channel_layout = channel_layout  # type: str
        self.codec_long_name = codec_long_name  # type: str
        self.channels = channels  # type: int
        self.bitrate = bitrate  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.language = language  # type: str
        self.start_time = start_time  # type: str
        self.sample_format = sample_format  # type: str
        self.frames = frames  # type: str
        self.codec_name = codec_name  # type: str
        self.duration = duration  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.time_base = time_base  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.frames is not None:
            result['Frames'] = self.frames
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('Frames') is not None:
            self.frames = m.get('Frames')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams(TeaModel):
    def __init__(self, index=None, language=None):
        self.index = index  # type: int
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreams(TeaModel):
    def __init__(self, video_streams=None, audio_streams=None, subtitle_streams=None):
        self.video_streams = video_streams  # type: list[GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams]
        self.audio_streams = audio_streams  # type: list[GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams]
        self.subtitle_streams = subtitle_streams  # type: list[GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams]

    def validate(self):
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.subtitle_streams:
            for k in self.subtitle_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMetaMediaStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        result['SubtitleStreams'] = []
        if self.subtitle_streams is not None:
            for k in self.subtitle_streams:
                result['SubtitleStreams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams()
                self.video_streams.append(temp_model.from_map(k))
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams()
                self.audio_streams.append(temp_model.from_map(k))
        self.subtitle_streams = []
        if m.get('SubtitleStreams') is not None:
            for k in m.get('SubtitleStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams()
                self.subtitle_streams.append(temp_model.from_map(k))
        return self


class GetMediaMetaResponseBodyMediaMeta(TeaModel):
    def __init__(self, media_format=None, media_streams=None):
        self.media_format = media_format  # type: GetMediaMetaResponseBodyMediaMetaMediaFormat
        self.media_streams = media_streams  # type: GetMediaMetaResponseBodyMediaMetaMediaStreams

    def validate(self):
        if self.media_format:
            self.media_format.validate()
        if self.media_streams:
            self.media_streams.validate()

    def to_map(self):
        _map = super(GetMediaMetaResponseBodyMediaMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_format is not None:
            result['MediaFormat'] = self.media_format.to_map()
        if self.media_streams is not None:
            result['MediaStreams'] = self.media_streams.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaFormat') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormat()
            self.media_format = temp_model.from_map(m['MediaFormat'])
        if m.get('MediaStreams') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreams()
            self.media_streams = temp_model.from_map(m['MediaStreams'])
        return self


class GetMediaMetaResponseBody(TeaModel):
    def __init__(self, media_uri=None, request_id=None, media_meta=None):
        self.media_uri = media_uri  # type: str
        self.request_id = request_id  # type: str
        self.media_meta = media_meta  # type: GetMediaMetaResponseBodyMediaMeta

    def validate(self):
        if self.media_meta:
            self.media_meta.validate()

    def to_map(self):
        _map = super(GetMediaMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_uri is not None:
            result['MediaUri'] = self.media_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_meta is not None:
            result['MediaMeta'] = self.media_meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaUri') is not None:
            self.media_uri = m.get('MediaUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaMeta') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMeta()
            self.media_meta = temp_model.from_map(m['MediaMeta'])
        return self


class GetMediaMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaMetaResponse, self).to_map()
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
            temp_model = GetMediaMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeConversionTaskRequest(TeaModel):
    def __init__(self, project=None, task_id=None):
        self.project = project  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeConversionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOfficeConversionTaskResponseBodyFailDetail(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeConversionTaskResponseBodyFailDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetOfficeConversionTaskResponseBody(TeaModel):
    def __init__(self, status=None, percent=None, finish_time=None, create_time=None, page_count=None,
                 notify_topic_name=None, request_id=None, notify_endpoint=None, src_uri=None, tgt_type=None, tgt_uri=None,
                 image_spec=None, external_id=None, task_id=None, fail_detail=None):
        self.status = status  # type: str
        self.percent = percent  # type: int
        self.finish_time = finish_time  # type: str
        self.create_time = create_time  # type: str
        self.page_count = page_count  # type: int
        self.notify_topic_name = notify_topic_name  # type: str
        self.request_id = request_id  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.src_uri = src_uri  # type: str
        self.tgt_type = tgt_type  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.image_spec = image_spec  # type: str
        self.external_id = external_id  # type: str
        self.task_id = task_id  # type: str
        self.fail_detail = fail_detail  # type: GetOfficeConversionTaskResponseBodyFailDetail

    def validate(self):
        if self.fail_detail:
            self.fail_detail.validate()

    def to_map(self):
        _map = super(GetOfficeConversionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.image_spec is not None:
            result['ImageSpec'] = self.image_spec
        if self.external_id is not None:
            result['ExternalID'] = self.external_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.fail_detail is not None:
            result['FailDetail'] = self.fail_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('ImageSpec') is not None:
            self.image_spec = m.get('ImageSpec')
        if m.get('ExternalID') is not None:
            self.external_id = m.get('ExternalID')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('FailDetail') is not None:
            temp_model = GetOfficeConversionTaskResponseBodyFailDetail()
            self.fail_detail = temp_model.from_map(m['FailDetail'])
        return self


class GetOfficeConversionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOfficeConversionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOfficeConversionTaskResponse, self).to_map()
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
            temp_model = GetOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeEditURLRequest(TeaModel):
    def __init__(self, project=None, src_uri=None, src_type=None, file_id=None, tgt_uri=None, user_id=None,
                 user_name=None, notify_endpoint=None, notify_topic_name=None, file_name=None):
        self.project = project  # type: str
        self.src_uri = src_uri  # type: str
        self.src_type = src_type  # type: str
        self.file_id = file_id  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeEditURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.user_id is not None:
            result['UserID'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('UserID') is not None:
            self.user_id = m.get('UserID')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetOfficeEditURLResponseBody(TeaModel):
    def __init__(self, request_id=None, access_token_expired_time=None, edit_url=None, access_token=None,
                 refresh_token=None, refresh_token_expired_time=None):
        self.request_id = request_id  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.edit_url = edit_url  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token = refresh_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeEditURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.edit_url is not None:
            result['EditURL'] = self.edit_url
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('EditURL') is not None:
            self.edit_url = m.get('EditURL')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class GetOfficeEditURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOfficeEditURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOfficeEditURLResponse, self).to_map()
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
            temp_model = GetOfficeEditURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficePreviewURLRequest(TeaModel):
    def __init__(self, project=None, src_uri=None, src_type=None, watermark_type=None, watermark_value=None,
                 watermark_fill_style=None, watermark_font=None, watermark_rotate=None, watermark_horizontal=None,
                 watermark_vertical=None):
        self.project = project  # type: str
        self.src_uri = src_uri  # type: str
        self.src_type = src_type  # type: str
        self.watermark_type = watermark_type  # type: int
        self.watermark_value = watermark_value  # type: str
        self.watermark_fill_style = watermark_fill_style  # type: str
        self.watermark_font = watermark_font  # type: str
        self.watermark_rotate = watermark_rotate  # type: float
        self.watermark_horizontal = watermark_horizontal  # type: int
        self.watermark_vertical = watermark_vertical  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficePreviewURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_value is not None:
            result['WatermarkValue'] = self.watermark_value
        if self.watermark_fill_style is not None:
            result['WatermarkFillStyle'] = self.watermark_fill_style
        if self.watermark_font is not None:
            result['WatermarkFont'] = self.watermark_font
        if self.watermark_rotate is not None:
            result['WatermarkRotate'] = self.watermark_rotate
        if self.watermark_horizontal is not None:
            result['WatermarkHorizontal'] = self.watermark_horizontal
        if self.watermark_vertical is not None:
            result['WatermarkVertical'] = self.watermark_vertical
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkValue') is not None:
            self.watermark_value = m.get('WatermarkValue')
        if m.get('WatermarkFillStyle') is not None:
            self.watermark_fill_style = m.get('WatermarkFillStyle')
        if m.get('WatermarkFont') is not None:
            self.watermark_font = m.get('WatermarkFont')
        if m.get('WatermarkRotate') is not None:
            self.watermark_rotate = m.get('WatermarkRotate')
        if m.get('WatermarkHorizontal') is not None:
            self.watermark_horizontal = m.get('WatermarkHorizontal')
        if m.get('WatermarkVertical') is not None:
            self.watermark_vertical = m.get('WatermarkVertical')
        return self


class GetOfficePreviewURLResponseBody(TeaModel):
    def __init__(self, request_id=None, preview_url=None, access_token_expired_time=None, access_token=None,
                 refresh_token=None, refresh_token_expired_time=None):
        self.request_id = request_id  # type: str
        self.preview_url = preview_url  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token = refresh_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficePreviewURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preview_url is not None:
            result['PreviewURL'] = self.preview_url
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreviewURL') is not None:
            self.preview_url = m.get('PreviewURL')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class GetOfficePreviewURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOfficePreviewURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOfficePreviewURLResponse, self).to_map()
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
            temp_model = GetOfficePreviewURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(self, project=None):
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, type=None, request_id=None, cu=None, create_time=None, endpoint=None, service_role=None,
                 project=None, region_id=None, billing_type=None, modify_time=None):
        self.type = type  # type: str
        self.request_id = request_id  # type: str
        self.cu = cu  # type: int
        self.create_time = create_time  # type: str
        self.endpoint = endpoint  # type: str
        self.service_role = service_role  # type: str
        self.project = project  # type: str
        self.region_id = region_id  # type: str
        self.billing_type = billing_type  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSetRequest(TeaModel):
    def __init__(self, project=None, set_id=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class GetSetResponseBody(TeaModel):
    def __init__(self, video_count=None, request_id=None, create_time=None, video_length=None, set_id=None,
                 image_count=None, face_count=None, set_name=None, modify_time=None):
        self.video_count = video_count  # type: int
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.video_length = video_length  # type: int
        self.set_id = set_id  # type: str
        self.image_count = image_count  # type: int
        self.face_count = face_count  # type: int
        self.set_name = set_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSetResponse, self).to_map()
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
            temp_model = GetSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoRequest(TeaModel):
    def __init__(self, project=None, set_id=None, video_uri=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.video_uri = video_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        return self


class GetVideoResponseBodyVideoTags(TeaModel):
    def __init__(self, tag_name=None, tag_confidence=None, tag_level=None, parent_tag_name=None):
        self.tag_name = tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoResponseBodyVideoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class GetVideoResponseBody(TeaModel):
    def __init__(self, modify_time=None, process_status=None, video_width=None, source_type=None, source_uri=None,
                 video_info=None, video_frame_tags_modify_time=None, remarks_a=None, video_faces_fail_reason=None,
                 remarks_b=None, video_faces_status=None, remarks_c=None, video_ocrmodify_time=None, remarks_d=None,
                 video_height=None, source_position=None, video_ocrfail_reason=None, video_frame_tags_status=None,
                 video_tags_fail_reason=None, video_tags_modify_time=None, video_ocrstatus=None, video_frames=None, request_id=None,
                 process_modify_time=None, video_sttmodify_time=None, process_fail_reason=None, create_time=None, external_id=None,
                 video_sttfail_reason=None, video_uri=None, video_frame_tags_fail_reason=None, video_format=None, video_sttstatus=None,
                 video_faces_modify_time=None, video_tags=None, video_duration=None, set_id=None, video_tags_status=None, file_size=None):
        self.modify_time = modify_time  # type: str
        self.process_status = process_status  # type: str
        self.video_width = video_width  # type: int
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.video_info = video_info  # type: str
        self.video_frame_tags_modify_time = video_frame_tags_modify_time  # type: str
        self.remarks_a = remarks_a  # type: str
        self.video_faces_fail_reason = video_faces_fail_reason  # type: str
        self.remarks_b = remarks_b  # type: str
        self.video_faces_status = video_faces_status  # type: str
        self.remarks_c = remarks_c  # type: str
        self.video_ocrmodify_time = video_ocrmodify_time  # type: str
        self.remarks_d = remarks_d  # type: str
        self.video_height = video_height  # type: int
        self.source_position = source_position  # type: str
        self.video_ocrfail_reason = video_ocrfail_reason  # type: str
        self.video_frame_tags_status = video_frame_tags_status  # type: str
        self.video_tags_fail_reason = video_tags_fail_reason  # type: str
        self.video_tags_modify_time = video_tags_modify_time  # type: str
        self.video_ocrstatus = video_ocrstatus  # type: str
        self.video_frames = video_frames  # type: int
        self.request_id = request_id  # type: str
        self.process_modify_time = process_modify_time  # type: str
        self.video_sttmodify_time = video_sttmodify_time  # type: str
        self.process_fail_reason = process_fail_reason  # type: str
        self.create_time = create_time  # type: str
        self.external_id = external_id  # type: str
        self.video_sttfail_reason = video_sttfail_reason  # type: str
        self.video_uri = video_uri  # type: str
        self.video_frame_tags_fail_reason = video_frame_tags_fail_reason  # type: str
        self.video_format = video_format  # type: str
        self.video_sttstatus = video_sttstatus  # type: str
        self.video_faces_modify_time = video_faces_modify_time  # type: str
        self.video_tags = video_tags  # type: list[GetVideoResponseBodyVideoTags]
        self.video_duration = video_duration  # type: float
        self.set_id = set_id  # type: str
        self.video_tags_status = video_tags_status  # type: str
        self.file_size = file_size  # type: int

    def validate(self):
        if self.video_tags:
            for k in self.video_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info
        if self.video_frame_tags_modify_time is not None:
            result['VideoFrameTagsModifyTime'] = self.video_frame_tags_modify_time
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.video_faces_fail_reason is not None:
            result['VideoFacesFailReason'] = self.video_faces_fail_reason
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.video_faces_status is not None:
            result['VideoFacesStatus'] = self.video_faces_status
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.video_ocrmodify_time is not None:
            result['VideoOCRModifyTime'] = self.video_ocrmodify_time
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.video_ocrfail_reason is not None:
            result['VideoOCRFailReason'] = self.video_ocrfail_reason
        if self.video_frame_tags_status is not None:
            result['VideoFrameTagsStatus'] = self.video_frame_tags_status
        if self.video_tags_fail_reason is not None:
            result['VideoTagsFailReason'] = self.video_tags_fail_reason
        if self.video_tags_modify_time is not None:
            result['VideoTagsModifyTime'] = self.video_tags_modify_time
        if self.video_ocrstatus is not None:
            result['VideoOCRStatus'] = self.video_ocrstatus
        if self.video_frames is not None:
            result['VideoFrames'] = self.video_frames
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.video_sttmodify_time is not None:
            result['VideoSTTModifyTime'] = self.video_sttmodify_time
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.video_sttfail_reason is not None:
            result['VideoSTTFailReason'] = self.video_sttfail_reason
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.video_frame_tags_fail_reason is not None:
            result['VideoFrameTagsFailReason'] = self.video_frame_tags_fail_reason
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.video_sttstatus is not None:
            result['VideoSTTStatus'] = self.video_sttstatus
        if self.video_faces_modify_time is not None:
            result['VideoFacesModifyTime'] = self.video_faces_modify_time
        result['VideoTags'] = []
        if self.video_tags is not None:
            for k in self.video_tags:
                result['VideoTags'].append(k.to_map() if k else None)
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_tags_status is not None:
            result['VideoTagsStatus'] = self.video_tags_status
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('VideoInfo') is not None:
            self.video_info = m.get('VideoInfo')
        if m.get('VideoFrameTagsModifyTime') is not None:
            self.video_frame_tags_modify_time = m.get('VideoFrameTagsModifyTime')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('VideoFacesFailReason') is not None:
            self.video_faces_fail_reason = m.get('VideoFacesFailReason')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('VideoFacesStatus') is not None:
            self.video_faces_status = m.get('VideoFacesStatus')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('VideoOCRModifyTime') is not None:
            self.video_ocrmodify_time = m.get('VideoOCRModifyTime')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('VideoOCRFailReason') is not None:
            self.video_ocrfail_reason = m.get('VideoOCRFailReason')
        if m.get('VideoFrameTagsStatus') is not None:
            self.video_frame_tags_status = m.get('VideoFrameTagsStatus')
        if m.get('VideoTagsFailReason') is not None:
            self.video_tags_fail_reason = m.get('VideoTagsFailReason')
        if m.get('VideoTagsModifyTime') is not None:
            self.video_tags_modify_time = m.get('VideoTagsModifyTime')
        if m.get('VideoOCRStatus') is not None:
            self.video_ocrstatus = m.get('VideoOCRStatus')
        if m.get('VideoFrames') is not None:
            self.video_frames = m.get('VideoFrames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('VideoSTTModifyTime') is not None:
            self.video_sttmodify_time = m.get('VideoSTTModifyTime')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('VideoSTTFailReason') is not None:
            self.video_sttfail_reason = m.get('VideoSTTFailReason')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('VideoFrameTagsFailReason') is not None:
            self.video_frame_tags_fail_reason = m.get('VideoFrameTagsFailReason')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('VideoSTTStatus') is not None:
            self.video_sttstatus = m.get('VideoSTTStatus')
        if m.get('VideoFacesModifyTime') is not None:
            self.video_faces_modify_time = m.get('VideoFacesModifyTime')
        self.video_tags = []
        if m.get('VideoTags') is not None:
            for k in m.get('VideoTags'):
                temp_model = GetVideoResponseBodyVideoTags()
                self.video_tags.append(temp_model.from_map(k))
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoTagsStatus') is not None:
            self.video_tags_status = m.get('VideoTagsStatus')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class GetVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoResponse, self).to_map()
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
            temp_model = GetVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTaskRequest(TeaModel):
    def __init__(self, project=None, task_type=None, task_id=None):
        self.project = project  # type: str
        self.task_type = task_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoTaskResponseBody(TeaModel):
    def __init__(self, status=None, progress=None, notify_endpoint=None, parameters=None, task_id=None,
                 end_time=None, request_id=None, task_type=None, start_time=None, notify_topic_name=None, error_message=None,
                 result=None):
        self.status = status  # type: str
        self.progress = progress  # type: int
        self.notify_endpoint = notify_endpoint  # type: str
        self.parameters = parameters  # type: str
        self.task_id = task_id  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.task_type = task_type  # type: str
        self.start_time = start_time  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.error_message = error_message  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoTaskResponse, self).to_map()
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
            temp_model = GetVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebofficeURLRequest(TeaModel):
    def __init__(self, project=None, src_type=None, file_id=None, user=None, permission=None, file=None,
                 notify_endpoint=None, notify_topic_name=None, watermark=None, hidecmb=None):
        self.project = project  # type: str
        self.src_type = src_type  # type: str
        self.file_id = file_id  # type: str
        self.user = user  # type: str
        self.permission = permission  # type: str
        self.file = file  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.watermark = watermark  # type: str
        self.hidecmb = hidecmb  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebofficeURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.user is not None:
            result['User'] = self.user
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.file is not None:
            result['File'] = self.file
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('File') is not None:
            self.file = m.get('File')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        return self


class GetWebofficeURLResponseBody(TeaModel):
    def __init__(self, refresh_token=None, request_id=None, access_token=None, refresh_token_expired_time=None,
                 weboffice_url=None, access_token_expired_time=None):
        self.refresh_token = refresh_token  # type: str
        self.request_id = request_id  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str
        self.weboffice_url = weboffice_url  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWebofficeURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetWebofficeURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWebofficeURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWebofficeURLResponse, self).to_map()
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
            temp_model = GetWebofficeURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexImageRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None, remarks_a=None, remarks_b=None, source_type=None,
                 source_uri=None, source_position=None, remarks_c=None, remarks_d=None, external_id=None, notify_endpoint=None,
                 notify_topic_name=None, remarks_array_a=None, remarks_array_b=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.source_position = source_position  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.external_id = external_id  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_array_b = remarks_array_b  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        return self


class IndexImageResponseBody(TeaModel):
    def __init__(self, remarks_array_b=None, modify_time=None, remarks_c=None, remarks_d=None, request_id=None,
                 create_time=None, external_id=None, remarks_array_a=None, remarks_a=None, image_uri=None, set_id=None,
                 remarks_b=None):
        self.remarks_array_b = remarks_array_b  # type: str
        self.modify_time = modify_time  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.external_id = external_id  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_a = remarks_a  # type: str
        self.image_uri = image_uri  # type: str
        self.set_id = set_id  # type: str
        self.remarks_b = remarks_b  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        return self


class IndexImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: IndexImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IndexImageResponse, self).to_map()
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
            temp_model = IndexImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexVideoRequest(TeaModel):
    def __init__(self, project=None, set_id=None, video_uri=None, remarks_a=None, remarks_b=None, tgt_uri=None,
                 remarks_c=None, remarks_d=None, external_id=None, notify_topic_name=None, notify_endpoint=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.video_uri = video_uri  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.external_id = external_id  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class IndexVideoResponseBody(TeaModel):
    def __init__(self, modify_time=None, request_id=None, create_time=None, external_id=None, video_uri=None,
                 remarks_a=None, remarks_b=None, remarks_c=None, remarks_d=None, set_id=None):
        self.modify_time = modify_time  # type: str
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.external_id = external_id  # type: str
        self.video_uri = video_uri  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class IndexVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: IndexVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IndexVideoResponse, self).to_map()
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
            temp_model = IndexVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceGroupsRequest(TeaModel):
    def __init__(self, project=None, set_id=None, marker=None, limit=None, order=None, order_by=None,
                 remarks_aquery=None, remarks_bquery=None, remarks_cquery=None, remarks_dquery=None, remarks_array_aquery=None,
                 remarks_array_bquery=None, external_id=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.marker = marker  # type: str
        self.limit = limit  # type: int
        self.order = order  # type: str
        self.order_by = order_by  # type: str
        self.remarks_aquery = remarks_aquery  # type: str
        self.remarks_bquery = remarks_bquery  # type: str
        self.remarks_cquery = remarks_cquery  # type: str
        self.remarks_dquery = remarks_dquery  # type: str
        self.remarks_array_aquery = remarks_array_aquery  # type: str
        self.remarks_array_bquery = remarks_array_bquery  # type: str
        self.external_id = external_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFaceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.remarks_aquery is not None:
            result['RemarksAQuery'] = self.remarks_aquery
        if self.remarks_bquery is not None:
            result['RemarksBQuery'] = self.remarks_bquery
        if self.remarks_cquery is not None:
            result['RemarksCQuery'] = self.remarks_cquery
        if self.remarks_dquery is not None:
            result['RemarksDQuery'] = self.remarks_dquery
        if self.remarks_array_aquery is not None:
            result['RemarksArrayAQuery'] = self.remarks_array_aquery
        if self.remarks_array_bquery is not None:
            result['RemarksArrayBQuery'] = self.remarks_array_bquery
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RemarksAQuery') is not None:
            self.remarks_aquery = m.get('RemarksAQuery')
        if m.get('RemarksBQuery') is not None:
            self.remarks_bquery = m.get('RemarksBQuery')
        if m.get('RemarksCQuery') is not None:
            self.remarks_cquery = m.get('RemarksCQuery')
        if m.get('RemarksDQuery') is not None:
            self.remarks_dquery = m.get('RemarksDQuery')
        if m.get('RemarksArrayAQuery') is not None:
            self.remarks_array_aquery = m.get('RemarksArrayAQuery')
        if m.get('RemarksArrayBQuery') is not None:
            self.remarks_array_bquery = m.get('RemarksArrayBQuery')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        return self


class ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary(TeaModel):
    def __init__(self, top=None, width=None, height=None, left=None):
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int
        self.left = left  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace(TeaModel):
    def __init__(self, face_id=None, image_uri=None, face_boundary=None, external_id=None, image_height=None,
                 image_width=None):
        self.face_id = face_id  # type: str
        self.image_uri = image_uri  # type: str
        self.face_boundary = face_boundary  # type: ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary
        self.external_id = external_id  # type: str
        self.image_height = image_height  # type: long
        self.image_width = image_width  # type: long

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super(ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceBoundary') is not None:
            temp_model = ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        return self


class ListFaceGroupsResponseBodyFaceGroups(TeaModel):
    def __init__(self, gender=None, create_time=None, remarks_c=None, group_cover_face=None, face_count=None,
                 remarks_array_b=None, remarks_d=None, max_age=None, group_id=None, group_name=None, remarks_a=None,
                 average_age=None, remarks_array_a=None, min_age=None, image_count=None, external_id=None, remarks_b=None,
                 modify_time=None):
        self.gender = gender  # type: str
        self.create_time = create_time  # type: str
        self.remarks_c = remarks_c  # type: str
        self.group_cover_face = group_cover_face  # type: ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace
        self.face_count = face_count  # type: int
        self.remarks_array_b = remarks_array_b  # type: str
        self.remarks_d = remarks_d  # type: str
        self.max_age = max_age  # type: float
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.remarks_a = remarks_a  # type: str
        self.average_age = average_age  # type: float
        self.remarks_array_a = remarks_array_a  # type: str
        self.min_age = min_age  # type: float
        self.image_count = image_count  # type: int
        self.external_id = external_id  # type: str
        self.remarks_b = remarks_b  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        if self.group_cover_face:
            self.group_cover_face.validate()

    def to_map(self):
        _map = super(ListFaceGroupsResponseBodyFaceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.group_cover_face is not None:
            result['GroupCoverFace'] = self.group_cover_face.to_map()
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.average_age is not None:
            result['AverageAge'] = self.average_age
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('GroupCoverFace') is not None:
            temp_model = ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace()
            self.group_cover_face = temp_model.from_map(m['GroupCoverFace'])
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListFaceGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, next_marker=None, face_groups=None):
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.face_groups = face_groups  # type: list[ListFaceGroupsResponseBodyFaceGroups]

    def validate(self):
        if self.face_groups:
            for k in self.face_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFaceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        result['FaceGroups'] = []
        if self.face_groups is not None:
            for k in self.face_groups:
                result['FaceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        self.face_groups = []
        if m.get('FaceGroups') is not None:
            for k in m.get('FaceGroups'):
                temp_model = ListFaceGroupsResponseBodyFaceGroups()
                self.face_groups.append(temp_model.from_map(k))
        return self


class ListFaceGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFaceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFaceGroupsResponse, self).to_map()
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
            temp_model = ListFaceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(self, project=None, set_id=None, create_time_start=None, marker=None, limit=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.create_time_start = create_time_start  # type: str
        self.marker = marker  # type: str
        self.limit = limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesCroppingSuggestion(TeaModel):
    def __init__(self, score=None, aspect_ratio=None, cropping_boundary=None):
        self.score = score  # type: float
        self.aspect_ratio = aspect_ratio  # type: str
        self.cropping_boundary = cropping_boundary  # type: ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesCroppingSuggestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class ListImagesResponseBodyImagesFacesEmotionDetails(TeaModel):
    def __init__(self, happy=None, surprised=None, calm=None, disgusted=None, angry=None, sad=None, scared=None):
        self.happy = happy  # type: float
        self.surprised = surprised  # type: float
        self.calm = calm  # type: float
        self.disgusted = disgusted  # type: float
        self.angry = angry  # type: float
        self.sad = sad  # type: float
        self.scared = scared  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesFacesEmotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesFacesFaceAttributesHeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributes(TeaModel):
    def __init__(self, glasses_confidence=None, glasses=None, mask=None, beard_confidence=None,
                 mask_confidence=None, beard=None, face_boundary=None, head_pose=None):
        self.glasses_confidence = glasses_confidence  # type: float
        self.glasses = glasses  # type: str
        self.mask = mask  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.mask_confidence = mask_confidence  # type: float
        self.beard = beard  # type: str
        self.face_boundary = face_boundary  # type: ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary
        self.head_pose = head_pose  # type: ListImagesResponseBodyImagesFacesFaceAttributesHeadPose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class ListImagesResponseBodyImagesFaces(TeaModel):
    def __init__(self, emotion_confidence=None, attractive=None, group_id=None, gender=None, face_id=None,
                 gender_confidence=None, face_quality=None, emotion=None, age=None, face_confidence=None, emotion_details=None,
                 face_attributes=None):
        self.emotion_confidence = emotion_confidence  # type: float
        self.attractive = attractive  # type: float
        self.group_id = group_id  # type: str
        self.gender = gender  # type: str
        self.face_id = face_id  # type: str
        self.gender_confidence = gender_confidence  # type: float
        self.face_quality = face_quality  # type: float
        self.emotion = emotion  # type: str
        self.age = age  # type: int
        self.face_confidence = face_confidence  # type: float
        self.emotion_details = emotion_details  # type: ListImagesResponseBodyImagesFacesEmotionDetails
        self.face_attributes = face_attributes  # type: ListImagesResponseBodyImagesFacesFaceAttributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = ListImagesResponseBodyImagesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class ListImagesResponseBodyImagesTags(TeaModel):
    def __init__(self, tag_level=None, parent_tag_name=None, tag_confidence=None, tag_name=None):
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListImagesResponseBodyImagesOCROCRBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesOCROCRBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesOCR(TeaModel):
    def __init__(self, ocrconfidence=None, ocrcontents=None, ocrboundary=None):
        self.ocrconfidence = ocrconfidence  # type: float
        self.ocrcontents = ocrcontents  # type: str
        self.ocrboundary = ocrboundary  # type: ListImagesResponseBodyImagesOCROCRBoundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesOCR, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class ListImagesResponseBodyImagesImageQuality(TeaModel):
    def __init__(self, overall_score=None, color=None, color_score=None, contrast_score=None, contrast=None,
                 exposure_score=None, clarity_score=None, clarity=None, exposure=None, composition_score=None):
        self.overall_score = overall_score  # type: float
        self.color = color  # type: float
        self.color_score = color_score  # type: float
        self.contrast_score = contrast_score  # type: float
        self.contrast = contrast  # type: float
        self.exposure_score = exposure_score  # type: float
        self.clarity_score = clarity_score  # type: float
        self.clarity = clarity  # type: float
        self.exposure = exposure  # type: float
        self.composition_score = composition_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesImageQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class ListImagesResponseBodyImagesAddress(TeaModel):
    def __init__(self, township=None, district=None, address_line=None, country=None, city=None, province=None):
        self.township = township  # type: str
        self.district = district  # type: str
        self.address_line = address_line  # type: str
        self.country = country  # type: str
        self.city = city  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyImagesAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(self, cropping_suggestion_status=None, image_quality_modify_time=None, tags_fail_reason=None,
                 remarks_c=None, create_time=None, source_type=None, faces_fail_reason=None, faces_modify_time=None,
                 image_time=None, ocrmodify_time=None, address_modify_time=None, image_quality_fail_reason=None,
                 faces_status=None, remarks_array_a=None, image_height=None, external_id=None, source_uri=None, file_size=None,
                 modify_time=None, source_position=None, image_quality_status=None, ocrfail_reason=None,
                 address_fail_reason=None, cropping_suggestion_modify_time=None, image_format=None, image_width=None,
                 remarks_array_b=None, orientation=None, remarks_d=None, tags_status=None, cropping_suggestion_fail_reason=None,
                 remarks_a=None, image_uri=None, tags_modify_time=None, ocrstatus=None, address_status=None, exif=None,
                 location=None, remarks_b=None, cropping_suggestion=None, faces=None, tags=None, ocr=None, image_quality=None,
                 address=None):
        self.cropping_suggestion_status = cropping_suggestion_status  # type: str
        self.image_quality_modify_time = image_quality_modify_time  # type: str
        self.tags_fail_reason = tags_fail_reason  # type: str
        self.remarks_c = remarks_c  # type: str
        self.create_time = create_time  # type: str
        self.source_type = source_type  # type: str
        self.faces_fail_reason = faces_fail_reason  # type: str
        self.faces_modify_time = faces_modify_time  # type: str
        self.image_time = image_time  # type: str
        self.ocrmodify_time = ocrmodify_time  # type: str
        self.address_modify_time = address_modify_time  # type: str
        self.image_quality_fail_reason = image_quality_fail_reason  # type: str
        self.faces_status = faces_status  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.image_height = image_height  # type: int
        self.external_id = external_id  # type: str
        self.source_uri = source_uri  # type: str
        self.file_size = file_size  # type: int
        self.modify_time = modify_time  # type: str
        self.source_position = source_position  # type: str
        self.image_quality_status = image_quality_status  # type: str
        self.ocrfail_reason = ocrfail_reason  # type: str
        self.address_fail_reason = address_fail_reason  # type: str
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time  # type: str
        self.image_format = image_format  # type: str
        self.image_width = image_width  # type: int
        self.remarks_array_b = remarks_array_b  # type: str
        self.orientation = orientation  # type: str
        self.remarks_d = remarks_d  # type: str
        self.tags_status = tags_status  # type: str
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason  # type: str
        self.remarks_a = remarks_a  # type: str
        self.image_uri = image_uri  # type: str
        self.tags_modify_time = tags_modify_time  # type: str
        self.ocrstatus = ocrstatus  # type: str
        self.address_status = address_status  # type: str
        self.exif = exif  # type: str
        self.location = location  # type: str
        self.remarks_b = remarks_b  # type: str
        self.cropping_suggestion = cropping_suggestion  # type: list[ListImagesResponseBodyImagesCroppingSuggestion]
        self.faces = faces  # type: list[ListImagesResponseBodyImagesFaces]
        self.tags = tags  # type: list[ListImagesResponseBodyImagesTags]
        self.ocr = ocr  # type: list[ListImagesResponseBodyImagesOCR]
        self.image_quality = image_quality  # type: ListImagesResponseBodyImagesImageQuality
        self.address = address  # type: ListImagesResponseBodyImagesAddress

    def validate(self):
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = ListImagesResponseBodyImagesCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListImagesResponseBodyImagesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListImagesResponseBodyImagesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = ListImagesResponseBodyImagesOCR()
                self.ocr.append(temp_model.from_map(k))
        if m.get('ImageQuality') is not None:
            temp_model = ListImagesResponseBodyImagesImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('Address') is not None:
            temp_model = ListImagesResponseBodyImagesAddress()
            self.address = temp_model.from_map(m['Address'])
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, request_id=None, next_marker=None, set_id=None, images=None):
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.set_id = set_id  # type: str
        self.images = images  # type: list[ListImagesResponseBodyImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImagesResponse, self).to_map()
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeConversionTaskRequest(TeaModel):
    def __init__(self, project=None, marker=None, max_keys=None):
        self.project = project  # type: str
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeConversionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        return self


class ListOfficeConversionTaskResponseBodyTasks(TeaModel):
    def __init__(self, status=None, percent=None, finish_time=None, create_time=None, page_count=None,
                 notify_topic_name=None, notify_endpoint=None, src_uri=None, tgt_type=None, tgt_uri=None, image_spec=None,
                 external_id=None, task_id=None):
        self.status = status  # type: str
        self.percent = percent  # type: int
        self.finish_time = finish_time  # type: str
        self.create_time = create_time  # type: str
        self.page_count = page_count  # type: int
        self.notify_topic_name = notify_topic_name  # type: str
        self.notify_endpoint = notify_endpoint  # type: str
        self.src_uri = src_uri  # type: str
        self.tgt_type = tgt_type  # type: str
        self.tgt_uri = tgt_uri  # type: str
        self.image_spec = image_spec  # type: str
        self.external_id = external_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeConversionTaskResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.image_spec is not None:
            result['ImageSpec'] = self.image_spec
        if self.external_id is not None:
            result['ExternalID'] = self.external_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('ImageSpec') is not None:
            self.image_spec = m.get('ImageSpec')
        if m.get('ExternalID') is not None:
            self.external_id = m.get('ExternalID')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListOfficeConversionTaskResponseBody(TeaModel):
    def __init__(self, next_marker=None, request_id=None, tasks=None):
        self.next_marker = next_marker  # type: str
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListOfficeConversionTaskResponseBodyTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOfficeConversionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListOfficeConversionTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListOfficeConversionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOfficeConversionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOfficeConversionTaskResponse, self).to_map()
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
            temp_model = ListOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectAPIsRequest(TeaModel):
    def __init__(self, project=None):
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectAPIsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class ListProjectAPIsResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None, apis=None):
        self.project = project  # type: str
        self.request_id = request_id  # type: str
        self.apis = apis  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectAPIsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.apis is not None:
            result['APIs'] = self.apis
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('APIs') is not None:
            self.apis = m.get('APIs')
        return self


class ListProjectAPIsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectAPIsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectAPIsResponse, self).to_map()
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
            temp_model = ListProjectAPIsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, marker=None, max_keys=None):
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(self, type=None, cu=None, create_time=None, service_role=None, endpoint=None, project=None,
                 region_id=None, billing_type=None, modify_time=None):
        self.type = type  # type: str
        self.cu = cu  # type: int
        self.create_time = create_time  # type: str
        self.service_role = service_role  # type: str
        self.endpoint = endpoint  # type: str
        self.project = project  # type: str
        self.region_id = region_id  # type: str
        self.billing_type = billing_type  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, next_marker=None, request_id=None, projects=None):
        self.next_marker = next_marker  # type: str
        self.request_id = request_id  # type: str
        self.projects = projects  # type: list[ListProjectsResponseBodyProjects]

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSetsRequest(TeaModel):
    def __init__(self, project=None, marker=None):
        self.project = project  # type: str
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListSetsResponseBodySets(TeaModel):
    def __init__(self, video_count=None, create_time=None, video_length=None, set_id=None, image_count=None,
                 face_count=None, set_name=None, modify_time=None):
        self.video_count = video_count  # type: int
        self.create_time = create_time  # type: str
        self.video_length = video_length  # type: int
        self.set_id = set_id  # type: str
        self.image_count = image_count  # type: int
        self.face_count = face_count  # type: int
        self.set_name = set_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSetsResponseBodySets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListSetsResponseBody(TeaModel):
    def __init__(self, next_marker=None, request_id=None, sets=None):
        self.next_marker = next_marker  # type: str
        self.request_id = request_id  # type: str
        self.sets = sets  # type: list[ListSetsResponseBodySets]

    def validate(self):
        if self.sets:
            for k in self.sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sets'] = []
        if self.sets is not None:
            for k in self.sets:
                result['Sets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sets = []
        if m.get('Sets') is not None:
            for k in m.get('Sets'):
                temp_model = ListSetsResponseBodySets()
                self.sets.append(temp_model.from_map(k))
        return self


class ListSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSetsResponse, self).to_map()
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
            temp_model = ListSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSetTagsRequest(TeaModel):
    def __init__(self, project=None, set_id=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSetTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class ListSetTagsResponseBodyTags(TeaModel):
    def __init__(self, tag_level=None, tag_name=None, tag_count=None):
        self.tag_level = tag_level  # type: int
        self.tag_name = tag_name  # type: str
        self.tag_count = tag_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSetTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        return self


class ListSetTagsResponseBody(TeaModel):
    def __init__(self, set_id=None, request_id=None, tags=None):
        self.set_id = set_id  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListSetTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSetTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSetTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListSetTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSetTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSetTagsResponse, self).to_map()
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
            temp_model = ListSetTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoAudiosRequest(TeaModel):
    def __init__(self, project=None, set_id=None, video_uri=None, marker=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.video_uri = video_uri  # type: str
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoAudiosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideoAudiosResponseBodyAudiosAudioTexts(TeaModel):
    def __init__(self, end_time=None, library=None, confidence=None, begin_time=None, channel_id=None,
                 emotion_value=None, speech_rate=None, text=None, person=None, silence_duration=None):
        self.end_time = end_time  # type: float
        self.library = library  # type: str
        self.confidence = confidence  # type: float
        self.begin_time = begin_time  # type: float
        self.channel_id = channel_id  # type: int
        self.emotion_value = emotion_value  # type: float
        self.speech_rate = speech_rate  # type: int
        self.text = text  # type: str
        self.person = person  # type: str
        self.silence_duration = silence_duration  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoAudiosResponseBodyAudiosAudioTexts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.library is not None:
            result['Library'] = self.library
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        if self.person is not None:
            result['Person'] = self.person
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Library') is not None:
            self.library = m.get('Library')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Person') is not None:
            self.person = m.get('Person')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class ListVideoAudiosResponseBodyAudios(TeaModel):
    def __init__(self, source_position=None, remarks_c=None, create_time=None, source_type=None,
                 audio_duration=None, audio_texts_status=None, audio_format=None, remarks_d=None, process_fail_reason=None,
                 process_modify_time=None, audio_rate=None, audio_uri=None, audio_texts_modify_time=None, remarks_a=None,
                 external_id=None, source_uri=None, process_status=None, audio_texts_fail_reason=None, remarks_b=None,
                 file_size=None, modify_time=None, audio_texts=None):
        self.source_position = source_position  # type: str
        self.remarks_c = remarks_c  # type: str
        self.create_time = create_time  # type: str
        self.source_type = source_type  # type: str
        self.audio_duration = audio_duration  # type: float
        self.audio_texts_status = audio_texts_status  # type: str
        self.audio_format = audio_format  # type: str
        self.remarks_d = remarks_d  # type: str
        self.process_fail_reason = process_fail_reason  # type: str
        self.process_modify_time = process_modify_time  # type: str
        self.audio_rate = audio_rate  # type: int
        self.audio_uri = audio_uri  # type: str
        self.audio_texts_modify_time = audio_texts_modify_time  # type: str
        self.remarks_a = remarks_a  # type: str
        self.external_id = external_id  # type: str
        self.source_uri = source_uri  # type: str
        self.process_status = process_status  # type: str
        self.audio_texts_fail_reason = audio_texts_fail_reason  # type: str
        self.remarks_b = remarks_b  # type: str
        self.file_size = file_size  # type: int
        self.modify_time = modify_time  # type: str
        self.audio_texts = audio_texts  # type: list[ListVideoAudiosResponseBodyAudiosAudioTexts]

    def validate(self):
        if self.audio_texts:
            for k in self.audio_texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideoAudiosResponseBodyAudios, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.audio_texts_status is not None:
            result['AudioTextsStatus'] = self.audio_texts_status
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.audio_rate is not None:
            result['AudioRate'] = self.audio_rate
        if self.audio_uri is not None:
            result['AudioUri'] = self.audio_uri
        if self.audio_texts_modify_time is not None:
            result['AudioTextsModifyTime'] = self.audio_texts_modify_time
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.audio_texts_fail_reason is not None:
            result['AudioTextsFailReason'] = self.audio_texts_fail_reason
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['AudioTexts'] = []
        if self.audio_texts is not None:
            for k in self.audio_texts:
                result['AudioTexts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('AudioTextsStatus') is not None:
            self.audio_texts_status = m.get('AudioTextsStatus')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('AudioRate') is not None:
            self.audio_rate = m.get('AudioRate')
        if m.get('AudioUri') is not None:
            self.audio_uri = m.get('AudioUri')
        if m.get('AudioTextsModifyTime') is not None:
            self.audio_texts_modify_time = m.get('AudioTextsModifyTime')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('AudioTextsFailReason') is not None:
            self.audio_texts_fail_reason = m.get('AudioTextsFailReason')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.audio_texts = []
        if m.get('AudioTexts') is not None:
            for k in m.get('AudioTexts'):
                temp_model = ListVideoAudiosResponseBodyAudiosAudioTexts()
                self.audio_texts.append(temp_model.from_map(k))
        return self


class ListVideoAudiosResponseBody(TeaModel):
    def __init__(self, video_uri=None, request_id=None, next_marker=None, set_id=None, audios=None):
        self.video_uri = video_uri  # type: str
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.set_id = set_id  # type: str
        self.audios = audios  # type: list[ListVideoAudiosResponseBodyAudios]

    def validate(self):
        if self.audios:
            for k in self.audios:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideoAudiosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Audios'] = []
        if self.audios is not None:
            for k in self.audios:
                result['Audios'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.audios = []
        if m.get('Audios') is not None:
            for k in m.get('Audios'):
                temp_model = ListVideoAudiosResponseBodyAudios()
                self.audios.append(temp_model.from_map(k))
        return self


class ListVideoAudiosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVideoAudiosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVideoAudiosResponse, self).to_map()
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
            temp_model = ListVideoAudiosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoFramesRequest(TeaModel):
    def __init__(self, project=None, set_id=None, video_uri=None, marker=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.video_uri = video_uri  # type: str
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideoFramesResponseBodyFramesFacesEmotionDetails(TeaModel):
    def __init__(self, happy=None, surprised=None, calm=None, disgusted=None, angry=None, sad=None, scared=None):
        self.happy = happy  # type: float
        self.surprised = surprised  # type: float
        self.calm = calm  # type: float
        self.disgusted = disgusted  # type: float
        self.angry = angry  # type: float
        self.sad = sad  # type: float
        self.scared = scared  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesFacesEmotionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributes(TeaModel):
    def __init__(self, glasses_confidence=None, glasses=None, mask=None, beard_confidence=None,
                 mask_confidence=None, beard=None, face_boundary=None, head_pose=None):
        self.glasses_confidence = glasses_confidence  # type: float
        self.glasses = glasses  # type: str
        self.mask = mask  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.mask_confidence = mask_confidence  # type: float
        self.beard = beard  # type: str
        self.face_boundary = face_boundary  # type: ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary
        self.head_pose = head_pose  # type: ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesFacesFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class ListVideoFramesResponseBodyFramesFaces(TeaModel):
    def __init__(self, emotion_confidence=None, attractive=None, group_id=None, gender=None, face_id=None,
                 gender_confidence=None, face_quality=None, emotion=None, age=None, face_confidence=None, emotion_details=None,
                 face_attributes=None):
        self.emotion_confidence = emotion_confidence  # type: float
        self.attractive = attractive  # type: float
        self.group_id = group_id  # type: str
        self.gender = gender  # type: str
        self.face_id = face_id  # type: str
        self.gender_confidence = gender_confidence  # type: float
        self.face_quality = face_quality  # type: float
        self.emotion = emotion  # type: str
        self.age = age  # type: int
        self.face_confidence = face_confidence  # type: float
        self.emotion_details = emotion_details  # type: ListVideoFramesResponseBodyFramesFacesEmotionDetails
        self.face_attributes = face_attributes  # type: ListVideoFramesResponseBodyFramesFacesFaceAttributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class ListVideoFramesResponseBodyFramesTags(TeaModel):
    def __init__(self, tag_level=None, parent_tag_name=None, tag_confidence=None, tag_name=None):
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListVideoFramesResponseBodyFramesOCROCRBoundary(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesOCROCRBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListVideoFramesResponseBodyFramesOCR(TeaModel):
    def __init__(self, ocrconfidence=None, ocrcontents=None, ocrboundary=None):
        self.ocrconfidence = ocrconfidence  # type: float
        self.ocrcontents = ocrcontents  # type: str
        self.ocrboundary = ocrboundary  # type: ListVideoFramesResponseBodyFramesOCROCRBoundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFramesOCR, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = ListVideoFramesResponseBodyFramesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class ListVideoFramesResponseBodyFrames(TeaModel):
    def __init__(self, tags_fail_reason=None, remarks_c=None, create_time=None, source_type=None,
                 faces_fail_reason=None, faces_modify_time=None, image_time=None, ocrmodify_time=None, faces_status=None,
                 image_height=None, external_id=None, source_uri=None, modify_time=None, file_size=None, source_position=None,
                 ocrfail_reason=None, image_format=None, image_width=None, orientation=None, remarks_d=None, tags_status=None,
                 remarks_a=None, image_uri=None, tags_modify_time=None, ocrstatus=None, exif=None, location=None,
                 remarks_b=None, faces=None, tags=None, ocr=None):
        self.tags_fail_reason = tags_fail_reason  # type: str
        self.remarks_c = remarks_c  # type: str
        self.create_time = create_time  # type: str
        self.source_type = source_type  # type: str
        self.faces_fail_reason = faces_fail_reason  # type: str
        self.faces_modify_time = faces_modify_time  # type: str
        self.image_time = image_time  # type: str
        self.ocrmodify_time = ocrmodify_time  # type: str
        self.faces_status = faces_status  # type: str
        self.image_height = image_height  # type: int
        self.external_id = external_id  # type: str
        self.source_uri = source_uri  # type: str
        self.modify_time = modify_time  # type: str
        self.file_size = file_size  # type: int
        self.source_position = source_position  # type: str
        self.ocrfail_reason = ocrfail_reason  # type: str
        self.image_format = image_format  # type: str
        self.image_width = image_width  # type: int
        self.orientation = orientation  # type: str
        self.remarks_d = remarks_d  # type: str
        self.tags_status = tags_status  # type: str
        self.remarks_a = remarks_a  # type: str
        self.image_uri = image_uri  # type: str
        self.tags_modify_time = tags_modify_time  # type: str
        self.ocrstatus = ocrstatus  # type: str
        self.exif = exif  # type: str
        self.location = location  # type: str
        self.remarks_b = remarks_b  # type: str
        self.faces = faces  # type: list[ListVideoFramesResponseBodyFramesFaces]
        self.tags = tags  # type: list[ListVideoFramesResponseBodyFramesTags]
        self.ocr = ocr  # type: list[ListVideoFramesResponseBodyFramesOCR]

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponseBodyFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListVideoFramesResponseBodyFramesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVideoFramesResponseBodyFramesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = ListVideoFramesResponseBodyFramesOCR()
                self.ocr.append(temp_model.from_map(k))
        return self


class ListVideoFramesResponseBody(TeaModel):
    def __init__(self, video_uri=None, request_id=None, next_marker=None, set_id=None, frames=None):
        self.video_uri = video_uri  # type: str
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.set_id = set_id  # type: str
        self.frames = frames  # type: list[ListVideoFramesResponseBodyFrames]

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = ListVideoFramesResponseBodyFrames()
                self.frames.append(temp_model.from_map(k))
        return self


class ListVideoFramesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVideoFramesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVideoFramesResponse, self).to_map()
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
            temp_model = ListVideoFramesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideosRequest(TeaModel):
    def __init__(self, project=None, set_id=None, create_time_start=None, marker=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.create_time_start = create_time_start  # type: str
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideosResponseBodyVideosVideoTags(TeaModel):
    def __init__(self, tag_level=None, parent_tag_name=None, tag_name=None, tag_confidence=None):
        self.tag_level = tag_level  # type: int
        self.parent_tag_name = parent_tag_name  # type: str
        self.tag_name = tag_name  # type: str
        self.tag_confidence = tag_confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideosResponseBodyVideosVideoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        return self


class ListVideosResponseBodyVideos(TeaModel):
    def __init__(self, create_time=None, remarks_c=None, video_tags_fail_reason=None, source_type=None,
                 video_duration=None, process_modify_time=None, video_frames=None, video_tags_status=None, external_id=None,
                 source_uri=None, modify_time=None, file_size=None, source_position=None, video_width=None, video_height=None,
                 video_format=None, remarks_d=None, video_uri=None, video_tags_modify_time=None, process_fail_reason=None,
                 remarks_a=None, process_status=None, remarks_b=None, video_tags=None):
        self.create_time = create_time  # type: str
        self.remarks_c = remarks_c  # type: str
        self.video_tags_fail_reason = video_tags_fail_reason  # type: str
        self.source_type = source_type  # type: str
        self.video_duration = video_duration  # type: float
        self.process_modify_time = process_modify_time  # type: str
        self.video_frames = video_frames  # type: int
        self.video_tags_status = video_tags_status  # type: str
        self.external_id = external_id  # type: str
        self.source_uri = source_uri  # type: str
        self.modify_time = modify_time  # type: str
        self.file_size = file_size  # type: int
        self.source_position = source_position  # type: str
        self.video_width = video_width  # type: int
        self.video_height = video_height  # type: int
        self.video_format = video_format  # type: str
        self.remarks_d = remarks_d  # type: str
        self.video_uri = video_uri  # type: str
        self.video_tags_modify_time = video_tags_modify_time  # type: str
        self.process_fail_reason = process_fail_reason  # type: str
        self.remarks_a = remarks_a  # type: str
        self.process_status = process_status  # type: str
        self.remarks_b = remarks_b  # type: str
        self.video_tags = video_tags  # type: list[ListVideosResponseBodyVideosVideoTags]

    def validate(self):
        if self.video_tags:
            for k in self.video_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideosResponseBodyVideos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.video_tags_fail_reason is not None:
            result['VideoTagsFailReason'] = self.video_tags_fail_reason
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.video_frames is not None:
            result['VideoFrames'] = self.video_frames
        if self.video_tags_status is not None:
            result['VideoTagsStatus'] = self.video_tags_status
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.video_tags_modify_time is not None:
            result['VideoTagsModifyTime'] = self.video_tags_modify_time
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['VideoTags'] = []
        if self.video_tags is not None:
            for k in self.video_tags:
                result['VideoTags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('VideoTagsFailReason') is not None:
            self.video_tags_fail_reason = m.get('VideoTagsFailReason')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('VideoFrames') is not None:
            self.video_frames = m.get('VideoFrames')
        if m.get('VideoTagsStatus') is not None:
            self.video_tags_status = m.get('VideoTagsStatus')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('VideoTagsModifyTime') is not None:
            self.video_tags_modify_time = m.get('VideoTagsModifyTime')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.video_tags = []
        if m.get('VideoTags') is not None:
            for k in m.get('VideoTags'):
                temp_model = ListVideosResponseBodyVideosVideoTags()
                self.video_tags.append(temp_model.from_map(k))
        return self


class ListVideosResponseBody(TeaModel):
    def __init__(self, request_id=None, next_marker=None, set_id=None, videos=None):
        self.request_id = request_id  # type: str
        self.next_marker = next_marker  # type: str
        self.set_id = set_id  # type: str
        self.videos = videos  # type: list[ListVideosResponseBodyVideos]

    def validate(self):
        if self.videos:
            for k in self.videos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Videos'] = []
        if self.videos is not None:
            for k in self.videos:
                result['Videos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.videos = []
        if m.get('Videos') is not None:
            for k in m.get('Videos'):
                temp_model = ListVideosResponseBodyVideos()
                self.videos.append(temp_model.from_map(k))
        return self


class ListVideosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVideosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVideosResponse, self).to_map()
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
            temp_model = ListVideosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoTasksRequest(TeaModel):
    def __init__(self, project=None, marker=None, max_keys=None, task_type=None):
        self.project = project  # type: str
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListVideoTasksResponseBodyTasks(TeaModel):
    def __init__(self, end_time=None, status=None, start_time=None, task_type=None, progress=None,
                 notify_endpoint=None, error_message=None, parameters=None, result=None, task_id=None, notify_topic_name=None):
        self.end_time = end_time  # type: str
        self.status = status  # type: str
        self.start_time = start_time  # type: str
        self.task_type = task_type  # type: str
        self.progress = progress  # type: int
        self.notify_endpoint = notify_endpoint  # type: str
        self.error_message = error_message  # type: str
        self.parameters = parameters  # type: str
        self.result = result  # type: str
        self.task_id = task_id  # type: str
        self.notify_topic_name = notify_topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVideoTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.result is not None:
            result['Result'] = self.result
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        return self


class ListVideoTasksResponseBody(TeaModel):
    def __init__(self, next_marker=None, request_id=None, tasks=None):
        self.next_marker = next_marker  # type: str
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListVideoTasksResponseBodyTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVideoTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListVideoTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListVideoTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVideoTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVideoTasksResponse, self).to_map()
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
            temp_model = ListVideoTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenImmServiceRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenImmServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenImmServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenImmServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenImmServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenImmServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenImmServiceResponse, self).to_map()
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
            temp_model = OpenImmServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProjectRequest(TeaModel):
    def __init__(self, project=None, service_role=None):
        self.project = project  # type: str
        self.service_role = service_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class PutProjectResponseBody(TeaModel):
    def __init__(self, project=None, modify_time=None, type=None, cu=None, service_role=None, request_id=None,
                 endpoint=None, create_time=None, region_id=None, billing_type=None):
        self.project = project  # type: str
        self.modify_time = modify_time  # type: str
        self.type = type  # type: str
        self.cu = cu  # type: int
        self.service_role = service_role  # type: str
        self.request_id = request_id  # type: str
        self.endpoint = endpoint  # type: str
        self.create_time = create_time  # type: str
        self.region_id = region_id  # type: str
        self.billing_type = billing_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.type is not None:
            result['Type'] = self.type
        if self.cu is not None:
            result['CU'] = self.cu
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        return self


class PutProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PutProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutProjectResponse, self).to_map()
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
            temp_model = PutProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshOfficeEditTokenRequest(TeaModel):
    def __init__(self, project=None, access_token=None, refresh_token=None):
        self.project = project  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshOfficeEditTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshOfficeEditTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, access_token_expired_time=None, refresh_token=None, access_token=None,
                 refresh_token_expired_time=None):
        self.request_id = request_id  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.refresh_token = refresh_token  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshOfficeEditTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshOfficeEditTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshOfficeEditTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshOfficeEditTokenResponse, self).to_map()
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
            temp_model = RefreshOfficeEditTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshOfficePreviewTokenRequest(TeaModel):
    def __init__(self, project=None, access_token=None, refresh_token=None):
        self.project = project  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshOfficePreviewTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshOfficePreviewTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, access_token_expired_time=None, refresh_token=None, access_token=None,
                 refresh_token_expired_time=None):
        self.request_id = request_id  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.refresh_token = refresh_token  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshOfficePreviewTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshOfficePreviewTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshOfficePreviewTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshOfficePreviewTokenResponse, self).to_map()
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
            temp_model = RefreshOfficePreviewTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(self, project=None, access_token=None, refresh_token=None):
        self.project = project  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebofficeTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, access_token_expired_time=None, refresh_token=None, access_token=None,
                 refresh_token_expired_time=None):
        self.request_id = request_id  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.refresh_token = refresh_token  # type: str
        self.access_token = access_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebofficeTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshWebofficeTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshWebofficeTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshWebofficeTokenResponse, self).to_map()
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
            temp_model = RefreshWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceGroupRequest(TeaModel):
    def __init__(self, project=None, set_id=None, group_id=None, group_name=None, group_cover_face_id=None,
                 remarks_a=None, remarks_b=None, remarks_c=None, remarks_d=None, remarks_array_a=None, remarks_array_b=None,
                 external_id=None, reset_items=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.group_cover_face_id = group_cover_face_id  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_array_b = remarks_array_b  # type: str
        self.external_id = external_id  # type: str
        self.reset_items = reset_items  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_cover_face_id is not None:
            result['GroupCoverFaceId'] = self.group_cover_face_id
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.reset_items is not None:
            result['ResetItems'] = self.reset_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupCoverFaceId') is not None:
            self.group_cover_face_id = m.get('GroupCoverFaceId')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ResetItems') is not None:
            self.reset_items = m.get('ResetItems')
        return self


class UpdateFaceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, group_id=None, set_id=None):
        self.request_id = request_id  # type: str
        self.group_id = group_id  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class UpdateFaceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFaceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFaceGroupResponse, self).to_map()
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
            temp_model = UpdateFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequestFaces(TeaModel):
    def __init__(self, face_id=None, group_id=None):
        self.face_id = face_id  # type: str
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageRequestFaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UpdateImageRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None, remarks_a=None, remarks_b=None, source_type=None,
                 source_uri=None, source_position=None, remarks_c=None, remarks_d=None, external_id=None, remarks_array_a=None,
                 remarks_array_b=None, faces=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.source_position = source_position  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.external_id = external_id  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_array_b = remarks_array_b  # type: str
        self.faces = faces  # type: list[UpdateImageRequestFaces]

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = UpdateImageRequestFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class UpdateImageShrinkRequest(TeaModel):
    def __init__(self, project=None, set_id=None, image_uri=None, remarks_a=None, remarks_b=None, source_type=None,
                 source_uri=None, source_position=None, remarks_c=None, remarks_d=None, external_id=None, remarks_array_a=None,
                 remarks_array_b=None, faces_shrink=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.image_uri = image_uri  # type: str
        self.remarks_a = remarks_a  # type: str
        self.remarks_b = remarks_b  # type: str
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.source_position = source_position  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.external_id = external_id  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_array_b = remarks_array_b  # type: str
        self.faces_shrink = faces_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.faces_shrink is not None:
            result['Faces'] = self.faces_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Faces') is not None:
            self.faces_shrink = m.get('Faces')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(self, remarks_array_b=None, modify_time=None, remarks_c=None, remarks_d=None, request_id=None,
                 create_time=None, external_id=None, remarks_array_a=None, remarks_a=None, image_uri=None, set_id=None,
                 remarks_b=None):
        self.remarks_array_b = remarks_array_b  # type: str
        self.modify_time = modify_time  # type: str
        self.remarks_c = remarks_c  # type: str
        self.remarks_d = remarks_d  # type: str
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.external_id = external_id  # type: str
        self.remarks_array_a = remarks_array_a  # type: str
        self.remarks_a = remarks_a  # type: str
        self.image_uri = image_uri  # type: str
        self.set_id = set_id  # type: str
        self.remarks_b = remarks_b  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageResponse, self).to_map()
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
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, project=None, new_cu=None, new_service_role=None):
        self.project = project  # type: str
        self.new_cu = new_cu  # type: int
        self.new_service_role = new_service_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.new_cu is not None:
            result['NewCU'] = self.new_cu
        if self.new_service_role is not None:
            result['NewServiceRole'] = self.new_service_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('NewCU') is not None:
            self.new_cu = m.get('NewCU')
        if m.get('NewServiceRole') is not None:
            self.new_service_role = m.get('NewServiceRole')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, type=None, request_id=None, cu=None, create_time=None, service_role=None, project=None,
                 region_id=None, modify_time=None):
        self.type = type  # type: str
        self.request_id = request_id  # type: str
        self.cu = cu  # type: int
        self.create_time = create_time  # type: str
        self.service_role = service_role  # type: str
        self.project = project  # type: str
        self.region_id = region_id  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSetRequest(TeaModel):
    def __init__(self, project=None, set_id=None, set_name=None):
        self.project = project  # type: str
        self.set_id = set_id  # type: str
        self.set_name = set_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.set_name is not None:
            result['SetName'] = self.set_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        return self


class UpdateSetResponseBody(TeaModel):
    def __init__(self, request_id=None, create_time=None, set_name=None, modify_time=None, set_id=None):
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.set_name = set_name  # type: str
        self.modify_time = modify_time  # type: str
        self.set_id = set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class UpdateSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSetResponse, self).to_map()
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
            temp_model = UpdateSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


