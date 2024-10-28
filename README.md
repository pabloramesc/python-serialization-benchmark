# Python Serialization Benchmark

This repository contains a benchmark of various serialization methods in Python, specifically focusing on **Pickle**, **MessagePack**, and **Protobuf**. The goal is to compare their performance in terms of serialization speed and data size for non-tabular data structures.

## Overview

Serialization is the process of converting a data structure into a format that can be easily stored or transmitted. Different serialization formats have varying performance characteristics and use cases. This benchmark aims to provide insights into which method is best suited for different scenarios.

## Serialization Methods

This benchmark tests three serialization methods:

- **Pickle**: A Python-specific serialization method that is easy to use but not very efficient for large datasets.
- **MessagePack**: A binary format that is more space-efficient than Pickle and is compatible with multiple programming languages.
- **Protobuf**: A compact, efficient binary serialization format developed by Google, suitable for structured data.

## Results

The benchmark results for serialization time and size are as follows:

- **Pickle**: 
  - Time: 0.037158s
  - Size: 279 bytes
- **MessagePack**: 
  - Time: 0.035214s
  - Size: 208 bytes
- **Protobuf**: 
  - Time: 0.010459s
  - Size: 33 bytes

Protobuf stands out as the most efficient in terms of both speed and size.

## Installation

To run the benchmarks, clone this repository and install the required libraries:

```bash
git clone https://github.com/yourusername/python-serialization-benchmark.git
cd python-serialization-benchmark
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.