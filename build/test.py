import NetworkPacket_pb2
import BuddyListNotifyCmd_pb2

request = NetworkPacket_pb2.NetworkPacket()

request.length = 3
request.short_object_id = 0xFF
request.type = 0x0A
request.buddy_list_notify_cmd.CopyFrom(BuddyListNotifyCmd_pb2.BuddyListNotifyCmd())
request.buddy_list_notify_cmd.buddy_name = "Whirl"
request.buddy_list_notify_cmd.logged_on = 1

print(request.SerializeToString())
print(request.WhichOneof("command"))

deserialised_request = NetworkPacket_pb2.NetworkPacket()

deserialised_request.ParseFromString(request.SerializeToString())

print(deserialised_request.length)
print(deserialised_request.short_object_id)
print(deserialised_request.type)
print(deserialised_request.buddy_list_notify_cmd.buddy_name)
print(deserialised_request.buddy_list_notify_cmd.logged_on)
