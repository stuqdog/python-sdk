"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'proto/rpc/examples/echo/v1/echo.proto')
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%proto/rpc/examples/echo/v1/echo.proto\x12\x1aproto.rpc.examples.echo.v1\x1a\x1cgoogle/api/annotations.proto"\'\n\x0bEchoRequest\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"(\n\x0cEchoResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"/\n\x13EchoMultipleRequest\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"0\n\x14EchoMultipleResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"+\n\x0fEchoBiDiRequest\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message",\n\x10EchoBiDiResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2\xf4\x02\n\x0bEchoService\x12\x80\x01\n\x04Echo\x12\'.proto.rpc.examples.echo.v1.EchoRequest\x1a(.proto.rpc.examples.echo.v1.EchoResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/rpc/examples/echo/v1/echo:\x01*\x12u\n\x0cEchoMultiple\x12/.proto.rpc.examples.echo.v1.EchoMultipleRequest\x1a0.proto.rpc.examples.echo.v1.EchoMultipleResponse"\x000\x01\x12k\n\x08EchoBiDi\x12+.proto.rpc.examples.echo.v1.EchoBiDiRequest\x1a,.proto.rpc.examples.echo.v1.EchoBiDiResponse"\x00(\x010\x01B.Z,go.viam.com/utils/proto/rpc/examples/echo/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.examples.echo.v1.echo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,go.viam.com/utils/proto/rpc/examples/echo/v1'
    _globals['_ECHOSERVICE'].methods_by_name['Echo']._loaded_options = None
    _globals['_ECHOSERVICE'].methods_by_name['Echo']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/rpc/examples/echo/v1/echo:\x01*'
    _globals['_ECHOREQUEST']._serialized_start = 99
    _globals['_ECHOREQUEST']._serialized_end = 138
    _globals['_ECHORESPONSE']._serialized_start = 140
    _globals['_ECHORESPONSE']._serialized_end = 180
    _globals['_ECHOMULTIPLEREQUEST']._serialized_start = 182
    _globals['_ECHOMULTIPLEREQUEST']._serialized_end = 229
    _globals['_ECHOMULTIPLERESPONSE']._serialized_start = 231
    _globals['_ECHOMULTIPLERESPONSE']._serialized_end = 279
    _globals['_ECHOBIDIREQUEST']._serialized_start = 281
    _globals['_ECHOBIDIREQUEST']._serialized_end = 324
    _globals['_ECHOBIDIRESPONSE']._serialized_start = 326
    _globals['_ECHOBIDIRESPONSE']._serialized_end = 370
    _globals['_ECHOSERVICE']._serialized_start = 373
    _globals['_ECHOSERVICE']._serialized_end = 745