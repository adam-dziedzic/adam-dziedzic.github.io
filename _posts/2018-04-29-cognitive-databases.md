---
layout: post
title:  "Cognitive databases"
date:   2018-04-29
desc: "notes on a paper"
keywords: "databaes nlp word2vec word-embeddings IBM Watson"
categories: [HTML]
tags: [databaes nlp word2vec word-embeddings IBM Watson]
icon: icon-html
---

## Notes on papers: [cognitive databases](https://arxiv.org/find/cs/1/au:+Shmueli_O/0/1/0/all/0/1), that is on using embeddings to extend Relational Query Processing.

## General idea

Copy data from relational tables into pure text (the transformation from a database content into the text ready for NLP processing can be done in many ways). For each word in the text corpus, create a vector (word embedding). This enables us to leverage many NLP tools/techniques to enhance SQL queries via UDFs and providing more semantic understanding of data.

They want to extract and use latent semantic information from all the database entities.
In other words, application of NLP (Natural Language Processing) based machine learning techniques for enhancing and answering relational queries.

Deep Dive used machine learning to convert input unstructured documents into a structured knowledge base. This paper proposes an opposite technique - flatten the database content and use it as a text corpus.

## 5C's:
1. Category: data mining on top of a database.
2. Context: how to provide semantic understanding of a database content.
3. Correctness: only an overview of capabilities that are offered by NLP using the Word2Vec (word embedding) on top of relational tables without any significant system or theory contributions.
4. Contributions: show the idea of how to harness NLP tools in the context of database systems.

## Main notes:

#### Example of queries:
1. Query 1: give 10 people most related to Mark (the text for word embedding extracted only from the DBMS for this query)
2. Query 2: which are the most dangerous vacation packages (use external sources + database content)

##### Their argument: formulating SQL queries to get the same results is a daunting task.

#### New capabilities, they claim the following unique capabilities:
1. ability to build joint cross-modal semantic model from multi-modal data,
2. transparent integration of novel cognitive queries into existing SQL query infrastructure,
3. using untyped  vector representations to support contextual semantic (i.e. not value based) queries across multiple SQL data types,  and
4. ability to import an externally trained semantic model and apply it to enable querying a database using a token not present in the database.

#### To the best of their knowledge, none of the current industrial, academic, or open source database systems support these capabilities.

### Theoretical aspects:
- word vectors can be used to compute the semantic and/or grammatical closeness of words as well as test for analogies
- closeness of vectors is determined by using the cosine or Jacard distance measures between words - they do not use Jackard but only the cosine distance
- very shallow representation of numbers - just as pure text 101.1 -> "101.1"
- you can extend the vectors for a row with vectors from the row to which the foreign key corresponds to (natural and easy extension)
- some additional operators/ UDF functions:
- proximityMAX() given two sets of vectors as parameters, it returns the highest cosine distance between a vector from one set and a vector from the other set
- proximityAVG() - generates two sets of tokens, one from its first and one from its second argument. Represents a set of tokens via a single vector which is the average of the vectors associated with the tokens in the set. Returns the cosine distance of the two vectors representing the two sets.
- subsetProximityAVG() - semantically in between the proximityMAX() and proximityAVG(). Takes additional parameter: size. Considers all sets of tokens out of sequnence1 of cardinality size and computes an average vector for each such subset. The same is done for sequence2 (the 3rd parameter). Returns maximum of cosine distances between average vectors of subsets.

### Systems issues:
- the vector training time can be very large -> use GPUs
- high cost of accessing the trained vectors from the system tables; note that the text form of the database content (for the word embedding) can be much larger that the content of the database itself (because e.g. each word can be proceeded with a table:column name and expressed as a 200 dimensional vector)
- the execution cost of CI (Cognitive Intelligence) queries is dependent on the performance of the distance function - their cosine distance is omnipresent and they did not really mention/use any other distance measure (apart from a single occurrence of the Jackard distance) between vectors in their
- distance function and performance trade-offs: higher dimensional vectors (they use standard 200 dimensional vectors) give better semantic expressiveness but longer training time and higher cost of calculation of the distances between vectors (also increase the storage footprint)
- view maintenance of vectors - the vectors and the text version of data is just a copy/another version of the data that has to be kept in sync with the main database content
- reducing redundant computations (proposed in the paper): for a given vector, we can first identify a candidate set of vectors that are spatially closer to it in the d dimensional vector space using either locality sensitive hashing (LSH) or clustering via the Spherical K-Means algorithm. Both approaches can be accelerated using SIMD or GPUs.
- they propose many other techniques how to make the NLP + DBMS synergy more viable by leveraging: distributed computing, multi-cores processing, SIMD and GPUs.

### Other issues:
- the thresholds for their semantic queries - e.g. for the cosine similarity measure, users have to specify the value from -1 (dissimilar) to 1 (very similar) - but how would users know which is the one that they want or which would make sense? Authors' answer - these  bounds are application dependent, much like hyperparameters in machine learning. One learns these by exploring the underlying database and running experiments. In the future, one can envision a tool that can guide users to select an appropriate numeric bound for a particular CI query.

### Systems used:
- the prototype was built on top of Spark - using Scala and Python
- they used the famous Word2Vec for the work embedding
- IBM Watson Visual Recognition System (VRS) for classification and text description

##### What is needed: a benchmark for evaluating and ranking CI (Cognitive Intelligence) systems.

## Two more things:

1. Updates of the text corpus and the word vectors. Authors of the papers don't specify how the (copied) raw text corpus (from the tables) would be updated. In the first paper (from 2016), they mentioned that the word embedding would have to be re-trained, however in the latter paper (2017) they found that there is a possibility of incremental training.

2. I think of the other approach. How can we leverage the existing database systems to propose schemas for unstructured data? We could flatten many databases to a text corpus and create the vectors from them with direct connection to the source schema, physical designs, etc. Then for a given unstructured input of data - let me say even to a subset of sources in a data lake - we could propose a schema (if we treat the data from the data lake as the text corpus and also create word embedding for it).

## Summary

In general, I think that this is just an idea of extending DBMS with word embedding. For now, it does not have any further significant insights. They only use features offered by expressing words as vectors but has not extended it beyond any loosely coupled DBMS + Word2Vec. It might make more sense to write/claim a system to support Word2Vec on a large scale for truly big data than just flatten the database content.

