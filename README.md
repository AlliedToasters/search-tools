# Search Tools
This is a library containing some tools for search science. Currently in development. Many of these tools are available through other libraries, so the primary contribution of this library is to implement them in a distributed fashion via pyspark. This library is intended primarily for use with pyspark.

## Text Matching
Text matching featurizers, (BM25, tfidf similarity, etc.) can be found in `search_tools.matching`. A usage demo is provided in [this notebook](BM25_demo.ipynb).

## Metrics
Ranking metrics functions can be found in `search_tools.metrics`. A NDCG demo in pyspark is available in [this notebook](ndcg_demo.ipynb).

## Installation
This library does not yet have a release (coming soon). In the meantime, clone this repository and install with `pip install .` .
