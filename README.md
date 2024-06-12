# WorldServer Protocol Buffers

[Protocol Buffers](https://protobuf.dev/) implemented for [Worlds](https://www.worlds.com/)'
[WorldServer](http://dev.worlds.net/private/GammaDocs/WorldServer.html) protocol.

## Testing

```shell
# Compile the protocol buffers for Python usage
tup

# Test an example serialization and deserialization scenario
python3 build/test.py
```

### Dependencies

- [`protoc`](https://grpc.io/docs/protoc-installation/) — Protocol buffer compiler
- [Python](https://www.python.org/) — Test adapter
- [Tup](https://gittup.org/tup/index.html) — Build system

# Licence

This project is licensed with the [GNU General Public License v3.0](./LICENSE>).
