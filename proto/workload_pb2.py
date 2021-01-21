# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='workload.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\032io.spiffe.workloadapi.grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eworkload.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x11\n\x0fX509SVIDRequest\"\xb6\x01\n\x10X509SVIDResponse\x12\x18\n\x05svids\x18\x01 \x03(\x0b\x32\t.X509SVID\x12\x0b\n\x03\x63rl\x18\x02 \x03(\x0c\x12\x42\n\x11\x66\x65\x64\x65rated_bundles\x18\x03 \x03(\x0b\x32\'.X509SVIDResponse.FederatedBundlesEntry\x1a\x37\n\x15\x46\x65\x64\x65ratedBundlesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"W\n\x08X509SVID\x12\x11\n\tspiffe_id\x18\x01 \x01(\t\x12\x11\n\tx509_svid\x18\x02 \x01(\x0c\x12\x15\n\rx509_svid_key\x18\x03 \x01(\x0c\x12\x0e\n\x06\x62undle\x18\x04 \x01(\x0c\"*\n\x07JWTSVID\x12\x11\n\tspiffe_id\x18\x01 \x01(\t\x12\x0c\n\x04svid\x18\x02 \x01(\t\"5\n\x0eJWTSVIDRequest\x12\x10\n\x08\x61udience\x18\x01 \x03(\t\x12\x11\n\tspiffe_id\x18\x02 \x01(\t\"*\n\x0fJWTSVIDResponse\x12\x17\n\x05svids\x18\x01 \x03(\x0b\x32\x08.JWTSVID\"\x13\n\x11JWTBundlesRequest\"w\n\x12JWTBundlesResponse\x12\x31\n\x07\x62undles\x18\x01 \x03(\x0b\x32 .JWTBundlesResponse.BundlesEntry\x1a.\n\x0c\x42undlesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"8\n\x16ValidateJWTSVIDRequest\x12\x10\n\x08\x61udience\x18\x01 \x01(\t\x12\x0c\n\x04svid\x18\x02 \x01(\t\"U\n\x17ValidateJWTSVIDResponse\x12\x11\n\tspiffe_id\x18\x01 \x01(\t\x12\'\n\x06\x63laims\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct2\x82\x02\n\x11SpiffeWorkloadAPI\x12\x31\n\x0c\x46\x65tchJWTSVID\x12\x0f.JWTSVIDRequest\x1a\x10.JWTSVIDResponse\x12<\n\x0f\x46\x65tchJWTBundles\x12\x12.JWTBundlesRequest\x1a\x13.JWTBundlesResponse0\x01\x12\x44\n\x0fValidateJWTSVID\x12\x17.ValidateJWTSVIDRequest\x1a\x18.ValidateJWTSVIDResponse\x12\x36\n\rFetchX509SVID\x12\x10.X509SVIDRequest\x1a\x11.X509SVIDResponse0\x01\x42\x1c\n\x1aio.spiffe.workloadapi.grpcb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_X509SVIDREQUEST = _descriptor.Descriptor(
  name='X509SVIDRequest',
  full_name='X509SVIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=65,
)


_X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY = _descriptor.Descriptor(
  name='FederatedBundlesEntry',
  full_name='X509SVIDResponse.FederatedBundlesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='X509SVIDResponse.FederatedBundlesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='X509SVIDResponse.FederatedBundlesEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=250,
)

_X509SVIDRESPONSE = _descriptor.Descriptor(
  name='X509SVIDResponse',
  full_name='X509SVIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='svids', full_name='X509SVIDResponse.svids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crl', full_name='X509SVIDResponse.crl', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='federated_bundles', full_name='X509SVIDResponse.federated_bundles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=250,
)


_X509SVID = _descriptor.Descriptor(
  name='X509SVID',
  full_name='X509SVID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spiffe_id', full_name='X509SVID.spiffe_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x509_svid', full_name='X509SVID.x509_svid', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x509_svid_key', full_name='X509SVID.x509_svid_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bundle', full_name='X509SVID.bundle', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=339,
)


_JWTSVID = _descriptor.Descriptor(
  name='JWTSVID',
  full_name='JWTSVID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spiffe_id', full_name='JWTSVID.spiffe_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='svid', full_name='JWTSVID.svid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=383,
)


_JWTSVIDREQUEST = _descriptor.Descriptor(
  name='JWTSVIDRequest',
  full_name='JWTSVIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audience', full_name='JWTSVIDRequest.audience', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spiffe_id', full_name='JWTSVIDRequest.spiffe_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=438,
)


_JWTSVIDRESPONSE = _descriptor.Descriptor(
  name='JWTSVIDResponse',
  full_name='JWTSVIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='svids', full_name='JWTSVIDResponse.svids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=482,
)


_JWTBUNDLESREQUEST = _descriptor.Descriptor(
  name='JWTBundlesRequest',
  full_name='JWTBundlesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=503,
)


_JWTBUNDLESRESPONSE_BUNDLESENTRY = _descriptor.Descriptor(
  name='BundlesEntry',
  full_name='JWTBundlesResponse.BundlesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='JWTBundlesResponse.BundlesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='JWTBundlesResponse.BundlesEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=624,
)

_JWTBUNDLESRESPONSE = _descriptor.Descriptor(
  name='JWTBundlesResponse',
  full_name='JWTBundlesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bundles', full_name='JWTBundlesResponse.bundles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_JWTBUNDLESRESPONSE_BUNDLESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=624,
)


_VALIDATEJWTSVIDREQUEST = _descriptor.Descriptor(
  name='ValidateJWTSVIDRequest',
  full_name='ValidateJWTSVIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audience', full_name='ValidateJWTSVIDRequest.audience', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='svid', full_name='ValidateJWTSVIDRequest.svid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=626,
  serialized_end=682,
)


_VALIDATEJWTSVIDRESPONSE = _descriptor.Descriptor(
  name='ValidateJWTSVIDResponse',
  full_name='ValidateJWTSVIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spiffe_id', full_name='ValidateJWTSVIDResponse.spiffe_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claims', full_name='ValidateJWTSVIDResponse.claims', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=769,
)

_X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY.containing_type = _X509SVIDRESPONSE
_X509SVIDRESPONSE.fields_by_name['svids'].message_type = _X509SVID
_X509SVIDRESPONSE.fields_by_name['federated_bundles'].message_type = _X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY
_JWTSVIDRESPONSE.fields_by_name['svids'].message_type = _JWTSVID
_JWTBUNDLESRESPONSE_BUNDLESENTRY.containing_type = _JWTBUNDLESRESPONSE
_JWTBUNDLESRESPONSE.fields_by_name['bundles'].message_type = _JWTBUNDLESRESPONSE_BUNDLESENTRY
_VALIDATEJWTSVIDRESPONSE.fields_by_name['claims'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['X509SVIDRequest'] = _X509SVIDREQUEST
DESCRIPTOR.message_types_by_name['X509SVIDResponse'] = _X509SVIDRESPONSE
DESCRIPTOR.message_types_by_name['X509SVID'] = _X509SVID
DESCRIPTOR.message_types_by_name['JWTSVID'] = _JWTSVID
DESCRIPTOR.message_types_by_name['JWTSVIDRequest'] = _JWTSVIDREQUEST
DESCRIPTOR.message_types_by_name['JWTSVIDResponse'] = _JWTSVIDRESPONSE
DESCRIPTOR.message_types_by_name['JWTBundlesRequest'] = _JWTBUNDLESREQUEST
DESCRIPTOR.message_types_by_name['JWTBundlesResponse'] = _JWTBUNDLESRESPONSE
DESCRIPTOR.message_types_by_name['ValidateJWTSVIDRequest'] = _VALIDATEJWTSVIDREQUEST
DESCRIPTOR.message_types_by_name['ValidateJWTSVIDResponse'] = _VALIDATEJWTSVIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

X509SVIDRequest = _reflection.GeneratedProtocolMessageType('X509SVIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _X509SVIDREQUEST,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:X509SVIDRequest)
  })
_sym_db.RegisterMessage(X509SVIDRequest)

X509SVIDResponse = _reflection.GeneratedProtocolMessageType('X509SVIDResponse', (_message.Message,), {

  'FederatedBundlesEntry' : _reflection.GeneratedProtocolMessageType('FederatedBundlesEntry', (_message.Message,), {
    'DESCRIPTOR' : _X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY,
    '__module__' : 'workload_pb2'
    # @@protoc_insertion_point(class_scope:X509SVIDResponse.FederatedBundlesEntry)
    })
  ,
  'DESCRIPTOR' : _X509SVIDRESPONSE,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:X509SVIDResponse)
  })
_sym_db.RegisterMessage(X509SVIDResponse)
_sym_db.RegisterMessage(X509SVIDResponse.FederatedBundlesEntry)

X509SVID = _reflection.GeneratedProtocolMessageType('X509SVID', (_message.Message,), {
  'DESCRIPTOR' : _X509SVID,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:X509SVID)
  })
_sym_db.RegisterMessage(X509SVID)

JWTSVID = _reflection.GeneratedProtocolMessageType('JWTSVID', (_message.Message,), {
  'DESCRIPTOR' : _JWTSVID,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:JWTSVID)
  })
_sym_db.RegisterMessage(JWTSVID)

JWTSVIDRequest = _reflection.GeneratedProtocolMessageType('JWTSVIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _JWTSVIDREQUEST,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:JWTSVIDRequest)
  })
_sym_db.RegisterMessage(JWTSVIDRequest)

JWTSVIDResponse = _reflection.GeneratedProtocolMessageType('JWTSVIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _JWTSVIDRESPONSE,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:JWTSVIDResponse)
  })
_sym_db.RegisterMessage(JWTSVIDResponse)

JWTBundlesRequest = _reflection.GeneratedProtocolMessageType('JWTBundlesRequest', (_message.Message,), {
  'DESCRIPTOR' : _JWTBUNDLESREQUEST,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:JWTBundlesRequest)
  })
_sym_db.RegisterMessage(JWTBundlesRequest)

JWTBundlesResponse = _reflection.GeneratedProtocolMessageType('JWTBundlesResponse', (_message.Message,), {

  'BundlesEntry' : _reflection.GeneratedProtocolMessageType('BundlesEntry', (_message.Message,), {
    'DESCRIPTOR' : _JWTBUNDLESRESPONSE_BUNDLESENTRY,
    '__module__' : 'workload_pb2'
    # @@protoc_insertion_point(class_scope:JWTBundlesResponse.BundlesEntry)
    })
  ,
  'DESCRIPTOR' : _JWTBUNDLESRESPONSE,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:JWTBundlesResponse)
  })
_sym_db.RegisterMessage(JWTBundlesResponse)
_sym_db.RegisterMessage(JWTBundlesResponse.BundlesEntry)

ValidateJWTSVIDRequest = _reflection.GeneratedProtocolMessageType('ValidateJWTSVIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEJWTSVIDREQUEST,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:ValidateJWTSVIDRequest)
  })
_sym_db.RegisterMessage(ValidateJWTSVIDRequest)

ValidateJWTSVIDResponse = _reflection.GeneratedProtocolMessageType('ValidateJWTSVIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEJWTSVIDRESPONSE,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:ValidateJWTSVIDResponse)
  })
_sym_db.RegisterMessage(ValidateJWTSVIDResponse)


DESCRIPTOR._options = None
_X509SVIDRESPONSE_FEDERATEDBUNDLESENTRY._options = None
_JWTBUNDLESRESPONSE_BUNDLESENTRY._options = None

_SPIFFEWORKLOADAPI = _descriptor.ServiceDescriptor(
  name='SpiffeWorkloadAPI',
  full_name='SpiffeWorkloadAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=772,
  serialized_end=1030,
  methods=[
  _descriptor.MethodDescriptor(
    name='FetchJWTSVID',
    full_name='SpiffeWorkloadAPI.FetchJWTSVID',
    index=0,
    containing_service=None,
    input_type=_JWTSVIDREQUEST,
    output_type=_JWTSVIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchJWTBundles',
    full_name='SpiffeWorkloadAPI.FetchJWTBundles',
    index=1,
    containing_service=None,
    input_type=_JWTBUNDLESREQUEST,
    output_type=_JWTBUNDLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ValidateJWTSVID',
    full_name='SpiffeWorkloadAPI.ValidateJWTSVID',
    index=2,
    containing_service=None,
    input_type=_VALIDATEJWTSVIDREQUEST,
    output_type=_VALIDATEJWTSVIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchX509SVID',
    full_name='SpiffeWorkloadAPI.FetchX509SVID',
    index=3,
    containing_service=None,
    input_type=_X509SVIDREQUEST,
    output_type=_X509SVIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPIFFEWORKLOADAPI)

DESCRIPTOR.services_by_name['SpiffeWorkloadAPI'] = _SPIFFEWORKLOADAPI

# @@protoc_insertion_point(module_scope)