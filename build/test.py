import network_packet_pb2 as network_packet
from commands import buddy_list_notify_command_pb2 as buddy_list_notify_command

request = network_packet.NetworkPacket()

request.length = 3
request.short_object_id = 0xFF
request.type = 0x0A
request.buddy_list_notify_command.CopyFrom(
    buddy_list_notify_command.BuddyListNotifyCommand()
)
request.buddy_list_notify_command.buddy_name = "Whirl"
request.buddy_list_notify_command.logged_on = 1

print(request.SerializeToString())
print(request.WhichOneof("command"))

deserialised_request = network_packet.NetworkPacket()

deserialised_request.ParseFromString(request.SerializeToString())

print(deserialised_request.length)
print(deserialised_request.short_object_id)
print(deserialised_request.type)
print(deserialised_request.buddy_list_notify_command.buddy_name)
print(deserialised_request.buddy_list_notify_command.logged_on)
