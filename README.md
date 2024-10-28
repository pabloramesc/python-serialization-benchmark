# Python Serialization Benchmark

This tool evaluates the performance of Pickle, MessagePack, and Protobuf serialization methods in Python.
It benchmarks and compares their serialization speed and data size for non-tabular data structures.

## Serialization Methods

- **Pickle**: Python-specific, easy to use but not very efficient for large datasets.
- **MessagePack**: Space-efficient binary format compatible with multiple languages.
- **Protobuf**: Compact, efficient binary format developed by Google for structured data.

## Benchmark Results

| Method       | Time       | Size      |
|--------------|------------|-----------|
| Pickle       | 0.037158s  | 279 bytes |
| MessagePack  | 0.035214s  | 208 bytes |
| Protobuf     | 0.010459s  | 33 bytes  |

Protobuf is the most efficient in terms of both speed and size.

## Quickstart

To run the benchmarks, clone this repository and execute the `benchmark.py` script:

```bash
git clone https://github.com/yourusername/python-serialization-benchmark.git
cd python-serialization-benchmark
pip install -r requirements.txt
python benchmark.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.