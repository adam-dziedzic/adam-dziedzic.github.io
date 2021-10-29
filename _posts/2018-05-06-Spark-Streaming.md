---
layout: post
title:  "Notes on a paper: Spark Streaming"
date:   2018-05-06
desc: "notes on a paper"
keywords: "streaming databases SOSP 2013 spark mike"
categories: [HTML]
tags: [streaming databases SOSP 2013 spark mike]
icon: icon-html
---

# These are my notes about the paper ["Discretized Streams: Fault-Tolerant Streaming Computation at Scale"](https://people.csail.mit.edu/matei/papers/2013/sosp_spark_streaming.pdf)

## Strong points:

1. Change of the paradigm - stream processing is no longer full of state maintenance but closer to the batch processing with simpler fault tolerance handling, fast recovery and mitigating the effect of stragglers.
2. The handling of fault-tolerance is better - it uses PARALLELISM 1) within a batch 2) across time intervals. The recovery is faster than for the upstream backup, especially because of the nice property that the larger the cluster, the lower the recovery time. The parallel recovery also applies to stragglers - it mitigates them by 1) detecting slow tasks (e.g., 2X slower than the other tasks on average) 2) speculatively launching more copies of the tasks in parallel on other machines. The net effect is that the speculative launch of redundant tasks masks the impact of slow nodes on the holistic progress of the system. The previous methods of recovery in streaming systems were much more complicated, for example, there were special protocols needed to synchronize the master nodes with the "slave" nodes - e.g. Borealis' DPC). The checkpointing is done asynchronously to bound the recovery time.
3. The whole idea behind the streaming and batch processing in Spark is based on a beautiful and neat application of functional programming paradigms to data processing. There is a unification of batch and streaming - a single programming and execution model for running streaming, batch and interactive jobs.
4. User friendly - for in-memory and on-line debugging. Users can fire a Spark console and query the streams on the fly / ad-hoc. It was very easy to implement the Markov Chain Monte Carlo simulation for traffic estimation from GPS data.


## Weak points:

1. No support for watermarks - a feature for dropping overly old data when sufficient time has passed. The first approximation of the feature is the implicit boundary between the small batches.
2. The main problem of the system is its long latency - a fixed minimum latency due to batching data (though some continuous operator systems, such as Borealis, add delays to ensure determinism). The obvious way to mitigate it is to decrease the window size and avoid firing a new process/task for each batch - but simply keep a pool of tasks that process the batches in a continuous way. It was addressed in the latest post from Databricks on streaming - millisecond low-latency of streaming - continuous mode that was built to process each transaction in the pipeline within 10-20 ms (as it is the case for the detection of fraudulent transactions). The main new contribution is the usage of continuous processing that uses long running tasks to continuously process events. Moreover, the progress is checkpointed by an adaptation of Chandy-Lamport algorithm. The fine-grained lineage graph helps to save on copying the data - on the other hand, the asynchronous checkpoints are used to prevent long lineages (to recompute lost partitions).
3. The experimental part is a bit straw-man comparison: it is possible to reduce the overhead of number of nodes for the upstream backup from 2X to 1.1X (for example it is possible to only send the write-log, or even a simple separation of data writes and log writes gives only about 15% overhead of the processing).
4. The notion of time is a bit distorted and they do not pay enough attention - through the whole paper it is assumed that the input data is time-stamped at the receiving node.
5. Not that many modification is Spark were needed to propose the streaming part - e.g. reduce the latency of launching the jobs (as a big initial overhead) from seconds to milliseconds.

## Notes:

1. The main requirement - large scale streaming systems must handle faults and stragglers.
2. Naiad - combines graph, streaming and batch processing without sacrificing latency but a full cluster rollback is required on recovery.
3. Great slides but also some complaints: https://www.slideshare.net/ptgoetz/apache-storm-vs-spark-streaming
4. Second latency acceptable to many applications (maybe exlucding the case of high-frequency algorithmic trading).
5. Spark 2.3 - they go to the continuous processing - they support users' timestamps - the initial problems were solved eventually.
6. No-batch - get a single answer faster, but hurts the throughput.
