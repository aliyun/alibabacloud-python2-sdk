# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CroppingSuggestion(TeaModel):
    def __init__(self, aspect_ratio=None, confidence=None, boundary=None):
        # AspectRatio
        self.aspect_ratio = aspect_ratio  # type: str
        # Confidence
        self.confidence = confidence  # type: float
        # Boundary
        self.boundary = boundary  # type: Boundary

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(CroppingSuggestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        return self


class Address(TeaModel):
    def __init__(self, language=None, address_line=None, country=None, province=None, city=None, district=None,
                 township=None):
        # Language
        self.language = language  # type: str
        # AddressLine
        self.address_line = address_line  # type: str
        # Country
        self.country = country  # type: str
        # Province
        self.province = province  # type: str
        # City
        self.city = city  # type: str
        # District
        self.district = district  # type: str
        # Township
        self.township = township  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Address, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.district is not None:
            result['District'] = self.district
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class SubtitleStream(TeaModel):
    def __init__(self, index=None, language=None, content=None):
        # Index
        self.index = index  # type: long
        # Language
        self.language = language  # type: str
        # Content
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubtitleStream, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class HeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        # Pitch
        self.pitch = pitch  # type: float
        # Roll
        self.roll = roll  # type: float
        # Yaw
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(HeadPose, self).to_map()
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


class Label(TeaModel):
    def __init__(self, language=None, label_name=None, label_level=None, label_confidence=None):
        # Language
        self.language = language  # type: str
        # LabelName
        self.label_name = label_name  # type: str
        # LabelLevel
        self.label_level = label_level  # type: long
        # LabelConfidence
        self.label_confidence = label_confidence  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(Label, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.label_level is not None:
            result['LabelLevel'] = self.label_level
        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')
        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')
        return self


class VideoStream(TeaModel):
    def __init__(self, index=None, language=None, codec_name=None, codec_long_name=None, profile=None,
                 codec_time_base=None, codec_tag_string=None, codec_tag=None, width=None, height=None, has_bframes=None,
                 sample_aspect_ratio=None, display_aspect_ratio=None, pixel_format=None, level=None, frame_rate=None,
                 average_frame_rate=None, time_base=None, start_time=None, duration=None, bitrate=None, frame_count=None):
        # Index
        self.index = index  # type: long
        # Language
        self.language = language  # type: str
        # CodecName
        self.codec_name = codec_name  # type: str
        # CodecLongName
        self.codec_long_name = codec_long_name  # type: str
        # Profile
        self.profile = profile  # type: str
        # CodecTimeBase
        self.codec_time_base = codec_time_base  # type: str
        # CodecTagString
        self.codec_tag_string = codec_tag_string  # type: str
        # CodecTag
        self.codec_tag = codec_tag  # type: str
        # Width
        self.width = width  # type: long
        # Height
        self.height = height  # type: long
        # HasBFrames
        self.has_bframes = has_bframes  # type: str
        # SampleAspectRatio
        self.sample_aspect_ratio = sample_aspect_ratio  # type: str
        # DisplayAspectRatio
        self.display_aspect_ratio = display_aspect_ratio  # type: str
        # PixelFormat
        self.pixel_format = pixel_format  # type: str
        # Level
        self.level = level  # type: long
        # FrameRate
        self.frame_rate = frame_rate  # type: float
        # AverageFrameRate
        self.average_frame_rate = average_frame_rate  # type: float
        # TimeBase
        self.time_base = time_base  # type: str
        # StartTime
        self.start_time = start_time  # type: float
        # Duration
        self.duration = duration  # type: float
        # Bitrate
        self.bitrate = bitrate  # type: long
        # FrameCount
        self.frame_count = frame_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoStream, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.level is not None:
            result['Level'] = self.level
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        return self


class Image(TeaModel):
    def __init__(self, image_width=None, image_height=None, exif=None, image_score=None, cropping_suggestions=None,
                 ocrcontents=None):
        # ImageWidth
        self.image_width = image_width  # type: long
        # ImageHeight
        self.image_height = image_height  # type: long
        # EXIF
        self.exif = exif  # type: str
        self.image_score = image_score  # type: ImageScore
        # CroppingSuggestions
        self.cropping_suggestions = cropping_suggestions  # type: list[CroppingSuggestion]
        # OCRContents
        self.ocrcontents = ocrcontents  # type: list[OCRContents]

    def validate(self):
        if self.image_score:
            self.image_score.validate()
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Image, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        return self


class Boundary(TeaModel):
    def __init__(self, width=None, height=None, left=None, top=None):
        # Width
        self.width = width  # type: long
        # Height
        self.height = height  # type: long
        # Left
        self.left = left  # type: long
        # Top
        self.top = top  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Boundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class AudioStream(TeaModel):
    def __init__(self, index=None, language=None, codec_name=None, codec_long_name=None, codec_time_base=None,
                 codec_tag_string=None, codec_tag=None, sample_format=None, sample_rate=None, channels=None, channel_layout=None,
                 time_base=None, start_time=None, duration=None, bitrate=None, lyric=None):
        # Index
        self.index = index  # type: long
        # Language
        self.language = language  # type: str
        # CodecName
        self.codec_name = codec_name  # type: str
        # CodecLongName
        self.codec_long_name = codec_long_name  # type: str
        # CodecTimeBase
        self.codec_time_base = codec_time_base  # type: str
        # CodecTagString
        self.codec_tag_string = codec_tag_string  # type: str
        # CodecTag
        self.codec_tag = codec_tag  # type: str
        # SampleFormat
        self.sample_format = sample_format  # type: str
        # SampleRate
        self.sample_rate = sample_rate  # type: long
        # Channels
        self.channels = channels  # type: long
        # ChannelLayout
        self.channel_layout = channel_layout  # type: str
        # TimeBase
        self.time_base = time_base  # type: str
        # StartTime
        self.start_time = start_time  # type: float
        # Duration
        self.duration = duration  # type: float
        # Bitrate
        self.bitrate = bitrate  # type: long
        # Lyric
        self.lyric = lyric  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AudioStream, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        return self


class ImageScore(TeaModel):
    def __init__(self, overall_quality_score=None):
        # OverallQualityScore
        self.overall_quality_score = overall_quality_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class OCRContents(TeaModel):
    def __init__(self, language=None, contents=None, confidence=None, boundary=None):
        # Language
        self.language = language  # type: str
        # Contents
        self.contents = contents  # type: str
        # Confidence
        self.confidence = confidence  # type: float
        # Boundary
        self.boundary = boundary  # type: Boundary

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(OCRContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        return self


class Face(TeaModel):
    def __init__(self, face_id=None, face_confidence=None, age=None, age_confidence=None, gender=None,
                 gender_confidence=None, emotion=None, emotion_confidence=None, face_cluster_id=None, mouth=None,
                 mouth_confidence=None, beard=None, beard_confidence=None, hat=None, hat_confidence=None, race=None,
                 race_confidence=None, mask=None, mask_confidence=None, glasses=None, glasses_confidence=None, left_eye=None,
                 left_eye_confidence=None, right_eye=None, right_eye_confidence=None, head_pose=None, boundary=None,
                 embeddings_float_32=None, embeddings_int_8=None):
        # FaceId
        self.face_id = face_id  # type: str
        # FaceConfidence
        self.face_confidence = face_confidence  # type: float
        # Age
        self.age = age  # type: long
        # AgeConfidence
        self.age_confidence = age_confidence  # type: float
        # Gender
        self.gender = gender  # type: str
        # GenderConfidence
        self.gender_confidence = gender_confidence  # type: float
        # Emotion
        self.emotion = emotion  # type: str
        # EmotionConfidence
        self.emotion_confidence = emotion_confidence  # type: float
        # FaceClusterId
        self.face_cluster_id = face_cluster_id  # type: str
        # Mouth
        self.mouth = mouth  # type: str
        # MouthConfidence
        self.mouth_confidence = mouth_confidence  # type: float
        # Beard
        self.beard = beard  # type: str
        # BeardConfidence
        self.beard_confidence = beard_confidence  # type: float
        # Hat
        self.hat = hat  # type: str
        # HatConfidence
        self.hat_confidence = hat_confidence  # type: float
        # Race
        self.race = race  # type: str
        # RaceConfidence
        self.race_confidence = race_confidence  # type: float
        # Mask
        self.mask = mask  # type: str
        # MaskConfidence
        self.mask_confidence = mask_confidence  # type: float
        # Glasses
        self.glasses = glasses  # type: str
        # GlassesConfidence
        self.glasses_confidence = glasses_confidence  # type: float
        # LeftEye
        self.left_eye = left_eye  # type: str
        # LeftEyeConfidence
        self.left_eye_confidence = left_eye_confidence  # type: float
        # RightEye
        self.right_eye = right_eye  # type: str
        # RightEyeConfidence
        self.right_eye_confidence = right_eye_confidence  # type: float
        self.head_pose = head_pose  # type: HeadPose
        self.boundary = boundary  # type: Boundary
        # EmbeddingsFloat32
        self.embeddings_float_32 = embeddings_float_32  # type: list[float]
        # EmbeddingsInt8
        self.embeddings_int_8 = embeddings_int_8  # type: list[int]

    def validate(self):
        if self.head_pose:
            self.head_pose.validate()
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(Face, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.age is not None:
            result['Age'] = self.age
        if self.age_confidence is not None:
            result['AgeConfidence'] = self.age_confidence
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.face_cluster_id is not None:
            result['FaceClusterId'] = self.face_cluster_id
        if self.mouth is not None:
            result['Mouth'] = self.mouth
        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.hat_confidence is not None:
            result['HatConfidence'] = self.hat_confidence
        if self.race is not None:
            result['Race'] = self.race
        if self.race_confidence is not None:
            result['RaceConfidence'] = self.race_confidence
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.left_eye is not None:
            result['LeftEye'] = self.left_eye
        if self.left_eye_confidence is not None:
            result['LeftEyeConfidence'] = self.left_eye_confidence
        if self.right_eye is not None:
            result['RightEye'] = self.right_eye
        if self.right_eye_confidence is not None:
            result['RightEyeConfidence'] = self.right_eye_confidence
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.embeddings_float_32 is not None:
            result['EmbeddingsFloat32'] = self.embeddings_float_32
        if self.embeddings_int_8 is not None:
            result['EmbeddingsInt8'] = self.embeddings_int_8
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('AgeConfidence') is not None:
            self.age_confidence = m.get('AgeConfidence')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('FaceClusterId') is not None:
            self.face_cluster_id = m.get('FaceClusterId')
        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')
        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('HatConfidence') is not None:
            self.hat_confidence = m.get('HatConfidence')
        if m.get('Race') is not None:
            self.race = m.get('Race')
        if m.get('RaceConfidence') is not None:
            self.race_confidence = m.get('RaceConfidence')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('LeftEye') is not None:
            self.left_eye = m.get('LeftEye')
        if m.get('LeftEyeConfidence') is not None:
            self.left_eye_confidence = m.get('LeftEyeConfidence')
        if m.get('RightEye') is not None:
            self.right_eye = m.get('RightEye')
        if m.get('RightEyeConfidence') is not None:
            self.right_eye_confidence = m.get('RightEyeConfidence')
        if m.get('HeadPose') is not None:
            temp_model = HeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('EmbeddingsFloat32') is not None:
            self.embeddings_float_32 = m.get('EmbeddingsFloat32')
        if m.get('EmbeddingsInt8') is not None:
            self.embeddings_int_8 = m.get('EmbeddingsInt8')
        return self


class File(TeaModel):
    def __init__(self, owner_id=None, project_name=None, dataset_name=None, object_type=None, object_id=None,
                 update_time=None, create_time=None, uri=None, filename=None, media_type=None, content_type=None, size=None,
                 file_hash=None, file_modified_time=None, file_create_time=None, file_access_time=None, produce_time=None,
                 lat_long=None, timezone=None, addresses=None, travel_cluster_id=None, orientation=None, faces=None,
                 face_count=None, labels=None, title=None, image_width=None, image_height=None, exif=None, image_score=None,
                 cropping_suggestions=None, ocrcontents=None, image_embeddings_float_32=None, image_embeddings_int_8=None,
                 video_width=None, video_height=None, video_taken_time=None, video_duration=None, video_bitrate=None,
                 video_start_time=None, video_streams=None, subtitles=None, video_embeddings_float_32=None,
                 video_embeddings_int_8=None, audio_taken_time=None, audio_duration=None, audio_bitrate=None, audio_streams=None,
                 artists=None, audio_covers=None, composer=None, performer=None, audio_language=None, album=None,
                 album_artist=None, audio_embeddings_float_32=None, audio_embeddings_int_8=None, document_language=None,
                 page_count=None, document_content=None, document_embeddings_float_32=None, document_embeddings_int_8=None,
                 etag=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None,
                 access_control_allow_origin=None, access_control_request_method=None, server_side_encryption_customer_algorithm=None,
                 server_side_encryption=None, server_side_data_encryption=None, server_side_encryption_key_id=None, storage_class=None,
                 object_acl=None, content_md_5=None, ossuser_meta=None, osstagging_count=None, osstagging=None,
                 ossexpiration=None, ossversion_id=None, ossdelete_marker=None, ossobject_type=None, custom_id=None,
                 custom_labels=None):
        # OwnerId
        self.owner_id = owner_id  # type: str
        # ProjectName
        self.project_name = project_name  # type: str
        # DatasetName
        self.dataset_name = dataset_name  # type: str
        # ObjectType
        self.object_type = object_type  # type: str
        # ObjectId
        self.object_id = object_id  # type: str
        # UpdateTime
        self.update_time = update_time  # type: str
        # CreateTime
        self.create_time = create_time  # type: str
        # URI
        self.uri = uri  # type: str
        # Filename
        self.filename = filename  # type: str
        # MediaType
        self.media_type = media_type  # type: str
        # ContentType
        self.content_type = content_type  # type: str
        # Size
        self.size = size  # type: long
        # FileHash
        self.file_hash = file_hash  # type: str
        # FileModifiedTime
        self.file_modified_time = file_modified_time  # type: str
        # FileCreateTime
        self.file_create_time = file_create_time  # type: str
        # FileAccessTime
        self.file_access_time = file_access_time  # type: str
        # ProduceTime
        self.produce_time = produce_time  # type: str
        # LatLong
        self.lat_long = lat_long  # type: str
        # Timezone
        self.timezone = timezone  # type: str
        # Addresses
        self.addresses = addresses  # type: list[Address]
        # TravelClusterId
        self.travel_cluster_id = travel_cluster_id  # type: str
        # Orientation
        self.orientation = orientation  # type: str
        # Faces
        self.faces = faces  # type: list[Face]
        # FaceCount
        self.face_count = face_count  # type: long
        # Labels
        self.labels = labels  # type: list[Label]
        # Title
        self.title = title  # type: str
        # ImageWidth
        self.image_width = image_width  # type: long
        # ImageHeight
        self.image_height = image_height  # type: long
        # EXIF
        self.exif = exif  # type: str
        self.image_score = image_score  # type: ImageScore
        # CroppingSuggestions
        self.cropping_suggestions = cropping_suggestions  # type: list[CroppingSuggestion]
        # OCRContents
        self.ocrcontents = ocrcontents  # type: list[OCRContents]
        # ImageEmbeddingsFloat32
        self.image_embeddings_float_32 = image_embeddings_float_32  # type: list[float]
        # ImageEmbeddingsInt8
        self.image_embeddings_int_8 = image_embeddings_int_8  # type: list[int]
        # VideoWidth
        self.video_width = video_width  # type: long
        # VideoHeight
        self.video_height = video_height  # type: long
        # VideoTakenTime
        self.video_taken_time = video_taken_time  # type: str
        # VideoDuration
        self.video_duration = video_duration  # type: float
        # VideoBitrate
        self.video_bitrate = video_bitrate  # type: long
        # VideoStartTime
        self.video_start_time = video_start_time  # type: float
        # VideoStreams
        self.video_streams = video_streams  # type: list[VideoStream]
        # Subtitles
        self.subtitles = subtitles  # type: list[SubtitleStream]
        # VideoEmbeddingsFloat32
        self.video_embeddings_float_32 = video_embeddings_float_32  # type: list[float]
        # VideoEmbeddingsInt8
        self.video_embeddings_int_8 = video_embeddings_int_8  # type: list[int]
        # AudioTakenTime
        self.audio_taken_time = audio_taken_time  # type: str
        # AudioDuration
        self.audio_duration = audio_duration  # type: float
        # AudioBitrate
        self.audio_bitrate = audio_bitrate  # type: float
        # AudioStreams
        self.audio_streams = audio_streams  # type: list[AudioStream]
        # Artists
        self.artists = artists  # type: list[str]
        # AudioCovers
        self.audio_covers = audio_covers  # type: list[Image]
        # Composer
        self.composer = composer  # type: str
        # Performer
        self.performer = performer  # type: str
        # AudioLanguage
        self.audio_language = audio_language  # type: str
        # Album
        self.album = album  # type: str
        # AlbumArtist
        self.album_artist = album_artist  # type: str
        # AudioEmbeddingsFloat32
        self.audio_embeddings_float_32 = audio_embeddings_float_32  # type: list[float]
        # AudioEmbeddingsInt8
        self.audio_embeddings_int_8 = audio_embeddings_int_8  # type: list[int]
        # DocumentLanguage
        self.document_language = document_language  # type: str
        # PageCount
        self.page_count = page_count  # type: long
        # DocumentContent
        self.document_content = document_content  # type: str
        # DocumentEmbeddingsFloat32
        self.document_embeddings_float_32 = document_embeddings_float_32  # type: list[float]
        # DocumentEmbeddingsInt8
        self.document_embeddings_int_8 = document_embeddings_int_8  # type: list[int]
        # ETag
        self.etag = etag  # type: str
        # CacheControl
        self.cache_control = cache_control  # type: str
        # ContentDisposition
        self.content_disposition = content_disposition  # type: str
        # ContentEncoding
        self.content_encoding = content_encoding  # type: str
        # ContentLanguage
        self.content_language = content_language  # type: str
        # AccessControlAllowOrigin
        self.access_control_allow_origin = access_control_allow_origin  # type: str
        # AccessControlRequestMethod
        self.access_control_request_method = access_control_request_method  # type: str
        # ServerSideEncryptionCustomerAlgorithm
        self.server_side_encryption_customer_algorithm = server_side_encryption_customer_algorithm  # type: str
        # ServerSideEncryption
        self.server_side_encryption = server_side_encryption  # type: str
        # ServerSideDataEncryption
        self.server_side_data_encryption = server_side_data_encryption  # type: str
        # ServerSideEncryptionKeyId
        self.server_side_encryption_key_id = server_side_encryption_key_id  # type: str
        # StorageClass
        self.storage_class = storage_class  # type: str
        # ObjectACL
        self.object_acl = object_acl  # type: str
        # ContentMd5
        self.content_md_5 = content_md_5  # type: str
        # OSSUserMeta
        self.ossuser_meta = ossuser_meta  # type: dict[str, any]
        # OSSTaggingCount
        self.osstagging_count = osstagging_count  # type: long
        # OSSTagging
        self.osstagging = osstagging  # type: dict[str, any]
        # OSSExpiration
        self.ossexpiration = ossexpiration  # type: str
        # OSSVersionId
        self.ossversion_id = ossversion_id  # type: str
        # OSSDeleteMarker
        self.ossdelete_marker = ossdelete_marker  # type: str
        # OSSObjectType
        self.ossobject_type = ossobject_type  # type: str
        # CustomId
        self.custom_id = custom_id  # type: str
        # CustomLabels
        self.custom_labels = custom_labels  # type: dict[str, any]

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.audio_covers:
            for k in self.audio_covers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(File, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.size is not None:
            result['Size'] = self.size
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_modified_time is not None:
            result['FileModifiedTime'] = self.file_modified_time
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_access_time is not None:
            result['FileAccessTime'] = self.file_access_time
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.travel_cluster_id is not None:
            result['TravelClusterId'] = self.travel_cluster_id
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.image_embeddings_float_32 is not None:
            result['ImageEmbeddingsFloat32'] = self.image_embeddings_float_32
        if self.image_embeddings_int_8 is not None:
            result['ImageEmbeddingsInt8'] = self.image_embeddings_int_8
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.video_taken_time is not None:
            result['VideoTakenTime'] = self.video_taken_time
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_start_time is not None:
            result['VideoStartTime'] = self.video_start_time
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.video_embeddings_float_32 is not None:
            result['VideoEmbeddingsFloat32'] = self.video_embeddings_float_32
        if self.video_embeddings_int_8 is not None:
            result['VideoEmbeddingsInt8'] = self.video_embeddings_int_8
        if self.audio_taken_time is not None:
            result['AudioTakenTime'] = self.audio_taken_time
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.audio_bitrate is not None:
            result['AudioBitrate'] = self.audio_bitrate
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.artists is not None:
            result['Artists'] = self.artists
        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k in self.audio_covers:
                result['AudioCovers'].append(k.to_map() if k else None)
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.audio_language is not None:
            result['AudioLanguage'] = self.audio_language
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.audio_embeddings_float_32 is not None:
            result['AudioEmbeddingsFloat32'] = self.audio_embeddings_float_32
        if self.audio_embeddings_int_8 is not None:
            result['AudioEmbeddingsInt8'] = self.audio_embeddings_int_8
        if self.document_language is not None:
            result['DocumentLanguage'] = self.document_language
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.document_content is not None:
            result['DocumentContent'] = self.document_content
        if self.document_embeddings_float_32 is not None:
            result['DocumentEmbeddingsFloat32'] = self.document_embeddings_float_32
        if self.document_embeddings_int_8 is not None:
            result['DocumentEmbeddingsInt8'] = self.document_embeddings_int_8
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.cache_control is not None:
            result['CacheControl'] = self.cache_control
        if self.content_disposition is not None:
            result['ContentDisposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_language is not None:
            result['ContentLanguage'] = self.content_language
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_control_request_method is not None:
            result['AccessControlRequestMethod'] = self.access_control_request_method
        if self.server_side_encryption_customer_algorithm is not None:
            result['ServerSideEncryptionCustomerAlgorithm'] = self.server_side_encryption_customer_algorithm
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.server_side_data_encryption is not None:
            result['ServerSideDataEncryption'] = self.server_side_data_encryption
        if self.server_side_encryption_key_id is not None:
            result['ServerSideEncryptionKeyId'] = self.server_side_encryption_key_id
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.object_acl is not None:
            result['ObjectACL'] = self.object_acl
        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5
        if self.ossuser_meta is not None:
            result['OSSUserMeta'] = self.ossuser_meta
        if self.osstagging_count is not None:
            result['OSSTaggingCount'] = self.osstagging_count
        if self.osstagging is not None:
            result['OSSTagging'] = self.osstagging
        if self.ossexpiration is not None:
            result['OSSExpiration'] = self.ossexpiration
        if self.ossversion_id is not None:
            result['OSSVersionId'] = self.ossversion_id
        if self.ossdelete_marker is not None:
            result['OSSDeleteMarker'] = self.ossdelete_marker
        if self.ossobject_type is not None:
            result['OSSObjectType'] = self.ossobject_type
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileModifiedTime') is not None:
            self.file_modified_time = m.get('FileModifiedTime')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileAccessTime') is not None:
            self.file_access_time = m.get('FileAccessTime')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('TravelClusterId') is not None:
            self.travel_cluster_id = m.get('TravelClusterId')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = Face()
                self.faces.append(temp_model.from_map(k))
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('ImageEmbeddingsFloat32') is not None:
            self.image_embeddings_float_32 = m.get('ImageEmbeddingsFloat32')
        if m.get('ImageEmbeddingsInt8') is not None:
            self.image_embeddings_int_8 = m.get('ImageEmbeddingsInt8')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('VideoTakenTime') is not None:
            self.video_taken_time = m.get('VideoTakenTime')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoStartTime') is not None:
            self.video_start_time = m.get('VideoStartTime')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('VideoEmbeddingsFloat32') is not None:
            self.video_embeddings_float_32 = m.get('VideoEmbeddingsFloat32')
        if m.get('VideoEmbeddingsInt8') is not None:
            self.video_embeddings_int_8 = m.get('VideoEmbeddingsInt8')
        if m.get('AudioTakenTime') is not None:
            self.audio_taken_time = m.get('AudioTakenTime')
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('AudioBitrate') is not None:
            self.audio_bitrate = m.get('AudioBitrate')
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Artists') is not None:
            self.artists = m.get('Artists')
        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k in m.get('AudioCovers'):
                temp_model = Image()
                self.audio_covers.append(temp_model.from_map(k))
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('AudioLanguage') is not None:
            self.audio_language = m.get('AudioLanguage')
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('AudioEmbeddingsFloat32') is not None:
            self.audio_embeddings_float_32 = m.get('AudioEmbeddingsFloat32')
        if m.get('AudioEmbeddingsInt8') is not None:
            self.audio_embeddings_int_8 = m.get('AudioEmbeddingsInt8')
        if m.get('DocumentLanguage') is not None:
            self.document_language = m.get('DocumentLanguage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('DocumentContent') is not None:
            self.document_content = m.get('DocumentContent')
        if m.get('DocumentEmbeddingsFloat32') is not None:
            self.document_embeddings_float_32 = m.get('DocumentEmbeddingsFloat32')
        if m.get('DocumentEmbeddingsInt8') is not None:
            self.document_embeddings_int_8 = m.get('DocumentEmbeddingsInt8')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('CacheControl') is not None:
            self.cache_control = m.get('CacheControl')
        if m.get('ContentDisposition') is not None:
            self.content_disposition = m.get('ContentDisposition')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentLanguage') is not None:
            self.content_language = m.get('ContentLanguage')
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessControlRequestMethod') is not None:
            self.access_control_request_method = m.get('AccessControlRequestMethod')
        if m.get('ServerSideEncryptionCustomerAlgorithm') is not None:
            self.server_side_encryption_customer_algorithm = m.get('ServerSideEncryptionCustomerAlgorithm')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('ServerSideDataEncryption') is not None:
            self.server_side_data_encryption = m.get('ServerSideDataEncryption')
        if m.get('ServerSideEncryptionKeyId') is not None:
            self.server_side_encryption_key_id = m.get('ServerSideEncryptionKeyId')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('ObjectACL') is not None:
            self.object_acl = m.get('ObjectACL')
        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')
        if m.get('OSSUserMeta') is not None:
            self.ossuser_meta = m.get('OSSUserMeta')
        if m.get('OSSTaggingCount') is not None:
            self.osstagging_count = m.get('OSSTaggingCount')
        if m.get('OSSTagging') is not None:
            self.osstagging = m.get('OSSTagging')
        if m.get('OSSExpiration') is not None:
            self.ossexpiration = m.get('OSSExpiration')
        if m.get('OSSVersionId') is not None:
            self.ossversion_id = m.get('OSSVersionId')
        if m.get('OSSDeleteMarker') is not None:
            self.ossdelete_marker = m.get('OSSDeleteMarker')
        if m.get('OSSObjectType') is not None:
            self.ossobject_type = m.get('OSSObjectType')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        return self


class SimpleQuery(TeaModel):
    def __init__(self, field=None, value=None, operation=None, sub_queries=None):
        # 需要查询的字段名
        self.field = field  # type: str
        # 需要查询的字段值
        self.value = value  # type: str
        # 运算符
        self.operation = operation  # type: str
        # 由 SimpleQuery 结构体组成的子查询数组
        self.sub_queries = sub_queries  # type: list[SimpleQuery]

    def validate(self):
        if self.sub_queries:
            for k in self.sub_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.value is not None:
            result['Value'] = self.value
        if self.operation is not None:
            result['Operation'] = self.operation
        result['SubQueries'] = []
        if self.sub_queries is not None:
            for k in self.sub_queries:
                result['SubQueries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        self.sub_queries = []
        if m.get('SubQueries') is not None:
            for k in m.get('SubQueries'):
                temp_model = SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k))
        return self


class BatchDeleteFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uris=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uris = uris  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchDeleteFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uris_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uris_shrink = uris_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchDeleteFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaResponseBody, self).to_map()
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


class BatchDeleteFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDeleteFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteFileMetaResponse, self).to_map()
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
            temp_model = BatchDeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uris=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uris = uris  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchGetFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uris_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uris_shrink = uris_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchGetFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, files=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.files = files  # type: list[File]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        return self


class BatchGetFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchGetFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetFileMetaResponse, self).to_map()
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
            temp_model = BatchGetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchIndexFileMetaRequestFiles(TeaModel):
    def __init__(self, uri=None, custom_labels=None):
        self.uri = uri  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchIndexFileMetaRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        return self


class BatchIndexFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, files=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[BatchIndexFileMetaRequestFiles]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchIndexFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = BatchIndexFileMetaRequestFiles()
                self.files.append(temp_model.from_map(k))
        return self


class BatchIndexFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, files_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchIndexFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        return self


class BatchIndexFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchIndexFileMetaResponseBody, self).to_map()
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


class BatchIndexFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchIndexFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchIndexFileMetaResponse, self).to_map()
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
            temp_model = BatchIndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFileMetaRequestFiles(TeaModel):
    def __init__(self, uri=None, custom_labels=None):
        self.uri = uri  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateFileMetaRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        return self


class BatchUpdateFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, files=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[BatchUpdateFileMetaRequestFiles]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUpdateFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = BatchUpdateFileMetaRequestFiles()
                self.files.append(temp_model.from_map(k))
        return self


class BatchUpdateFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, files_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        return self


class BatchUpdateFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateFileMetaResponseBody, self).to_map()
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


class BatchUpdateFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUpdateFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUpdateFileMetaResponse, self).to_map()
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
            temp_model = BatchUpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        # ProjectName
        self.project_name = project_name  # type: str
        # DatasetName
        self.dataset_name = dataset_name  # type: str
        # URI
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBindingResponse, self).to_map()
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
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, description=None, template_id=None,
                 dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 数据集名称
        self.dataset_name = dataset_name  # type: str
        # 对数据集的描述
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(self, request_id=None, project_name=None, dataset_name=None, create_time=None, description=None):
        # 请求 ID
        self.request_id = request_id  # type: str
        # 项目名称
        self.project_name = project_name  # type: str
        # 数据集名称
        self.dataset_name = dataset_name  # type: str
        # 数据集创建时间
        self.create_time = create_time  # type: long
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDatasetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDatasetResponse, self).to_map()
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
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, project_name=None, description=None, service_role=None, template_id=None, project_qps=None,
                 project_tps=None, project_max_dataset_count=None, dataset_max_ossbind_count=None,
                 dataset_max_file_count=None, dataset_max_entity_count=None, dataset_max_relation_count=None,
                 dataset_max_total_file_size=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 项目描述
        self.description = description  # type: str
        # 服务角色
        self.service_role = service_role  # type: str
        self.template_id = template_id  # type: str
        self.project_qps = project_qps  # type: long
        self.project_tps = project_tps  # type: long
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.description is not None:
            result['Description'] = self.description
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.project_qps is not None:
            result['ProjectQPS'] = self.project_qps
        if self.project_tps is not None:
            result['ProjectTPS'] = self.project_tps
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ProjectQPS') is not None:
            self.project_qps = m.get('ProjectQPS')
        if m.get('ProjectTPS') is not None:
            self.project_tps = m.get('ProjectTPS')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, project_name=None, create_time=None, request_id=None, description=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 项目创建时间
        self.create_time = create_time  # type: long
        # 本次请求的唯一 ID
        self.request_id = request_id  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        # A short description of struct
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBindingResponse, self).to_map()
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
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatasetResponseBody, self).to_map()
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


class DeleteDatasetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDatasetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatasetResponse, self).to_map()
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
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileMetaResponseBody, self).to_map()
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


class DeleteFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileMetaResponse, self).to_map()
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
            temp_model = DeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, project_name=None):
        # 项目名称
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 本次请求的唯一 ID
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


class FuzzyQueryRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, project_name=None, dataset_name=None, query=None):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: long
        # 项目名称
        self.project_name = project_name  # type: str
        # Dataset 名称
        self.dataset_name = dataset_name  # type: str
        # 用于搜索的字符串
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FuzzyQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class FuzzyQueryResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, files=None):
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # 本次请求的唯一 Id
        self.request_id = request_id  # type: str
        self.files = files  # type: list[File]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FuzzyQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        return self


class FuzzyQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FuzzyQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FuzzyQueryResponse, self).to_map()
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
            temp_model = FuzzyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetBindingResponseBodyBinding(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, state=None, phase=None, reason=None,
                 create_time=None, update_time=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.state = state  # type: str
        self.phase = phase  # type: str
        self.reason = reason  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBindingResponseBodyBinding, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.state is not None:
            result['State'] = self.state
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetBindingResponseBody(TeaModel):
    def __init__(self, request_id=None, binding=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.binding = binding  # type: GetBindingResponseBodyBinding

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super(GetBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Binding') is not None:
            temp_model = GetBindingResponseBodyBinding()
            self.binding = temp_model.from_map(m['Binding'])
        return self


class GetBindingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBindingResponse, self).to_map()
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
            temp_model = GetBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(self, request_id=None, project_name=None, dataset_name=None, template_id=None, create_time=None,
                 update_time=None, description=None, dataset_max_ossbind_count=None, dataset_max_file_count=None,
                 dataset_max_entity_count=None, dataset_max_relation_count=None, dataset_max_total_file_size=None, bind_count=None,
                 file_count=None, total_file_size=None):
        self.request_id = request_id  # type: str
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.template_id = template_id  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long
        self.description = description  # type: str
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.bind_count = bind_count  # type: long
        self.file_count = file_count  # type: long
        self.total_file_size = total_file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDatasetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDatasetResponse, self).to_map()
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None, files=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # File list.
        self.files = files  # type: list[File]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        return self


class GetFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileMetaResponse, self).to_map()
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
            temp_model = GetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileSignedURIRequest(TeaModel):
    def __init__(self, project_name=None, uri=None):
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileSignedURIRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileSignedURIResponseBody(TeaModel):
    def __init__(self, request_id=None, uri=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 签名地址
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileSignedURIResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileSignedURIResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFileSignedURIResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileSignedURIResponse, self).to_map()
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
            temp_model = GetFileSignedURIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(self, project_name=None):
        # 项目名称
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, project_name=None, description=None, service_role=None, template_id=None, create_time=None,
                 update_time=None, project_qps=None, project_tps=None, project_max_dataset_count=None,
                 dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, dataset_count=None, file_count=None, total_file_size=None,
                 request_id=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 项目描述
        self.description = description  # type: str
        # 服务角色
        self.service_role = service_role  # type: str
        # 工作流
        self.template_id = template_id  # type: str
        # 项目创建时间
        self.create_time = create_time  # type: long
        # 项目修改时间
        self.update_time = update_time  # type: long
        # 项目QPS
        self.project_qps = project_qps  # type: long
        # 项目TPS
        self.project_tps = project_tps  # type: long
        # 最大媒体集数量
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        # 当前项目每个媒体集最大绑定数
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        # 当前项目每个媒体集最大文件数
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        # 当前项目每个媒体集最大实体数
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        # 当前项目每个媒体集最大关系数
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        # 当前项目每个媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        # 媒体集数量
        self.dataset_count = dataset_count  # type: long
        # 项目当前文件数量
        self.file_count = file_count  # type: long
        # 项目当前文件总大小
        self.total_file_size = total_file_size  # type: long
        # 本次请求的唯一 ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.description is not None:
            result['Description'] = self.description
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.project_qps is not None:
            result['ProjectQPS'] = self.project_qps
        if self.project_tps is not None:
            result['ProjectTPS'] = self.project_tps
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ProjectQPS') is not None:
            self.project_qps = m.get('ProjectQPS')
        if m.get('ProjectTPS') is not None:
            self.project_tps = m.get('ProjectTPS')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class IndexFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, custom_labels=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        return self


class IndexFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, custom_labels_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        return self


class IndexFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexFileMetaResponseBody, self).to_map()
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


class IndexFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: IndexFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IndexFileMetaResponse, self).to_map()
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
            temp_model = IndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, max_results=None, next_token=None):
        # A short description of struct
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListBindingsResponseBodyBindingsBinding(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, state=None, phase=None, reason=None,
                 create_time=None, update_time=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.state = state  # type: str
        self.phase = phase  # type: str
        self.reason = reason  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingsResponseBodyBindingsBinding, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.state is not None:
            result['State'] = self.state
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListBindingsResponseBodyBindings(TeaModel):
    def __init__(self, binding=None):
        self.binding = binding  # type: ListBindingsResponseBodyBindingsBinding

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super(ListBindingsResponseBodyBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = ListBindingsResponseBodyBindingsBinding()
            self.binding = temp_model.from_map(m['Binding'])
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(self, request_id=None, next_token=None, bindings=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.next_token = next_token  # type: str
        self.bindings = bindings  # type: list[ListBindingsResponseBodyBindings]

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListBindingsResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class ListBindingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBindingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindingsResponse, self).to_map()
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
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(self, project_name=None, max_results=None, next_token=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 返回最大个数
        self.max_results = max_results  # type: long
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListDatasetsResponseBodyDatasets(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, workflow=None, create_time=None, update_time=None,
                 description=None, dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, bind_count=None):
        # ProjectName
        self.project_name = project_name  # type: str
        # DatasetName
        self.dataset_name = dataset_name  # type: str
        self.workflow = workflow  # type: str
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long
        self.description = description  # type: str
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.bind_count = bind_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasetsResponseBodyDatasets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.workflow is not None:
            result['Workflow'] = self.workflow
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Workflow') is not None:
            self.workflow = m.get('Workflow')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(self, request_id=None, next_token=None, datasets=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.next_token = next_token  # type: str
        # Responses
        self.datasets = datasets  # type: list[ListDatasetsResponseBodyDatasets]

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDatasetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = ListDatasetsResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k))
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDatasetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDatasetsResponse, self).to_map()
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None):
        # 返回结果的最大个数
        self.max_results = max_results  # type: long
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
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


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(self, project_name=None, service_role=None, workflow=None, description=None, create_time=None,
                 update_time=None, project_qps=None, project_tps=None, project_max_dataset_count=None,
                 dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, dataset_count=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 服务角色
        self.service_role = service_role  # type: str
        # 工作流
        self.workflow = workflow  # type: str
        # 项目描述
        self.description = description  # type: str
        # 项目创建时间
        self.create_time = create_time  # type: long
        # 项目上次修改时间
        self.update_time = update_time  # type: long
        # 项目QPS
        self.project_qps = project_qps  # type: long
        # 项目TPS
        self.project_tps = project_tps  # type: long
        # 最大媒体集数
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        # 项目下每个媒体集最多绑定数
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        # 项目下每个媒体集最大文件数量
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        # 项目下每个媒体集最大实体数
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        # 项目下每个媒体集最大关系数
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        # 项目下每个媒体集最大文件总大小
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        # 媒体集数量
        self.dataset_count = dataset_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.workflow is not None:
            result['Workflow'] = self.workflow
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.project_qps is not None:
            result['ProjectQPS'] = self.project_qps
        if self.project_tps is not None:
            result['ProjectTPS'] = self.project_tps
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Workflow') is not None:
            self.workflow = m.get('Workflow')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ProjectQPS') is not None:
            self.project_qps = m.get('ProjectQPS')
        if m.get('ProjectTPS') is not None:
            self.project_tps = m.get('ProjectTPS')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, next_token=None, projects=None, request_id=None):
        # 当总结果个数大于MaxResults时，用于翻页的token
        self.next_token = next_token  # type: str
        # 由ProjectItem组成的数组
        self.projects = projects  # type: list[ListProjectsResponseBodyProjects]
        # 本次请求的唯一 ID
        self.request_id = request_id  # type: str

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ResumeBindingRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class ResumeBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeBindingResponseBody, self).to_map()
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


class ResumeBindingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeBindingResponse, self).to_map()
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
            temp_model = ResumeBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SimpleQueryRequestAggregations(TeaModel):
    def __init__(self, field=None, operation=None):
        # 聚合字段的字段名
        self.field = field  # type: str
        # 聚合字段的聚合操作符
        self.operation = operation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryRequestAggregations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class SimpleQueryRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, project_name=None, dataset_name=None, query=None,
                 sort=None, order=None, aggregations=None):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        # 项目名称
        self.project_name = project_name  # type: str
        # Dataset 名称
        self.dataset_name = dataset_name  # type: str
        self.query = query  # type: SimpleQuery
        # 排序方式，默认 DESC
        self.sort = sort  # type: str
        # 排序字段
        self.order = order  # type: str
        # 聚合字段
        self.aggregations = aggregations  # type: list[SimpleQueryRequestAggregations]

    def validate(self):
        if self.query:
            self.query.validate()
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.query is not None:
            result['Query'] = self.query.to_map()
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.order is not None:
            result['Order'] = self.order
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Query') is not None:
            temp_model = SimpleQuery()
            self.query = temp_model.from_map(m['Query'])
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryRequestAggregations()
                self.aggregations.append(temp_model.from_map(k))
        return self


class SimpleQueryShrinkRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, project_name=None, dataset_name=None, query_shrink=None,
                 sort=None, order=None, aggregations_shrink=None):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        # 项目名称
        self.project_name = project_name  # type: str
        # Dataset 名称
        self.dataset_name = dataset_name  # type: str
        self.query_shrink = query_shrink  # type: str
        # 排序方式，默认 DESC
        self.sort = sort  # type: str
        # 排序字段
        self.order = order  # type: str
        # 聚合字段
        self.aggregations_shrink = aggregations_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.order is not None:
            result['Order'] = self.order
        if self.aggregations_shrink is not None:
            result['Aggregations'] = self.aggregations_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Aggregations') is not None:
            self.aggregations_shrink = m.get('Aggregations')
        return self


class SimpleQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(self, value=None, count=None):
        # 分组聚合的值
        self.value = value  # type: str
        # 分组聚合的计数
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryResponseBodyAggregationsGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class SimpleQueryResponseBodyAggregations(TeaModel):
    def __init__(self, field=None, operation=None, value=None, groups=None):
        # 聚合字段名
        self.field = field  # type: str
        # 聚合字段的聚合操作符
        self.operation = operation  # type: str
        # 聚合的统计结果
        self.value = value  # type: float
        # 分组聚合的结果
        self.groups = groups  # type: list[SimpleQueryResponseBodyAggregationsGroups]

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQueryResponseBodyAggregations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class SimpleQueryResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, files=None, aggregations=None):
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # 本次请求的唯一 Id
        self.request_id = request_id  # type: str
        # 文件列表
        self.files = files  # type: list[File]
        # 聚合字段的字段名
        self.aggregations = aggregations  # type: list[SimpleQueryResponseBodyAggregations]

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k))
        return self


class SimpleQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SimpleQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SimpleQueryResponse, self).to_map()
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
            temp_model = SimpleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBindingRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, reason=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class StopBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopBindingResponseBody, self).to_map()
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


class StopBindingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopBindingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopBindingResponse, self).to_map()
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
            temp_model = StopBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, description=None, template_id=None,
                 dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, reset_items=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.reset_items = reset_items  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.reset_items is not None:
            result['ResetItems'] = self.reset_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('ResetItems') is not None:
            self.reset_items = m.get('ResetItems')
        return self


class UpdateDatasetShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, description=None, template_id=None,
                 dataset_max_ossbind_count=None, dataset_max_file_count=None, dataset_max_entity_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, reset_items_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.reset_items_shrink = reset_items_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasetShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.reset_items_shrink is not None:
            result['ResetItems'] = self.reset_items_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('ResetItems') is not None:
            self.reset_items_shrink = m.get('ResetItems')
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasetResponseBody, self).to_map()
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


class UpdateDatasetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDatasetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDatasetResponse, self).to_map()
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
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileMetaRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, custom_labels=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        return self


class UpdateFileMetaShrinkRequest(TeaModel):
    def __init__(self, project_name=None, dataset_name=None, uri=None, custom_labels_shrink=None):
        self.project_name = project_name  # type: str
        self.dataset_name = dataset_name  # type: str
        self.uri = uri  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.uri is not None:
            result['URI'] = self.uri
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        return self


class UpdateFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileMetaResponseBody, self).to_map()
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


class UpdateFileMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFileMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFileMetaResponse, self).to_map()
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
            temp_model = UpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, project_name=None, service_role=None, description=None, template_id=None, project_qps=None,
                 project_tps=None, project_max_dataset_count=None, dataset_max_ossbind_count=None,
                 dataset_max_file_count=None, dataset_max_entity_count=None, dataset_max_relation_count=None, reset_items=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 服务角色
        self.service_role = service_role  # type: str
        # 项目描述
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.project_qps = project_qps  # type: long
        self.project_tps = project_tps  # type: long
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.reset_items = reset_items  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.project_qps is not None:
            result['ProjectQPS'] = self.project_qps
        if self.project_tps is not None:
            result['ProjectTPS'] = self.project_tps
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.reset_items is not None:
            result['ResetItems'] = self.reset_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ProjectQPS') is not None:
            self.project_qps = m.get('ProjectQPS')
        if m.get('ProjectTPS') is not None:
            self.project_tps = m.get('ProjectTPS')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('ResetItems') is not None:
            self.reset_items = m.get('ResetItems')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(self, project_name=None, service_role=None, description=None, template_id=None, project_qps=None,
                 project_tps=None, project_max_dataset_count=None, dataset_max_ossbind_count=None,
                 dataset_max_file_count=None, dataset_max_entity_count=None, dataset_max_relation_count=None, reset_items_shrink=None):
        # 项目名称
        self.project_name = project_name  # type: str
        # 服务角色
        self.service_role = service_role  # type: str
        # 项目描述
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.project_qps = project_qps  # type: long
        self.project_tps = project_tps  # type: long
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.dataset_max_ossbind_count = dataset_max_ossbind_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.reset_items_shrink = reset_items_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.project_qps is not None:
            result['ProjectQPS'] = self.project_qps
        if self.project_tps is not None:
            result['ProjectTPS'] = self.project_tps
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.dataset_max_ossbind_count is not None:
            result['DatasetMaxOSSBindCount'] = self.dataset_max_ossbind_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.reset_items_shrink is not None:
            result['ResetItems'] = self.reset_items_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ProjectQPS') is not None:
            self.project_qps = m.get('ProjectQPS')
        if m.get('ProjectTPS') is not None:
            self.project_tps = m.get('ProjectTPS')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('DatasetMaxOSSBindCount') is not None:
            self.dataset_max_ossbind_count = m.get('DatasetMaxOSSBindCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('ResetItems') is not None:
            self.reset_items_shrink = m.get('ResetItems')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
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


