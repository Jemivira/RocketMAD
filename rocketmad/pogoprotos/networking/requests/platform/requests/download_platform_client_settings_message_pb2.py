# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/download_platform_client_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/download_platform_client_settings_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n`pogoprotos/networking/requests/platform/requests/download_platform_client_settings_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\"8\n%DownloadPlatformClientSettingsMessage\x12\x0f\n\x07message\x18\x01 \x01(\tb\x06proto3')
)




_DOWNLOADPLATFORMCLIENTSETTINGSMESSAGE = _descriptor.Descriptor(
  name='DownloadPlatformClientSettingsMessage',
  full_name='pogoprotos.networking.requests.platform.requests.DownloadPlatformClientSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pogoprotos.networking.requests.platform.requests.DownloadPlatformClientSettingsMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['DownloadPlatformClientSettingsMessage'] = _DOWNLOADPLATFORMCLIENTSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadPlatformClientSettingsMessage = _reflection.GeneratedProtocolMessageType('DownloadPlatformClientSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADPLATFORMCLIENTSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.download_platform_client_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.DownloadPlatformClientSettingsMessage)
  ))
_sym_db.RegisterMessage(DownloadPlatformClientSettingsMessage)


# @@protoc_insertion_point(module_scope)
