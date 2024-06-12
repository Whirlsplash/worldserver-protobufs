import NetworkPacket_pb2
import BuddyListNotifyCommand_pb2

request = NetworkPacket_pb2.NetworkPacket()

request.length = 3
request.short_object_id = 0xFF
request.type = 0x0A
request.buddy_list_notify_command.CopyFrom(
    BuddyListNotifyCommand_pb2.BuddyListNotifyCommand()
)
request.buddy_list_notify_command.buddy_name = "Whirl"
request.buddy_list_notify_command.logged_on = 1

print(request.SerializeToString())
print(request.WhichOneof("command"))

deserialised_request = NetworkPacket_pb2.NetworkPacket()

deserialised_request.ParseFromString(request.SerializeToString())

print(deserialised_request.length)
print(deserialised_request.short_object_id)
print(deserialised_request.type)
print(deserialised_request.buddy_list_notify_command.buddy_name)
print(deserialised_request.buddy_list_notify_command.logged_on)
