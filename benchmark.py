"""
 Copyright (c) 2024 Pablo Ramirez Escudero
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

import pickle
import msgpack
import person_pb2
import timeit

# Sample non-tabular data
data = {
    "name": "Alice",
    "surname": "Bennett",
    "age": 30,
    "money": 12537.21,
    "children": [{"name": "Bob", "age": 5}, {"name": "Charlie", "age": 3}],
    "is_married": True,
    "hobbies": ["reading", "hiking", "painting", "cycling"],
    "address": {
        "street": "123 Elm St",
        "city": "Springfield",
        "state": "IL",
        "zip": "62704",
    },
}

# Initialize Protobuf data outside the tests
person = person_pb2.Person(name="Alice", age=30, is_married=True)

# Add children to Protobuf structure
child1 = person.children.add()
child1.name = "Bob"
child1.age = 5

child2 = person.children.add()
child2.name = "Charlie"
child2.age = 3


# 1. Pickle Serialization and Deserialization
def pickle_test():
    # Serialize
    pickle_data = pickle.dumps(data)
    # Deserialize
    unpickled_data = pickle.loads(pickle_data)
    # Check deserialization correctness
    assert unpickled_data == data, "Pickle deserialization failed!"
    return len(pickle_data)


# 2. MessagePack Serialization and Deserialization
def msgpack_test():
    # Serialize
    msgpack_data = msgpack.packb(data)
    # Deserialize
    unmsgpack_data = msgpack.unpackb(msgpack_data)
    # Check deserialization correctness
    assert unmsgpack_data == data, "MessagePack deserialization failed!"
    return len(msgpack_data)


# 3. Protobuf Serialization and Deserialization
def protobuf_test():
    # Serialize
    protobuf_data = person.SerializeToString()
    # Deserialize
    person_deserialized = person_pb2.Person()
    person_deserialized.ParseFromString(protobuf_data)
    # Check deserialization correctness using direct comparison
    assert person == person_deserialized, "Protobuf deserialization failed!"
    return len(protobuf_data)


# Timing the methods
pickle_time = timeit.timeit(lambda: pickle_test(), number=10000)
msgpack_time = timeit.timeit(lambda: msgpack_test(), number=10000)
protobuf_time = timeit.timeit(lambda: protobuf_test(), number=10000)

# Display Results
print(f"Pickle:      Time: {pickle_time:.6f}s, Size: {pickle_test()} bytes")
print(f"MessagePack: Time: {msgpack_time:.6f}s, Size: {msgpack_test()} bytes")
print(f"Protobuf:    Time: {protobuf_time:.6f}s, Size: {protobuf_test()} bytes")
