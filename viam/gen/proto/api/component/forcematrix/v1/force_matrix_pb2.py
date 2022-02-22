"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5proto/api/component/forcematrix/v1/force_matrix.proto\x12"proto.api.component.forcematrix.v1\x1a\x1cgoogle/api/annotations.proto"D\n\x06Matrix\x12\x12\n\x04rows\x18\x01 \x01(\rR\x04rows\x12\x12\n\x04cols\x18\x02 \x01(\rR\x04cols\x12\x12\n\x04data\x18\x03 \x03(\rR\x04data"\'\n\x11ReadMatrixRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"X\n\x12ReadMatrixResponse\x12B\n\x06matrix\x18\x01 \x01(\x0b2*.proto.api.component.forcematrix.v1.MatrixR\x06matrix"\'\n\x11DetectSlipRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"9\n\x12DetectSlipResponse\x12#\n\rslip_detected\x18\x01 \x01(\x08R\x0cslipDetected2\x84\x03\n\x12ForceMatrixService\x12\xb1\x01\n\nReadMatrix\x125.proto.api.component.forcematrix.v1.ReadMatrixRequest\x1a6.proto.api.component.forcematrix.v1.ReadMatrixResponse"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/force_matrix/{name}/matrix\x12\xb9\x01\n\nDetectSlip\x125.proto.api.component.forcematrix.v1.DetectSlipRequest\x1a6.proto.api.component.forcematrix.v1.DetectSlipResponse"<\x82\xd3\xe4\x93\x026\x124/api/v1/component/force_matrix/{name}/slip_detectionBe\n/com.viam.rdk.proto.api.component.forcematrix.v1Z2go.viam.com/rdk/proto/api/component/forcematrix/v1b\x06proto3')
_MATRIX = DESCRIPTOR.message_types_by_name['Matrix']
_READMATRIXREQUEST = DESCRIPTOR.message_types_by_name['ReadMatrixRequest']
_READMATRIXRESPONSE = DESCRIPTOR.message_types_by_name['ReadMatrixResponse']
_DETECTSLIPREQUEST = DESCRIPTOR.message_types_by_name['DetectSlipRequest']
_DETECTSLIPRESPONSE = DESCRIPTOR.message_types_by_name['DetectSlipResponse']
Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), {'DESCRIPTOR': _MATRIX, '__module__': 'proto.api.component.forcematrix.v1.force_matrix_pb2'})
_sym_db.RegisterMessage(Matrix)
ReadMatrixRequest = _reflection.GeneratedProtocolMessageType('ReadMatrixRequest', (_message.Message,), {'DESCRIPTOR': _READMATRIXREQUEST, '__module__': 'proto.api.component.forcematrix.v1.force_matrix_pb2'})
_sym_db.RegisterMessage(ReadMatrixRequest)
ReadMatrixResponse = _reflection.GeneratedProtocolMessageType('ReadMatrixResponse', (_message.Message,), {'DESCRIPTOR': _READMATRIXRESPONSE, '__module__': 'proto.api.component.forcematrix.v1.force_matrix_pb2'})
_sym_db.RegisterMessage(ReadMatrixResponse)
DetectSlipRequest = _reflection.GeneratedProtocolMessageType('DetectSlipRequest', (_message.Message,), {'DESCRIPTOR': _DETECTSLIPREQUEST, '__module__': 'proto.api.component.forcematrix.v1.force_matrix_pb2'})
_sym_db.RegisterMessage(DetectSlipRequest)
DetectSlipResponse = _reflection.GeneratedProtocolMessageType('DetectSlipResponse', (_message.Message,), {'DESCRIPTOR': _DETECTSLIPRESPONSE, '__module__': 'proto.api.component.forcematrix.v1.force_matrix_pb2'})
_sym_db.RegisterMessage(DetectSlipResponse)
_FORCEMATRIXSERVICE = DESCRIPTOR.services_by_name['ForceMatrixService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n/com.viam.rdk.proto.api.component.forcematrix.v1Z2go.viam.com/rdk/proto/api/component/forcematrix/v1'
    _FORCEMATRIXSERVICE.methods_by_name['ReadMatrix']._options = None
    _FORCEMATRIXSERVICE.methods_by_name['ReadMatrix']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/force_matrix/{name}/matrix'
    _FORCEMATRIXSERVICE.methods_by_name['DetectSlip']._options = None
    _FORCEMATRIXSERVICE.methods_by_name['DetectSlip']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/api/v1/component/force_matrix/{name}/slip_detection'
    _MATRIX._serialized_start = 123
    _MATRIX._serialized_end = 191
    _READMATRIXREQUEST._serialized_start = 193
    _READMATRIXREQUEST._serialized_end = 232
    _READMATRIXRESPONSE._serialized_start = 234
    _READMATRIXRESPONSE._serialized_end = 322
    _DETECTSLIPREQUEST._serialized_start = 324
    _DETECTSLIPREQUEST._serialized_end = 363
    _DETECTSLIPRESPONSE._serialized_start = 365
    _DETECTSLIPRESPONSE._serialized_end = 422
    _FORCEMATRIXSERVICE._serialized_start = 425
    _FORCEMATRIXSERVICE._serialized_end = 813