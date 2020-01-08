# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_import.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import unittest_import_public_pb2 as google_dot_protobuf_dot_unittest__import__public__pb2

from google.protobuf.unittest_import_public_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/unittest_import.proto',
  package='protobuf_unittest_import',
  syntax='proto2',
  serialized_options=b'\n\030com.google.protobuf.testH\001\370\001\001',
  serialized_pb=b'\n%google/protobuf/unittest_import.proto\x12\x18protobuf_unittest_import\x1a,google/protobuf/unittest_import_public.proto\"\x1a\n\rImportMessage\x12\t\n\x01\x64\x18\x01 \x01(\x05*<\n\nImportEnum\x12\x0e\n\nIMPORT_FOO\x10\x07\x12\x0e\n\nIMPORT_BAR\x10\x08\x12\x0e\n\nIMPORT_BAZ\x10\t*1\n\x10ImportEnumForMap\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x46OO\x10\x01\x12\x07\n\x03\x42\x41R\x10\x02\x42\x1f\n\x18\x63om.google.protobuf.testH\x01\xf8\x01\x01P\x00'
  ,
  dependencies=[google_dot_protobuf_dot_unittest__import__public__pb2.DESCRIPTOR,],
  public_dependencies=[google_dot_protobuf_dot_unittest__import__public__pb2.DESCRIPTOR,])

_IMPORTENUM = _descriptor.EnumDescriptor(
  name='ImportEnum',
  full_name='protobuf_unittest_import.ImportEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMPORT_FOO', index=0, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPORT_BAR', index=1, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPORT_BAZ', index=2, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=141,
  serialized_end=201,
)
_sym_db.RegisterEnumDescriptor(_IMPORTENUM)

ImportEnum = enum_type_wrapper.EnumTypeWrapper(_IMPORTENUM)
_IMPORTENUMFORMAP = _descriptor.EnumDescriptor(
  name='ImportEnumForMap',
  full_name='protobuf_unittest_import.ImportEnumForMap',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_IMPORTENUMFORMAP)

ImportEnumForMap = enum_type_wrapper.EnumTypeWrapper(_IMPORTENUMFORMAP)
IMPORT_FOO = 7
IMPORT_BAR = 8
IMPORT_BAZ = 9
UNKNOWN = 0
FOO = 1
BAR = 2



_IMPORTMESSAGE = _descriptor.Descriptor(
  name='ImportMessage',
  full_name='protobuf_unittest_import.ImportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='d', full_name='protobuf_unittest_import.ImportMessage.d', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['ImportMessage'] = _IMPORTMESSAGE
DESCRIPTOR.enum_types_by_name['ImportEnum'] = _IMPORTENUM
DESCRIPTOR.enum_types_by_name['ImportEnumForMap'] = _IMPORTENUMFORMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportMessage = _reflection.GeneratedProtocolMessageType('ImportMessage', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTMESSAGE,
  '__module__' : 'google.protobuf.unittest_import_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest_import.ImportMessage)
  })
_sym_db.RegisterMessage(ImportMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
