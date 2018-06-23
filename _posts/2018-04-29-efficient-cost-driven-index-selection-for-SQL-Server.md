---
layout: post
title:  "An Efficient, Cost-Driven Index Selection Tool for Microsoft SQL Server"
date:   2018-04-29
desc: "notes on a paper"
keywords: "databaes vldb microsoft 1997 auto-admin tuning DBMS"
categories: [HTML]
tags: [databaes vldb microsoft 1997 auto-admin tuning DBMS]
icon: icon-html
---

# An Efficient, Cost-Driven Index Selection Tool for Microsoft SQL Server (VLDB 1997)

## These are my notes on the paper:

The main approch is not to use any 1) query-syntax-based method or 2) knowledge base with best practices method but instead 3) re-use the optimizer with its what-if mode to cost potential physical designs (in this case - only indexes). The main focus in on how to recommend a decent set of indexes (a.k.a. a configuration) in a reasonable amount of time. To this end a 3 techniques are applied:

### Candidate index selection - choose the best index for each query separately

Determine the best configuration for each query independently. Treat each query from the total wokload, as a separte workload. If the query is read-only, then usually the indexes covering all admissible columns (which are used in the where or group by clauses) are chosen. If a query contains some modifications, then the maintenance of the index is taken into account and it might be the case that no index is recommended for the query.

### Configuration enumeration via a "falstart-greedy" algorithm

The candidate index selection step gives a set of indexes for each query, then takes the union of them and considers the configuration for the whole workload. If there is a constraint of max k indexes then we have to prune the set of all indexes. We do it via a greedy algorithm. (m,k) greedy algorithm: m - is a seed denoting a number <= k, thus we start with some number m of indexes (heuristic and experiments claim that it is good to start from m = 2). This m indexes are chosen by full enumeration of all possible m indexes, and selecting an optimal set of m indexes. From this point on (after full search of the best possible m indexes), we greedily try to add an index at a time, in each step trying to find the index that would end up with the biggest total reduction of the cost of the workload.

### Consider multi-column indexes (e.g. a B+ tree on two columns)

An iterative approach is adopted here - it is called MC-LEAD. Take into account multi-column indexes of increasing width. Intution is that for a two-column indexes to be desirable, a single-column index on its leading column must be desirable. MC-LEAD - a 2-column index is selected only if its leading column was in a winning 1-column index (an index chosen from the set of all 1-column indexes considered), the second column in the 2-column index must be admisible (the 2nd column is part of the where or a group by clause in a query).



