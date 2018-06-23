---
layout: post
title:  "Database Tuning Advisor for Microsoft SQL Server 2005"
date:   2018-04-30
desc: "notes on a paper"
keywords: "database Microsoft msr DTA SQL Server tuning advisor DBMS vldb 2004"
categories: [HTML]
tags: [database Microsoft msr DTA SQL Server tuning advisor DBMS vldb 2004]
icon: icon-html
---

# [Database Tuning Advisor for Microsoft SQL Server 2005](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/VLDB04.pdf)

## Overview

The paper is an overview of the DTA (Database Tuning Advisor) which was release in 2005. The tool is able to recommend indexes, materialized views and partitioning (usually ranged and aligned - the same partitions are present on tables and indexes). There were several automated physical design tools developed by commercial database vendors, however, the DTA tool seemed to be the most advanced one. For example, it offered fully integrated recommendation, where, for instance, indexes and materialized views were considered simultaneously and not in a one-by-one fashion or so called in the staging manner. These tools consider not only the single objective of improving a general performance of a given workload, but also take into account scalability (the tuning time should be reasonable and do not impose too much overhead on a production server), manageability (the usage of horizontal range partitioning to ensure easy backup/restore, to add new data or remove old data), and functionality (the features provided by the DTA - e.g., scriptability - an XML schema for input/output that enhances scriptability and cusomizability of the tool; and efficient tuning in production/test server scenarios).

Back then, one of the main concern was the scalability. This was addressed in DTA as well by enabling it to scale to large databases and workloads via:
- workload compression (extract query signatures which denote the query templates; consider a single query per template; the workload to be optimized consists of the queries - from each template just a single one);
- reduced statistics creation (do not keep redundant statistics but share them among different configurations/physical designs within a configuration);
- exploit the test server to reduce the load on the production server (extend DTA to specify for a simulation: workload, configuration, and also the underlying hardware, e.g., specify number of CPUs on which to run the workload or the available memory).

The key word is simulation - do not copy any data for tuning or do not create new physical designs for testing the performance but imitate the structures, data, use sampling effectively and leverage the "what-if" type of analysis as well as query optimizer plans and costing.

## Extensions added to DTA:

### How to provide the workload for tuning?

The workload is a set of SQL statements that execute against the database server. A workload can be obtained by using SQL Server Profiler, a tool for logging events that execute on a server. In the current version of DTA, the Query Store can be used to collect the information about the workload for the tuning purposes (and it retains the information between server restarts): [How To Tune a Workload from Query Store in dta.exe command line Utility?](https://docs.microsoft.com/en-us/sql/relational-databases/performance/tuning-database-using-workload-from-query-store?view=sql-server-2017#how-to-tune-a-workload-from-query-store-in-dtaexe-command-line-utility)

### The main benefits of keeping the tuning advisor in sync/step with the query optimizer:
1. The recommended physical design will be (with a very high probability) used by the query optimizer.
2. Query optimizer cost model evolves over time, which makes the costing for hypothetical physical designs probably better.
3. Via the query optimizer, we also take into account the hardware environment where queries will be executed (this hardware environment can be simulated, thus we can run the workload on a test server and tune it there for the environment of the production server).

### Recap (from the previous papers on DTA): Falstart greedy search schema $$(m,k)$$.

If we are limited to only k indexes, but our tuning recommends many more, than we have to narrow down the selection. It can be done by first choosing a small number $$m$$ of indexes, this is the best possible configuration of m indexes. Then, we add a single index at a time, choosing the one that decrease the overall workload cost the most, in a greedy fashion, until we reach the configuration with the required $$k$$ indexes.

### Steps of workload tuning in DTA:
1. Column group restriction (a pre-processing step): similar to the data mining algorithm of frequent itemsets - aim is to find *interesting* columns, eliminate from consideration columns that can have only a marginal impact on the final configuration (e.g. take only the columns that appear in the queries, let's say, at least 2 times).
2. Candidate selection: choose the best configuration (set of indexes, materialized views, partitioning) for each query in the workload separately. The configurations' cost is based on the "what-if" analysis carried out by the query optimizer.
3. Merging: take into account the whole workload - especially the modification queries and the storage footprint constraints, propose another set of candidates (of indexes or materialized views) that could benefit the whole workload.
4. Enumeration: finally consider all the candidates (from the candidate selection and the merging steps) to produce the final configuration. the Greedy $$(m,k)$$ schema is used for this purpose.

### Scaling to large workloads, 3 options:
1. sample queries from the workload - this ignores how costly the queries are;
2. Tune the top k most expensive queries - many workloads are templatizes - so you might end up catering only to a single template.
3. Find signatures of the queries (basically templates behind the queries) and then tune for the set of templates (with an example of a single query per template). Two queries have the same signature if they are identical in all respects except for the constants referenced in the query.

### Tuning on the test server

Copy only the metadata about the databases from the production to the test server. If some statistics for an index are missing, then create them on the production server (this is the biggest overhead). The main idea is to simulate as much as possible and reduce the load on the production server by running the tuning on the test server. Moreover, the production environment can be simulate on the test server, by specifying a specific hardware (number of CPUs, memory available) for the tuning on the test server.

### Experiments:
Overall, the experiments are comprehensive. It is worth mentioning that the DTA does a better job than some DBAs. For example, for workload from one of the customers, the hand-tuned design was worse than a baseline (only indexes to enforce primary/uniquer keys) due to presence of updates. For this workload, DTA correctly recommended no additional physical design structures. For the TPC-H benchmark with 10GB of the input data, the size of the raw data in database was 12.8 GB. After the tuning, the expected performance improvement based on the costing from the query optimizer should increase by 88% but the decrease in the total workload execution time was 83%. The total storage space alloted was three times the raw data size. The compression of the workload (based on the templates and the signatures) provided even 40X improvement in tuning time for workloads with many query templates with a small degradation in the quality (0.5% or 1%). However, for the workload without any templates, such as TPC-H, the reduction in the tuning time was 1% (with, of course, no decrease in the quality - perhaps the number of extracted templates was equal to the total number of queries in the TPC-H benchmark, which is 22). 

### Limitations:

1. Microsoft SQL Server 2005 supports only a single-column range partitioning. It was improved later on slightly:
   - *Bad News*: The partition function has to be defined on a single column;
   - *Good News*: That single column could be a persisted computed column that is a combination of the two columns you're trying to partition by.
2. Query optimizer (on which the physical recommendations are made) do not model all the aspects of query execution, e.g., the impact of indexes on locking behavior.


