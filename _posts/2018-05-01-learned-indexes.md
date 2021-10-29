---
layout: post
title:  "Notes on a paper: Learned indexes"
date:   2018-05-04
desc: "notes on a paper"
keywords: "machine-learning SIGMOD 2018 learned-indexes "
categories: [HTML]
tags: [machine-learning SIGMOD 2018 learned-indexes]
icon: icon-html
---

# The Case for Learned Index Structures

I think that if the learned indexed work as presented in the experiments, then they (i.e. Tim Kraska and the Google's team) found a new approach how to leverage Machine Learning (specifically Neural Networks in the future of more integrated CPU-GUP-TPU hardware) to improve the "old" database architecture in a bit different way. On the high level, they treat a B+tree as a model or simply a function from a search key (or range) to an output position. They clearly motivate that only with the future performance improvement of GPUs/TPUs (1000x in 2025) we can achieve much better performance with Neural Networks than with B+trees (that work on CPUs) - section 2.1. Taking into consideration my work from the last internship at MSR (Microsoft Research), they definitely should compare with column store indexes (especially sorted ones for the read-only workload – they focus primarily on the analytical workloads anyway). Further on, they do provide many details, e.g. compare B+trees and Neural Networks comprehensively in the experimental part, and even go into the implementation details of the dense/sparse hash maps (Google has its own internal highly-optimized hash-maps).

Regarding auto indexing, it would change/extend the arena quite a bit. Of course, we still have to decide on which attributes we should build the indexes on, but the space of possible indexes would be much broader (many more possible models, or we could just map B+trees, hash maps etc. to specific per-arranged models) and the parameters for a given index could be found automatically: “Furthermore, auto-tuning techniques could be used to further reduce the time it takes to find the best index configuration” (but by this auto-tuning they mean selecting parameters for a single model/index).

So, the performance tuning of the database with learned indexes would be much harder – not only selecting attributes for indexes but also tuning the parameters for indexes themselves. However, this approach to indexing strengthens the motivation for auto-admin tools and poses new interesting challenges.

I think that it also depends on the use case. I was an intern at Google and read a few papers where they argue that in many cases they have to analyze humongous data sets (that usually are read or append only). The possibility of decreasing the size of the indexes significantly and no need for updates seems to be like the place the learned indexes can excel at.

One area that should be still explored is how to cater for workloads with many updates/inserts/deletes for the learned indexes. Interestingly enough, if, let's say, we have the append-only workload and the data distribution does not change then we don't really have to modify the index.

## Strong points:
1. There are already databases that are only-GPU based, so such indexes would be a perfect match.
2. When we zoom in to individual record on the CDF curve (Cumulative Distribution Function), we can see many discontinuities which are hard to learn - too much entropy. The idea with the last mile access supported with B+trees seems to be viable - even with a better approach to explore the benefits of both B+trees and machine learning models within the same index. Then, we could adjust the percentage of usage of both structures while building the index to find the the best performing combination,  usually - with B+tree at the bottom of the index, and the machine learning models (simple linear models or simple neural nets) on the top of the index.
3. They use interesting tricks, for example, let's extract the model, i.e. all the weights, to a bare structure in C++ that eludes all the overheads by shedding the Python interface, additional function calls or batch processing used for large scale machine learning.

## Weak points:
1. A costly procedure to give the error upper bounds (min/max error) where the key should be searched within.
2. If a key does not exist in the index, the index can point to the range which is outside the min-max range, maybe we would end up with traversing the whole dataset to make sure that a key does not exist.
3. They don't explore the interesting scope of the relation between precision required and complexity of the model, subsequently between the complexity of the model and the search time. These are the crucial dimensions to judge the performance of the new proposed indexes.
4. If we want to use GPUs/TPUs we have to deal with the long transfer time between CPU and GPU which is in 1000 of cycles, whereas scanning a leaf node from a B+tree, even with a cache-miss takes only 150 cycles (50 cycles for the scan and additional 100 cycles incurred by the cache-miss).
5. Clearly, the vanilla models presented in section 2.3 are extremely bad and much slower than B+trees: "The search time to find the data with the help of the prediction almost had no benefit over a full search over the data".
6. B+trees are cache efficient (keeping only the top of the trees in cache), whereas the neural nets require all the weights to compute the prediction.
7. There is a dichotomy of errors: in the machine learning models we optimize for the average error while for the learned indexes we are optimizing for the min-max errors (the min-max range of positions that we have to check to answer the question if the searched key is present, and if so where, or is absent in the index).
8. The biggest challenge is the last-mile accuracy.
9. It is not crystal clear how they train the staged models - they do give the loss functions but they do not do the full end-to-end training, I suppose for a model lower in the stage, only the search keys that go through the model in the current learning stage, contribute to the loss - but these keys taken into account for the less in a staged model might be very different through the learning process, i.e. fluctuate a lot, thus it is not explained when we stop training and if the loss really decreases and model converges.
10. New leaf-node search strategies - does not seem to be like a great gain in performance.
11. Why don't we use word embeddings for the indexing of strings?

## Other notes:
1. Regarding the Clipper system - this paper states that you should never use TensorFlow for inference.

