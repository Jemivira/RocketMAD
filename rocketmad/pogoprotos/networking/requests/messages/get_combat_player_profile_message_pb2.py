# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_combat_player_profile_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_combat_player_profile_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nOpogoprotos/networking/requests/messages/get_combat_player_profile_message.proto\x12\'pogoprotos.networking.requests.messages\"2\n\x1dGetCombatPlayerProfileMessage\x12\x11\n\tplayer_id\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETCOMBATPLAYERPROFILEMESSAGE = _descriptor.Descriptor(
  name='GetCombatPlayerProfileMessage',
  full_name='pogoprotos.networking.requests.messages.GetCombatPlayerProfileMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.requests.messages.GetCombatPlayerProfileMessage.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['GetCombatPlayerProfileMessage'] = _GETCOMBATPLAYERPROFILEMESSAGE

GetCombatPlayerProfileMessage = _reflection.GeneratedProtocolMessageType('GetCombatPlayerProfileMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETCOMBATPLAYERPROFILEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_combat_player_profile_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetCombatPlayerProfileMessage)
  ))
_sym_db.RegisterMessage(GetCombatPlayerProfileMessage)


# @@protoc_insertion_point(module_scope)