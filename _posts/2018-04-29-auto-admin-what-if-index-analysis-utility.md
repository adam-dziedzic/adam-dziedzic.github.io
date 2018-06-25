---
layout: post
title:  "AutoAdmin What-if Index Analysis Utility"
date:   2018-04-29
desc: "notes on a paper"
keywords: "databaes sigmod microsoft 1998 auto-admin tuning DBMS"
categories: [HTML]
tags: [databaes sigmod microsoft 1998 auto-admin tuning DBMS]
icon: icon-html
---

### Notes on a paper: AutoAdmin "What-if" Index Analysis Utility

First, still even today the tools to analyze query performance in databases are not perfect. Let's look at this comment from this website: https://goo.gl/6xxnS6:

*A whole recommendation is not very helpful. It is often suggested to create N indices to achieve an X% improvement. Of these N indexes, almost always 1 or 2 are the indices most contributing, others weigh the database work without great gain. I suggest adding a column where we can see the contribution of each index to the X% improvement. To do this today, it takes a long time, because you need it reevaluate each suggested index one by one.*

There was an effort in 1998 to provide a comprehensive visualisations of: workload, configurations and cost and index usage statistics.

1. Workload analysis: this consists of queries and their structural properties (query type: select/update/insert/delete, it it is an aggregation query (with the group by clause) or not, whether the query has nested subqueries, columns on which join conditions exists).
2. Configuration analysis: consists of indexes and their strucutral properties (size of the index, table on which the index is built, time of creation, whether or not the index is clustered).
3. Cost and index usage: the most important part of the system - exhibits relationship objects that capture the interaction between a specific configuration and queries in a workload.

### Queries

Users are provided with a specialized interface to query the hypthetical designs, however, in principle, they can write the SQL queries on their own against the analysis data tables.

### Main execution: estimate configuration (set of indexes) for a query

1. Create all needed hypothetical indexes in the configuration.
2. Request the optimizer to:
   1. Restirct its choice of indexes to those in the given configuration (the database catalog cannot be modified, as the other real queries might be running in the system, but this configuations can be specified on the users session level).
   2. Consider the table and index sizes in the database to be adjusted by the scaling values (users can specify that a given table can grow in the future - as expected scale of the current size).
3. Request the optimizer to produce the optimal execution plan for the query and gather the results:
   1. the cost of the query
   2. indexes (if any) used to answer the query

### Adaptive sampling strategy for creating hypothetical indexes

#### Side note

An interseting side note is a short description of a sampling strategy (described in detail in another paper), but explained enough and worth mentioning here.

#### Algorithm

An adaptive page-level sampling algorithm is used to efficiently gather statistical measures relevant to query optimization. Incrementally, sample of size $$\sqrt(n) = m$$ is drawn, where $$n$$ is the number of pages in the table. The samples are stores in a sample-table, in sorted order. The statistical measures contain, for example, equi-depth histograms. After the first sample is drawn and the statistics gathered, we draw another sample and verify if the new sample has "similar" statistical characteristics as the previously sampled data stored in sample-table (for now, the table contains just a single sample of size m). To be precise, we check if the values in the new sample are divided approximately in equal numbers in each bin of the equi-depth histogram. If the statistics are in a certain ballpark similar, we finish the algorithm. Otherwise, the last sample is merged into the sample-table and the statistics are updated. We repeat the process until the aggreement in statistics between the sample-table and a newly drawn sample is reached, all we drawn some specified number of samples. 

## Main takeaways

The index anslysis utility is indespensible - and this is what this paper addresses. Analyze the impact of current or hyptothetical indexes on the performance of your workload (set of queries). This approach is based on relative estimation of the cost that enables a large class of analysis at low cost. The authors implemented a tool that can use hypothetical indexes to predict workload cost, this was achieved by using sampling based techniques.

Thus, the most useful command provided is: Esimtate Configuration (set of indexes) of <workload_name> for <configuration_name>