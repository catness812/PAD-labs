# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: journal_svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11journal_svc.proto\x12\x05proto\"9\n\x05\x45ntry\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"3\n\x14RegisterEntryRequest\x12\x1b\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x0c.proto.Entry\"(\n\x15RegisterEntryResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\\\n\x0eJournalService\x12J\n\rRegisterEntry\x12\x1b.proto.RegisterEntryRequest\x1a\x1c.proto.RegisterEntryResponseB\x06Z\x04./pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'journal_svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004./pb'
  _globals['_ENTRY']._serialized_start=28
  _globals['_ENTRY']._serialized_end=85
  _globals['_REGISTERENTRYREQUEST']._serialized_start=87
  _globals['_REGISTERENTRYREQUEST']._serialized_end=138
  _globals['_REGISTERENTRYRESPONSE']._serialized_start=140
  _globals['_REGISTERENTRYRESPONSE']._serialized_end=180
  _globals['_JOURNALSERVICE']._serialized_start=182
  _globals['_JOURNALSERVICE']._serialized_end=274
# @@protoc_insertion_point(module_scope)