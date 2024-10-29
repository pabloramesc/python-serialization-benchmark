# Python Serialization Benchmark

This tool evaluates the performance of JSON, Pickle, MessagePack, and Protobuf serialization methods in Python.
It benchmarks and compares their serialization speed and data size for non-tabular data structures.

## Serialization Methods

- **JSON**: Text-based format widely used for data interchange, human-readable but not space-efficient.
- **Pickle**: Python-specific, easy to use but not very efficient for large datasets.
- **MessagePack**: Space-efficient binary format compatible with multiple languages.
- **Protobuf**: Compact, efficient binary format developed by Google for structured data.

## Benchmark Results

| Method       | Time       | Size       |
|--------------|------------|------------|
| JSON         | 0.761769s  | 2371 bytes |
| Pickle       | 0.085776s  | 1189 bytes |
| MessagePack  | 0.080905s  | 1115 bytes |
| Protobuf     | 0.027018s  | 928 bytes  |

Protobuf is the most efficient in terms of both speed and size, while JSON, although human-readable, is the slowest and largest in size.

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