import network_packet_pb2 as network_packet
from commands import buddy_list_notify_command_pb2 as buddy_list_notify_command
import command_pb2 as command

request = network_packet.NetworkPacket()

request.short_object_id = 0xFF
request.type = command.BUDDYLISTNOTIFYCMD
request.buddy_list_notify_command.CopyFrom(
    buddy_list_notify_command.BuddyListNotifyCommand()
)
request.buddy_list_notify_command.buddy_name = "Whirl"
request.buddy_list_notify_command.logged_on = 1
request.length = 3 + len(request.buddy_list_notify_command.buddy_name) + 1 + 1

print(f"SerializeToString(): {request.SerializeToString()}")
print(f"request.WhichOneof('command'): {request.WhichOneof('command')}")
print()

deserialised_request = network_packet.NetworkPacket()

deserialised_request.ParseFromString(request.SerializeToString())

print(f"deserialised_request.length: {deserialised_request.length}")
print(f"deserialised_request.short_object_id: {deserialised_request.short_object_id}")
print(f"deserialised_request.type: {deserialised_request.type}")
print(
    f"deserialised_request.buddy_list_notify_command.buddy_name: {deserialised_request.buddy_list_notify_command.buddy_name}"
)
print(
    f"deserialised_request.buddy_list_notify_command.logged_on: {deserialised_request.buddy_list_notify_command.logged_on}"
)
print()


def parse_network_packet(raw_bytes):
    net_packet = network_packet.NetworkPacket()

    net_packet.length = raw_bytes[0]
    net_packet.short_object_id = raw_bytes[1]
    net_packet.type = raw_bytes[2]

    command_type = net_packet.type

    match command_type:
        case command.BUDDYLISTNOTIFYCMD:
            print("This is a BuddyListNotifyCommand.")
        case command.PROPREQCMD:
            print("This is a PropRequestCommand.")
        case _:
            print(f"This is an unknown command type: {command_type}.")

    return net_packet


print(parse_network_packet(b"\x03\xff\x1e"))
print(parse_network_packet(b"\x03\x00\x1a"))
print(parse_network_packet(b"\x03\xff\x0a"))
