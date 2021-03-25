# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_val.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key_val.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rkey_val.proto\"+\n\rstore_request\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"\x1d\n\x0estore_response\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"\x1e\n\x0fget_key_request\x12\x0b\n\x03key\x18\x01 \x01(\t\"!\n\x10get_key_response\x12\r\n\x05value\x18\x01 \x03(\x05\"\x1e\n\x0f\x61ll_key_request\x12\x0b\n\x03key\x18\x01 \x01(\t\"$\n\x10\x61ll_key_response\x12\x10\n\x08response\x18\x01 \x03(\t\"%\n\x12key_length_request\x12\x0f\n\x07get_key\x18\x01 \x01(\t\")\n\x13key_length_response\x12\x12\n\nkey_length\x18\x01 \x01(\x05\x32\xe7\x01\n\tmaster_kv\x12.\n\tstore_key\x12\x0e.store_request\x1a\x0f.store_response\"\x00\x12\x30\n\x07get_key\x12\x10.get_key_request\x1a\x11.get_key_response\"\x00\x12\x35\n\x0cget_all_keys\x12\x10.all_key_request\x1a\x11.all_key_response\"\x00\x12\x41\n\x12get_number_of_keys\x12\x13.key_length_request\x1a\x14.key_length_response\"\x00\x62\x06proto3'
)




_STORE_REQUEST = _descriptor.Descriptor(
  name='store_request',
  full_name='store_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='store_request.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='store_request.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=17,
  serialized_end=60,
)


_STORE_RESPONSE = _descriptor.Descriptor(
  name='store_response',
  full_name='store_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='store_response.ack', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=62,
  serialized_end=91,
)


_GET_KEY_REQUEST = _descriptor.Descriptor(
  name='get_key_request',
  full_name='get_key_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='get_key_request.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=93,
  serialized_end=123,
)


_GET_KEY_RESPONSE = _descriptor.Descriptor(
  name='get_key_response',
  full_name='get_key_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='get_key_response.value', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=125,
  serialized_end=158,
)


_ALL_KEY_REQUEST = _descriptor.Descriptor(
  name='all_key_request',
  full_name='all_key_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='all_key_request.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=160,
  serialized_end=190,
)


_ALL_KEY_RESPONSE = _descriptor.Descriptor(
  name='all_key_response',
  full_name='all_key_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='all_key_response.response', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=192,
  serialized_end=228,
)


_KEY_LENGTH_REQUEST = _descriptor.Descriptor(
  name='key_length_request',
  full_name='key_length_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_key', full_name='key_length_request.get_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=230,
  serialized_end=267,
)


_KEY_LENGTH_RESPONSE = _descriptor.Descriptor(
  name='key_length_response',
  full_name='key_length_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_length', full_name='key_length_response.key_length', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=269,
  serialized_end=310,
)

DESCRIPTOR.message_types_by_name['store_request'] = _STORE_REQUEST
DESCRIPTOR.message_types_by_name['store_response'] = _STORE_RESPONSE
DESCRIPTOR.message_types_by_name['get_key_request'] = _GET_KEY_REQUEST
DESCRIPTOR.message_types_by_name['get_key_response'] = _GET_KEY_RESPONSE
DESCRIPTOR.message_types_by_name['all_key_request'] = _ALL_KEY_REQUEST
DESCRIPTOR.message_types_by_name['all_key_response'] = _ALL_KEY_RESPONSE
DESCRIPTOR.message_types_by_name['key_length_request'] = _KEY_LENGTH_REQUEST
DESCRIPTOR.message_types_by_name['key_length_response'] = _KEY_LENGTH_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

store_request = _reflection.GeneratedProtocolMessageType('store_request', (_message.Message,), {
  'DESCRIPTOR' : _STORE_REQUEST,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:store_request)
  })
_sym_db.RegisterMessage(store_request)

store_response = _reflection.GeneratedProtocolMessageType('store_response', (_message.Message,), {
  'DESCRIPTOR' : _STORE_RESPONSE,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:store_response)
  })
_sym_db.RegisterMessage(store_response)

get_key_request = _reflection.GeneratedProtocolMessageType('get_key_request', (_message.Message,), {
  'DESCRIPTOR' : _GET_KEY_REQUEST,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:get_key_request)
  })
_sym_db.RegisterMessage(get_key_request)

get_key_response = _reflection.GeneratedProtocolMessageType('get_key_response', (_message.Message,), {
  'DESCRIPTOR' : _GET_KEY_RESPONSE,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:get_key_response)
  })
_sym_db.RegisterMessage(get_key_response)

all_key_request = _reflection.GeneratedProtocolMessageType('all_key_request', (_message.Message,), {
  'DESCRIPTOR' : _ALL_KEY_REQUEST,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:all_key_request)
  })
_sym_db.RegisterMessage(all_key_request)

all_key_response = _reflection.GeneratedProtocolMessageType('all_key_response', (_message.Message,), {
  'DESCRIPTOR' : _ALL_KEY_RESPONSE,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:all_key_response)
  })
_sym_db.RegisterMessage(all_key_response)

key_length_request = _reflection.GeneratedProtocolMessageType('key_length_request', (_message.Message,), {
  'DESCRIPTOR' : _KEY_LENGTH_REQUEST,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:key_length_request)
  })
_sym_db.RegisterMessage(key_length_request)

key_length_response = _reflection.GeneratedProtocolMessageType('key_length_response', (_message.Message,), {
  'DESCRIPTOR' : _KEY_LENGTH_RESPONSE,
  '__module__' : 'key_val_pb2'
  # @@protoc_insertion_point(class_scope:key_length_response)
  })
_sym_db.RegisterMessage(key_length_response)



_MASTER_KV = _descriptor.ServiceDescriptor(
  name='master_kv',
  full_name='master_kv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=313,
  serialized_end=544,
  methods=[
  _descriptor.MethodDescriptor(
    name='store_key',
    full_name='master_kv.store_key',
    index=0,
    containing_service=None,
    input_type=_STORE_REQUEST,
    output_type=_STORE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_key',
    full_name='master_kv.get_key',
    index=1,
    containing_service=None,
    input_type=_GET_KEY_REQUEST,
    output_type=_GET_KEY_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_all_keys',
    full_name='master_kv.get_all_keys',
    index=2,
    containing_service=None,
    input_type=_ALL_KEY_REQUEST,
    output_type=_ALL_KEY_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_number_of_keys',
    full_name='master_kv.get_number_of_keys',
    index=3,
    containing_service=None,
    input_type=_KEY_LENGTH_REQUEST,
    output_type=_KEY_LENGTH_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MASTER_KV)

DESCRIPTOR.services_by_name['master_kv'] = _MASTER_KV

# @@protoc_insertion_point(module_scope)