import NetPacket_pb2
import BuddyListNotifyCmd_pb2

request = NetPacket_pb2.NetPacket()

request.length = 3
request.short_object_id = 0xFF
request.command_type = 0x0A
request.buddy_list_notify_cmd.CopyFrom(BuddyListNotifyCmd_pb2.BuddyListNotifyCmd())
request.buddy_list_notify_cmd.buddy_name = "Whirl"
request.buddy_list_notify_cmd.logged_on = 1

print(request.SerializeToString())
print(request.WhichOneof("packet"))

deserialised_request = NetPacket_pb2.NetPacket()

deserialised_request.ParseFromString(request.SerializeToString())

print(deserialised_request.length)
print(deserialised_request.short_object_id)
print(deserialised_request.command_type)
print(deserialised_request.buddy_list_notify_cmd.buddy_name)
print(deserialised_request.buddy_list_notify_cmd.logged_on)
